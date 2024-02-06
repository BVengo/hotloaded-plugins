from .base_plugin import BasePlugin


class Plugin2(BasePlugin):
    def get_description(self) -> str:
        return "Added a new plugin 2!"
