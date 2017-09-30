#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.metrics import dp
from kivymd.tabs import MDTab
from kivymd.list import MDList, TwoLineIconListItem, ILeftBodyTouch
from kivymd.button import MDIconButton, MDRaisedButton
from kivymd.label import MDLabel
from kivymd.dialog import MDDialog
from utils import get_data


Builder.load_string("""
<ScheduleScreen>
    name: 'schedule'
    MDSpinner:
        id: spinner
        active: True
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    MDTabbedPanel:
        id: schedule_tabs
        tab_display_mode: 'text'
""")


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class Track(TwoLineIconListItem):

    colors = {
            # rgb(241, 194, 65)
            'Sala Aventurine e Alexandrite': [0.94, 0.76, 0.25, .4],
            # rgb(87, 193, 219)
            'Sala Amethyst': [0.34, 0.75, 0.85, .4],
            # rgb(86, 184, 103)
            'Sala Crystal': [0.33, 0.72, 0.4, .4],
            'default': [0.5, 0.5, 0.5, .4],
    }

    def __init__(self, *args, **kwargs):
        self.info = kwargs.pop('info')
        kwargs['type'] = 'three-line'
        kwargs['text'] = self.info['time']
        kwargs['secondary_text'] = self.info['title'].upper()

        super(Track, self).__init__(*args, **kwargs)

        icon = IconLeftSampleWidget(icon=self.info.get('icon', 'bulletin-board'))

        if 'place' in self.info:
            label = self.ids._lbl_primary
            place = self.info['place'].replace('Sala', '')
            label.text += ' - {}'.format(place)

            color = self.colors[self.info['place']]
            icon.ids.content.color = color

        self.add_widget(icon)


    def on_release(self):
        if not self.info.get('speaker'):
            return

        box = BoxLayout(height=dp(500), orientation='vertical',
                        size_hint_y=None)

        # adding avatar widget
        if self.info['speaker'].get('avatar'):
            image = AsyncImage(source=self.info['speaker']['avatar'],
                               allow_stretch=True)
            box.add_widget(image)

        # adding place widget
        if self.info.get('place'):
            place = MDRaisedButton(text=self.info['place'], elevation_normal=2,
                                   opposite_colors=True,
                                   pos_hint={'center_x': .5, 'center_y': .4})
            box.add_widget(place)

        # adding description widget
        label = MDLabel(font_style='Body1', theme_text_color='Primary',
                        text=self._parse_text(), size_hint_y=None)
        label.bind(texture_size=label.setter('size'))

        box.add_widget(label)
        self.dialog = MDDialog(title=self.info['speaker']['name'],
                               content=box,
                               size_hint=(1, None),
                               height=dp(500),
                               auto_dismiss=False)

        self.dialog.add_action_button('Fechar',
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def _parse_text(self):
        text = self.info['about']
        if len(text) >= 1000:
            text = u'{}...'.format(text[:1000])
        return text


class ScheduleScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(ScheduleScreen, self).__init__(*args, **kwargs)
        self.tracks = get_data('tracks')

    def on_enter(self):
        # schedules already populated
        if self.ids.schedule_tabs.ids.tab_manager.screens:
            return

        # populating schedules
        for i in range(6, 12):
            track_day = str(i)
            tab = MDTab(id=str(i), name=str(i), text='{} Out'.format(i))
            # tab schedule
            sv = ScrollView(id='tab_{}'.format(i), do_scroll_x=False)
            l = MDList()

            for track in self.tracks[track_day]:
                item = Track(info=track)
                l.add_widget(item)

            sv.add_widget(l)
            tab.add_widget(sv)
            self.ids.schedule_tabs.add_widget(tab)

        self.ids.spinner.active = False
