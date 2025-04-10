from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import string
import random


try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
try:
  nltk.download('punkt')
except LookupError:
  nltk.download('punkt')


class Chatbot:
    def __init__(self, agent_transfer_threshold=-0.5):
        self.stop_words = set(stopwords.words('english'))
        self.punctuation = string.punctuation
        self.agent_transfer_threshold = agent_transfer_threshold  # Adjustable threshold
        self.positive_responses = [
            "I'm glad I could help!",
            "Wonderful to hear!",
            "That's fantastic!",
            "Excellent! Let me know if you need anything else."
        ]
        self.negative_responses = [
            "I understand.  I'm connecting you with a live agent now.",
            "I'm really sorry I couldn't resolve this.  One moment while I find an agent.",
            "I'm transferring you to someone who can better assist you."
        ]
        self.neutral_responses = [
            "Could you please elaborate?",
            "Can you provide a bit more detail?",
            "I'm not quite sure I understand. Can you rephrase?",
            "I need more information to assist you properly."
        ]
        self.greetings = [
            "Hello, how can I help you today?",
            "Hi there! What can I assist you with?",
            "Greetings! How may I be of service?"
        ]
        self.exit_commands = ["bye", "goodbye", "exit", "quit", "end"]

    def preprocess_message(self, message):
    
        message = message.lower()
        message = ''.join([char for char in message if char not in self.punctuation])
        tokens = message.split()
        tokens = [word for word in tokens if word not in self.stop_words]
        return " ".join(tokens)

    def analyze_sentiment(self, message):

        analysis = TextBlob(message)
        return analysis.sentiment.polarity

    def generate_response(self, sentiment_score):
        
        if sentiment_score > 0.2:  # Slightly higher positive threshold
            return random.choice(self.positive_responses)
        elif sentiment_score < self.agent_transfer_threshold:
            return random.choice(self.negative_responses)
        else:
            return random.choice(self.neutral_responses)

    def start_chat(self):
        print(random.choice(self.greetings)) #Start with a random greeting

        while True:
            user_message = input("You: ").strip()

            if user_message.lower() in self.exit_commands:
                print("Chatbot: Goodbye!")
                break

            processed_message = self.preprocess_message(user_message)
            sentiment_score = self.analyze_sentiment(processed_message)
            chatbot_message = self.generate_response(sentiment_score)

            print(f"Chatbot: {chatbot_message} (Sentiment score: {sentiment_score:.2f})")  # Display sentiment

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_chat()
