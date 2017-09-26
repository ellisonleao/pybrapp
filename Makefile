PYTHON = python
# needs kivy installed or in PYTHONPATH

.PHONY: atlas theming apk run install

atlas:
	$(PYTHON) -m kivy.atlas atlas 1024 data/assets/*
run: atlas
	$(PYTHON) main.py -m screen:droid2,portrait -m inspector
apk:
	buildozer android debug
apk_release:
	buildozer android release
