import os

openai_api_key = os.getenv("OPENAI_API_KEY")
infura_url = os.getenv("INFURA_URL")

print("OpenAI API Key:", openai_api_key[:8] + "...")
print("Infura URL:", infura_url)

# Contoh request sederhana
import requests

try:
    r = requests.get(infura_url)
    print("Status Infura:", r.status_code)
except Exception as e:
    print("Error:", e)
