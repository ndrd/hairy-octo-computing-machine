from gi.repository import Gtk, Gio
from gui import MakeUp

class CVApp(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="apps.test.helloworld",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)
        
    def on_activate(self, data=None):
        gui = MakeUp()
        window = gui.get_window()
        window.show_all()
        self.add_window(window)
    
if __name__ == "__main__":
    app = CVApp()
    app.run(None)