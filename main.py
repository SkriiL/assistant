from weather import get_weather


class Assistant:
    def start_assistant(self):
        print('Hello, what do you want me to do?')

    def pick_action(self, text):
        text = text.lower()
        if 'weather' in text or 'wetter' in text:
            print(get_weather())


if __name__ == '__main__':
    assistant = Assistant()
    assistant.start_assistant()
    while True:
        text = input('You: ')
        assistant.pick_action(text)
