from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot("SimpleBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train("chatterbot.corpus.english")

# Main interaction loop
print("SimpleBot: Hello! Type 'exit' to end the conversation.")
while True:
    # Get user input
    user_input = input("You: ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("SimpleBot: Goodbye!")
        break

    # Get the chatbot's response
    response = chatbot.get_response(user_input)
    print("SimpleBot:", response)
