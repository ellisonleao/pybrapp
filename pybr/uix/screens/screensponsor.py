from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from network import get_data
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView


class Sponsor(BoxLayout):
    '''This is a simple BoxLayout that holds the image'''
    data = ObjectProperty(None)


class ScreenSponsor(Screen):

    Builder.load_string('''
<ScreenSponsor>
    name: 'ScreenSponsor'
    ScrollView
        ScrollGrid
            BackLabel
                text: "Patrocinadores"
                backcolor: app.base_inactive_color[:3] + [.5]
                pos_hint: {'top':1}
                size_hint: 1 , None
                font_size: dp(20)
            GridLayout
                id: main
                rows: 5
                cols: 2
                row_default_height: 150
                size_hint_y: None
                allow_strech: True
                padding: '9dp'
                spacing: '9dp'
            BoxLayout:
                id: footer_box
                size_hint_y: None
                padding: dp(9)
                spacing: dp(9)

<Footer@ActiveButton>
    text: 'Patrocine-nos'
    size_hint_y: None
    height: dp(40)
    on_release:
        import webbrowser
        webbrowser.open('https://docs.google.com/presentation/d/1-8u0QWpi5zL21zZ9xehx0wxebXHi5zE0hKNbBtU4ncI/pub?start=false&loop=false&delayms=3000')

<Sponsor>
    orientation: 'vertical'
    spacing: dp(12)
    size_hint: 1, 1
    SponsorImage
        size_hint: 1,.8
        allow_stretch: False
        halign: 'center'
        valign: 'middle'
        padding: dp(9), dp(9)
    BackLabel
        text: self.parent.data['name']
        size_hint: 1, None
        font_size: dp(14)

<SponsorImage@ButtonBehavior+Image>
    source: self.parent.data['logo']
    on_release:
        import webbrowser
        webbrowser.open(self.parent.data['website'])
''')

    def on_enter(self, onsuccess=False):
        '''Series of actions to be performed when Schedule screen is entered
        '''

        # this should update the file on disk
        sponsors = get_data('sponsors', onsuccess=onsuccess)
        if not sponsors:
            return

        sponsors = sponsors.get('0.0.1')
        main_box = self.ids.main
        main_box.clear_widgets()
        for s in sponsors:
            bl = Factory.Sponsor(size_hint_y=.8 / len(sponsors), data=s)
            main_box.add_widget(bl)

        main_box.bind(minimum_height=main_box.setter('height'))

        footer_box = self.ids.footer_box
        footer_box.clear_widgets()
        footer_box.add_widget(Factory.Footer())

        Factory.Animation(opacity=1, d=.5).start(main_box)
