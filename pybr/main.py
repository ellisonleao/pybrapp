# -*- coding: utf8 -*-

import os
import sys
from os.path import abspath, dirname

from kivy.app import App
from kivy.properties import ListProperty, StringProperty
from uix.pybrapp import PybrAppScreenManager

os.environ['KIVY_DATA_DIR'] = abspath(dirname(__file__)) + '/data'
script_path = os.path.dirname(os.path.realpath(__file__))
module_path = script_path + '/uix/screens/'
sys.path.insert(0, module_path)

__version__ = '1.0.0'


class PyConApp(App):
    """ Our main app class"""

    # rgb(62, 146, 228)
    base_active_bright = ListProperty([.24, .58, .89, 1])

    # rgb(62, 146, 228)
    base_active_color = ListProperty([.24, .58, .89, 1])
    """This is the base Color in the app that is used to denote the currently
    active widgets, active buttons and highlited areas. Format
    is RGBA.

    :attr:`base_active_color` is a :class:`~kivy.properties.ListProperty`

    """

    base_inactive_color = ListProperty([9. / 256., 26. / 256., 66. / 256., 1])
    """This is the base Color in the app that is used to denote the currently
    inactive items, inactive buttons and highlited areas. Format
    is RGBA.

    :attr:`base_inactive_color` is a :class:`~kivy.properties.ListProperty`

    """

    base_inactive_light = ListProperty([.5, .5, .5, 1])
    """This is the base Color in the app that is used to denote the currently
    active color used to display active buttons and highlited areas. Format
    is RGBA.

    :attr:`base_active_color` is a :class:`~kivy.properties.ListProperty`

    """

    # rgb(62, 146, 228)
    base_color = ListProperty([62. / 255, 146. / 255, 228. / 255, 1])
    """This is the base Color in the app that is used to for backgrounds.

    :attr:`base_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(250, 250, 250, 1)
    """

    event_name = StringProperty('')
    """
    This is the name of the event.

    :attr:`event_name` is a :class:`~kivy.properties.StringProperty`

    defaults to ''
    """

    venue_name = StringProperty('')
    """
    This is the name of the venue.

    :attr:`venue_name` is a :class:`~kivy.properties.StringProperty`

    defaults to ''
    """

    def build(self):
        self.script_path = script_path
        self.icon = 'data/icon.png'
        # Here we build our own navigation higherarchy.
        # So we can decide what to do when the back
        # button is pressed.
        self._navigation_higherarchy = []
        # this is the main entry point of our app
        sm = PybrAppScreenManager()
        # This `sm` is the root widget of our app refered by app.root
        return sm

    def on_pause(self):
        # return True to allow for the app to pause
        return True

    def on_start(self):
        # bind to the keyboard to listen to
        # specific key codes
        from utils.keyboard import hook_keyboard
        hook_keyboard()
        # let's load our first screen
        self.load_screen('StartupScreen')

    def go_back_in_history(self):
        try:
            # check webbbrowser
            # if webbrowser._opened:
            #     webbrowser.close()
            #     return
            # go back to previous screen
            # first pop current screen
            scr = self._navigation_higherarchy.pop()
            if scr.name == 'ScreenSchedule':
                # we are at top of Nav higherarchy
                from utils import pause_app
                pause_app()
                return

            # we are not at root of Nav higherarchy
            scr = self._navigation_higherarchy[-1]
            self.load_screen(
                scr.name,
                manager=scr.manager,
                store_back=False)
        except IndexError:
            # at root of app. Pause it.
            from utils import pause_app
            pause_app()

    def load_screen(self, screen, manager=None, store_back=True):
        """Load the provided screen:
        arguments::
            `screen`: is the name of the screen to be loaded
            `manager`: the manager to load this screen, this defaults to
            the main class.
        """
        store_back = False if screen == 'StartupScreen' else store_back

        manager = manager or self.root
        # load screen modules dynamically
        # for example load_screen('LoginScreen')
        # will look for uix/screens/loginscreen
        # load LoginScreen
        module_path = screen.lower()
        if not hasattr(self, module_path):
            import imp
            module = imp.load_module(screen, *imp.find_module(module_path))
            screen_class = getattr(module, screen)
            sc = screen_class()
            sc.from_back = not store_back
            setattr(self, module_path, sc)
            manager.add_widget(sc)

        else:
            sc = getattr(self, module_path)

        sc.from_back = not store_back
        manager.current = screen

        if store_back:
            self._navigation_higherarchy.append(sc)

        return getattr(self, module_path)


# Check if app is started as main and only then insitantiate the App class.
if __name__ == '__main__':
    PyConApp().run()
