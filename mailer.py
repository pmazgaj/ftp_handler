import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from FTP_script.settings import ATTACHMENTS


class Mailer:
    """Send an email (with or without attachment) - to specific recipient(s)"""

    @staticmethod
    def add_attachment(msg: MIMEMultipart, filename: str):
        """
        add attachment to an email
        :param filename: attachment name and extension
        :type msg: get string message, append file to it, return modified object
        """
        file_path = os.path.join(ATTACHMENTS, filename)
        if not os.path.isfile(file_path):
            print('Attachment was not added, invalid path {}'.format(file_path))
            return None

        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename = {}'.format(filename))
            msg.attach(part)
        return None

    def send_mail(self, from_address: str, password: str, to_address: str, subject: str, message: str, smtp_dict: dict,
                  domain: str, attachment=False) -> None:
        """
        send email to specific user
        """
        smtp = smtp_dict.get(domain).get('smtp')
        port = smtp_dict.get(domain).get('port')
        try:
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = subject

            body = message
            msg.attach(MIMEText(body, 'plain'))

            if attachment is True:
                self.add_attachment(msg=msg, filename='dummys.png')

            server = smtplib.SMTP(smtp, port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(from_address, password)
            text = msg.as_string()
            print('text: {}'.format(text))
            server.sendmail(from_address, to_address, text)
            server.quit()
            print("Successfully sent email to {}".format(to_address))
        except Exception as err:
            print(err)
            print("Error: unable to send email to {}".format(to_address))
