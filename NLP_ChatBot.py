from textblob import TextBlob

class Chatbot:
    def __init__(self):
        pass

    def start_chat(self):
        print("Hello, how can I help you ?")
        while True:
            user_message = input("You: ").strip()

            # Preprocess the user message (e.g., remove stop words, handle contractions)
            # ...

            sentiment_analyzer = TextBlob(user_message)
            sentiment_score = sentiment_analyzer.sentiment.polarity

            if sentiment_score > 0:
                chatbot_message = f"Chatbot: That's great to hear! \n Sentiment score:{sentiment_score} \n"
            elif sentiment_score < 0:
                chatbot_message = f"Chatbot: I'm sorry to hear that. Would you like me to connect you to a live agent? \n Sentiment score: {sentiment_score} \n"
            else:
                chatbot_message = f"Chatbot: Can you provide me more information? \n  Sentiment score: {sentiment_score}  \n"

            print(chatbot_message)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_chat()