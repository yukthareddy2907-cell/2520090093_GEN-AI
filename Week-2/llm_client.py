from abc import ABC, abstractmethod
import requests

# Common interface
class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a text response for the given prompt."""
        pass


# Gemini cloud provider
class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gemini-2.5-flash"):
        # Import inside __init__ or top-level; imported here so unit tests don't require google-genai
        from google import genai
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text


# Ollama local provider
class OllamaProvider(LLMProvider):
    def __init__(self, model: str = "llama3.2", host: str = "http://localhost:11434"):
        self.model = model
        self.url = f"{host}/api/generate"

    def generate(self, prompt: str) -> str:
        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )
        except requests.exceptions.ConnectionError:
            raise ConnectionError(
                f"Could not connect to Ollama at {self.url}. "
                "Make sure the Ollama application is running on your machine."
            )

        if response.status_code == 404:
            raise RuntimeError(
                f"Model '{self.model}' is not installed in Ollama.\n"
                f"Please open a terminal and run: ollama pull {self.model}"
            )

        response.raise_for_status()
        return response.json().get("response", "")


# Common client
class LLMClient:
    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def generate(self, prompt: str) -> str:
        return self.provider.generate(prompt)
