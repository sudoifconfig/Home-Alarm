import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


class SendEmailClass:

    def __init__(self,email_sender,email_reciver,email_pass):
        self.email_sender = email_sender
        self.email_reciver = email_reciver
        self.email_pass = email_pass


    def send_jpg(self,ImgFileName):
        #img_path = os.path.join("..", ImgFileName)  # Navigate to the parent directory

        with open(ImgFileName, 'rb') as f:
            img_data = f.read()

        msg = MIMEMultipart()
        msg['Subject'] = 'subject'
        msg['From'] = self.email_sender
        msg['To'] = self.email_reciver

        text = MIMEText("test")
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)


    # ogbe asld dpes lcmc


        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.email_sender,self.email_pass)
        s.sendmail(self.email_sender,self.email_reciver, msg.as_string())
        s.quit()