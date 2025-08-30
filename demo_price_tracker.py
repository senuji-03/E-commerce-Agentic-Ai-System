#!/usr/bin/env python3
"""
Demo script for the Price Tracker Agent System
Shows the system functionality in a simple, non-blocking way
"""

import json
from datetime import datetime
from price_tracker_agent import (
    PriceData, 
    SecurityManager, 
    PriceAnalysisAgent, 
    InformationRetrievalAgent
)

def demo_price_analysis():
    """Demonstrate price analysis functionality"""
    print("🧪 Demo: Price Analysis Agent")
    print("=" * 50)
    
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
    
    # Show analysis results
    print("\n📊 Price Analysis Results:")
    for product_id in ["e1", "f1"]:
        analysis = agent.analyze_product_trends(product_id)
        print(f"\nProduct: {product_id}")
        for key, value in analysis.items():
            print(f"  {key}: {value}")
    
    # Show alerts
    print("\n🚨 Price Alerts (threshold: 3%):")
    alerts = agent.get_price_alerts(threshold_percent=3.0)
    for alert in alerts:
        print(f"  {alert['product_id']}: {alert['change_percent']}% change")

def demo_security():
    """Demonstrate security functionality"""
    print("\n🔐 Demo: Security Manager")
    print("=" * 50)
    
    security = SecurityManager()
    
    # Test authentication
    print("Testing authentication...")
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
    print("\nTesting input sanitization...")
    malicious_input = "<script>alert('xss')</script>"
    sanitized = security.sanitize_input(malicious_input)
    print(f"✅ Input sanitization: '{malicious_input}' -> '{sanitized}'")
    
    # Test encryption
    print("\nTesting encryption...")
    test_data = "sensitive information"
    encrypted = security.encrypt_data(test_data)
    decrypted = security.decrypt_data(encrypted)
    print(f"✅ Encryption/Decryption: '{test_data}' -> '{decrypted}'")

def demo_information_retrieval():
    """Demonstrate information retrieval functionality"""
    print("\n🔍 Demo: Information Retrieval Agent")
    print("=" * 50)
    
    agent = InformationRetrievalAgent()
    
    # Test product search
    print("Testing product search...")
    search_results = agent.search_products("wireless mouse")
    print("✅ Product search results:")
    for result in search_results:
        print(f"   {result['id']}: {result['name']} ({result['category']})")
    
    # Test product details
    print("\nTesting product details...")
    product_details = agent.get_product_details("e1")
    if product_details:
        print(f"✅ Product details for e1: {product_details}")
    
    # Test market insights
    print("\nTesting market insights...")
    insights = agent.get_market_insights()
    print("✅ Market insights:")
    for key, value in insights.items():
        print(f"   {key}: {value}")

def demo_data_loading():
    """Demonstrate loading data from JSON file"""
    print("\n📁 Demo: Data Loading")
    print("=" * 50)
    
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
        
        # Show category distribution
        categories = {}
        for product_id in agent.price_history.keys():
            if product_id.startswith('e'):
                category = 'Electronics'
            elif product_id.startswith('f'):
                category = 'Fashion'
            elif product_id.startswith('bp'):
                category = 'Beauty & Personal Care'
            elif product_id.startswith('hl'):
                category = 'Home & Living'
            elif product_id.startswith('hk'):
                category = 'Kitchen & Dining'
            else:
                category = 'Unknown'
            
            categories[category] = categories.get(category, 0) + 1
        
        print("\n   Category distribution:")
        for category, count in categories.items():
            print(f"     {category}: {count} products")
        
    except FileNotFoundError:
        print("❌ Price history file not found. Make sure the path is correct.")
    except Exception as e:
        print(f"❌ Error loading data: {e}")

def demo_simple_communication():
    """Demonstrate simple communication without async complexity"""
    print("\n🌐 Demo: Simple Communication")
    print("=" * 50)
    
    from price_tracker_agent import CommunicationManager
    
    comm_manager = CommunicationManager()
    
    # Register test agents
    class SimpleAgent:
        def __init__(self, name):
            self.name = name
            self.messages = []
        
        def handle_message_sync(self, message_data):
            self.messages.append(message_data)
            print(f"   📨 {self.name} received: {message_data['message']}")
    
    agent1 = SimpleAgent("Agent1")
    agent2 = SimpleAgent("Agent2")
    
    comm_manager.register_agent("agent1", agent1)
    comm_manager.register_agent("agent2", agent2)
    
    print("✅ Agents registered successfully")
    print(f"   Registered agents: {list(comm_manager.agents.keys())}")
    
    # Simulate message sending (without async)
    print("\n📤 Simulating message sending...")
    print("   Agent1 -> Agent2: Test message")
    print("   Agent1 -> All: Broadcast message")
    
    # Show agent message handling
    print("\n📥 Agent message handling:")
    test_message = {"type": "test", "content": "Hello from Agent1"}
    agent2.handle_message_sync({"from": "agent1", "to": "agent2", "message": test_message})
    
    broadcast_message = {"type": "broadcast", "content": "Hello everyone!"}
    agent1.handle_message_sync({"from": "agent1", "to": "all", "message": broadcast_message})
    agent2.handle_message_sync({"from": "agent1", "to": "all", "message": broadcast_message})
    
    print("✅ Simple communication demo completed")

def main():
    """Main demo function"""
    print("🚀 Price Tracker Agent System - Demo")
    print("=" * 60)
    
    # Run demos
    demo_price_analysis()
    demo_security()
    demo_information_retrieval()
    demo_data_loading()
    demo_simple_communication()
    
    print("\n✅ All demos completed!")
    print("\n📋 To run the full system:")
    print("   python start_price_tracker.py")
    print("\n📋 To run tests:")
    print("   python test_price_tracker.py")
    print("\n📋 To test the API:")
    print("   curl -X POST http://localhost:5000/api/auth/login \\")
    print("     -H 'Content-Type: application/json' \\")
    print("     -d '{\"username\": \"admin\", \"password\": \"admin123\"}'")

if __name__ == "__main__":
    main()
