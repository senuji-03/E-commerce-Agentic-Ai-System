import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const PriceTracker = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [token, setToken] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [priceData, setPriceData] = useState(null);
  const [alerts, setAlerts] = useState([]);
  const [insights, setInsights] = useState(null);
  
  const navigate = useNavigate();

  // Login function
  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      const response = await fetch('http://127.0.0.1:5000/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: 'admin',
          password: 'admin123'
        })
      });
      
      const data = await response.json();
      
      if (response.ok) {
        setToken(data.token);
        setIsAuthenticated(true);
        localStorage.setItem('agentToken', data.token);
      } else {
        setError(data.error || 'Login failed');
      }
    } catch (err) {
      setError('Cannot connect to agent system. Make sure the Python server is running.');
    } finally {
      setLoading(false);
    }
  };

  // Fetch price analysis
  const fetchPriceAnalysis = async (productId) => {
    if (!token) return;
    
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/analyze/${productId}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      
      if (response.ok) {
        const data = await response.json();
        setPriceData(data);
      }
    } catch (err) {
      console.error('Error fetching price analysis:', err);
    }
  };

  // Fetch price alerts
  const fetchAlerts = async () => {
    if (!token) return;
    
    try {
      const response = await fetch('http://127.0.0.1:5000/api/alerts?threshold=3.0', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      
      if (response.ok) {
        const data = await response.json();
        setAlerts(data);
      }
    } catch (err) {
      console.error('Error fetching alerts:', err);
    }
  };

  // Fetch market insights
  const fetchInsights = async () => {
    if (!token) return;
    
    try {
      const response = await fetch('http://127.0.0.1:5000/api/insights', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      
      if (response.ok) {
        const data = await response.json();
        setInsights(data);
      }
    } catch (err) {
      console.error('Error fetching insights:', err);
    }
  };

  // Load token from localStorage on component mount
  useEffect(() => {
    const savedToken = localStorage.getItem('agentToken');
    if (savedToken) {
      setToken(savedToken);
      setIsAuthenticated(true);
    }
  }, []);

  // Fetch data when authenticated
  useEffect(() => {
    if (isAuthenticated && token) {
      fetchAlerts();
      fetchInsights();
    }
  }, [isAuthenticated, token]);

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4">
        <div className="max-w-md mx-auto bg-white rounded-xl shadow-lg p-8">
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold text-gray-900 mb-2">🤖 AI Agent System</h1>
            <p className="text-gray-600">Access the intelligent price tracking agents</p>
          </div>
          
          <form onSubmit={handleLogin} className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Username
              </label>
              <input
                type="text"
                defaultValue="admin"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                readOnly
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Password
              </label>
              <input
                type="password"
                defaultValue="admin123"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                readOnly
              />
            </div>
            
            {error && (
              <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-md">
                {error}
              </div>
            )}
            
            <button
              type="submit"
              disabled={loading}
              className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'Connecting...' : 'Connect to AI Agents'}
            </button>
          </form>
          
          <div className="mt-6 text-center text-sm text-gray-500">
            <p>Default credentials: admin / admin123</p>
            <p className="mt-2">Make sure the Python agent server is running on port 5000</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8 px-4">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">🤖 AI Price Tracker Agents</h1>
          <p className="text-xl text-gray-600">Intelligent price analysis powered by multiple AI agents</p>
          <button
            onClick={() => {
              setIsAuthenticated(false);
              setToken('');
              localStorage.removeItem('agentToken');
            }}
            className="mt-4 px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700"
          >
            Disconnect
          </button>
        </div>

        {/* Quick Actions */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white p-6 rounded-xl shadow-lg">
            <h3 className="text-lg font-semibold mb-4">🔍 Quick Price Analysis</h3>
            <div className="space-y-3">
              <input
                type="text"
                placeholder="Enter product ID (e.g., e1, f1)"
                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                onKeyPress={(e) => {
                  if (e.key === 'Enter') {
                    fetchPriceAnalysis(e.target.value);
                  }
                }}
              />
              <button
                onClick={() => {
                  const input = document.querySelector('input[placeholder*="product ID"]');
                  if (input.value) fetchPriceAnalysis(input.value);
                }}
                className="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700"
              >
                Analyze Price
              </button>
            </div>
          </div>

          <div className="bg-white p-6 rounded-xl shadow-lg">
            <h3 className="text-lg font-semibold mb-4">🚨 Price Alerts</h3>
            <p className="text-gray-600 mb-3">Current alerts: {alerts.length}</p>
            <button
              onClick={fetchAlerts}
              className="w-full bg-red-600 text-white py-2 rounded-md hover:bg-red-700"
            >
              Refresh Alerts
            </button>
          </div>

          <div className="bg-white p-6 rounded-xl shadow-lg">
            <h3 className="text-lg font-semibold mb-4">📊 Market Insights</h3>
            <p className="text-gray-600 mb-3">Latest market data</p>
            <button
              onClick={fetchInsights}
              className="w-full bg-green-600 text-white py-2 rounded-md hover:bg-green-700"
            >
              Get Insights
            </button>
          </div>
        </div>

        {/* Price Analysis Results */}
        {priceData && (
          <div className="bg-white rounded-xl shadow-lg p-6 mb-8">
            <h3 className="text-2xl font-bold mb-6">📈 Price Analysis Results</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <div className="text-center">
                <div className="text-3xl font-bold text-blue-600">{priceData.current_price}</div>
                <div className="text-sm text-gray-600">Current Price</div>
              </div>
              <div className="text-center">
                <div className={`text-3xl font-bold ${priceData.price_change >= 0 ? 'text-green-600' : 'text-red-600'}`}>
                  {priceData.price_change >= 0 ? '+' : ''}{priceData.price_change}
                </div>
                <div className="text-sm text-gray-600">Price Change</div>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold text-purple-600">{priceData.trend}</div>
                <div className="text-sm text-gray-600">Trend</div>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold text-orange-600">{priceData.predicted_price}</div>
                <div className="text-sm text-gray-600">Predicted Price</div>
              </div>
            </div>
            
            {priceData.llm_insights && (
              <div className="mt-6 p-4 bg-blue-50 rounded-lg">
                <h4 className="font-semibold mb-2">🤖 AI Insights</h4>
                <p className="text-gray-700">{priceData.llm_insights}</p>
              </div>
            )}
          </div>
        )}

        {/* Price Alerts */}
        {alerts.length > 0 && (
          <div className="bg-white rounded-xl shadow-lg p-6 mb-8">
            <h3 className="text-2xl font-bold mb-6">🚨 Price Alerts</h3>
            <div className="space-y-4">
              {alerts.map((alert, index) => (
                <div key={index} className="flex items-center justify-between p-4 bg-red-50 rounded-lg border border-red-200">
                  <div>
                    <div className="font-semibold">Product {alert.product_id}</div>
                    <div className="text-sm text-gray-600">
                      {alert.change_percent}% change detected
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="font-semibold">Rs. {alert.current_price}</div>
                    <div className="text-sm text-gray-600">
                      Previous: Rs. {alert.previous_price}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Market Insights */}
        {insights && (
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-2xl font-bold mb-6">📊 Market Insights</h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="text-center p-4 bg-blue-50 rounded-lg">
                <div className="text-3xl font-bold text-blue-600">{insights.total_products}</div>
                <div className="text-sm text-gray-600">Total Products</div>
              </div>
              <div className="text-center p-4 bg-green-50 rounded-lg">
                <div className="text-3xl font-bold text-green-600">{insights.market_trend}</div>
                <div className="text-sm text-gray-600">Market Trend</div>
              </div>
              <div className="text-center p-4 bg-purple-50 rounded-lg">
                <div className="text-3xl font-bold text-purple-600">{insights.categories.length}</div>
                <div className="text-sm text-gray-600">Categories</div>
              </div>
            </div>
            
            <div className="mt-6">
              <h4 className="font-semibold mb-3">Product Categories</h4>
              <div className="flex flex-wrap gap-2">
                {insights.categories.map((category, index) => (
                  <span key={index} className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm">
                    {category}
                  </span>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default PriceTracker;
