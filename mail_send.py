import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

# Load the .env file
load_dotenv()
# Access the environment variables
sender_email = os.getenv('sender_email')
sender_password = os.getenv('sender_password')

# Load the config file
config = configparser.ConfigParser()
config.read('config.ini')
# Access the config variables
recipient_list = config['Test_data_1']['recipient_list']
subject = config['Test_data_1']['subject']
body = config['Test_data_1']['body']


def send_email(sender_email, sender_password, recipient_list, subject, body):
  """Sends an email to a list of recipients.

  Args:
    sender_email: The sender's email address.
    sender_password: The sender's email password.
    recipient_list: A list of recipient email addresses.
    subject: The email subject.
    body: The email body.
  """

  try:
    # Create a secure SMTP session
    smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
    port = 587
    smtp_obj = smtplib.SMTP(smtp_server, port)
    smtp_obj.starttls()
    smtp_obj.login(sender_email, sender_password)

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ", ".join(recipient_list)  # Combine recipients into a string
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))  # You can use 'html' for HTML content

    # Send the email
    smtp_obj.sendmail(sender_email, recipient_list, message.as_string())
    print("Email sent successfully!")

  except Exception as e:
    print("Error sending email:", e)
  finally:
    smtp_obj.quit()



send_email(sender_email, sender_password, recipient_list, subject, body)
