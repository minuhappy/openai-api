from openai import OpenAI

from service.constants.common_constants import API_KEY

default_client = OpenAI(api_key=API_KEY)
