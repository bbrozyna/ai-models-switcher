from config import get_ai_provider
from client_flow.flow_manager import ClientFlowManager

if __name__ == "__main__":
    provider = get_ai_provider("openai")
    flow = ClientFlowManager(provider)
    flow.run_flow()
