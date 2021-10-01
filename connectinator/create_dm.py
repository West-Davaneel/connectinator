

class CreateDm:

    def __init__(self, client, user_ids: list):
        self.response = client.conversations_open(users = user_ids)

        if not self.response.get("ok"):
            raise Exception("Did not successfully create DM 😢")


    def get_channel_id(self):
        return self.response.get("channel")["id"]

        


