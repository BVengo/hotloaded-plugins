from .base_plugin import BasePlugin


class Plugin1(BasePlugin):
    def get_description(self) -> str:
        return "Changed plugin 1 description!"
