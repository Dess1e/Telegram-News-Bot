

class TelegramUser:
    def __init__(self, id, modules: str):
        self.id = id
        self.enabled_modules = modules.split(':')



