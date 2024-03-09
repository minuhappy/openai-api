from service.util import open_ai_client


class MessageService:
    def create(self, thread_id, content, role="user"):
        client = open_ai_client.default_client
        thread_message = client.beta.threads.messages.create(
            thread_id=thread_id,
            role=role,
            content=content,
        )
        print(thread_message)

    def list_messages(self, thread_id):
        client = open_ai_client.default_client
        messages = client.beta.threads.messages.list(thread_id)
        print(messages.data[0].content[0].text.value)

        # data = json.loads(thread_messages.json())
        # pretty_json = json.dumps(data, indent=4)
        # print(pretty_json)
