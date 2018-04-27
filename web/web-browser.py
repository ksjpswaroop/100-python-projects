import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, Gio, WebKit2

def on_destroy(window):
    Gtk.main_quit()

def load_page(widget):
    url = address_bar.get_text()
    if url.startswith("http://") or url.startswith("https://"):
        webview.load_uri(url)
    else:
        url = "https://" + url
        address_bar.set_text(url)
        webview.load_uri(url)

window = Gtk.Window()
window.set_default_size(800, 600)
window.set_title("BrowseryPy")
window.connect("destroy", on_destroy)


container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
window.add(container)

address_bar_container = Gtk.Box(spacing=6)
container.pack_start(address_bar_container, False, False, 0)

address_bar = Gtk.Entry()
address_bar.set_text("https://www.gnome.org")
address_bar_container.pack_start(address_bar, True, True, 0)

webview_container = Gtk.Box(spacing=6)
container.pack_start(webview_container, True, True, 0)

webview = WebKit2.WebView()
webview.load_uri("https://www.gnome.org")
webview_container.pack_start(webview, True, True, 0)

#actions
address_bar.connect("activate", load_page)

window.show_all()

Gtk.main()
