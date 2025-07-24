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

## License
MIT