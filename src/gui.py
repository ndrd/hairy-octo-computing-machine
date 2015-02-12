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
		content_box = self.__builder.get_object("content_box")

		content_box.add(stack)
		stack_switcher = Gtk.StackSwitcher()
		stack_switcher.set_stack(stack)
		header.add(stack_switcher)

		self.window.set_titlebar(header)
		self.add_controllers()

	def get_window(self):
		self.window.show_all()
		return self.window


	def create_stack(self):
		stack = Gtk.Stack()
		stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		stack.set_transition_duration(1000)

		canvas = Gtk.DrawingArea()
		container_image = Gtk.Grid()

		self.image1 = Gtk.Image()
		self.image2 = Gtk.Image()

		scrolled1 = Gtk.ScrolledWindow()
		scrolled2 = Gtk.ScrolledWindow()

		scrolled1.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
		scrolled2.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

		scrolled1.set_min_content_height(600)
		scrolled2.set_min_content_height(600)

		scrolled1.add(self.image1)
		scrolled2.add(self.image2)
		#attach(child, left, top, width, height)
		#container_image.attach(scrolled1,0,0,1,1)
		#container_image.attach(scrolled2,1,0,1,1)

		flowbox = Gtk.FlowBox()
		flowbox.set_valign(Gtk.Align.START)
		flowbox.set_max_children_per_line(2)
		flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

		flowbox.add(scrolled1)
		flowbox.add(scrolled2)

		stack.add_titled(canvas, "canvas", "Canvas")
		stack.add_titled(flowbox, "Images", "Filters")
		
		return stack
		
	def add_controllers(self):
		handlers = {
			"on_open_clicked": self.open_image,
			"on_save_clicked": self.save_image,
			"visible_child_changed": self.child_changed
		}
		self.__builder.connect_signals(handlers)

	def open_image(self, button):
		path = self.get_image_from_dialog()
		if path == None:
			return
		self.image1.set_from_file(path)
		self.image2.set_from_file(path)

	def save_image(self, button):
		print "Must save image"

	def child_changed(self, thing):
		print "The child has changed"

	def get_image_from_dialog(self):
		path = None
		dialog = Gtk.FileChooserDialog("Please choose a file", self.window,
			Gtk.FileChooserAction.OPEN,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
			Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

		self.add_filters(dialog)

		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			path = dialog.get_filename()
		dialog.destroy()
		return path


	def add_filters(self, dialog):
		filter_any = Gtk.FileFilter()
		filter_any.set_name("Image Files")
		filter_any.add_pixbuf_formats()
		dialog.add_filter(filter_any)







		