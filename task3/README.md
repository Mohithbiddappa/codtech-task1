# Task 3: AI Chatbot with NLP

## Objective
To build an intelligent chatbot using **Natural Language Processing (NLP)** with Python. The chatbot should understand basic user queries and respond accordingly.

## Description

- Used `NLTK` (Natural Language Toolkit) for tokenization and lemmatization
- Created a structured `intents.json` file for mapping patterns to intents and responses
- Implemented simple logic to classify user inputs using keyword matching
- Designed to simulate an AI assistant that can greet, introduce itself, and say goodbye

## Technologies Used

- Python
- NLTK (`wordnet`, `omw-1.4`)
- JSON (for intents database)

## Files Included

- `chatbot_task3.py` – main chatbot logic
- `intents.json` – intents and responses
- `README.md` – this documentation

##  How to Run

1. **Install dependencies:**

   ```bash
   pip install nltk

2. Download NLTK resources (first-time only):

   python
    
    import nltk
    nltk.download('wordnet')
    nltk.download('omw-1.4')

3. Run the chatbot:

   bash

     python chatbot_task3.py

4.Sample Queries:

  pgsql

  hello
  what is your name
  how old are you
  bye

 Completed by : Mohith MB
 CodTech Internship – 2025