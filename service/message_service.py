import json

from service.util import open_ai_client
from service.util.json_util import JsonUtil


class MessageService:
    def __init__(self):
        self.client = open_ai_client.default_client

    def create(self, thread_id, content, role="user"):
        try:
            thread_message = self.client.beta.threads.messages.create(
                thread_id=thread_id,
                role=role,
                content=content,
            )
            JsonUtil.print_json(thread_message)
        except Exception as e:
            print(f"Error creating message: {e}")

    def list_messages(self, thread_id):
        try:
            messages = self.client.beta.threads.messages.list(thread_id)
            # print(messages.data[0].content[0].text.value)

            # data = json.loads(messages.json())
            # pretty_json = json.dumps(data, indent=4)
            # print(pretty_json)

            data = json.loads(messages.json())
            JsonUtil.print_json(data)
        except Exception as e:
            print(f"Error listing messages: {e}")
