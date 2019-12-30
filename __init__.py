from mycroft import MycroftSkill, intent_file_handler


class MarineWeather(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('weather.marine.intent')
    def handle_weather_marine(self, message):
        self.speak_dialog('weather.marine')


def create_skill():
    return MarineWeather()

