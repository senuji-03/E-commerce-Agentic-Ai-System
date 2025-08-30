#!/usr/bin/env python3
"""
Startup script for the Price Tracker Agent System
Provides a simple way to start the system with configuration
"""

import os
import sys
import asyncio
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'flask', 'numpy', 'pandas', 'sklearn', 'openai', 
        'transformers', 'spacy', 'cryptography', 'jwt'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install with: pip install -r requirements.txt")
        return False
    
    return True

def check_config():
    """Check if configuration is set up"""
    config_file = Path("config.env")
    if not config_file.exists():
        print("⚠️  Configuration file not found.")
        print("📝 Copy config.env.example to config.env and configure it.")
        return False
    
    # Check for required environment variables
    required_vars = ['OPENAI_API_KEY']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("⚠️  Missing environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n🔑 Set them in your environment or config.env file")
        return False
    
    return True

def check_data_file():
    """Check if price history data file exists"""
    data_file = Path("frontend/src/data/pricehistory.json")
    if not data_file.exists():
        print("❌ Price history data file not found:")
        print(f"   {data_file}")
        print("\n📁 Make sure the file exists and the path is correct")
        return False
    
    return True

async def start_system():
    """Start the price tracker system"""
    try:
        from price_tracker_agent import PriceTrackerSystem
        
        system = PriceTrackerSystem()
        await system.start_system()
        
    except KeyboardInterrupt:
        print("\n🛑 System stopped by user")
        # Clean up communication manager
        if hasattr(system, 'communication_manager'):
            system.communication_manager.stop()
    except Exception as e:
        print(f"\n❌ Error starting system: {e}")
        print("🔍 Check the logs for more details")
        raise

def main():
    """Main startup function"""
    print("🚀 Price Tracker Agent System - Startup")
    print("=" * 50)
    
    # Check dependencies
    print("🔍 Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    print("✅ Dependencies OK")
    
    # Check configuration
    print("🔍 Checking configuration...")
    if not check_config():
        print("⚠️  Configuration issues found, but continuing...")
    else:
        print("✅ Configuration OK")
    
    # Check data file
    print("🔍 Checking data file...")
    if not check_data_file():
        sys.exit(1)
    print("✅ Data file OK")
    
    # Start the system
    print("\n🚀 Starting Price Tracker System...")
    print("📡 System will be available at: http://localhost:5000")
    print("🔑 Default credentials: admin / admin123")
    print("⏹️  Press Ctrl+C to stop the system")
    print("=" * 50)
    
    try:
        asyncio.run(start_system())
    except KeyboardInterrupt:
        print("\n🛑 System stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting system: {e}")
        print("🔍 Check the logs for more details")
        sys.exit(1)

if __name__ == "__main__":
    main()
