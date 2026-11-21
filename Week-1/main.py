import os
from dotenv import load_dotenv
from openai import OpenAI

# Step 1: Load API key
load_dotenv()

# Step 2: Read API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found!")

# Step 3: Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Step 4: Send prompt to AI
response = client.responses.create(
    model="gpt-5.5",
    input="What is Artificial Intelligence? Explain in simple words."
)

# Step 5: Display AI response
print("\nLLM Response:")
print(response.output_text)