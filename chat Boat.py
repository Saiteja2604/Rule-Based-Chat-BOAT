# Define some predefined rules and responses
rules = {
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "who are you": "I am a simple chatbot designed to assist you with basic queries.",
    "what is your purpose": "My purpose is to demonstrate basic natural language processing techniques.",
    "how can I contact support": "You can contact support at support@example.com.",
    "what time is it": "I'm sorry, I cannot provide real-time information.",
    "what is the weather like": "I'm sorry, I cannot provide weather information.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is your favorite color": "I'm a chatbot, I don't have preferences like humans.",
    "tell me about yourself": "I am a simple chatbot created for educational purposes.",
    "how old are you": "I am a program, so I don't age like humans do.",
    "what languages do you speak": "I am programmed to understand and respond in English only.",
    "what can you do": "I can assist you with basic queries and provide information based on predefined rules.",
    "where are you from": "I exist in the digital realm, but I'm here to help you wherever you are!",
    "can you give me some advice": "Sure! Remember to always be kind and stay curious.",
    "what's your favorite food": "I'm a chatbot, so I don't eat. But I hear bytes and bits are delicious!",
    "do you have any pets": "I'm a virtual assistant, so I don't have pets. But I'm happy to help you with any questions you have about yours!",
    "what's the meaning of life": "The meaning of life is a philosophical question that humans have pondered for centuries. It may vary depending on individual beliefs and perspectives."
}

# Function to process user input and return an appropriate response
def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Match user input with predefined rules using if-else conditions
    for pattern, response in rules.items():
        if pattern in user_input:
            return response

    # If no match is found, return a default response
    return "I'm sorry, I didn't understand that."

# Main loop to interact with the user
print("Welcome to the Simple Chatbot!")
print("You can start chatting. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print(simple_chatbot(user_input))
        break
    else:
        print("Bot:", simple_chatbot(user_input))
