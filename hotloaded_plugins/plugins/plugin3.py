from .base_plugin import BasePlugin


class Plugin3(BasePlugin):
    def get_description(self) -> str:
        return "Fixed plugin 3!"
