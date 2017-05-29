"""
main module to handle everything
"""
from mailer import Mailer
# from user import FTPUser
from user import MailUser
from message import Message
from settings import SENDER_LOGIN_2, SENDER_PASSWORD_2, SMTP_DICT

from FTP_script.settings import SENDER_LOGIN, SENDER_PASSWORD


def main():
    mailer = Mailer()
    user = MailUser("pmpythontester", "starababa", '')

    messages_templates = [Message("Jesteś złym człowiekiem {}".format('ziomek')),
                          Message("Jesteś dobrym człowiekiem {}".format('ziomek'))]
    for msg in messages_templates:
        msg = 'siemanko youtube'
        mailer.send_mail(from_address=SENDER_LOGIN_2, password=SENDER_PASSWORD_2, to_address='gocha44@op.pl',
                         subject='Anything you want', message='{}'.format(msg), smtp_dict=SMTP_DICT, domain='onet',
                         attachment=True
                         )


if __name__ == "__main__":
    main()
