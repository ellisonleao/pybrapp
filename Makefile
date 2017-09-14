PYTHON = python
# needs kivy installed or in PYTHONPATH

.PHONY: theming apk run

theming:
	$(PYTHON) -m kivy.atlas pybr/data/default 1024 tools/theming/*.png tools/theming/*.jpg
run: theming
	$(PYTHON) pybr/main.py -m screen:droid2,portrait -m inspector
apk:
	bulldozer android_new debug
apk_release:
	buildozer android_new release
