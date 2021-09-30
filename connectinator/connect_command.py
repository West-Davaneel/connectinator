import logging

from slack_bolt.logger import messages

class ConnectCommand:

    question_type_names_dict = {
        0: "A Compliment (not a question)", 
        1: "Shallow",
        2: "Deep"
    }

    question_type_emojis_dict = {
        0: "heart_eyes",
        1: "relaxed",
        2: "hugging_face"
    }





    def __init__(self, client, say):
        self.say = say 
        self.client = client


    def ask_for_question_type(self):
        question_types_string = "What kind of question do you want? React with your response"
       
        for question_type in self.question_type_names_dict:
            emoji = self.question_type_emojis_dict[question_type]
            question_name = self.question_type_names_dict[question_type]

            question_types_string += \
                f"\n :{emoji}:" + \
                f" {question_name}"
                
        response = self.say(question_types_string)
        return response

    def add_question_options_as_reactions(self, response):
        channel = response.get("channel")
        message_timestamp = response.get("ts")

        for question_type in self.question_type_emojis_dict:
            emoji = self.question_type_emojis_dict[question_type]
            self.client.reactions_add(
                channel=channel,
                timestamp=message_timestamp,
                name=emoji,
            )



    def do_command(self):
        response = self.ask_for_question_type()
        self.add_question_options_as_reactions(response)