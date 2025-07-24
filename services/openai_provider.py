import openai

from utils.logger import get_logger

from .ai_base import AIBaseProvider


class OpenAIProvider(AIBaseProvider):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        self.client = openai.OpenAI(api_key=api_key)
        self.logger = get_logger(self.__class__.__name__)
        self.logger.info(f"Initialized OpenAIProvider with model: {self.model}")

    def send_prompt(self, prompt: str) -> str:
        self.logger.info(f"Sending prompt to OpenAI: {prompt}")
        try:
            response = self.client.chat.completions.create(
                model=self.model, messages=[{"role": "user", "content": prompt}]
            )
            self.logger.info("Received response from OpenAI.")
            self.logger.info(f"OpenAI response: {response}")
            return response
        except openai.OpenAIError as e:
            self.logger.error(f"OpenAIError while sending prompt: {type(e).__name__}: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error while sending prompt: {type(e).__name__}: {e}")
            raise
