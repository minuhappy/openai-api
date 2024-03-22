from dataclasses import dataclass

from service.util.json_util import JsonUtil
from service.util.open_ai_client import default_client


@dataclass
class AssistantConfig:
    name = "Math Tutor"
    instructions = """
    You are a personal math tutor. 
    When asked a question, write and run Python code to answer the question.
    """
    tools = [{"type": "code_interpreter"}]
    model = "gpt-3.5-turbo-1106"


class AssistantsService:
    @staticmethod
    def create_assistant(config: AssistantConfig):
        assistant = default_client.beta.assistants.create(
            name=config.name,
            instructions=config.instructions,
            tools=config.tools,
            model=config.model
        )

        JsonUtil.print_json(assistant)
        return assistant

# class AssistantsService:
#     def __init__(self, api_key):
#         self.client = OpenAI(api_key=api_key)

#     def create_assistant(self, config: AssistantConfig):

#         return self.client.beta.assistants.create(
#             name=config.name,
#             instructions=config.instructions,
#             tools=config.tools,
#             model=config.model
#         )
