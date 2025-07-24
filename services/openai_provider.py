from .ai_base import AIBaseProvider

class OpenAIProvider(AIBaseProvider):
    def send_prompt(self, prompt: str) -> str:
        # TODO: Implement OpenAI API call
        return f"OpenAI response to: {prompt}" 