import os

SENDER_LOGIN = 'pmpythontester@gmail.com'
SENDER_PASSWORD = 'starababa'

SENDER_LOGIN_2 = 'gocha44@op.pl'
SENDER_PASSWORD_2 = 'mazgajek60'

SMTP_DICT = {'gmail': {'smtp': 'smtp.gmail.com', 'port': 587}, 'onet': {'smtp': 'smtp.poczta.onet.pl', 'port': 587}}

PROJECT_PATH = os.path.join(os.path.dirname(os.path.abspath('.')), 'FTP_script')
ATTACHMENTS = os.path.join(PROJECT_PATH, 'attachments')

# mailer.send_email_alternative(login, password, sender, receiver, message, server, port)

# mailer.send_email_alternative('gocha44', 'mazgajek60', 'gocha44@op.pl', 'gocha44@op.pl', 'hejka',
#                               'smtp.poczta.onet.pl', 465)
# mailer.send_email_alternative('gocha44', 'mazgajek60', 'gocha44@op.pl', 'gocha44@op.pl', 'hejka',
#  'smtp.poczta.onet.pl', 587)
#
# mailer.send_email_alternative('gocha44', 'mazgajek60', 'gocha44@op.pl', 'gocha44@op.pl',
#  'hejka', 'imap.poczta.onet.pl', 143)
# mailer.send_email_alternative('gocha44', 'mazgajek60', 'gocha44@op.pl', 'gocha44@op.pl',
#  'hejka', 'imap.poczta.onet.pl', 993)
#
# mailer.send_email_alternative('gocha44', 'mazgajek60', 'gocha44@op.pl', 'gocha44@op.pl',
#  'hejka', 'pop3.poczta.onet.pl', 110)
# mailer.send_email_alternative('gocha44', 'mazgajek60', 'gocha44@op.pl', 'gocha44@op.pl',
#  'hejka', 'pop3.poczta.onet.pl', 995)
