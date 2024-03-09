import json

from service.assistants_service import AssistantsService, AssistantConfig
from service.constants.common_constants import THREAD_ID, ASSISTANT_ID, RUN_ID
from service.thread_service import ThreadService
from service.util import open_ai_client


def create_assistant():
    config = AssistantConfig()
    my_assistant = AssistantsService.create_assistant(config)

    print(my_assistant)


def create_thread(): ThreadService().create()


def create_message(thread_id, content, role="user"):
    client = open_ai_client.default_client
    thread_message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role=role,
        content=content,
    )
    print(thread_message)


def create_run(thread_id, assistant_id):
    client = open_ai_client.default_client
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    print(run)


def retrieve_run(thread_id, run_id):
    client = open_ai_client.default_client
    run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )
    print(run)

def list_messages(thread_id):
    client = open_ai_client.default_client
    messages = client.beta.threads.messages.list(thread_id)
    print(messages.data[0].content[0].text.value)

    # data = json.loads(thread_messages.json())
    # pretty_json = json.dumps(data, indent=4)
    # print(pretty_json)



def main():
    # create_assistant()
    # create_thread()
    # create_message(THREAD_ID, "Hello")
    # create_run(THREAD_ID, ASSISTANT_ID)
    retrieve_run(THREAD_ID, RUN_ID)
    # list_messages(THREAD_ID)


if __name__ == "__main__":
    main()
