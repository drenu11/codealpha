import nltk
from nltk.chat.util import Chat, reflections

# Predefined conversation pairs: List of question and answer pairs
pairs = [
    [r"hi|hello", ["Hello!", "Hi there!"]],
    [r"how are you?", ["I'm doing well, how about you?", "I'm great, thanks for asking!"]],
    [r"what is your name?", ["I am a simple chatbot.", "You can call me Chatbot."]],
    [r"what do you do?", ["I chat with people like you!", "I can answer simple questions."]],
    [r"sorry|apologies", ["No problem!", "It's okay, don't worry."]],
    [r"bye|goodbye", ["Goodbye!", "See you later!"]],
]

# Initialize Chat object with pairs and reflections for human-like responses
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hi! I'm your chatbot. Type 'bye' to exit the conversation.")
chatbot.converse()
