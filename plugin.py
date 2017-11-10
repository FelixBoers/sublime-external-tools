import os
import sublime
import sublime_plugin
import subprocess

from . import settings

class ExternalToolsRunCommand(sublime_plugin.WindowCommand):
    def run(self, id=None, cmd=None, working_dir=None):
        self.environ = os.environ.copy()
        self.apps = settings.ViewSettings(self.window.active_view()).get('apps')

        if self.apps.count == 0:
            sublime.status_message("No apps defined")
            return

        if id is not None:
            app = next(a for a in self.apps if a['id'] == id)
            if (app is None):
                sublime.status_message("App with id %s not found" % (id))
                return
            self.run_app(app)
        elif cmd is not None:
            self.run_cmd(cmd, working_dir=working_dir)
        else:
            self.open_app_selection_panel()

    def open_app_selection_panel(self):
        apps = [a['name'] for a in self.apps]
        self.window.show_quick_panel(apps, self.on_app_selected)

    def on_app_selected(self, index):
        if index != -1:
            app = self.apps[index]
            self.run_app(app)

    def run_app(self, app):
        if 'name' in app:
            name = app['name']
        else:
            name = app['id']

        working_dir = None
        if 'working_dir' in app:
            working_dir = app['working_dir']

        if working_dir is not None and working_dir.strip() == "":
            working_dir = None

        self.run_cmd(self.expand_variables(app['cmd']), name, working_dir)

    def run_cmd(self, cmd, name=None, working_dir=None):
        expanded = self.expand_variables(cmd)
        working_dir = self.expand_variables(working_dir)
        print("External tool: %s (in %s)" % (expanded, working_dir or 'default dir'))
        sublime.status_message("Start %s" % name or expanded)
        subprocess.Popen(expanded, cwd=working_dir)

    def expand_variables(self, value):
        variables = self.get_variables()
        if type(value) is list:
            expanded = [
                sublime.expand_variables(p, variables)
                for p in value
                if p is not None and not p.isspace()
            ]
        else:
            expanded = sublime.expand_variables(value, variables)
        return expanded

    def get_variables(self):
        variables = self.window.extract_variables()
        variables.update(self.environ)
        return variables
