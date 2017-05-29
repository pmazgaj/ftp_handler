import smtplib
from datetime import datetime


class MailUser:
    """Create program user (can send mail) - not recipient"""
    def __init__(self, login, password, domain):
        self.login = login
        self.password = password
        self.domain = domain
        self.connected = False

    def connect_to_smtp(self, user_mail: str, user_password: str):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(user_mail, user_password)
        except:
            print('Something went wrong...')
        else:
            self.connected = True

    def create_mail(self):
        return "{}{}".format(self.login, self.domain)


class FTPUser:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def connect_to_ftp() -> bool:
        """
        connect to given ftp address (login and password required)
        """
        pass

    @staticmethod
    def get_current_system_time() -> str:
        """
        Get user system time in format %H:%M:%S
        """
        user_system_time = datetime.now().strftime("%H:%M:%S")
        return user_system_time

    @staticmethod
    def get_current_system_date() -> str:
        """
        Get user system date in format "%d.%m.%Y"
        """
        user_system_date = datetime.now().strftime("%d.%m.%Y")
        return user_system_date
