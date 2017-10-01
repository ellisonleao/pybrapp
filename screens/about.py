#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<AboutScreen>
    name: 'about'
    ScrollView:
        id: scroll
        do_scroll_x: False
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(800)
            padding: dp(15)
            spacing: dp(15)
            Image:
                source: 'atlas://atlas/logo'
                allow_stretch: True
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Secondary'
                text: ut.get_data('texts')['about']
""")


class AboutScreen(Screen):
    pass
