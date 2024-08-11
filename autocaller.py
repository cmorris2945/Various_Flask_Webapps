import pyautogui
import time
import os

# Make sure Skype is running
os.system("start skype:+18005550199?call")  # Replace phonenumber with the actual number

time.sleep(5)  # Wait for Skype to load and initiate the call

# Leave a message after a certain duration
time.sleep(30)  # Adjust this based on when voicemail is expected
pyautogui.write('hey jackass')
pyautogui.press('enter')

