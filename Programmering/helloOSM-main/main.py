# Kivy
from kivy.app import App
from kivy.lang import Builder
# Kivy MapView
from kivy.garden.mapview import MapView, MapMarkerPopup
# Kivy properties
from kivy.properties import NumericProperty, StringProperty

class Content(MapView):
    def build(self):
        return self

class POIMarkerPopup(MapMarkerPopup):
    latitude = NumericProperty()
    longitude = NumericProperty()
    title = StringProperty()
    description = StringProperty()
    imageUrl = StringProperty()

class MapApp(App):
     def build(self):
         with open('mapViewGUI.kv', encoding='utf8') as f:
             root_widget = Builder.load_string(f.read())
         root_widget.build()
         return root_widget

if __name__ in ('__main__', '__android__'):
    MapApp().run()
