class Message:
    def __init__(self, text):
        self.text = text

    def get_message(self, text):
        if text is None:
            text = self.text
        return Message(text)
