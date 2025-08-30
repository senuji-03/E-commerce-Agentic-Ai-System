# 🚀 Price Tracker Agent System

A sophisticated multi-agent system for intelligent price tracking and analysis with advanced AI capabilities.

## ✨ Features

### 🤖 **Multiple Interacting Intelligent Agents**
- **SecurityManager Agent**: Handles authentication, input sanitization, and encryption
- **LLMAgent**: Provides LLM-powered natural language processing and analysis
- **PriceAnalysisAgent**: Analyzes price trends and makes predictions
- **InformationRetrievalAgent**: Manages data retrieval and organization
- **CommunicationManager**: Coordinates inter-agent communication

### 🧠 **LLM Integration**
- OpenAI GPT-3.5-turbo integration for intelligent price analysis
- Natural language insights and trend explanations
- Context-aware price recommendations

### 🔍 **NLP Techniques**
- **Named Entity Recognition (NER)**: Extracts product names, categories, and entities
- **Text Summarization**: Condenses long price analysis reports
- **Sentiment Analysis**: Analyzes market sentiment from text data

### 📊 **Information Retrieval Module**
- Advanced product search capabilities
- Market insights and analytics
- Caching system for improved performance

### 🔐 **Security Features**
- **JWT Authentication**: Secure user authentication system
- **Input Sanitization**: Prevents injection attacks
- **Data Encryption**: Encrypts sensitive information
- **Token Management**: Secure session handling

### 🌐 **Agent Communication Protocols**
- **HTTP REST API**: External system integration
- **Asynchronous Messaging**: Inter-agent communication
- **Socket Support**: Real-time communication capabilities
- **Message Queuing**: Reliable message delivery

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd price-tracker-system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install spaCy Model
```bash
python -m spacy download en_core_web_sm
```

### 4. Configure Environment
```bash
cp config.env.example config.env
# Edit config.env with your API keys and configuration
```

### 5. Set Up API Keys
```bash
# Get your OpenAI API key from: https://platform.openai.com/
export OPENAI_API_KEY="your-api-key-here"
```

## 🚀 Usage

### Starting the System
```bash
python price_tracker_agent.py
```

The system will start on `http://localhost:5000`

### API Endpoints

#### Authentication
```bash
POST /api/auth/login
{
    "username": "admin",
    "password": "admin123"
}
```

#### Price Analysis
```bash
GET /api/analyze/{product_id}
Authorization: Bearer {your-jwt-token}
```

#### Price Alerts
```bash
GET /api/alerts?threshold=5.0
Authorization: Bearer {your-jwt-token}
```

#### Product Search
```bash
POST /api/search
Authorization: Bearer {your-jwt-token}
{
    "query": "wireless mouse"
}
```

#### Market Insights
```bash
GET /api/insights
Authorization: Bearer {your-jwt-token}
```

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key
- `JWT_SECRET`: Secret key for JWT tokens
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 5000)
- `ENCRYPTION_KEY`: Encryption key for sensitive data

### Price Alert Settings
- `DEFAULT_ALERT_THRESHOLD`: Default percentage change for alerts (default: 5.0%)
- `ALERT_CHECK_INTERVAL`: How often to check for alerts (default: 5 minutes)

## 📊 Data Structure

### Price History JSON Format
```json
[
  {
    "product_id": "e1",
    "date": "2025-08-01",
    "price": 5100
  }
]
```

### Product Categories
- **Electronics (e1-e20)**: Computers, phones, accessories
- **Fashion (f1-f20)**: Clothing, shoes, accessories
- **Kitchen & Dining (hk1-hk20)**: Appliances, cookware
- **Beauty & Personal Care (bp1-bp20)**: Cosmetics, personal care
- **Home & Living (hl1-hl20)**: Furniture, home decor

## 🧪 Testing

### Test the API
```bash
# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Get token from response and use it
TOKEN="your-jwt-token-here"

# Analyze a product
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5000/api/analyze/e1

# Get price alerts
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5000/api/alerts?threshold=3.0
```

## 🔍 Example Analysis Output

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
  "llm_insights": "The wireless mouse shows a slight downward trend with moderate volatility. This suggests a competitive market with potential for further price adjustments."
}
```

## 🚨 Price Alerts

The system automatically monitors price changes and generates alerts when:
- Price changes exceed the threshold percentage
- Significant volatility is detected
- Unusual price patterns are identified

## 🔮 Future Enhancements

- **Real-time Price Monitoring**: Web scraping and API integration
- **Machine Learning Models**: Advanced prediction algorithms
- **Market Sentiment Analysis**: Social media and news integration
- **Portfolio Management**: Track multiple products and categories
- **Mobile App**: React Native mobile application
- **Dashboard**: Real-time analytics dashboard

## 🐛 Troubleshooting

### Common Issues

1. **OpenAI API Error**
   - Verify your API key is correct
   - Check your OpenAI account balance
   - Ensure the API key has proper permissions

2. **spaCy Model Not Found**
   ```bash
   python -m spacy download en_core_web_sm
   ```

3. **Port Already in Use**
   - Change the port in config.env
   - Kill the process using the port: `lsof -ti:5000 | xargs kill -9`

4. **Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

### Logs
Check the console output for detailed error messages and system status.

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the troubleshooting section

---

**Built with ❤️ using Python, Flask, OpenAI, and advanced AI technologies**
