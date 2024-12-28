import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Advanced POS System", page_icon="🛒", layout="wide")

# Initialize session state for inventory and cart
if 'inventory' not in st.session_state:
    st.session_state['inventory'] = pd.DataFrame({
        'Item': ['Apple', 'Banana', 'Orange', 'Milk', 'Bread'],
        'Price': [1.0, 0.5, 0.75, 2.5, 1.5],
        'Stock': [50, 100, 75, 30, 40]
    })
if 'cart' not in st.session_state:
    st.session_state['cart'] = []

# Title and description
st.title("🛒 Advanced POS System")
st.write("Welcome to the Advanced POS System. Manage inventory, create orders, and process checkouts seamlessly.")

# Tab layout
tabs = st.tabs(["Inventory", "New Order", "Checkout"])

# Inventory Management Tab
with tabs[0]:
    st.header("Inventory Management")
    st.write("View and update your inventory below:")

    inventory = st.session_state['inventory']

    st.dataframe(inventory, use_container_width=True)

    with st.expander("Update Inventory"):
        item_name = st.text_input("Item Name")
        item_price = st.number_input("Price", min_value=0.0, value=0.0, step=0.01)
        item_stock = st.number_input("Stock", min_value=0, value=0, step=1)
        
        if st.button("Add/Update Item"):
            if item_name:
                if item_name in inventory['Item'].values:
                    idx = inventory[inventory['Item'] == item_name].index[0]
                    inventory.loc[idx, 'Price'] = item_price
                    inventory.loc[idx, 'Stock'] = item_stock
                else:
                    new_item = pd.DataFrame({
                        'Item': [item_name],
                        'Price': [item_price],
                        'Stock': [item_stock]
                    })
                    inventory = pd.concat([inventory, new_item], ignore_index=True)
                st.session_state['inventory'] = inventory
                st.success("Inventory updated successfully!")
            else:
                st.error("Please enter an item name.")

# New Order Tab
with tabs[1]:
    st.header("New Order")
    st.write("Add items to the cart from the inventory:")

    item_to_add = st.selectbox("Select Item", inventory['Item'].values)
    quantity_to_add = st.number_input("Quantity", min_value=1, value=1, step=1)

    if st.button("Add to Cart"):
        item_data = inventory[inventory['Item'] == item_to_add].iloc[0]
        if quantity_to_add <= item_data['Stock']:
            inventory.loc[inventory['Item'] == item_to_add, 'Stock'] -= quantity_to_add
            st.session_state['inventory'] = inventory
            st.session_state['cart'].append({
                'Item': item_to_add,
                'Quantity': quantity_to_add,
                'Price': item_data['Price'],
                'Total': item_data['Price'] * quantity_to_add
            })
            st.success(f"Added {quantity_to_add} {item_to_add}(s) to the cart.")
        else:
            st.error("Not enough stock available.")

    st.write("### Cart:")
    if st.session_state['cart']:
        cart_df = pd.DataFrame(st.session_state['cart'])
        st.dataframe(cart_df, use_container_width=True)
    else:
        st.write("The cart is empty.")

# Checkout Tab
with tabs[2]:
    st.header("Checkout")
    st.write("Review the cart and process payment:")

    if st.session_state['cart']:
        cart_df = pd.DataFrame(st.session_state['cart'])
        st.dataframe(cart_df, use_container_width=True)
        total_amount = cart_df['Total'].sum()
        st.write(f"### Total Amount: ${total_amount:.2f}")

        if st.button("Process Payment"):
            st.session_state['cart'] = []
            st.success("Payment successful! The cart has been cleared.")
            st.session_state['inventory'] = inventory
    else:
        st.write("The cart is empty. Add items to the cart before checkout.")

# Footer
st.write("---")
st.markdown(
    "Made with ❤️ using [Streamlit](https://streamlit.io). Manage your POS efficiently!"
)
