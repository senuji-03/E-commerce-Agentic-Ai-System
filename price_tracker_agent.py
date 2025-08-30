#!/usr/bin/env python3
"""
Price Tracker Agent System
A multi-agent system for intelligent price tracking and analysis

Features:
- Multiple interacting intelligent agents
- LLM integration for natural language processing
- NLP techniques (NER, Summarization)
- Information retrieval module
- Security features (authentication, input sanitization, encryption)
- Agent communication protocols (HTTP, sockets)
"""

import json
import asyncio
import logging
import hashlib
import hmac
import base64
import socket
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from transformers import pipeline
import spacy
from cryptography.fernet import Fernet
import jwt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
CONFIG = {
    "openai_api_key": "your-openai-api-key-here",
    "jwt_secret": "your-jwt-secret-here",
    "encryption_key": Fernet.generate_key(),
    "port": 5000,
    "host": "0.0.0.0"
}

# Initialize encryption
cipher = Fernet(CONFIG["encryption_key"])

@dataclass
class PriceData:
    """Data class for price information"""
    product_id: str
    date: str
    price: float
    category: str = ""
    trend: str = "stable"
    confidence: float = 0.0

class SecurityManager:
    """Handles authentication, input sanitization, and encryption"""
    
    def __init__(self):
        self.active_tokens = set()
    
    def authenticate_user(self, username: str, password: str) -> Optional[str]:
        """Authenticate user and return JWT token"""
        # In production, use proper user database
        if username == "admin" and password == "admin123":
            token = jwt.encode(
                {"username": username, "exp": datetime.utcnow() + timedelta(hours=24)},
                CONFIG["jwt_secret"],
                algorithm="HS256"
            )
            self.active_tokens.add(token)
            return token
        return None
    
    def verify_token(self, token: str) -> bool:
        """Verify JWT token"""
        try:
            payload = jwt.decode(token, CONFIG["jwt_secret"], algorithms=["HS256"])
            return token in self.active_tokens
        except jwt.ExpiredSignatureError:
            self.active_tokens.discard(token)
            return False
        except jwt.InvalidTokenError:
            return False
    
    def sanitize_input(self, data: str) -> str:
        """Sanitize user input to prevent injection attacks"""
        dangerous_chars = ["<", ">", "'", '"', "&", ";", "|", "`", "$", "(", ")", "{", "}"]
        for char in dangerous_chars:
            data = data.replace(char, "")
        return data
    
    def encrypt_data(self, data: str) -> bytes:
        """Encrypt sensitive data"""
        return cipher.encrypt(data.encode())
    
    def decrypt_data(self, encrypted_data: bytes) -> str:
        """Decrypt encrypted data"""
        return cipher.decrypt(encrypted_data).decode()

