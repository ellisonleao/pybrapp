#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.grid import SmartTileWithLabel

from utils import get_data


Builder.load_string("""
<SponsorsScreen>
    name: 'sponsors'
    ScrollView:
        do_scroll_x: False
        GridLayout:
            id: sponsors_grid
            cols: 1
            row_default_height: dp(150)
            row_force_default: True
            size_hint_y: None
            height: self.minimum_height
            padding: dp(4), dp(4)
            spacing: dp(4)
""")


class SponsorsScreen(Screen):
    def on_enter(self):
        sponsors = get_data('sponsors')
        grid = self.ids.sponsors_grid
        color = [0.64, 0.84, 0.98, 0.5]
        for sponsor in sponsors:
            grid.add_widget(SmartTileWithLabel(mipmap=True, keep_ratio=True,
                                               box_color=color, overlap=False,
                                               text=sponsor['name'],
                                               source=sponsor['logo']))
