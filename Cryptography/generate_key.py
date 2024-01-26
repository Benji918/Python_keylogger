from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def save_key(key, filename="encryption.txt"):
    with open(filename, "wb") as key_file:
        key_file.write(key)


def load_key(filename="encryption.txt"):
    return open(filename, "rb").read()

#
# def encrypt_file(key, input_file, output_file):
#     cipher_suite = Fernet(key)
#     with open(input_file, 'rb') as file:
#         plaintext = file.read()
#     encrypted_text = cipher_suite.encrypt(plaintext)
#     with open(output_file, 'wb') as file:
#         file.write(encrypted_text)
#
#
# def decrypt_file(key, input_file, output_file):
#     cipher_suite = Fernet(key)
#     with open(input_file, 'rb') as file:
#         encrypted_text = file.read()
#     decrypted_text = cipher_suite.decrypt(encrypted_text)
#     with open(output_file, 'wb') as file:
#         file.write(decrypted_text)
#
#
# Example usage:
key = generate_key()
save_key(key)
#
# encrypt_file(key, "example.txt", "encrypted_example.txt")
#
# loaded_key = load_key()
# decrypt_file(loaded_key, "encrypted_example.txt", "decrypted_example.txt")
