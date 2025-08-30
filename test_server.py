#!/usr/bin/env python3
"""
Simple server test script for the Price Tracker Agent System
Tests if the Flask server is running and responding correctly
"""

import requests
import json
import time

def test_server():
    """Test the server endpoints"""
    base_url = "http://127.0.0.1:5000"
    
    print("🧪 Testing Price Tracker Agent System Server")
    print("=" * 60)
    
    # Test 1: Home endpoint
    print("\n1️⃣ Testing Home Endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            data = response.json()
            print("✅ Home endpoint working!")
            print(f"   Message: {data.get('message', 'N/A')}")
            print(f"   Version: {data.get('version', 'N/A')}")
            print(f"   Available endpoints: {len(data.get('endpoints', {}))}")
        else:
            print(f"❌ Home endpoint failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Is it running?")
        print("   Start the server with: python start_price_tracker.py")
        return False
    except Exception as e:
        print(f"❌ Error testing home endpoint: {e}")
        return False
    
    # Test 2: Test endpoint
    print("\n2️⃣ Testing Health Check Endpoint...")
    try:
        response = requests.get(f"{base_url}/api/test")
        if response.status_code == 200:
            data = response.json()
            print("✅ Health check working!")
            print(f"   Status: {data.get('status', 'N/A')}")
            print(f"   Message: {data.get('message', 'N/A')}")
            print(f"   Agents: {data.get('agents', [])}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error testing health check: {e}")
        return False
    
    # Test 3: Login endpoint
    print("\n3️⃣ Testing Authentication Endpoint...")
    try:
        login_data = {"username": "admin", "password": "admin123"}
        response = requests.post(
            f"{base_url}/api/auth/login",
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            token = data.get('token')
            print("✅ Authentication working!")
            print(f"   Message: {data.get('message', 'N/A')}")
            print(f"   Token received: {'Yes' if token else 'No'}")
            
            if token:
                # Test 4: Price analysis with token
                print("\n4️⃣ Testing Price Analysis Endpoint...")
                headers = {"Authorization": f"Bearer {token}"}
                response = requests.get(f"{base_url}/api/analyze/e1", headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    print("✅ Price analysis working!")
                    print(f"   Product ID: {data.get('product_id', 'N/A')}")
                    print(f"   Current Price: {data.get('current_price', 'N/A')}")
                    print(f"   Trend: {data.get('trend', 'N/A')}")
                    print(f"   Predicted Price: {data.get('predicted_price', 'N/A')}")
                    
                    # Test 5: Price alerts
                    print("\n5️⃣ Testing Price Alerts Endpoint...")
                    response = requests.get(f"{base_url}/api/alerts?threshold=3.0", headers=headers)
                    
                    if response.status_code == 200:
                        data = response.json()
                        print("✅ Price alerts working!")
                        print(f"   Number of alerts: {len(data)}")
                        if data:
                            alert = data[0]
                            print(f"   Sample alert: Product {alert.get('product_id')} - {alert.get('change_percent')}% change")
                    else:
                        print(f"❌ Price alerts failed: {response.status_code}")
                        
                    # Test 6: Market insights
                    print("\n6️⃣ Testing Market Insights Endpoint...")
                    response = requests.get(f"{base_url}/api/insights", headers=headers)
                    
                    if response.status_code == 200:
                        data = response.json()
                        print("✅ Market insights working!")
                        print(f"   Total products: {data.get('total_products', 'N/A')}")
                        print(f"   Market trend: {data.get('market_trend', 'N/A')}")
                        print(f"   Categories: {len(data.get('categories', []))}")
                    else:
                        print(f"❌ Market insights failed: {response.status_code}")
                        
                else:
                    print(f"❌ Price analysis failed: {response.status_code}")
                    print(f"   Response: {response.text}")
            else:
                print("❌ No token received from login")
                return False
                
        else:
            print(f"❌ Authentication failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing authentication: {e}")
        return False
    
    print("\n🎉 All tests completed successfully!")
    print("\n📋 Server is working correctly. You can now:")
    print("   - Use the API endpoints in your frontend")
    print("   - Test with Postman or curl")
    print("   - Integrate with your React application")
    
    return True

def main():
    """Main function"""
    print("🚀 Price Tracker Agent System - Server Test")
    print("=" * 60)
    
    # Wait a moment for server to be ready
    print("⏳ Waiting for server to be ready...")
    time.sleep(2)
    
    # Run tests
    success = test_server()
    
    if success:
        print("\n✅ Server is fully functional!")
    else:
        print("\n❌ Server has issues. Check the error messages above.")
        print("\n🔧 Troubleshooting:")
        print("   1. Make sure server is running: python start_price_tracker.py")
        print("   2. Check console for error messages")
        print("   3. Verify all dependencies are installed")
        print("   4. Check if port 5000 is available")

if __name__ == "__main__":
    main()
