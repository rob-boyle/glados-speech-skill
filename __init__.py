from mycroft import MycroftSkill, intent_file_handler


class GladosSpeech(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('speech.glados.intent')
    def handle_speech_glados(self, message):
        self.speak_dialog('speech.glados')


def create_skill():
    return GladosSpeech()

