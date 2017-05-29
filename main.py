"""
main module to handle everything
"""
from mailer import Mailer
# from user import FTPUser
from user import MailUser
from message import Message
from settings import SENDER_LOGIN_2, SENDER_PASSWORD_2, SMTP_DICT


def main():
    mailer = Mailer()
    user = MailUser("pmpythontester", "starababa", '')

    messages_templates = [Message("Jesteś złym człowiekiem {}".format('ziomek')),
                          Message("Jesteś dobrym człowiekiem {}".format('ziomek'))]
    for msg in messages_templates:
        mailer.send_mail(from_address=SENDER_LOGIN_2, password=SENDER_PASSWORD_2, to_address='gocha44@op.pl',
                         subject='Empty', message='{}'.format(msg), smtp_dict=SMTP_DICT, domain='onet', attachment=False
                         )


if __name__ == "__main__":
    main()
