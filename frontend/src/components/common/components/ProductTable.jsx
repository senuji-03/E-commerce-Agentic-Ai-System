import React, { useState } from 'react';
import { ITEMS } from '../functions/items';

const ProductTable = () => {
  const [sortBy, setSortBy] = useState('id');
  const [sortOrder, setSortOrder] = useState('asc');
  const [filterCategory, setFilterCategory] = useState('All');

  // Get unique categories
  const categories = ['All', ...new Set(ITEMS.map(item => item.type))];

  // Filter and sort products
  const filteredAndSortedItems = ITEMS
    .filter(item => filterCategory === 'All' || item.type === filterCategory)
    .sort((a, b) => {
      let aValue = a[sortBy];
      let bValue = b[sortBy];
      
      if (sortBy === 'price') {
        // Extract numeric value from "Rs. X,XXX" format
        aValue = Number(aValue.replace(/[^\d]/g, ''));
        bValue = Number(bValue.replace(/[^\d]/g, ''));
      }
      
      if (sortOrder === 'asc') {
        return aValue > bValue ? 1 : -1;
      } else {
        return aValue < bValue ? 1 : -1;
      }
    });

  const handleSort = (field) => {
    if (sortBy === field) {
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      setSortBy(field);
      setSortOrder('asc');
    }
  };

  const formatPrice = (price) => {
    // If price is already formatted as "Rs. X,XXX", return as is
    if (typeof price === 'string' && price.startsWith('Rs.')) {
      return price;
    }
    // Otherwise, format as before
    return new Intl.NumberFormat('en-LK', {
      style: 'currency',
      currency: 'LKR',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(price);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-neutral-800 mb-4">
          Complete <span className="gradient-text">Product Catalog</span>
        </h1>
        <p className="text-lg text-neutral-600">
          Browse through our comprehensive collection of products across all categories
        </p>
      </div>

      {/* Filters */}
      <div className="flex flex-wrap gap-4 justify-center mb-8">
        <div className="flex items-center gap-2">
          <label className="text-neutral-700 font-medium">Filter by Category:</label>
          <select
            value={filterCategory}
            onChange={(e) => setFilterCategory(e.target.value)}
            className="px-4 py-2 border border-neutral-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          >
            {categories.map(category => (
              <option key={category} value={category}>{category}</option>
            ))}
          </select>
        </div>
        
        <div className="text-neutral-600">
          Showing {filteredAndSortedItems.length} of {ITEMS.length} products
        </div>
      </div>

      {/* Product Table */}
      <div className="bg-white rounded-xl shadow-soft overflow-hidden border border-neutral-200">
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gradient-to-r from-primary-500 to-primary-600 text-white">
              <tr>
                <th 
                  className="px-6 py-4 text-left font-semibold cursor-pointer hover:bg-primary-600 transition-colors"
                  onClick={() => handleSort('id')}
                >
                  ID {sortBy === 'id' && (sortOrder === 'asc' ? '↑' : '↓')}
                </th>
                <th 
                  className="px-6 py-4 text-left font-semibold cursor-pointer hover:bg-primary-600 transition-colors"
                  onClick={() => handleSort('title')}
                >
                  Product Name {sortBy === 'title' && (sortOrder === 'asc' ? '↑' : '↓')}
                </th>
                <th 
                  className="px-6 py-4 text-left font-semibold cursor-pointer hover:bg-primary-600 transition-colors"
                  onClick={() => handleSort('type')}
                >
                  Category {sortBy === 'type' && (sortOrder === 'asc' ? '↑' : '↓')}
                </th>
                <th 
                  className="px-6 py-4 text-left font-semibold cursor-pointer hover:bg-primary-600 transition-colors"
                  onClick={() => handleSort('price')}
                >
                  Price (Rs.) {sortBy === 'price' && (sortOrder === 'asc' ? '↑' : '↓')}
                </th>
                <th className="px-6 py-4 text-left font-semibold">Rating</th>
                <th className="px-6 py-4 text-left font-semibold">Image</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-neutral-200">
              {filteredAndSortedItems.map((item, index) => (
                <tr 
                  key={item.id} 
                  className={`hover:bg-neutral-50 transition-colors ${index % 2 === 0 ? 'bg-white' : 'bg-neutral-50'}`}
                >
                  <td className="px-6 py-4 font-mono text-sm text-primary-600 font-medium">
                    {item.id}
                  </td>
                  <td className="px-6 py-4">
                    <div>
                      <div className="font-medium text-neutral-900">{item.title}</div>
                      <div className="text-sm text-neutral-500 mt-1">{item.details}</div>
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-primary-100 text-primary-800">
                      {item.type}
                    </span>
                  </td>
                  <td className="px-6 py-4 font-semibold text-neutral-900">
                    {formatPrice(item.price)}
                  </td>
                  <td className="px-6 py-4">
                    <div className="flex items-center gap-1">
                      <span className="text-yellow-500">★</span>
                      <span className="text-sm text-neutral-700">{item.stars}.0</span>
                      <span className="text-xs text-neutral-500">({item.rates})</span>
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    <div className="w-16 h-16 rounded-lg overflow-hidden border border-neutral-200">
                      <img 
                        src={item.imageSrc} 
                        alt={item.title}
                        className="w-full h-full object-cover"
                        onError={(e) => {
                          e.target.src = '/placeholder-image.png';
                          e.target.alt = 'Image not available';
                        }}
                      />
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Summary */}
      <div className="mt-8 text-center">
        <div className="inline-flex items-center gap-8 bg-white px-8 py-4 rounded-xl shadow-soft border border-neutral-200">
          <div>
            <div className="text-2xl font-bold text-primary-600">{ITEMS.length}</div>
            <div className="text-sm text-neutral-600">Total Products</div>
          </div>
          <div className="w-px h-12 bg-neutral-300"></div>
          <div>
            <div className="text-2xl font-bold text-accent-600">{categories.length - 1}</div>
            <div className="text-sm text-neutral-600">Categories</div>
          </div>
          <div className="w-px h-12 bg-neutral-300"></div>
          <div>
            <div className="text-2xl font-bold text-green-600">
              {formatPrice(ITEMS.reduce((sum, item) => sum + item.price, 0))}
            </div>
            <div className="text-sm text-neutral-600">Total Value</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductTable;
