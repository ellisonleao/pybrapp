#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivymd.theming import ThemeManager


class PybrApp(App):
    theme_cls = ThemeManager()


if __name__ == "__main__":
    PybrApp().run()
