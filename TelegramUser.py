

class TelegramUser:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.state = None

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def get_enabled_spiders(self):
        ...

    def set_enabled_spiders(self, data: str):
        ...
