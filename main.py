import streamlit as str
from encryption import encrypt_main

str.markdown("# Python encryption")
str.markdown("""
Encrypting a message with Python involves utilizing cryptographic algorithms to transform plaintext into ciphertext, ensuring confidentiality and security.
""")
str.code("""
removed_spaces_message = remove_spaces_from_string(message)
message_length = get_string_length(removed_spaces_message)
secrete_key_string : str = generate_secret_key(message_length)
encrypted_message : str = encrypt(removed_spaces_message, secrete_key_string)
""")

str.markdown("## Getting started")

message_input = str.text_input("Enter message to encrypt: (Enter when done)", placeholder="e.g. I love python")

str.markdown("### Output")

if (message_input != ""):
    output = encrypt_main(message_input)
    str.write(f"Encrypted message: {output}")

    

