import RedTitle from "../common/components/RedTitle";
import PropTypes from "prop-types";
import Arrows from "../common/components/Arrows";
import i18n from "../common/components/LangConfig";
import { Link } from "react-router-dom";
import { Grid } from "@mui/material";

const Category = ({ icon, name, gradient }) => (
  <Link to="category">
    <button
      onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
      className={`w-full hover:animate-pulse flex gap-4 items-center justify-center flex-col bg-white py-8 rounded-xl border border-neutral-200 transition-all duration-300 hover:shadow-elegant hover:-translate-y-2 ${gradient}`}
    >
      <div className="text-4xl">{icon}</div>
      <div className="text-lg font-medium text-neutral-800">{name}</div>
    </button>
  </Link>
);

const CategoryList = () => {
  const categories = [
    {
      icon: "💻",
      name: "Electronics",
      gradient: "hover:bg-gradient-to-br hover:from-blue-50 hover:to-indigo-100",
    },
    {
      icon: "👗",
      name: "Fashion",
      gradient: "hover:bg-gradient-to-br hover:from-pink-50 hover:to-rose-100",
    },
    {
      icon: "🍽️",
      name: "Kitchen & Dining",
      gradient: "hover:bg-gradient-to-br hover:from-orange-50 hover:to-amber-100",
    },
    {
      icon: "✨",
      name: "Beauty & Personal Care",
      gradient: "hover:bg-gradient-to-br hover:from-purple-50 hover:to-violet-100",
    },
    {
      icon: "🏠",
      name: "Home & Living",
      gradient: "hover:bg-gradient-to-br hover:from-green-50 hover:to-emerald-100",
    },
  ];

  return (
    <Grid container spacing={3} justifyContent="center" alignItems="center">
      {categories.map((category, index) => (
        <Grid item key={index} xs={12} sm={6} md={4} lg={2.4} xl={2.4}>
          <Category 
            icon={category.icon} 
            name={category.name} 
            gradient={category.gradient}
          />
        </Grid>
      ))}
    </Grid>
  );
};

const Categories = () => {
  return (
    <div className="px-4 py-16 bg-gradient-to-br from-neutral-50 to-white">
      <div className="max-w-7xl mx-auto">
        <RedTitle title="Product Categories" />
        <div className="flex gap-20 flex-col md:flex-row mb-12">
          <h2 className="text-2xl md:text-4xl font-bold text-neutral-800">
            Explore Our <span className="gradient-text">Product Categories</span>
          </h2>
          <Arrows />
        </div>
        <CategoryList />
        
        {/* Product Catalog Link */}
        <div className="text-center mt-12">
          <Link 
            to="/productTable" 
            className="inline-flex items-center gap-2 px-8 py-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-semibold rounded-xl shadow-soft hover:shadow-glow transition-all duration-300 transform hover:-translate-y-1"
          >
            <span>View Complete Product Catalog</span>
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Categories;

Category.propTypes = {
  icon: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  gradient: PropTypes.string.isRequired,
};
