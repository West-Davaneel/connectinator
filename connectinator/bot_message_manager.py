'''
Keep track of messages sent by bot
'''
import csv
import logging 

class BotMessageManager:

    field_names = [
        "ts",
        "channel"
    ]
    def __init__(self, bot_messages_file: str = 'bot_messages.csv'):
        self.bot_messages_file = bot_messages_file

        try:
            with open(self.bot_messages_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                self.bot_messages = list(reader)
                logging.debug(f"messages = {self.bot_messages}")
        except FileNotFoundError:
            with open(self.bot_messages_file, 'w+', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.field_names)
                writer.writeheader()
                self.bot_messages = list()

    def add_message(self, ts, channel):
        self.bot_messages.append({"ts": ts, "channel": channel})
        with open(self.bot_messages_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.field_names)

            for message in self.bot_messages:
                writer.writerow(message)

    def is_connect_command_message(self, ts, channel):
        message = {"ts": ts, "channel": channel}

        return message in self.bot_messages