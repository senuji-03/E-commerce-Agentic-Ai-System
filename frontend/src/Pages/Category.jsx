import { useState } from "react";
import { Grid, Typography, Menu, MenuItem, Button } from "@mui/material";
import { Link } from "react-router-dom";
import FlashSaleItem from "../components/common/components/FlashSaleItem";
import i18n from "../components/common/components/LangConfig";
import { ITEMS } from "../components/common/functions/items";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import ViewAll from "../components/common/components/ViewAll";
import WhiteButton from "../components/common/components/WhiteButton";

const Category = () => {
  const [anchorEl, setAnchorEl] = useState(null);
  const [selectedCategory, setSelectedCategory] = useState("Electronics");

  const handleMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  const handleCategorySelect = (category) => {
    setSelectedCategory(category);
    setAnchorEl(null);
  };

  // Filter ITEMS based on the selected category
  const filteredItems = ITEMS.filter((item) => item.type === selectedCategory);

  const categories = [
    "Electronics",
    "Fashion", 
    "Kitchen & Dining",
    "Beauty & Personal Care",
    "Home & Living"
  ];

  return (
    <div className="container mx-auto mt-40 flex flex-col gap-5 bg-gradient-to-br from-neutral-50 to-white min-h-screen">
      <div className="px-4 py-8">
        <Typography variant="h3" align="center" gutterBottom className="text-4xl font-bold text-neutral-800 mb-8">
          Browse By <span className="gradient-text">Category</span>
        </Typography>
        
        <div className="flex justify-center mb-8">
          <Button
            style={{
              background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
              color: "white",
              fontWeight: "bold",
              padding: "12px 24px",
              borderRadius: "12px",
              textTransform: "capitalize",
              boxShadow: "0 4px 15px rgba(102, 126, 234, 0.4)",
            }}
            variant="contained"
            startIcon={<ArrowDropDownIcon />}
            onClick={handleMenuOpen}
            className="hover:shadow-lg transition-all duration-300"
          >
            {selectedCategory}
          </Button>

          <Menu
            id="category-menu"
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={handleMenuClose}
            className="mt-1 flex items-center justify-center mx-1"
            PaperProps={{
              style: {
                borderRadius: "12px",
                boxShadow: "0 10px 25px rgba(0, 0, 0, 0.1)",
              },
            }}
          >
            {categories.map((category) => (
              <MenuItem
                className="w-48 text-lg hover:bg-gradient-to-r hover:from-blue-50 hover:to-indigo-50 transition-all duration-200"
                key={category}
                onClick={() => handleCategorySelect(category)}
              >
                <span className="mx-auto font-medium">{category}</span>
              </MenuItem>
            ))}
          </Menu>
        </div>

        <div className="text-center mb-8">
          <Typography variant="h6" className="text-neutral-600 mb-2">
            Showing {filteredItems.length} products in {selectedCategory}
          </Typography>
          <Typography variant="body1" className="text-neutral-500">
            Discover amazing products in this category
          </Typography>
        </div>

        <div className="relative mx-2 my-10 flex flex-row gap-2 md:gap-12 transition-transform duration-300 transform">
          <Grid container spacing={4} justifyContent="center" alignItems="center">
            {filteredItems.map((item, index) => (
              <Grid item key={item.id} xs={12} sm={6} md={4} lg={3} xl={3}>
                <FlashSaleItem
                  item={item}
                  index={index}
                  totalItems={filteredItems.length}
                  stars={item.stars}
                  rates={item.rates}
                />
              </Grid>
            ))}
          </Grid>
        </div>

        {filteredItems.length === 0 && (
          <div className="text-center py-16">
            <Typography variant="h5" className="text-neutral-500 mb-4">
              No products found in this category
            </Typography>
            <Typography variant="body1" className="text-neutral-400">
              Please select a different category or check back later
            </Typography>
          </div>
        )}

        <div className="mt-12 flex justify-center gap-5 md:gap-20 items-center md:mx-12">
          <Link to="..">
            <WhiteButton name="Back to Home" />
          </Link>
          <ViewAll name="View All Products" />
        </div>
      </div>
    </div>
  );
};

export default Category;
