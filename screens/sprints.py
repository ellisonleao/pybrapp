#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_string("""
<SprintsScreen>
    name: 'sprints'
    ScrollView:
        id: scroll
        do_scroll_x: False
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(1000)
            padding: dp(48)
            Image:
                source: 'atlas://atlas/sprint'
                allow_stretch: True
            MDLabel:
                id: 'sprints-label'
                font_style: 'Body1'
                theme_text_color: 'Secondary'
                text: ut.get_data('texts')['sprint']
""")


class SprintsScreen(Screen):
    pass
