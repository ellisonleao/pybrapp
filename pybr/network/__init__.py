import json

from kivy.app import App

app = App.get_running_app()


def get_data(endpoint, onsuccess=False):
    filepath = app.script_path + '/data/' + endpoint + '.json'
    jsondata = json.load(open(filepath))

    return jsondata
