class ChatInterface:
    def receive_input(self):
        return input("User: ")

    def send_response(self, response):
        print("Support: " + response)
