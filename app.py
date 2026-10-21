import streamlit as st

# --- TOP HEADER WITH LOGO SIDE-BY-SIDE ---
col_logo, col_title = st.columns([1, 4])

with col_logo:
  try:
    st.image(
        "logo.png", width=100
    )  # Make sure her logo is saved as logo.png on desktop
  except:
    st.write("🏷️ [Logo]")

with col_title:
  st.title("🍲 Kitchen Citizen Online Order")

st.write(
    "Welcome! Meals are freshly cooked. Delivery takes 1-2 hrs depending on"
    " your location. Place your order below and we will deliver it to you in"
    " real time."
)

# --- MENU DISPLAY ---
st.subheader("Today's Menu")
st.markdown("*All rice comes in Basmati rice*")

# --- RICE SECTION WITH HER CUSTOM PHOTO ---
st.markdown("### 🍚 Rice Dishes")
try:
  st.image(
      "Jollof.jpg", width=400, caption="Freshly made signature rice dishes"
  )
except:
  st.write(
      "*(Jollof.jpg image will appear here once placed in the folder)*"
  )

st.markdown("""
- **1. 9ja Smokey Jollof Rice & Turkey** - ₦10,000
- **2. 9ja Smokey Jollof Rice & Chicken** - ₦9,000
- **3. Signature Coconut Rice & Turkey** - ₦14,000
- **4. Signature Coconut Rice & Chicken** - ₦13,000
- **5. Asun Smokey Jollof Rice & Turkey** - ₦14,000
- **6. Asun Smokey Jollof Rice & Chicken** - ₦12,500
- **9. Beef Sausage Meat Rice & Turkey** - ₦15,000
- **10. Beef Sausage Meat Rice & Chicken** - ₦14,000
""")

st.markdown("---")

# --- NOODLES SECTION WITH HER CUSTOM PHOTO ---
st.markdown("### 🍝 Noodles & Pastas")
try:
  st.image("Noodles.jpg", width=400, caption="Special Suya Noodles & Pastas")
except:
  st.write(
      "*(Noodles.jpg image will appear here once placed in the folder)*"
  )

st.markdown("""
- **7. Special Suya Noodles & Turkey** - ₦10,000
- **8. Special Suya Noodles & Chicken** - ₦9,000
- **11. Stir Fry Spaghetti & Turkey** - ₦12,500
- **12. Stir Fry Spaghetti & Chicken** - ₦11,000
- **13. Beef Penne Pasta & Turkey** - ₦13,000
- **14. Beef Penne Pasta & Chicken** - ₦12,000
""")

st.markdown("---")

# --- SMOOTHIES SECTION WITH HER CUSTOM PHOTO ---
st.markdown("### 🥤 Fresh Juices & Smoothies")
try:
  st.image("Smoothies.jpg", width=400, caption="Fresh Juices & Smoothies")
except:
  st.write(
      "*(Smoothies.jpg image will appear here once placed in the folder)*"
  )

st.markdown("""
- **15. Pineapple Juice** - ₦3,000
- **16. Banana Smoothie** - ₦8,000
- **17. Vita Melon Juice** - ₦3,000
- **18. Apple Smoothie** - ₦10,000
- **19. Strawberry Smoothie** - ₦10,000
""")

st.markdown("---")

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
    # Pricing Dictionary
    menu_prices = {
        "9ja Smokey Jollof Rice & Turkey (₦10,000)": 10000,
        "9ja Smokey Jollof Rice & Chicken (₦9,000)": 9000,
        "Signature Coconut Rice & Turkey (₦14,000)": 14000,
        "Signature Coconut Rice & Chicken (₦13,000)": 13000,
        "Asun Smokey Jollof Rice & Turkey (₦14,000)": 14000,
        "Asun Smokey Jollof Rice & Chicken (₦12,500)": 12500,
        "Special Suya Noodles & Turkey (₦10,000)": 10000,
        "Special Suya Noodles & Chicken (₦9,000)": 9000,
        "Beef Sausage Meat Rice & Turkey (₦15,000)": 15000,
        "Beef Sausage Meat Rice & Chicken (₦14,000)": 14000,
        "Stir Fry Spaghetti & Turkey (₦12,500)": 12500,
        "Stir Fry Spaghetti & Chicken (₦11,000)": 11000,
        "Beef Penne Pasta & Turkey (₦13,000)": 13000,
        "Beef Penne Pasta & Chicken (₦12,000)": 12000,
        "Pineapple Juice (₦3,000)": 3000,
        "Banana Smoothie (₦8,000)": 8000,
        "Vita Melon Juice (₦3,000)": 3000,
        "Apple Smoothie (₦10,000)": 10000,
        "Strawberry Smoothie (₦10,000)": 10000,
    }

    unit_price = menu_prices.get(food_choice, 0)
    total_price = unit_price * quantity

    # --- DISPLAY RECEIPT & PAYMENT DETAILS ---
    st.success("Order Placed Successfully! 🎉")
    st.markdown("### Order Summary")
    st.write(f"**Customer:** {customer_name}")
    st.write(f"**Delivery Address:** {delivery_address}")
    st.write(f"**Item:** {food_choice} (x{quantity})")
    st.write(f"**Total Amount to Pay:** ₦{total_price:,}")

    # Bank Transfer Details Added Here
    st.markdown("---")
    st.markdown("### 💳 Payment Instructions")
    st.write(
        "Please make your bank transfer to the account details below, and send"
        " your payment receipt to delivery confirmation:"
    )
    st.info("""
    - **Bank Name:** Moniepoint
    - **Account Number:** 5336678922
    - **Account Name:** Kitchen Citizen
    """)
