'''ScreenSponsor:
Display all the logos of the sponsors.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from network import get_data
from kivy.factory import Factory
from kivy.uix.stacklayout import StackLayout



class Sponsor(StackLayout):
    ''' This is a simple StackLayout that holds the image
    '''
    data = ObjectProperty(None)


class ScreenSponsor(Screen):


    Builder.load_string('''
<ScreenSponsor>
    name: 'ScreenSponsor'
    BoxLayout
        orientation: 'vertical'
        spacing: dp(4)
        id:main
        BackLabel
            text: "Sponsors"
            backcolor: app.base_inactive_color[:3] + [.5]
            pos_hint:{'top':1}
            size_hint: 1 , None
            height: dp(10)
            font_size:dp(20)

<Footer@BoxLayout>
    size_hint_y: .2
    padding: dp(9)
    spacing: dp(9)
    ActiveButton
        text: 'Patrocine-nos'
        size_hint_y: None
        height: dp(40)
        on_release:
            import webbrowser
            webbrowser.open('https://docs.google.com/presentation/d/1-8u0QWpi5zL21zZ9xehx0wxebXHi5zE0hKNbBtU4ncI/pub?start=false&loop=false&delayms=3000')

<Sponsor>
    orientation: 'tb-rl'
    spacing: dp(12)
    size_hint: 1, 1
    BackLabel
        text: self.parent.data['name']
        size_hint: 1, None
        height: dp(20)
        font_size:dp(18)
    SponsorImage
        on_release:
            import webbrowser
            webbrowser.open(root.data['website'])

<SponsorImage@ButtonBehavior+AsyncImage>
    size_hint:1,.8
    halign: 'center'
    padding: dp(10), dp(10)
    valign: 'middle'
    allow_stretch:False
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
        main_box = self.ids.main;
        main_box.clear_widgets()
        for s in sponsors:
            bl = Factory.Sponsor(size_hint_y=.8/len(sponsors), data=s)
            main_box.add_widget(bl)
        footer = Factory.Footer()
        main_box.add_widget(footer)

