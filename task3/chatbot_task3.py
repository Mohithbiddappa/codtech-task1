import nltk
import json
import random
import string
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer

# Download NLTK resources (only once needed)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load intent data from JSON file
with open('intents.json') as file:
    data = json.load(file)

lemmatizer = WordNetLemmatizer()
tokenizer = TreebankWordTokenizer()

# Preprocessing: tokenize and lemmatize
def preprocess(sentence):
    tokens = tokenizer.tokenize(sentence.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

# Match user input to intent patterns
def classify_intent(user_input):
    user_tokens = preprocess(user_input)
    for intent in data['intents']:
        for pattern in intent['patterns']:
            pattern_tokens = preprocess(pattern)
            if all(word in user_tokens for word in pattern_tokens):
                return intent['tag']
    return None

# Choose a random response from the matched intent
def get_response(tag):
    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "Sorry, I don't understand."

# Run the chatbot
print("🤖 CodTech Chatbot (type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Bot: Goodbye!")
        break

    intent_tag = classify_intent(user_input)
    if intent_tag:
        print("Bot:", get_response(intent_tag))
    else:
        print("Bot: I'm not sure how to respond to that.")
