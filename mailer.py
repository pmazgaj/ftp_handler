import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Mailer:
    def __init__(self):
        pass

    @staticmethod
    def add_attachment(msg):
        """
        add attachment to mail
        """
        filename = "NAME OF THE FILE WITH ITS EXTENSION"
        attachment = open("PATH OF THE FILE", "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename = {}'.format(filename))
        msg.attach(part)

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

            msg.attach(MIMEText(body.encode(), 'plain'))

            if attachment is True:
                self.add_attachment(msg)

            server = smtplib.SMTP(smtp, port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(from_address, password)
            text = msg.as_string()
            server.sendmail(from_address, to_address, text)
            server.quit()
            print("Successfully sent email to {}".format(to_address))
        except Exception as err:
            print(err)
            print("Error: unable to send email to {}".format(to_address))
