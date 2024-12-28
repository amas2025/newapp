import streamlit as st
from cryptography.fernet import Fernet

# Set the page configuration
st.set_page_config(page_title="Symmetric Encryption & Decryption", page_icon="🔐", layout="centered")

# Generate or load a secret key
@st.cache_data
def generate_key():
    return Fernet.generate_key()

# Initialize the key and Fernet object
key = generate_key()
fernet = Fernet(key)

# Streamlit app content
st.title("🔐 Advanced Symmetric Encryption & Decryption")
st.write("This web app allows you to securely encrypt and decrypt messages using symmetric encryption.")

# Sidebar for encryption and decryption options
st.sidebar.header("Options")
mode = st.sidebar.radio("Choose Mode", ["Encrypt", "Decrypt"])

# Input fields
st.write("---")
st.subheader("Enter your input")
user_text = st.text_area("Text", placeholder="Enter the text here...")

if mode == "Encrypt":
    if st.button("Encrypt Text"):
        if user_text:
            encrypted_text = fernet.encrypt(user_text.encode()).decode()
            st.write("### Encrypted Text:")
            st.code(encrypted_text)
            st.write("### Secret Key (Keep this safe!):")
            st.code(key.decode())
        else:
            st.warning("Please enter text to encrypt.")

elif mode == "Decrypt":
    user_key = st.text_input("Enter the secret key")
    if st.button("Decrypt Text"):
        if user_text and user_key:
            try:
                fernet_decrypt = Fernet(user_key.encode())
                decrypted_text = fernet_decrypt.decrypt(user_text.encode()).decode()
                st.write("### Decrypted Text:")
                st.success(decrypted_text)
            except Exception as e:
                st.error(f"Decryption failed: {e}")
        else:
            st.warning("Please provide both text and a valid key for decryption.")

st.write("---")
st.markdown(
    "Made with ❤️ using [Streamlit](https://streamlit.io) and [Cryptography](https://cryptography.io)"
)
