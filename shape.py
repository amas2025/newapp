import streamlit as st

def generate_shape_from_text(character, text):
    """Generate a shape that visually represents the text."""
    shape = []
    for i, letter in enumerate(text):
        spaces = " " * (len(text) - i - 1)  # Create spaces to align the shape
        line = spaces + (character * (2 * i + 1)) + spaces
        shape.append(line)
    return "\n".join(shape)

# Streamlit app
def main():
    st.title("Shape Generator from Text")
    st.markdown("### Create a shape resembling your text using the first alphabet!")

    input_text = st.text_input("Enter text (the first letter will be used to create the shape):", max_chars=50)
    generate_button = st.button("Generate Shape")

    if generate_button and input_text:
        character = input_text[0].upper()  # Use the first character of the input
        st.markdown(f"### Shape of '{input_text}'")
        st.text(f"Character used: {character}")

        # Generate the shape
        shape = generate_shape_from_text(character, input_text)
        st.code(shape)

if __name__ == "__main__":
    main()
