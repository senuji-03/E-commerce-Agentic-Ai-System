# 🧪 **Complete Testing Guide - Price Tracker Agent System**

## 🚨 **Problem: 404 Error Fixed!**

The issue was that the Flask routes weren't properly configured. I've fixed this by adding:
- ✅ **Home route** (`/`) - Shows API documentation
- ✅ **Test route** (`/api/test`) - Verifies server is working
- ✅ **All API routes** properly configured

## 🔧 **Step-by-Step Testing Process**

### **Step 1: Restart the Server**
```bash
# Stop the current server (Ctrl+C)
# Then restart it
python start_price_tracker.py
```

### **Step 2: Test Basic Connectivity**
Open your browser and go to:
```
http://127.0.0.1:5000/
```

**Expected Result:** You should see a JSON response with API documentation:
```json
{
  "message": "Price Tracker Agent System API",
  "version": "1.0.0",
  "endpoints": {
    "home": "/",
    "login": "/api/auth/login",
    "analyze": "/api/analyze/<product_id>",
    "alerts": "/api/alerts",
    "search": "/api/search",
    "insights": "/api/insights"
  }
}
```

### **Step 3: Test Server Health**
```
http://127.0.0.1:5000/api/test
```

**Expected Result:** Server status and agent information:
```json
{
  "status": "success",
  "message": "Price Tracker Agent System is running!",
  "timestamp": "2025-01-XX...",
  "agents": ["security", "llm", "price_analysis", "info_retrieval"]
}
```

## 🌐 **Testing All API Endpoints**

### **1. Authentication Test**
```bash
# Test login endpoint
curl -X POST http://127.0.0.1:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Expected Result:**
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "message": "Login successful"
}
```

### **2. Price Analysis Test**
```bash
# First get a token (copy from login response)
TOKEN="your-token-here"

# Test price analysis for product e1
curl -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:5000/api/analyze/e1
```

**Expected Result:**
```json
{
  "product_id": "e1",
  "current_price": 4950,
  "previous_price": 5000,
  "price_change": -50,
  "price_change_percent": -1.0,
  "trend": "decreasing",
  "volatility": 75.0,
  "predicted_price": 4900,
  "prediction_confidence": 0.85,
  "data_points": 3,
  "llm_insights": "AI analysis of price trends..."
}
```

### **3. Price Alerts Test**
```bash
# Get price alerts with 3% threshold
curl -H "Authorization: Bearer $TOKEN" \
  "http://127.0.0.1:5000/api/alerts?threshold=3.0"
```

**Expected Result:**
```json
[
  {
    "product_id": "e1",
    "current_price": 4950,
    "previous_price": 5000,
    "change_percent": 1.0,
    "alert_type": "price_change",
    "timestamp": "2025-01-XX..."
  }
]
```

### **4. Product Search Test**
```bash
# Search for products
curl -X POST http://127.0.0.1:5000/api/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"query": "wireless mouse"}'
```

**Expected Result:**
```json
[
  {"id": "e1", "name": "Wireless Mouse", "category": "Electronics"},
  {"id": "f1", "name": "Men's T-Shirt", "category": "Fashion"}
]
```

### **5. Market Insights Test**
```bash
# Get market insights
curl -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:5000/api/insights
```

**Expected Result:**
```json
{
  "total_products": 100,
  "categories": ["Electronics", "Fashion", "Kitchen & Dining", "Beauty & Personal Care", "Home & Living"],
  "price_range": {"min": 300, "max": 350000},
  "market_trend": "stable",
  "last_updated": "2025-01-XX..."
}
```

## 🧪 **Browser Testing (Easier)**

### **1. Test Home Page**
- Open: `http://127.0.0.1:5000/`
- Should show API documentation

### **2. Test Health Check**
- Open: `http://127.0.0.1:5000/api/test`
- Should show server status

### **3. Test Authentication (Using Browser Dev Tools)**
```javascript
// In browser console
fetch('http://127.0.0.1:5000/api/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ username: 'admin', password: 'admin123' })
})
.then(r => r.json())
.then(console.log);
```

### **4. Test Price Analysis (After getting token)**
```javascript
// Replace YOUR_TOKEN with actual token
fetch('http://127.0.0.1:5000/api/analyze/e1', {
  headers: { 'Authorization': 'Bearer YOUR_TOKEN' }
})
.then(r => r.json())
.then(console.log);
```

## 🐛 **Troubleshooting Common Issues**

### **Issue 1: Still Getting 404**
**Solution:**
1. Make sure server is running: `python start_price_tracker.py`
2. Check console for any error messages
3. Verify the server started successfully

### **Issue 2: Import Errors**
**Solution:**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### **Issue 3: Port Already in Use**
**Solution:**
```bash
# Kill process using port 5000
lsof -ti:5000 | xargs kill -9
# Or change port in config.env
```

### **Issue 4: Authentication Fails**
**Solution:**
- Default credentials: `admin` / `admin123`
- Check if JWT_SECRET is set in config.env

## 📱 **Testing with Postman (Recommended)**

### **1. Import Collection**
Create a new collection in Postman with these requests:

#### **Login Request**
- **Method:** POST
- **URL:** `http://127.0.0.1:5000/api/auth/login`
- **Headers:** `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

#### **Price Analysis Request**
- **Method:** GET
- **URL:** `http://127.0.0.1:5000/api/analyze/e1`
- **Headers:** `Authorization: Bearer {{token}}`

#### **Price Alerts Request**
- **Method:** GET
- **URL:** `http://127.0.0.1:5000/api/alerts?threshold=3.0`
- **Headers:** `Authorization: Bearer {{token}}`

### **2. Set Environment Variables**
- Create environment variable: `token`
- Set it from login response

## 🎯 **What to Expect When Working**

### **✅ Success Indicators:**
1. **Server starts** without errors
2. **Home page** (`/`) shows API docs
3. **Test endpoint** (`/api/test`) works
4. **Login** returns JWT token
5. **All API calls** return proper data
6. **Console shows** agent registration messages

### **❌ Failure Indicators:**
1. **404 errors** on all routes
2. **Import errors** when starting
3. **Port conflicts**
4. **Authentication failures**
5. **Empty responses** from API

## 🚀 **Next Steps After Testing**

Once everything works:

1. **Integrate with React frontend** (see integration guide)
2. **Add more sophisticated analysis**
3. **Implement real-time price monitoring**
4. **Add user management system**
5. **Scale the system**

## 💡 **Pro Tips**

- **Always start with** `/` and `/api/test` endpoints
- **Use Postman** for easier API testing
- **Check console logs** for detailed error messages
- **Test authentication first**, then other endpoints
- **Keep the demo script** for quick functionality checks

---

**🎯 Ready to test? Follow this guide step by step and you'll see your intelligent agents in action!**
