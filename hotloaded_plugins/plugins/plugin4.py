from .base_plugin import BasePlugin


class Plugin4(BasePlugin):
    def get_description(self) -> str:
        return "Added plugin4! (Also deleted Plugin1)"
