from dotenv import load_dotenv
import os
from anthropic import Anthropic

# Load .env file
load_dotenv()

# Access variables
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

# print(f"Anthropic API Key: {anthropic_api_key}")

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content[0].text)