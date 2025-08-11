import os
from dotenv import load_dotenv
from web3 import Web3
import openai

# Load secrets
load_dotenv("secrets.env")

# Get keys from secrets.env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INFURA_URL = os.getenv("INFURA_URL")

# Setup clients
openai.api_key = OPENAI_API_KEY
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Test Web3 connection
if web3.is_connected():
    print("Connected to Ethereum via Infura!")
else:
    print("Failed to connect to Infura.")

# Example OpenAI request
def ask_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for DAO governance."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message["content"]

# Run bot
if __name__ == "__main__":
    while True:
        user_input = input("Ask DAO Bot: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = ask_gpt(user_input)
        print("Bot:", answer)
