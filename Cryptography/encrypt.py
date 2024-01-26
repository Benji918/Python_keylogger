from cryptography.fernet import Fernet
from generate_key import load_key, save_key, generate_key


def encrypt_file(key, input_file, output_file):
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as file:
        plaintext = file.read()
    encrypted_text = cipher_suite.encrypt(plaintext)
    with open(output_file, 'wb') as file:
        file.write(encrypted_text)


key = generate_key()
save_key(key)

encrypt_file(key, "C:\\Users\\Kodi_\\Documents\\keylogger\\key_log.txt", "e_key_log.txt")
