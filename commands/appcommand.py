import sublime_plugin
from FileManager.sublimefunctions import get_settings, to_snake_case

class AppCommand(sublime_plugin.ApplicationCommand):

    def is_visible(self, *args, **kwargs):
        settings = get_settings()
        return bool(settings.get('show_' +
                             to_snake_case(self.__class__.__name__.replace('Fm', ''))) and
                (self.is_enabled(*args, **kwargs) or not settings.get('menu_without_dirstraction')))
