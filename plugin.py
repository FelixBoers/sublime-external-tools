import os
import sublime
import sublime_plugin
import time
import subprocess

from . import settings

class ExternalToolsRunCommand(sublime_plugin.WindowCommand):
    def run(self, id=None):        
        self.apps = settings.ViewSettings(self.window.active_view()).get('apps')        

        if (self.apps.count == 0):
            sublime.status_message("No apps defined")
            return

        if (id is not None):
            app = next(a for a in self.apps if a['id'] == id)
            if (app is None):
                sublime.status_message("App with id %s not found" % (id))
                return            
            self.run_app(app)
        else:
            self.open_app_selection_panel()

    def open_app_selection_panel(self):
        apps = [a['name'] for a in self.apps]
        self.window.show_quick_panel(apps, self.on_app_selected)        

    def on_app_selected(self, index):
        if (index != -1):
            app = self.apps[index]
            self.run_app(app)

    def run_app(self, app):
        cmd = self.expand_variables(app['cmd'])        
        print(cmd)
        sublime.status_message("Start %s" % app['name'])
        subprocess.Popen(cmd)    
    
    def expand_variables(self, cmd):
        variables = self.get_variables()
        return [sublime.expand_variables(p, variables) for p in cmd]

    def get_variables(self):
        return self.window.extract_variables()