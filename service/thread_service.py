from service.util import open_ai_client
from service.util.json_util import JsonUtil


class ThreadService:
    def create(self):
        client = open_ai_client.default_client
        empty_thread = client.beta.threads.create()
        JsonUtil.print_json(empty_thread)
