from service.util import open_ai_client


class ThreadService:
    def create(self):
        client = open_ai_client.default_client
        empty_thread = client.beta.threads.create()
        print(empty_thread)

