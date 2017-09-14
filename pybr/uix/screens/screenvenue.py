# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarker


class ScreenVenue(Screen):

    Builder.load_string("""
<ScreenVenue>
    name: 'ScreenVenue'
    BoxLayout
        spacing: dp(13)
        orientation: 'vertical'
        padding: dp(4)
        BoxLayout
            orientation: 'vertical'
            SingleLineLabel:
                text: app.venue_name
                halign: 'center'
                size_hint_y: None
                height: dp(25)
                padding: dp(4), dp(8)
            AsyncImage:
                id: img_venue
                source: 'atlas://data/default/venue'
                allow_stretch: True
                keep_ratio: True
        Splitter
            sizable_from: 'top'
            padding: dp(13)
            MapView:
                zoom: 15
                lat: -19.922624
                lon: -43.937925
                MapMarker
                    lat: -19.922624
                    lon: -43.937925
        BoxLayout:
            size_hint: 1, None
            height: dp(45)
            spacing: dp(13)
            padding: dp(4)
            ActiveButton:
                text: 'Abrir Mapa'
                on_release:
                    import webbrowser
                    webbrowser.open('https://goo.gl/maps/Dv2jNT5qacF2')
""")
