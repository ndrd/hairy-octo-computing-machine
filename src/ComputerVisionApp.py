#!/usr/bin/env python

#
# @author J.Andrade <ndrd@ciencias.unam.mx>
# @date 11-Febrero-2015
#

from gi.repository import Gtk, Gio
from gui import MakeUp

class CvApp(Gtk.Application):
	def __init__(self):
		Gtk.Application.__init__(self, application_id="mx.unam.ciencias",
								flags=Gio.ApplicationFlags.FLAGS_NONE)
		self.connect("activate", self.init_gui)

	def init_gui(self, data=None):
		pass
		gui = MakeUp()
		window = gui.get_window()
		window.show_all()
		self.add_window(window)

if __name__ == "__main__":
	app = CvApp()
	app.run(None)