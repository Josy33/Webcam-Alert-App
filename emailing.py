import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "xxxxxxxxxxxxxx"
SENDER = "josiahottojoey@gmail.com"
RECEIVER = "josiahottojoey@gmail.com"

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "Suspected criminal from your VILLAGE!"
    email_message.set_content("Your VILLAGE PEOPLE have succeeded!, "
                              "Your VILLAGE PEOPLE have succeeded!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/20.png")