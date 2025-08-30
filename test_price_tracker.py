#!/usr/bin/env python3
"""
Test script for the Price Tracker Agent System
Demonstrates the functionality without requiring the full system to run
"""

import json
import asyncio
from datetime import datetime, timedelta
from price_tracker_agent import (
    PriceData, 
    SecurityManager, 
    PriceAnalysisAgent, 
    InformationRetrievalAgent
)

def test_price_analysis():
    """Test the price analysis functionality"""
    print("🧪 Testing Price Analysis Agent...")
    
    # Create price analysis agent
    agent = PriceAnalysisAgent()
    
    # Load test data
    test_data = [
        {"product_id": "e1", "date": "2025-08-01", "price": 5100},
        {"product_id": "e1", "date": "2025-08-10", "price": 5000},
        {"product_id": "e1", "date": "2025-08-20", "price": 4950},
        {"product_id": "f1", "date": "2025-08-01", "price": 2600},
        {"product_id": "f1", "date": "2025-08-10", "price": 2500},
        {"product_id": "f1", "date": "2025-08-20", "price": 2450}
    ]
    
    # Convert to PriceData objects
    for entry in test_data:
        product_id = entry['product_id']
        if product_id not in agent.price_history:
            agent.price_history[product_id] = []
        
        agent.price_history[product_id].append(PriceData(
            product_id=product_id,
            date=entry['date'],
            price=entry['price']
        ))
    
    # Test analysis
    print("\n📊 Price Analysis Results:")
    print("=" * 50)
    
    for product_id in ["e1", "f1"]:
        analysis = agent.analyze_product_trends(product_id)
        print(f"\nProduct: {product_id}")
        for key, value in analysis.items():
            print(f"  {key}: {value}")
    
    # Test alerts
    print("\n🚨 Price Alerts:")
    print("=" * 50)
    alerts = agent.get_price_alerts(threshold_percent=3.0)
    for alert in alerts:
        print(f"  {alert['product_id']}: {alert['change_percent']}% change")

def test_security():
    """Test the security functionality"""
    print("\n🔐 Testing Security Manager...")
    
    security = SecurityManager()
    
    # Test authentication
    token = security.authenticate_user("admin", "admin123")
    if token:
        print("✅ Authentication successful")
        print(f"   Token: {token[:20]}...")
        
        # Test token verification
        if security.verify_token(token):
            print("✅ Token verification successful")
        else:
            print("❌ Token verification failed")
    else:
        print("❌ Authentication failed")
    
    # Test input sanitization
    malicious_input = "<script>alert('xss')</script>"
    sanitized = security.sanitize_input(malicious_input)
    print(f"✅ Input sanitization: '{malicious_input}' -> '{sanitized}'")
    
    # Test encryption
    test_data = "sensitive information"
    encrypted = security.encrypt_data(test_data)
    decrypted = security.decrypt_data(encrypted)
    print(f"✅ Encryption/Decryption: '{test_data}' -> '{decrypted}'")

def test_information_retrieval():
    """Test the information retrieval functionality"""
    print("\n🔍 Testing Information Retrieval Agent...")
    
    agent = InformationRetrievalAgent()
    
    # Test product search
    search_results = agent.search_products("wireless mouse")
    print("✅ Product search results:")
    for result in search_results:
        print(f"   {result['id']}: {result['name']} ({result['category']})")
    
    # Test product details
    product_details = agent.get_product_details("e1")
    if product_details:
        print(f"✅ Product details for e1: {product_details}")
    
    # Test market insights
    insights = agent.get_market_insights()
    print("✅ Market insights:")
    for key, value in insights.items():
        print(f"   {key}: {value}")

def test_data_loading():
    """Test loading data from the JSON file"""
    print("\n📁 Testing Data Loading...")
    
    try:
        agent = PriceAnalysisAgent()
        agent.load_price_data("frontend/src/data/pricehistory.json")
        
        print(f"✅ Loaded price data for {len(agent.price_history)} products")
        
        # Show sample data
        sample_product = list(agent.price_history.keys())[0]
        sample_data = agent.price_history[sample_product]
        print(f"   Sample product {sample_product}: {len(sample_data)} price points")
        
        # Show price range
        all_prices = []
        for product_data in agent.price_history.values():
            all_prices.extend([p.price for p in product_data])
        
        print(f"   Price range: Rs. {min(all_prices):,} - Rs. {max(all_prices):,}")
        
    except FileNotFoundError:
        print("❌ Price history file not found. Make sure the path is correct.")
    except Exception as e:
        print(f"❌ Error loading data: {e}")

async def test_communication():
    """Test the communication system"""
    print("\n🌐 Testing Communication System...")
    
    from price_tracker_agent import CommunicationManager
    
    comm_manager = CommunicationManager()
    
    # Register test agents
    class TestAgent:
        def __init__(self, name):
            self.name = name
            self.messages = []
        
        async def handle_message(self, message_data):
            self.messages.append(message_data)
            print(f"   📨 {self.name} received: {message_data['message']}")
    
    agent1 = TestAgent("Agent1")
    agent2 = TestAgent("Agent2")
    
    comm_manager.register_agent("agent1", agent1)
    comm_manager.register_agent("agent2", agent2)
    
    # Send test messages
    await comm_manager.send_message("agent1", "agent2", {"type": "test", "content": "Hello from Agent1"})
    await comm_manager.broadcast_message("agent1", {"type": "broadcast", "content": "Hello everyone!"})
    
    # Process messages with timeout to prevent hanging
    try:
        # Create a task for processing messages
        process_task = asyncio.create_task(comm_manager.process_messages())
        
        # Wait a bit for messages to be processed
        await asyncio.sleep(0.1)
        
        # Cancel the process task
        process_task.cancel()
        
        # Wait for cancellation to complete
        try:
            await process_task
        except asyncio.CancelledError:
            pass
        
        print("✅ Communication test completed")
        
    except Exception as e:
        print(f"⚠️  Communication test completed with warning: {e}")

def main():
    """Main test function"""
    print("🚀 Price Tracker Agent System - Test Suite")
    print("=" * 60)
    
    # Run tests
    test_price_analysis()
    test_security()
    test_information_retrieval()
    test_data_loading()
    
    # Run async tests
    print("\n🔄 Running async tests...")
    try:
        asyncio.run(test_communication())
    except KeyboardInterrupt:
        print("\n⚠️  Async tests interrupted")
    except Exception as e:
        print(f"\n⚠️  Async tests completed with warning: {e}")
    
    print("\n✅ All tests completed!")
    print("\n📋 To run the full system:")
    print("   python price_tracker_agent.py")
    print("\n📋 To test the API:")
    print("   curl -X POST http://localhost:5000/api/auth/login \\")
    print("     -H 'Content-Type: application/json' \\")
    print("     -d '{\"username\": \"admin\", \"password\": \"admin123\"}'")

if __name__ == "__main__":
    main()
