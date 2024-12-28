import streamlit as st
import random

def generate_rectangle(character, rows, cols):
    """Generate a rectangle with given character."""
    return "\n".join([character * cols for _ in range(rows)])

def generate_triangle(character, rows):
    """Generate a triangle with given character."""
    return "\n".join([character * i for i in range(1, rows + 1)])

def generate_cube(character, rows):
    """Generate a cube representation with given character."""
    cube_face = "\n".join([character * rows for _ in range(rows)])
    return f"{cube_face}\n\n{cube_face}\n\n{cube_face}"

def generate_sphere(character, rows):
    """Generate a sphere-like shape with given character."""
    sphere = []
    for i in range(rows):
        spaces = " " * abs(rows // 2 - i)
        chars = character * (rows - abs(rows // 2 - i) * 2)
        sphere.append(f"{spaces}{chars}{spaces}")
    return "\n".join(sphere)

# Streamlit app
def main():
    st.title("Shape Generator")
    st.markdown("### Generate shapes based on your input text!")

    input_text = st.text_input("Enter text (the first letter will be used to create the shape):", max_chars=20)
    shape_type = st.selectbox("Select a shape:", ["Rectangle", "Triangle", "Cube", "Sphere"])
    rows = st.slider("Number of rows:", min_value=5, max_value=20, value=10)
    generate_button = st.button("Generate Shape")

    if generate_button and input_text:
        character = input_text[0].upper()  # Use the first character of the input
        cols = random.randint(5, 20)  # Random number of columns for rectangle

        st.markdown(f"### Shape: {shape_type}")
        st.text(f"Character used: {character}")

        if shape_type == "Rectangle":
            shape = generate_rectangle(character, rows, cols)
        elif shape_type == "Triangle":
            shape = generate_triangle(character, rows)
        elif shape_type == "Cube":
            shape = generate_cube(character, rows)
        elif shape_type == "Sphere":
            shape = generate_sphere(character, rows)
        else:
            shape = "Invalid Shape"

        st.code(shape)

if __name__ == "__main__":
    main()
