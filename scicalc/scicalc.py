import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from math import *

class calcWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self,title="Scientific Calculator")
		outer_box = Gtk.Box(spacing=10, orientation = Gtk.Orientation.VERTICAL)
		self.add(outer_box)

		entry = Gtk.Entry()
		outer_box.pack_start(entry,True,True,0)
		grid = Gtk.Grid()
		outer_box.pack_start(grid,True,True,0)

		def button_clicked(button):
			text = entry.get_text()
			text = text + button.props.label
			entry.set_text(text)
		
		def cleartext(self):
			entry.set_text("")

		def evaluate(self):
			eq = entry.get_text()
			entry.set_text(str(eval(eq)))

		

		def delsingle(self):
			text = entry.get_text()
			text=text[:-1]
			entry.set_text(text)



		#buttons
		button9 = Gtk.Button(label = "9");
		button8 = Gtk.Button(label = "8");
		button7 = Gtk.Button(label = "7");
		delete = Gtk.Button(label = "DEL");
		ac = Gtk.Button(label = "AC");
		button4 = Gtk.Button(label = "4");
		button5 = Gtk.Button(label = "5");
		button6 = Gtk.Button(label = "6");
		multiply = Gtk.Button(label = "*");
		divide = Gtk.Button(label = "/");
		button1 = Gtk.Button(label = "1");
		button2 = Gtk.Button(label = "2");
		button3 = Gtk.Button(label = "3");
		plus = Gtk.Button(label = "+");
		minus = Gtk.Button(label = "-");
		button0 = Gtk.Button(label = "9");
		ans = Gtk.Button(label = "=");
		dot = Gtk.Button(label = ".")

		openbr = Gtk.Button(label = "(")
		closebr = Gtk.Button(label = ")")
		clear = Gtk.Button(label = "C")
		root = Gtk.Button(label = "root")
		log = Gtk.Button(label = "log")


		other_buttons = (divide,plus,minus,multiply)
		for button_name in other_buttons:
			button_name.connect('clicked', button_clicked)

		digits=(button1, button2,button3,button4,button5,button6,button7,button8,button9,button0,openbr,closebr)
		for i in digits:
			i.connect('clicked', button_clicked)

		#connecting special buttons
		ans.connect('clicked',evaluate)
		#ac.connect('clicked',clear)
		delete.connect('clicked',delsingle)
		clear.connect("clicked",cleartext)



		grid.add(button9)
		grid.attach(button8,1,0,1,1)
		grid.attach_next_to(button7,button8,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(divide,button7,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(button6,button9,Gtk.PositionType.BOTTOM,1,1)
		grid.attach_next_to(button5,button6,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(button4,button5,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(multiply,button4,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(button3,button6,Gtk.PositionType.BOTTOM,1,1)
		grid.attach_next_to(button2,button3,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(button1,button2,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(minus,button1,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(button0,button3,Gtk.PositionType.BOTTOM,1,1)
		grid.attach_next_to(dot,button0,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(ans,dot,Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(plus,ans,Gtk.PositionType.RIGHT,1,1)

		grid.attach_next_to(openbr,button9,Gtk.PositionType.TOP,1,1)
		grid.attach_next_to(closebr,button8,Gtk.PositionType.TOP,1,1)
		grid.attach_next_to(clear,button7,Gtk.PositionType.TOP,1,1)
		grid.attach_next_to(delete,divide,Gtk.PositionType.TOP,1,1)








		

		

calcWindow = calcWindow()
calcWindow.connect('delete-event',Gtk.main_quit)
calcWindow.show_all()
Gtk.main()			

