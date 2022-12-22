import smtplib
import json
import os


class EmailSend():
    def __init__(self, receiver_mails: list, cc_mails: list = [], bcc_mails: list = []):
        self.receiver_mails = receiver_mails
        self.cc_mails = cc_mails
        self.bcc_mails = bcc_mails
        file_path = os.path.abspath(__file__)  # full path of your script
        # full path of the directory of your script
        dir_path = os.path.dirname(file_path)
        config_file_path = os.path.join(
            dir_path, 'config.json')  # absolute zip file path
        with open(config_file_path, 'r') as c:
            self.mail_data = json.load(c)["mail_data"]

    def send_email(self, SUBJECT: str, TEXT: str):
        try:
            # create a smtp object
            fromaddr = self.mail_data['sender_mail']
            message_subject = SUBJECT
            message_text = TEXT
            message = "From: %s\r\n" % fromaddr + "To: %s\r\n" % ",".join(self.receiver_mails) + "CC: %s\r\n" % ",".join(
                self.cc_mails) + "Subject: %s\r\n" % message_subject + "\r\n" + message_text
            toaddrs = self.receiver_mails + self.cc_mails + self.bcc_mails
            server = smtplib.SMTP('mail.codeaza-apps.com', 587)
            server.starttls()
            server.login(self.mail_data['sender_mail'],
                         self.mail_data['sender_password'])
            server.set_debuglevel(1)
            server.sendmail(fromaddr, toaddrs, message)
            server.quit()
        except smtplib.SMTPException as e:
            print(e)
            print("Error: unable to send email")
