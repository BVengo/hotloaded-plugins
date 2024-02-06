from .base_plugin import BasePlugin


class Plugin1(BasePlugin):
    def get_description(self) -> str:
        return "Added plugin 3! Note that 2 should be deleted...."
