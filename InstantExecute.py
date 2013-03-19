#
#    Made by lowliet
#

import sublime, sublime_plugin
import subprocess, os

class Instantexecute_runCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings('InstantExecute.sublime-settings')
        python_path = settings.get("python_path", "python")

        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        for region in self.view.sel():
            if region.begin() != region.end():
                self.view.replace(edit, region, subprocess.Popen([python_path, "-c", self.view.substr(region)], startupinfo = startupinfo, stdout = subprocess.PIPE).communicate()[0].strip())