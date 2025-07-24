class ClientFlowManager:
    def __init__(self, ai_model):
        self.ai = ai_model

    def run_flow(self):  # TODO: Implement flow logicyour flow.")
        prompt = "Hello AI model, how are you?"
        response = self.ai.send_prompt(prompt)
        print("Model responded:", response)

        # further steps...
