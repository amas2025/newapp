import streamlit as st

def generate_shape_from_text(character, text):
    """Generate a shape that mimics the entered text's structure."""
    words = text.split()
    shape = "\n".join([character * len(word) for word in words])
    return shape

# Streamlit app
def main():
    st.title("Shape Generator")
    st.markdown("### Generate a shape that matches the structure of your text!")

    input_text = st.text_input("Enter text (the first letter will be used to create the shape):", max_chars=50)
    generate_button = st.button("Generate Shape")

    if generate_button and input_text:
        character = input_text[0].upper()  # Use the first character of the input
        st.markdown("### Generated Shape")
        st.text(f"Character used: {character}")

        # Generate the shape
        shape = generate_shape_from_text(character, input_text)
        st.code(shape)

if __name__ == "__main__":
    main()
