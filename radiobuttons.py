#This one needs some work. I don't understand the best way to just determine which radio button is selected


import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Create the box that the button goes in
        #Note that the orientation of the box is set to vertical, so widgets are added to the box in vertical order. It can also be horizontal
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_child(self.box1)   #Horizontal box goes in window
        self.box1.append(self.box2) #Put the vertical box in box 1
        self.box1.append(self.box3) #Put another vertical box in box 1
        #I believe this is how we organize our application layout, with these invisible boxes that determine where everything goes

        #Create a button
        self.button = Gtk.Button(label="Hello")
        self.box2.append(self.button)
        self.button.connect('clicked', self.hello)


        self.radio1 = Gtk.CheckButton(label="test1")
        self.radio2 = Gtk.CheckButton(label="test2")
        self.radio3 = Gtk.CheckButton(label="test3")
        self.radio2.set_group(self.radio1)
        self.radio3.set_group(self.radio1)

        self.box2.append(self.radio1)
        self.box2.append(self.radio2)
        self.box2.append(self.radio3)

        self.radio1.connect("toggled", self.radio_toggled)

        #Set the window size and title
        self.set_default_size(600, 250)
        self.set_title("MyApp")

    def hello(self, button):
        print("Hello world!")

    def radio_toggled(self, radio1):
        print("test")

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)

