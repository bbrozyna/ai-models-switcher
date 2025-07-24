from .ai_base import AIBaseProvider

class GeminiProvider(AIBaseProvider):
    def send_prompt(self, prompt: str) -> str:
        # TODO: Implement Gemini API call
        return f"Gemini response to: {prompt}" 