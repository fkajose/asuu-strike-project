import smtplib
from email.message import EmailMessage

MY_EMAIL = input("Enter sender email address: ")
MY_PASSWORD = input("Enter sender password or application password: ")

TARGET_EMAIL = input("Enter recipient(s) email address: ")

with open("mailing/mail.html", "r") as mail_file:
    html_body = mail_file.read()

with open("mailing/mail.txt", "r") as mail_file:
    text_body = mail_file.read()


msg = EmailMessage()
msg["Subject"] = "Student Survey: Effects of Strike"
msg["From"] = MY_EMAIL
msg["To"] = TARGET_EMAIL
msg.set_content(text_body)
msg.add_alternative(html_body, subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    try:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(msg)
        print(f"Successfully sent the mail! Check!")
    except smtplib.SMTPConnectError:
        print(f"Hmmn. Something went wrong with the connection.")
    except smtplib.SMTPAuthenticationError:
        print(
            "Failed to send email. Your account has 2-factor Authentication enabled. You need to remove or create an application password instead. Learn more at https://support.google.com/mail/?p=InvalidSecondFactor"
        )
