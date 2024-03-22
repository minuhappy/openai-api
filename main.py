from service.assistants_service import AssistantsService, AssistantConfig
from service.constants.common_constants import THREAD_ID, ASSISTANT_ID, RUN_ID
from service.message_service import MessageService
from service.run_service import RunService
from service.util import json_util
from service.util.json_util import JsonUtil


def create_assistant():
    config = AssistantConfig()
    my_assistant = AssistantsService.create_assistant(config)
    print(my_assistant)


def main():
    # create_assistant()
    # ThreadService().create()
    # MessageService().create(THREAD_ID, "Hello")
    # RunService().create(THREAD_ID, ASSISTANT_ID)
    RunService().retrieve(THREAD_ID, 'run_4FSTkbiVwKK8k3XbKXV2JPTw')
    # MessageService().list_messages(THREAD_ID)


if __name__ == "__main__":
    main()
