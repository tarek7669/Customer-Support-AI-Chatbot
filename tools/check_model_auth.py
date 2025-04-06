import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"
}

model = "deepseek-ai/DeepSeek-V3-0324"  # replace with your target model

response = requests.get(f"https://huggingface.co/api/models/{model}", headers=headers)

if response.status_code == 200:
    print(f"Yout HF API KEY: {os.getenv('HUGGINGFACEHUB_API_TOKEN')}")
    print("✅ You have access to this model.")
elif response.status_code == 403:
    print("❌ You do NOT have access to this model (Forbidden).")
elif response.status_code == 401:
    print("❌ Invalid or missing token.")
else:
    print(f"Unexpected error: {response.status_code}")
    print(response.json())
