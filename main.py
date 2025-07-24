from client_flow.flow_manager import ClientFlowManager
from services.provider_switcher import get_ai_provider

if __name__ == "__main__":
    provider = get_ai_provider("openai")
    client_flow_manager = ClientFlowManager(provider)
    client_flow_manager.run_flow()
