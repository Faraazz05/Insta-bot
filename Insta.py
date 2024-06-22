# Import the required libraries
import random
from InstagramAPI import InstagramAPI 

# Function to generate a fake IP address
def generate_fake_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Initialize the Instagram API
username = "your_username"
password = "your_password"
bot = InstagramAPI(username, password)

# Function to send a message with a photo
def send_message_with_photo(bot, recipient_username, message_text, photo_path):
    # Send the message
    bot.send_message(message_text, [recipient_username])

    # Upload and send the photo
    bot.upload_photo(photo_path, caption=message_text, recipients=[recipient_username])

# Function to spam a target account with fake IP addresses
def spam_target_account(bot, target_username, spam_count):
    for _ in range(spam_count):
        fake_ip = generate_fake_ip()
        message_text = f"Hey there. Your fake IP address is: {fake_ip}"
        bot.send_message(message_text, [target_username])

# Login to your Instagram account
bot.login()

# Define the recipient's username and the message
recipient_username = "Faraazz05"
message_text = "Hey there."

# Define the path to the photo you want to send
photo_path = "/path/to/your/photo.jpg"

# Send the message with a photo
send_message_with_photo(bot, recipient_username, message_text, photo_path)

# Spam the target account with fake IP addresses
spam_target_account(bot, recipient_username, 10)