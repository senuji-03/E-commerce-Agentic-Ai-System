# E-commerce Agentic AI System - Updated

## 🎯 Project Overview
A modern, responsive e-commerce platform built with React, featuring a comprehensive product catalog with 5 main categories and an elegant, modern design system.

## ✨ New Features & Updates

### 🏷️ Product Categories
The system now features **5 main product categories** with **100 products total**:

1. **Electronics** (20 products) - e1 to e20
   - Wireless Mouse, Bluetooth Headphones, Smartwatch, Laptop, etc.
   - Price range: LKR 1,500 - LKR 350,000

2. **Fashion** (20 products) - f1 to f20
   - Men's/Women's T-Shirts, Jeans, Hoodies, Dresses, etc.
   - Price range: LKR 800 - LKR 10,000

3. **Kitchen & Dining** (20 products) - hk1 to hk20
   - Blender, Air Fryer, Microwave Oven, Coffee Maker, etc.
   - Price range: LKR 1,200 - LKR 40,000

4. **Beauty & Personal Care** (20 products) - bp1 to bp20
   - Facial Cleanser, Moisturizer, Shampoo, Makeup Kit, etc.
   - Price range: LKR 300 - LKR 5,000

5. **Home & Living** (20 products) - hl1 to hl20
   - Sofa Set, Dining Table, Office Chair, Bookshelf, etc.
   - Price range: LKR 3,800 - LKR 120,000

### 🎨 Modern Theme & Design
- **New Color Palette**: Modern primary, accent, and neutral colors
- **Gradient Backgrounds**: Beautiful gradient overlays and backgrounds
- **Enhanced Shadows**: Soft, elegant shadow system
- **Modern Typography**: Inter font family for better readability
- **Improved Scrollbars**: Custom styled scrollbars with gradients
- **Responsive Design**: Mobile-first approach with modern breakpoints

### 📊 Product Catalog Table
- **Complete Product Table**: View all 100 products in a sortable table
- **Category Filtering**: Filter products by category
- **Sortable Columns**: Sort by ID, Product Name, Category, or Price
- **Price Formatting**: LKR currency formatting
- **Product Images**: Thumbnail images for each product
- **Rating Display**: Star ratings and review counts

## 🚀 Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn

### Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd E-commerce-Agentic-Ai-System
```

2. Install dependencies:
```bash
cd frontend
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:5173`

## 🛠️ Technology Stack

- **Frontend**: React 18 with Vite
- **Styling**: Tailwind CSS with custom design system
- **UI Components**: Material-UI (MUI)
- **State Management**: React Context API
- **Routing**: React Router v6
- **Icons**: Emoji icons and custom SVGs
- **Animations**: CSS transitions and hover effects

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── common/
│   │   │   ├── components/
│   │   │   │   ├── ProductTable.jsx    # New: Complete product catalog
│   │   │   │   └── ...
│   │   │   └── functions/
│   │   │       └── items.js            # Updated: New product database
│   │   ├── Home/
│   │   │   └── Categories.jsx          # Updated: New category design
│   │   └── Header/
│   │       └── Navigations.jsx         # Updated: Added ProductTable link
│   ├── Pages/
│   │   ├── Category.jsx                # Updated: New category filtering
│   │   └── ...
│   ├── App.jsx                         # Updated: Modern styling
│   ├── index.css                       # Updated: New design system
│   └── routes.js                       # Updated: Added ProductTable route
├── tailwind.config.js                  # Updated: New color scheme
└── ...
```

## 🎯 Key Routes

- `/` - Home page with category overview
- `/category` - Browse products by category
- `/productTable` - Complete product catalog table
- `/allProducts` - All products grid view
- `/cart` - Shopping cart
- `/wishlist` - User wishlist
- `/checkout` - Checkout process

## 🔧 Customization

### Adding New Products
Edit `frontend/src/components/common/functions/items.js` to add new products:

```javascript
{
  id: "unique_id",
  imageSrc: "../assets/Category/ProductImage.jpg",
  title: "Product Name",
  price: 5000,
  stars: 4,
  rates: 100,
  discount: "",
  quantity: 0,
  type: "Category Name",
  details: "Product description",
}
```

### Modifying Theme Colors
Edit `frontend/tailwind.config.js` to customize the color scheme:

```javascript
colors: {
  'primary': {
    500: '#0ea5e9',  // Main brand color
    600: '#0284c7',  // Darker shade
  },
  'accent': {
    500: '#d946ef',  // Accent color
  }
}
```

## 📱 Responsive Design

The application is fully responsive with breakpoints:
- **Mobile**: xs (0px+)
- **Tablet**: sm (640px+)
- **Desktop**: md (768px+)
- **Large Desktop**: lg (1024px+)
- **Extra Large**: xl (1280px+)

## 🎨 Design System

### Color Palette
- **Primary**: Blue tones (#0ea5e9, #0284c7)
- **Accent**: Purple tones (#d946ef, #c026d3)
- **Neutral**: Gray scale (#fafafa to #171717)

### Typography
- **Primary Font**: Inter (modern, clean)
- **Fallbacks**: system-ui, sans-serif

### Shadows
- **Soft**: Subtle shadows for cards
- **Elegant**: Enhanced shadows for hover effects
- **Glow**: Special glow effects for buttons

## 🚀 Deployment

The application is configured for deployment on Vercel:

1. Build the project:
```bash
npm run build
```

2. Deploy to Vercel:
```bash
vercel --prod
```

## 📈 Future Enhancements

- [ ] Advanced search and filtering
- [ ] Product comparison tools
- [ ] User reviews and ratings system
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Dark mode toggle
- [ ] Product recommendations
- [ ] Inventory management system

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Developer

**Mahmoud Mansy**
- LinkedIn: [Mahmoud Mansy](https://www.linkedin.com/in/mahmoud-mansy-a189a5232/)
- GitHub: [GitHub Profile]

---

**Last Updated**: December 2024
**Version**: 2.0.0 - Modern Theme & Product Categories
