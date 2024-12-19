import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    sender_email = "your_email@gmail.com"
    receiver_email = ["tech@themedius.ai", "hr@themedius.ai"]
    password = "your_email_password"

    # Create the email
    subject = "Python (Selenium) Assignment - Avinash Vikram Singh"
    body = """
    Dear Tech Team,

    Please find the details below for the Python (Selenium) Assignment submission:

    Assignment: The completed assignment is attached to this email.

    Approach Documentation: The brief documentation explaining the approach is included in the attached files.

    GitHub Repository: https://github.com/AVINASH0052?tab=repositories

    Availability: Full-time availability is confirmed for the next 3-6 months, from 10 am to 7 pm.

    Thank you for this opportunity. Looking forward to hearing from the team.

    Best regards,
    Avinash Vikram Singh
    Contact: 7052985015
    Email: avinashvs0052@gmail.com
    """

    # Create MIME object
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = ", ".join(receiver_email)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Attach file
    file_path = "/path/to/assignment.zip"  # Replace with actual file path
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={file_path.split('/')[-1]}",
    )
    msg.attach(part)

    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_email()
