import nltk
from nltk.chat.util import Chat, reflections

# Predefined patterns and responses for the chatbot
pairs = [
    ['hello', ['Hi there!', 'Hello!', 'Hey!']],
    ['what is your name', ['My name is ChatBot.', 'You can call me ChatBot.']],
    ['how are you', ['I am good, thank you!', 'I am doing well.']],
    ['bye', ['Goodbye!', 'See you later.', 'Bye!']],
    ['default', ['I am not sure how to respond to that.', 'Can you please rephrase?']],
]

# Create a chat instance
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def chat_bot():
    print("ChatBot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == '__main__':
    nltk.download('punkt')
    chat_bot()
