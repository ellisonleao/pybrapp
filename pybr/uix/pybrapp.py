# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder


class PybrAppScreenManager(ScreenManager):
	Builder.load_string("""
#:import WipeTransition kivy.uix.screenmanager.WipeTransition

<PybrAppScreenManager>
    transition: WipeTransition()
""")
