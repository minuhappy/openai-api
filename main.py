from service.assistants_service import AssistantsService, AssistantConfig
from service.constants.common_constants import THREAD_ID
from service.message_service import MessageService


def create_assistant():
    config = AssistantConfig()
    my_assistant = AssistantsService.create_assistant(config)
    print(my_assistant)


def main():
    # create_assistant()
    # ThreadService().create()
    # MessageService().create(THREAD_ID, "Hello")
    # create_run(THREAD_ID, ASSISTANT_ID)
    # RunService().retrieve(THREAD_ID, RUN_ID)
    MessageService().list_messages(THREAD_ID)


if __name__ == "__main__":
    main()
