import sublime
import sublime_plugin

STVER = int(sublime.version())
ST3 = STVER >= 3000

def get(key, default=None):
    try:
        settings = get.settings
    except AttributeError:
        settings = sublime.load_settings('ExternalTools.sublime-settings')
        get.settings = settings
    return settings.get(key, default)

class ViewSettings(object):
    def __init__(self, view):
        self._settings = view.settings()

    def get(self, key, default=None):
        result = self._settings.get('external_tools_' + key)
        if (result is not None):
            return result
        return get(key, default)

class ExternalToolsOpenFileCommand(sublime_plugin.ApplicationCommand):
    @staticmethod
    def run(file):
        platform = {
            'osx': 'OSX',
            'windows': 'Windows',
            'linux': 'Linux'
        }[sublime.platform()]
        file = file.replace('${platform}', platform)
        sublime.run_command('open_file', {'file': file})

class ExternalToolsEditSettingsCommand(sublime_plugin.ApplicationCommand):
    @staticmethod
    def run(**kwargs):
        sublime.run_command('edit_settings', kwargs)

    @staticmethod
    def is_visible():
        return STVER >= 3124
