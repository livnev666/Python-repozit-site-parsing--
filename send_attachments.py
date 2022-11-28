import os
import smtplib
from testy import EMAIL_PASSWORD, MY_EMAIL, ALL_MAIL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mimetypes
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import sched
import time


def send_email():

    sender = MY_EMAIL
    password = EMAIL_PASSWORD
    server = smtplib.SMTP('smtp.list.ru', 587)
    server.starttls()

    try:
        with open('email_template.html') as file:
            template = file.read()
    except IOError:
        return 'The template file doesnt found!'
    try:
        server.login(sender, password)
        # ALL_MAIL = ['mail', 'mail'...]
        recipients = ALL_MAIL
        msg = MIMEMultipart()
        msg['Subject'] = 'Happy New Year!'
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        msg.attach(MIMEText("Sorry, but I'm practicing. You won't have to suffer much."))
        msg.attach(MIMEText(template, 'html'))

        for i in os.listdir('attachment'):
            filename = os.path.basename(i)
            ftype, encoding = mimetypes.guess_type(i)
            file_type, subtype = ftype.split('/')
            # print (file_type, subtype)

            if file_type == 'text':
                with open('attachment/' + i) as file:
                    text = MIMEText(file.read())
            elif file_type == 'image':
                with open('attachment/' + i, 'rb') as file:
                    text = MIMEImage(file.read(), subtype)
            elif file_type == 'audio':
                with open('attachment/' + i, 'rb') as file:
                    text = MIMEAudio(file.read(), subtype)
            elif file_type == 'application':
                with open('attachment/' + i, 'rb') as file:
                    text = MIMEApplication(file.read(), subtype)
            else:
                with open('attachment/' + i, 'rb') as file:
                    text = MIMEBase(file_type, subtype)
                    text.set_payload(file.read())
                    encoders.encode_base64(text)

            text.add_header('content-disposition', 'attachment', filename=filename)
            msg.attach(text)

        server.sendmail(sender, recipients, msg.as_string())
        return 'The message was sent'
    except Exception as ex:
        print ('Check your login or password')
        return ex


def main_message():

    print (send_email())


main_message()