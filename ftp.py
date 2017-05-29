class FTP:
    def __init__(self):
        self.connection_open = False

    @staticmethod
    def file_exist() -> bool:
        """
        Check if file exist on ftp
        """
        pass

    @staticmethod
    def get_file_modification_time() -> str:
        """
        Get user system time in format %H:%M:%S
        """
        file_modification_time = datetime.now().strftime("%H:%M:%S")
        print(file_modification_time)
        return file_modification_time

    @staticmethod
    def get_file_modification_date() -> str:
        """
        Get user system date in format "%d.%m.%Y"
        """
        file_modification_date = datetime.now().strftime("%d.%m.%Y")
        print(file_modification_date)
        return file_modification_date

    @staticmethod
    def is_valid_date_offset(user_date, offset):
        """
        return True if file_date - current_date < offset
        """
        return
