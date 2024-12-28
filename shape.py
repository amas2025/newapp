import streamlit as st
import math

# Set the page configuration
st.set_page_config(page_title="Advanced Scientific Calculator", page_icon="🔢", layout="centered")

# Title and description
st.title("🔢 Advanced Scientific Calculator")
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    h1 { text-align: center; font-size: 2.5em; color: #2c3e50; }
    .stButton button { background-color: #3498db; color: white; border-radius: 5px; }
    .stButton button:hover { background-color: #2980b9; }
</style>
""", unsafe_allow_html=True)
st.write("Perform basic and advanced scientific calculations with an intuitive interface!")

# Sidebar for user input
st.sidebar.header("Choose Operation")
operation = st.sidebar.selectbox(
    "Select the operation to perform:",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root",
        "Logarithm",
        "Sine",
        "Cosine",
        "Tangent",
        "Factorial",
    ]
)

# Input fields based on the operation
st.sidebar.write("---")
st.sidebar.subheader("Enter your values:")
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    num1 = st.sidebar.number_input("First number", value=0.0, format="%.5f")
    num2 = st.sidebar.number_input("Second number", value=0.0, format="%.5f")

elif operation in ["Square Root", "Logarithm", "Sine", "Cosine", "Tangent", "Factorial"]:
    num1 = st.sidebar.number_input("Enter the number", value=0.0, format="%.5f")

# Perform the selected operation
result = None
if st.sidebar.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        elif operation == "Power":
            result = math.pow(num1, num2)
        elif operation == "Square Root":
            result = math.sqrt(num1) if num1 >= 0 else "Error: Negative input"
        elif operation == "Logarithm":
            result = math.log(num1) if num1 > 0 else "Error: Logarithm of non-positive number"
        elif operation == "Sine":
            result = math.sin(math.radians(num1))
        elif operation == "Cosine":
            result = math.cos(math.radians(num1))
        elif operation == "Tangent":
            result = math.tan(math.radians(num1))
        elif operation == "Factorial":
            result = math.factorial(int(num1)) if num1 >= 0 and num1.is_integer() else "Error: Factorial of non-integer or negative number"
    except Exception as e:
        result = f"Error: {str(e)}"

    # Display the result
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Result:")
    st.success(result if result is not None else "No calculation performed.")

# Footer
st.markdown("""
---
<div style="text-align: center; font-size: 0.85em; color: #7f8c8d;">
    Made with ❤️ using <a href="https://streamlit.io" style="color: #2980b9;">Streamlit</a>
</div>
""", unsafe_allow_html=True)
