print("===================================")
print("     Welcome to AI Chatbot 🤖")
print("Type 'bye' or 'exit' to quit.")
print("===================================\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is Rule-Based AI Chatbot.")

    elif user == "who created you":
        print("Bot: I was created using Python programming.")

    elif user == "help":
        print("Bot: You can ask me simple questions like:")
        print("     hello")
        print("     how are you")
        print("     what is your name")
        print("     who created you")
        print("     bye")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a great day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")
