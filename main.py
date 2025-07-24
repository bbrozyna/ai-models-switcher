from services.provider_switcher import get_ai_provider

# from client_flow.flow_manager import ClientFlowManager

if __name__ == "__main__":
    provider = get_ai_provider("openai")
    response = provider.send_prompt("Hello, how are you?")
    print(response)
    print(response.choices[0].message.content)
    # flow = ClientFlowManager(provider)
    # flow.run_flow()
