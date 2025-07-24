from config import API_KEYS
from services.gemini_provider import GeminiProvider
from services.openai_provider import OpenAIProvider


def get_ai_provider(name: str):
    if name == "openai":
        return OpenAIProvider(api_key=API_KEYS["openai"])
    elif name == "gemini":
        # TODO: Replace 'client=...' with actual Gemini client initialization
        return GeminiProvider(client="your-gemini-client")
    else:
        raise ValueError(f"Unknown provider: {name}")
