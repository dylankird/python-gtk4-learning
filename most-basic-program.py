import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.present()

app = Gtk.Application()
app.connect('activate', on_activate)

app.run(None)

#This is the minimal amount of code needed to show a window.
#However, there is a proper way to do everything which is detailed in better-structured.py
