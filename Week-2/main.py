import os
from dotenv import load_dotenv
from llm_client import (
    GeminiProvider,
    OllamaProvider,
    LLMClient
)

# Load environment variables from .env
load_dotenv(override=True)

def main():
    print("=" * 50)
    print("Provider-Agnostic LLM Client (Gemini & Ollama)")
    print("=" * 50)

    provider_name = input(
        "Choose provider (gemini/ollama): "
    ).strip().lower()

    if provider_name == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key or api_key == "Give your API Key here…" or api_key == "your_actual_gemini_api_key_here":
            raise ValueError(
                "Gemini API key not found in .env! Please set GEMINI_API_KEY in your .env file."
            )
        # Allows optional GEMINI_MODEL env var or defaults to gemini-2.5-flash
        model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        provider = GeminiProvider(api_key=api_key, model=model_name)
        print(f"Using Gemini Provider (Model: {model_name})")

    elif provider_name == "ollama":
        model_name = os.getenv("OLLAMA_MODEL", "llama3.2")
        provider = OllamaProvider(model=model_name)
        print(f"Using Ollama Provider (Model: {model_name})")

    else:
        raise ValueError(f"Invalid provider selected: '{provider_name}'. Choose 'gemini' or 'ollama'.")

    client = LLMClient(provider)
    prompt = input("\nEnter your question: ")

    print("\nGenerating response... Please wait.")
    try:
        answer = client.generate(prompt)
        print("\nLLM Response:")
        print("-" * 50)
        print(answer)
        print("-" * 50)
    except Exception as e:
        print("\n[ERROR] Could not generate response:")
        print(e)

if __name__ == "__main__":
    main()