class LLMAgent:
    """LLM-powered agent for natural language processing and analysis"""
    
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=CONFIG["openai_api_key"])
        self.nlp_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
        
        # Load spaCy model for NER
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            logger.warning("spaCy model not found. Install with: python -m spacy download en_core_web_sm")
            self.nlp = None
    
    def analyze_price_trends(self, price_data: List[PriceData]) -> str:
        """Analyze price trends using LLM"""
        try:
            # Create summary of price data
            summary = f"Product prices over time: {len(price_data)} data points. "
            summary += f"Price range: {min(p.price for p in price_data)} to {max(p.price for p in price_data)}. "
            
            # Calculate trend
            prices = [p.price for p in price_data]
            if len(prices) > 1:
                trend = "increasing" if prices[-1] > prices[0] else "decreasing" if prices[-1] < prices[0] else "stable"
                summary += f"Overall trend: {trend}."
            
            # Use LLM for analysis
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a price analysis expert. Provide insights about price trends."},
                    {"role": "user", "content": f"Analyze this price data: {summary}"}
                ],
                max_tokens=150
            )
            
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"LLM analysis failed: {e}")
            return "Price trend analysis unavailable"
    
    def extract_entities(self, text: str) -> List[str]:
        """Extract named entities using spaCy NER"""
        if not self.nlp:
            return []
        
        doc = self.nlp(text)
        entities = [ent.text for ent in doc.ents]
        return entities
    
    def summarize_text(self, text: str) -> str:
        """Summarize text using Hugging Face pipeline"""
        try:
            if len(text) < 100:
                return text
            
            summary = self.nlp_pipeline(text, max_length=130, min_length=30, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            logger.error(f"Summarization failed: {e}")
            return text[:100] + "..."

class PriceAnalysisAgent:
    """Agent responsible for price analysis and predictions"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = LinearRegression()
        self.price_history = {}
    
    def load_price_data(self, file_path: str):
        """Load price history data from JSON file"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Group by product_id
            for entry in data:
                product_id = entry['product_id']
                if product_id not in self.price_history:
                    self.price_history[product_id] = []
                
                self.price_history[product_id].append(PriceData(
                    product_id=product_id,
                    date=entry['date'],
                    price=entry['price']
                ))
            
            logger.info(f"Loaded price data for {len(self.price_history)} products")
        except Exception as e:
            logger.error(f"Failed to load price data: {e}")
    
    def analyze_product_trends(self, product_id: str) -> Dict:
        """Analyze price trends for a specific product"""
        if product_id not in self.price_history:
            return {"error": "Product not found"}
        
        prices = self.price_history[product_id]
        if len(prices) < 2:
            return {"error": "Insufficient data for analysis"}
        
        # Sort by date
        prices.sort(key=lambda x: x.date)
        
        # Calculate basic statistics
        price_values = [p.price for p in prices]
        current_price = price_values[-1]
        previous_price = price_values[-2]
        price_change = current_price - previous_price
        price_change_percent = (price_change / previous_price) * 100
        
        # Determine trend
        if price_change > 0:
            trend = "increasing"
        elif price_change < 0:
            trend = "decreasing"
        else:
            trend = "stable"
        
        # Calculate volatility
        volatility = np.std(price_values)
        
        # Simple prediction using linear regression
        try:
            dates_numeric = [(datetime.strptime(p.date, "%Y-%m-%d") - datetime(2025, 8, 1)).days for p in prices]
            X = np.array(dates_numeric).reshape(-1, 1)
            y = np.array(price_values)
            
            X_scaled = self.scaler.fit_transform(X)
            self.model.fit(X_scaled, y)
            
            # Predict next price (7 days ahead)
            next_date = max(dates_numeric) + 7
            next_date_scaled = self.scaler.transform([[next_date]])
            predicted_price = self.model.predict(next_date_scaled)[0]
            
            prediction_confidence = self.model.score(X_scaled, y)
        except Exception as e:
            logger.error(f"Prediction failed: {e}")
            predicted_price = current_price
            prediction_confidence = 0.0
        
        return {
            "product_id": product_id,
            "current_price": current_price,
            "previous_price": previous_price,
            "price_change": price_change,
            "price_change_percent": round(price_change_percent, 2),
            "trend": trend,
            "volatility": round(volatility, 2),
            "predicted_price": round(predicted_price, 2),
            "prediction_confidence": round(prediction_confidence, 3),
            "data_points": len(prices)
        }
    
    def get_price_alerts(self, threshold_percent: float = 5.0) -> List[Dict]:
        """Get price alerts for significant changes"""
        alerts = []
        
        for product_id, prices in self.price_history.items():
            if len(prices) < 2:
                continue
            
            prices.sort(key=lambda x: x.date)
            current_price = prices[-1].price
            previous_price = prices[-2].price
            
            price_change_percent = abs((current_price - previous_price) / previous_price) * 100
            
            if price_change_percent >= threshold_percent:
                alerts.append({
                    "product_id": product_id,
                    "current_price": current_price,
                    "previous_price": previous_price,
                    "change_percent": round(price_change_percent, 2),
                    "alert_type": "price_change",
                    "timestamp": datetime.now().isoformat()
                })
        
        return alerts

class InformationRetrievalAgent:
    """Agent responsible for retrieving and organizing information"""
    
    def __init__(self):
        self.cache = {}
        self.cache_ttl = 3600  # 1 hour
    
    def search_products(self, query: str) -> List[Dict]:
        """Search for products based on query"""
        # In a real system, this would search a product database
        # For now, return mock results
        return [
            {"id": "e1", "name": "Wireless Mouse", "category": "Electronics"},
            {"id": "f1", "name": "Men's T-Shirt", "category": "Fashion"},
            {"id": "bp1", "name": "Facial Cleanser", "category": "Beauty"}
        ]
    
    def get_product_details(self, product_id: str) -> Optional[Dict]:
        """Get detailed information about a product"""
        # Mock product database
        products = {
            "e1": {"name": "Wireless Mouse", "category": "Electronics", "description": "High-precision wireless mouse"},
            "f1": {"name": "Men's T-Shirt", "category": "Fashion", "description": "Comfortable cotton t-shirt"},
            "bp1": {"name": "Facial Cleanser", "category": "Beauty", "description": "Gentle facial cleanser"}
        }
        
        return products.get(product_id)
    
    def get_market_insights(self) -> Dict:
        """Get general market insights"""
        return {
            "total_products": 100,
            "categories": ["Electronics", "Fashion", "Kitchen & Dining", "Beauty & Personal Care", "Home & Living"],
            "price_range": {"min": 300, "max": 350000},
            "market_trend": "stable",
            "last_updated": datetime.now().isoformat()
        }

class CommunicationManager:
    """Manages communication between agents and external systems"""
    
    def __init__(self, host: str = "localhost", port: int = 5000):
        self.host = host
        self.port = port
        self.agents = {}
        self.message_queue = asyncio.Queue()
        self._running = False
    
    def register_agent(self, agent_id: str, agent):
        """Register an agent for communication"""
        self.agents[agent_id] = agent
        logger.info(f"Registered agent: {agent_id}")
    
    async def send_message(self, from_agent: str, to_agent: str, message: Dict):
        """Send message between agents"""
        if to_agent in self.agents:
            await self.message_queue.put({
                "from": from_agent,
                "to": to_agent,
                "message": message,
                "timestamp": datetime.now().isoformat()
            })
            logger.info(f"Message sent from {from_agent} to {to_agent}")
        else:
            logger.warning(f"Agent {to_agent} not found")
    
    async def broadcast_message(self, from_agent: str, message: Dict):
        """Broadcast message to all agents"""
        for agent_id in self.agents:
            if agent_id != from_agent:
                await self.send_message(from_agent, agent_id, message)
    
    async def process_messages(self):
        """Process message queue"""
        self._running = True
        try:
            while self._running:
                try:
                    # Use wait_for to allow cancellation
                    message_data = await asyncio.wait_for(
                        self.message_queue.get(), 
                        timeout=1.0
                    )
                    
                    to_agent = message_data["to"]
                    
                    if to_agent in self.agents:
                        # Process message based on agent type
                        agent = self.agents[to_agent]
                        if hasattr(agent, 'handle_message'):
                            await agent.handle_message(message_data)
                    
                    self.message_queue.task_done()
                    
                except asyncio.TimeoutError:
                    # Continue loop on timeout
                    continue
                except asyncio.CancelledError:
                    logger.info("Message processing cancelled")
                    break
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
                    
        finally:
            self._running = False
    
    def stop(self):
        """Stop the communication manager"""
        self._running = False

class PriceTrackerSystem:
    """Main system coordinating all agents"""
    
    def __init__(self):
        self.security_manager = SecurityManager()
        self.llm_agent = LLMAgent()
        self.price_analysis_agent = PriceAnalysisAgent()
        self.info_retrieval_agent = InformationRetrievalAgent()
        self.communication_manager = CommunicationManager()
        
        # Register agents
        self.communication_manager.register_agent("security", self.security_manager)
        self.communication_manager.register_agent("llm", self.llm_agent)
        self.communication_manager.register_agent("price_analysis", self.price_analysis_agent)
        self.communication_manager.register_agent("info_retrieval", self.info_retrieval_agent)
        
        # Load price data
        self.price_analysis_agent.load_price_data("frontend/src/data/pricehistory.json")
        
        # Initialize Flask app
        self.app = Flask(__name__)
        CORS(self.app)
        self.setup_routes()
    
    def setup_routes(self):
        """Setup Flask API routes"""
        
        @self.app.route('/')
        def home():
            """Home page with API documentation"""
            return jsonify({
                "message": "Price Tracker Agent System API",
                "version": "1.0.0",
                "endpoints": {
                    "home": "/",
                    "login": "/api/auth/login",
                    "analyze": "/api/analyze/<product_id>",
                    "alerts": "/api/alerts",
                    "search": "/api/search",
                    "insights": "/api/insights"
                },
                "usage": "Use /api/auth/login to get a token, then use other endpoints with Authorization: Bearer <token>"
            })
        
        @self.app.route('/api/analyze/<product_id>', methods=['GET'])
        def analyze_product(product_id):
            """Analyze price trends for a specific product"""
            # Verify authentication
            token = request.headers.get('Authorization', '').replace('Bearer ', '')
            if not self.security_manager.verify_token(token):
                return jsonify({"error": "Unauthorized"}), 401
            
            # Sanitize input
            product_id = self.security_manager.sanitize_input(product_id)
            
            # Get analysis
            analysis = self.price_analysis_agent.analyze_product_trends(product_id)
            
            # Use LLM for additional insights
            if "error" not in analysis:
                llm_insights = self.llm_agent.analyze_price_trends(
                    self.price_analysis_agent.price_history.get(product_id, [])
                )
                analysis["llm_insights"] = llm_insights
            
            return jsonify(analysis)
        
        @self.app.route('/api/alerts', methods=['GET'])
        def get_alerts():
            """Get price alerts"""
            token = request.headers.get('Authorization', '').replace('Bearer ', '')
            if not self.security_manager.verify_token(token):
                return jsonify({"error": "Unauthorized"}), 401
            
            threshold = request.args.get('threshold', 5.0, type=float)
            alerts = self.price_analysis_agent.get_price_alerts(threshold)
            return jsonify(alerts)
        
        @self.app.route('/api/search', methods=['POST'])
        def search_products():
            """Search for products"""
            token = request.headers.get('Authorization', '').replace('Bearer ', '')
            if not self.security_manager.verify_token(token):
                return jsonify({"error": "Unauthorized"}), 401
            
            data = request.get_json()
            query = self.security_manager.sanitize_input(data.get('query', ''))
            
            results = self.info_retrieval_agent.search_products(query)
            return jsonify(results)
        
        @self.app.route('/api/insights', methods=['GET'])
        def get_insights():
            """Get market insights"""
            token = request.headers.get('Authorization', '').replace('Bearer ', '')
            if not self.security_manager.verify_token(token):
                return jsonify({"error": "Unauthorized"}), 401
            
            insights = self.info_retrieval_agent.get_market_insights()
            return jsonify(insights)
        
        @self.app.route('/api/auth/login', methods=['POST'])
        def login():
            """User authentication"""
            data = request.get_json()
            username = data.get('username', '')
            password = data.get('password', '')
            
            token = self.security_manager.authenticate_user(username, password)
            if token:
                return jsonify({"token": token, "message": "Login successful"})
            else:
                return jsonify({"error": "Invalid credentials"}), 401
        
        @self.app.route('/api/test', methods=['GET'])
        def test_endpoint():
            """Test endpoint to verify server is working"""
            return jsonify({
                "status": "success",
                "message": "Price Tracker Agent System is running!",
                "timestamp": datetime.now().isoformat(),
                "agents": list(self.communication_manager.agents.keys())
            })
    
    async def start_system(self):
        """Start the price tracker system"""
        logger.info("Starting Price Tracker System...")
        
        # Start message processing
        asyncio.create_task(self.communication_manager.process_messages())
        
        # Start Flask app in a separate thread
        def run_flask():
            self.app.run(host=CONFIG["host"], port=CONFIG["port"], debug=False)
        
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()
        
        logger.info(f"Price Tracker System started on {CONFIG['host']}:{CONFIG['port']}")
        
        # Keep the system running
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            logger.info("Shutting down Price Tracker System...")

async def main():
    """Main function"""
    system = PriceTrackerSystem()
    await system.start_system()

if __name__ == "__main__":
    asyncio.run(main())
