# AI Models Switcher

A modular Python project for switching between different AI model providers (e.g., OpenAI, Gemini) with a unified interface.

## Setup
1. **Clone the repository**
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set your API keys in `config.py`**

## Development
- **Pre-commit hooks:**
  - Install with: `pre-commit install`
  - Run manually: `pre-commit run --all-files`
- **Linters:**
  - Black, isort, and Flake8 are used for code formatting and linting.
- **GitHub Actions:**
  - Linting runs automatically on pull requests to `main`.

## Usage Example
```python
from services.provider_switcher import get_ai_provider

provider = get_ai_provider("openai")
response = provider.send_prompt("Hello, AI!")
print(response)
```

## Extending Providers
- Add new provider classes in `services/` and update `provider_switcher.py`.

## Architecture & Dependencies

- **ClientFlowManager** (in `client_flow/flow_manager.py`):
  - Orchestrates the client interaction flow.
  - Depends on an AI model instance (e.g., OpenAIProvider, GeminiProvider) to generate responses.
  - Example: `self.ai.generate(prompt)` calls the provider's method to get a response.

- **Services** (in `services/`):
  - Contain provider classes (e.g., `OpenAIProvider`, `GeminiProvider`) that implement a unified interface for sending prompts to different AI models.
  - The `provider_switcher.py` module selects and instantiates the correct provider based on configuration or user choice.

- **Config** (in `config.py`):
  - Stores API keys and default provider settings.
  - Used by service providers to authenticate and configure API clients.

**Dependency Flow:**
1. `config.py` provides credentials and settings.
2. `provider_switcher.py` uses config to instantiate the correct provider.
3. `ClientFlowManager` receives the provider and uses it to run the client flow.

**Example:**
```python
from services.provider_switcher import get_ai_provider
from client_flow.flow_manager import ClientFlowManager
from config import DEFAULT_PROVIDER

provider = get_ai_provider(DEFAULT_PROVIDER)
manager = ClientFlowManager(provider)
manager.run_flow()
```

## License
MIT