PYTHON = python
# needs kivy installed or in PYTHONPATH

.PHONY: theming apk run

theming:
	$(PYTHON) -m kivy.atlas pybr/data/default 1024 tools/theming/*.png
run: theming
	$(PYTHON) pybr/main.py -m screen:droid2,portrait -m inspector
apk:
	buildozer android debug
apk_release:
	buildozer android release
