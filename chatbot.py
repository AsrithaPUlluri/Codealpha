import nltk # type: ignore
from nltk.chat.util import Chat, reflections # type: ignore

# Define a list of pairs that match user input to bot responses
requestAndresponse= [
    (r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hi there! What can I do for you?']) ,
    (r'how are you|how are you doing', ['I am fine, thank you!', 'I am just a computer program, but I am doing well!']) ,
    (r'what are you doing', ['Iam trying to help you']),
    (r'what is your name', ['I am a chatbot created by you!', 'You can call me Chatbot.']),
    (r'quit|exit|bye', ['Goodbye! Have a great day!', 'Bye! Take care.']),
    (r'(.*)', ['I am sorry, I did not understand that.', 'Could you please rephrase?']),
    (r'can i give u a name',['Sure its my pleasure',])

]

# Create a chatbot instance
chatbot = Chat(requestAndresponse, reflections)

def conversation():
    print("Hello! I'm here to help. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

conversation()