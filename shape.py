import streamlit as st
import math

# Set the page configuration
st.set_page_config(page_title="Advanced Scientific Calculator", page_icon="🔢")

# Title and description
st.title("🔢 Advanced Scientific Calculator")
st.write("Perform basic and advanced scientific calculations with ease!")

# Sidebar for user input
operation = st.sidebar.selectbox(
    "Select Operation",
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
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)

elif operation in ["Square Root", "Logarithm", "Sine", "Cosine", "Tangent", "Factorial"]:
    num1 = st.number_input("Enter the number", value=0.0)

# Perform the selected operation
result = None
if st.button("Calculate"):
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
    st.write("### Result:")
    st.success(result)

# Footer
st.write("---")
st.write("Made with ❤️ using Streamlit")
