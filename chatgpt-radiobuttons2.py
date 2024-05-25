import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_child(self.box1)
        self.box1.append(self.box2)
        self.box1.append(self.box3)

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
        self.radio2.connect("toggled", self.radio_toggled)
        self.radio3.connect("toggled", self.radio_toggled)

        self.set_default_size(600, 250)
        self.set_title("MyApp")

    def hello(self, button):
        if self.radio1.get_active():
            print("Hello world! - Test 1 selected")
        elif self.radio2.get_active():
            print("Hello world! - Test 2 selected")
        elif self.radio3.get_active():
            print("Hello world! - Test 3 selected")
        else:
            print("Hello world! - No radio button selected")

    def radio_toggled(self, radio):
        if radio.get_active():
            if radio == self.radio1:
                print("Test 1 selected")
            elif radio == self.radio2:
                print("Test 2 selected")
            elif radio == self.radio3:
                print("Test 3 selected")

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)

