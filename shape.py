import streamlit as st
import math

# Set the page configuration
st.set_page_config(page_title="Advanced Scientific Calculator", page_icon="🧮", layout="wide")

# Title and description
st.title("🧮 Advanced Scientific Calculator")
st.markdown("""
<style>
    .main { background-color: #eaf2f8; }
    h1 { text-align: center; font-size: 2.8em; color: #2c3e50; }
    .stButton button { background-color: #1abc9c; color: white; border-radius: 5px; font-size: 1.2em; padding: 10px; }
    .stButton button:hover { background-color: #16a085; }
    .stSidebar .sidebar-content { padding: 20px; background-color: #ecf0f1; }
</style>
""", unsafe_allow_html=True)
st.write("Welcome! Perform a variety of mathematical and scientific calculations effortlessly.")

# Sidebar for user input
st.sidebar.header("Calculator Options")
operation = st.sidebar.selectbox(
    "Choose an operation:",
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
st.sidebar.subheader("Enter Input Values:")
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    num1 = st.sidebar.number_input("First Number:", value=0.0, format="%.5f")
    num2 = st.sidebar.number_input("Second Number:", value=0.0, format="%.5f")

elif operation in ["Square Root", "Logarithm", "Sine", "Cosine", "Tangent", "Factorial"]:
    num1 = st.sidebar.number_input("Input Number:", value=0.0, format="%.5f")

# Add Calculate button
if st.sidebar.button("Calculate Now", help="Click to calculate based on the selected operation"):
    try:
        result = None
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
        
        # Display the result
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("Calculation Result:")
        st.info(f"**Result:** {result}", icon="✅")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Footer with branding
st.markdown("""
---
<div style="text-align: center; font-size: 0.9em; color: #7f8c8d;">
    Crafted with ❤️ using <a href="https://streamlit.io" style="color: #1abc9c;">Streamlit</a> | 
    <a href="https://github.com/" style="color: #3498db;">View on GitHub</a>
</div>
""", unsafe_allow_html=True)
