PyBR Kivy App
=============

**Original APP made for [PyDelhiConf](https://github.com/pydelhi/pydelhi_mobile)**

## Kivy Installation:
- https://kivy.org/docs/installation/installation.html
- If you intend to use VirtualEnv, https://kivy.org/docs/installation/installation-linux.html#installation-in-a-virtual-environment

## Install using pip and virtualenv
   - Create a virtualenv
   - Install Cython first
   - Install the dependencies

### Create a virtualenv
    $ sudo apt install virtualenvwrapper
    $ echo -e "# Enable virtualenvwrapper\nsource /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc
    $ mkvirtualenv pybrapp
    $ mkdir -p ~/projects/python
    $ cd ~/projects/python
    $ git clone git@github.com:ellisonleao/pybrapp.git
    $ cd pybrapp

### Install Cython first
    $ pip install -r run-this-first-requirements.txt

### Install the dependencies
    $ pip install -r requirements.txt


## Make sure you build the theme before using the app.
   - Make sure you have `pillow` installed. `pip install pillow --user`
   - Paste/change the image in pybr/tools/theming
   - Change your directory to pybr
   - Run command ``make theming``

### To test install kivy and run the following::

    $ python pybr/main.py -m screen:droid2,portrait -m inspector

Alternatively, you can use the command below to update theme and execute the application:

    $ make run

### Help on screens
- https://kivy.org/docs/api-kivy.modules.screen.html


This command will aggregate all the png images in your file to one atlas
from which the images are loaded.

## to make apk **prefer linux**

1. Install buildozer: pip install buildozer
2. Edit the buildozer.spec to specify if you have android ndk and sdk,
   if not they will be automatically be downloaded by the next step.
3. Connect your mobile, enable usb debugging, Then goto pybr
   folder and type `make apk`

Link to a existing vm that can be re-used will be added for convenience.

## to make ipa for ios **

1. Install XCode with latest updates & latest command line tools
2. pip install buildozer
3. goto the app folder and do `buildozer init`
4. edit the buildoze.spec and add details for ios
5. run `buildozer ios debug`

**How to add a screen**

Step 1: Create a new file, add the following Template for a clean Screen

	'''Module XYZ:
	This is the documentation for the Module that explains the
	main usecase of this Module and details it's usage.
	'''

	from kivy.uix.screenmanager import Screen
	from kivy.lang import Builder

	class ScreenSponsor(Screen):
	    '''This is the documentation for the Screen that explains
	    the main usecase of this Screen and details it's usage.
	    '''

	    # Here we define the UI of this screen.
	    Builder.load_string('''
<ScreenSponsor>
	name: 'ScreenSponsor'
	# your Widgets here,  we just use 2 buttons in boxlayout as demo
	BoxLayout
	    Button
	    Button
	''')

Take special note of the names::

    The `name: ScreenSponsor`, in this same as the class name `class ScreenSponsor(...)`.


Step 2: Save the file as `screensponsor.py` in the folder `<pybrapp/pybr/uix/screens>`. Take note to name the file same as the class name,  in our case `ScreenSponsor` in lowercase with .py appended at end.

That's it. Now to load this screen::

    Button:
    	on_release:
            app.load_screen('ScreenSponsor', manager=app.navigation_manager)

`manager=` is a optional parameter, which specifies which `ScreenManager` to load this screen in.
If it is omitted this screen will be loaded into the main Screen Manager Which is responsobile for loading `StartupScreen` and `NavigationScreen`.
