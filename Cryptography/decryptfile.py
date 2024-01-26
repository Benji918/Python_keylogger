from cryptography.fernet import Fernet
from generate_key import load_key


def decrypt_file(key, input_file, output_file):
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_text = file.read()
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    with open(output_file, 'wb') as file:
        file.write(decrypted_text)


loaded_key = load_key()
print(loaded_key)
decrypt_file('AMncv3akEPnB5MBYwFrQ4upzymNLZHVMJw_ZmJtPaNU=', "e_key_log.txt", "d_key_log.txt")
