from gi.repository import Gtk
import cairo

class MakeUp(object):
	"""Creates the UI fot the app"""
	def __init__(self):
		self.__builder = Gtk.Builder()
		self.__builder.add_from_file("../data/app.ui")
		self.window =  self.__builder.get_object("window")
		header = self.__builder.get_object("header")

		stack = self.create_stack()
		stack_switcher = Gtk.StackSwitcher()
		stack_switcher.set_stack(stack)
		
		header.add(stack_switcher)
		self.window.set_titlebar(header)

	def get_window(self):
		self.window.show_all()
		return self.window


	def create_stack(self):
		stack = Gtk.Stack()
		stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		stack.set_transition_duration(1000)

		canvas = Gtk.DrawingArea()
		stack.add_titled(canvas, "Canvas", "canvas")

		image = self.__builder.get_object("")

		return stack
		






		