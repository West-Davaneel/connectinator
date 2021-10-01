import random

class Reply:
    def __init__(self, user_id, say):
        self.user_id = user_id
        self.say = say


    def reply(self):

        replies = [
            f"Howdy <@{self.user_id}>!",
            f"Hellloooooo",
            f"Use /connect to connect with a stranger!",
            f"Use /connect to connect with a workmate",
            f"What's that <@{self.user_id}>? Feeling disconnected? Use /connect to connect with a workmate 😻",
            f"You know, you're a cool person, <@{self.user_id}>",
            f"That reminds me, Workday is a pretty cool place to work at!",
            f"<@{self.user_id}>, do you know why Workday is callled Workday? I can't seem to think of an explanation...",
            f"<@{self.user_id}> did you know I tell Dad Jokes? Haha, just kidding. I'm not sad about it....",
        ]

        chosen_reply = random.choice(replies)

        self.say(chosen_reply)