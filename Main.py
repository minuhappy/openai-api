from service.AssistantsService import AssistantsService, AssistantConfig


def createAssistant():
    config = AssistantConfig()
    my_assistant = AssistantsService.create_assistant(config)

    print(my_assistant)


def main():
    # createAssistant()
    print('Start!!')


if __name__ == "__main__":
    main()
