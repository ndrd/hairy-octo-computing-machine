from gi.repository import Gtk

class MakeUp(object):
	"""Creates the UI fot the app"""
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file("../data/app.ui")
		self.window =  builder.get_object("window")
		header = builder.get_object("header")
		self.window.set_titlebar(header)

	def get_window(self):
		self.window.show_all()
		return self.window




		