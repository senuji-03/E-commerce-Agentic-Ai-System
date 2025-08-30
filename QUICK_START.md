# 🚀 Quick Start Guide - Price Tracker Agent System

## ⚡ **Get Started in 5 Minutes!**

### 1. **Install Dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2. **Configure Environment**
```bash
# Copy the example config
cp config.env.example config.env

# Edit config.env with your OpenAI API key
# (You already have one in the example file!)
```

### 3. **Test the System**
```bash
# Run the demo (recommended first)
python demo_price_tracker.py

# Or run tests
python test_price_tracker.py
```

### 4. **Start the Full System**
```bash
python start_price_tracker.py
```

### 5. **Access the API**
- **URL**: `http://localhost:5000`
- **Login**: `admin` / `admin123`

## 🔧 **What Each Script Does**

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `demo_price_tracker.py` | **Demo mode** - Shows all features without starting server | ✅ **Start here!** |
| `test_price_tracker.py` | **Test mode** - Comprehensive testing | After demo |
| `start_price_tracker.py` | **Production mode** - Starts full API server | When ready to use API |
| `price_tracker_agent.py` | **Core system** - Main agent system | Imported by other scripts |

## 🧪 **Try the Demo First**

The demo script shows:
- ✅ Price analysis and predictions
- ✅ Security features (auth, encryption)
- ✅ Information retrieval
- ✅ Data loading from your JSON file
- ✅ Agent communication

**No server startup required!** Perfect for testing.

## 🚨 **Troubleshooting**

### **Common Issues:**

1. **"Module not found" errors**
   ```bash
   pip install -r requirements.txt
   ```

2. **spaCy model missing**
   ```bash
   python -m spacy download en_core_web_sm
   ```

3. **Port 5000 already in use**
   ```bash
   # Kill the process using port 5000
   lsof -ti:5000 | xargs kill -9
   ```

4. **JSON file not found**
   - Make sure `frontend/src/data/pricehistory.json` exists
   - Check the file path in your project

### **Test Commands:**

```bash
# Test individual components
python -c "from price_tracker_agent import PriceAnalysisAgent; print('✅ Import successful')"

# Test data loading
python -c "import json; data=json.load(open('frontend/src/data/pricehistory.json')); print(f'✅ Loaded {len(data)} price records')"
```

## 🌟 **What You'll See**

### **Demo Output:**
```
🚀 Price Tracker Agent System - Demo
============================================================

🧪 Demo: Price Analysis Agent
==================================================

📊 Price Analysis Results:

Product: e1
  product_id: e1
  current_price: 4950
  previous_price: 5000
  price_change: -50
  price_change_percent: -1.0
  trend: decreasing
  volatility: 75.0
  predicted_price: 4900
  prediction_confidence: 0.85
  data_points: 3

🚨 Price Alerts (threshold: 3%):
  e1: 1.0% change
  f1: 2.0% change

🔐 Demo: Security Manager
==================================================
Testing authentication...
✅ Authentication successful
   Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...

🔍 Demo: Information Retrieval Agent
==================================================
✅ Product search results:
   e1: Wireless Mouse (Electronics)
   f1: Men's T-Shirt (Fashion)
   bp1: Facial Cleanser (Beauty)

📁 Demo: Data Loading
==================================================
✅ Loaded price data for 100 products
   Sample product e1: 3 price points
   Price range: Rs. 300 - Rs. 350,000

   Category distribution:
     Electronics: 20 products
     Fashion: 20 products
     Beauty & Personal Care: 20 products
     Home & Living: 20 products
     Kitchen & Dining: 20 products

🌐 Demo: Simple Communication
==================================================
✅ Agents registered successfully
   Registered agents: ['agent1', 'agent2']

📤 Simulating message sending...
   Agent1 -> Agent2: Test message
   Agent1 -> All: Broadcast message

📥 Agent message handling:
   📨 Agent2 received: {'type': 'test', 'content': 'Hello from Agent1'}
   📨 Agent1 received: {'type': 'broadcast', 'content': 'Hello everyone!'}
   📨 Agent2 received: {'type': 'broadcast', 'content': 'Hello everyone!'}
✅ Simple communication demo completed

✅ All demos completed!
```

## 🚀 **Next Steps**

1. **Run the demo**: `python demo_price_tracker.py`
2. **Start the API**: `python start_price_tracker.py`
3. **Test the API**: Use the curl commands in the README
4. **Integrate**: Connect to your frontend or other systems

## 💡 **Pro Tips**

- **Start with demo**: Always run `demo_price_tracker.py` first
- **Check logs**: Console output shows what's happening
- **API testing**: Use Postman or curl for API testing
- **Environment**: Make sure your OpenAI API key is set

---

**🎯 Ready to go? Run `python demo_price_tracker.py` and see the magic!**
