import streamlit as st

# --- WEB APP FRONTEND DESIGN ---
st.title("🍲 Kitchen Citizen Online Order")
st.write(
    "Welcome! Meal are freshly cooked. Delivery takes 1-2 hrs depending on your location. Place your order below and we will deliver it to you in real"
    " time."
)

# --- MENU DISPLAY ---
st.subheader("Today's Menu")
st.markdown("""
- **1. Jollof Rice & Chicken** - ₦2,500
- **2. Fried Plantain & Fish** - ₦1,800
- **3. Bottled Water** - ₦500
""")

# --- USER INPUT WIDGETS ---
food_choice = st.selectbox(
    "Select your meal:",
    [
        "9ja Smokey Jollof Rice & Turkey (₦10,000)",
        "9ja Smokey Jollof Rice & Chicken (₦9,000)",
        "Signature Coconut Rice & Turkey (₦14,000)",
        "Signature Coconut Rice & Chicken (₦13,000)",
        "Asun Smokey Jollof Rice & Turkey (₦14,000)",
        "Asun Smokey Jollof Rice & Chicken (₦12,500)",
        "Special Suya Noodles & Turkey (₦10,000)",
        "Special Suya Noodles & Chicken (₦9,000)",
        "Beef Sausage Meat Rice & Turkey (₦15,000)",
        "Beef Sausage Meat Rice & Chicken (₦14,000)",
        "Stir Fry Spaghetti & Turkey (₦12,500)",
        "Stir Fry Spaghetti & Chicken (₦11,000)",
        "Beef Penne Pasta & Turkey (₦13,000)",
        "Beef Penne Pasta & Chicken (₦12,000)",
        "Pineapple Juice (₦3,000)",
        "Banana Smoothie (₦8,000)",
        "Vita Melon Juice (₦3,000)",
        "Apple Smoothie (₦10,000)",
        "Strawberry Smoothie (₦10,000)",
    ],
)

quantity = st.number_input(
    "How many portions?", min_value=1, max_value=20, value=1
)

customer_name = st.text_input("Your Name:")
delivery_address = st.text_input("Delivery Address:")

# --- CALCULATE & SUBMIT BUTTON ---
if st.button("Place Order Now"):
  if customer_name == "" or delivery_address == "":
    st.error("Please enter your name and delivery address before submitting!")
  else:
    # Determine price based on selection
    if "Jollof" in food_choice:
      unit_price = 2500
      item_name = "Jollof Rice & Chicken"
    elif "Plantain" in food_choice:
      unit_price = 1800
      item_name = "Fried Plantain & Fish"
    else:
      unit_price = 500
      item_name = "Bottled Water"

    total_price = unit_price * quantity

    # --- DISPLAY RECEIPT ON THE WEB PAGE ---
    st.success("Order Placed Successfully! 🎉")
    st.markdown("### Order Summary")
    st.write(f"**Customer:** {customer_name}")
    st.write(f"**Delivery Address:** {delivery_address}")
    st.write(f"**Item:** {item_name} (x{quantity})")
    st.write(f"**Total Amount to Pay:** ₦{total_price}")
    st.info("We have received your order ticket!")
