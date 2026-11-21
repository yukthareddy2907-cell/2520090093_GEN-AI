# Week 2: Provider-Agnostic LLM Client

A unified, provider-agnostic LLM interface in Python that supports both cloud-hosted APIs (Google Gemini) and local models (Ollama running Llama 3.2).

---

## 📁 Project Structure

```text
Week-2/
├── .env                 # Environment variables (API keys)
├── requirements.txt     # Python dependencies
├── llm_client.py        # Abstract base class & provider implementations (Gemini, Ollama, Client)
├── main.py              # Interactive CLI script
├── test_client.py       # Unit tests using FakeProvider
└── README.md            # Setup and execution guide
```

---

## 🚀 Setup & Installation

### 1. Install Python Dependencies
Run the following command in your terminal/PowerShell:
```bash
pip install -r requirements.txt
```
*(Note: The assignment document had a typo `pip install requirements.py` — make sure to use `-r requirements.txt`)*

### 2. Configure Google Gemini API Key
1. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/).
2. Open `.env` and replace `your_actual_gemini_api_key_here` with your key:
   ```env
   GEMINI_API_KEY=AIzaSy...
   ```

### 3. Install & Run Ollama (For Local Models)
1. Download Ollama for Windows from [ollama.com/download](https://ollama.com/download).
2. Install Ollama and verify it is running in PowerShell:
   ```bash
   ollama --version
   ```
3. Pull the `llama3.2` model:
   ```bash
   ollama pull llama3.2
   ```

---

## 🧪 Running Unit Tests

Run the unit tests to verify the client interface without needing live API calls:
```bash
python test_client.py
```
or with pytest:
```bash
pytest
```

---

## 💻 Running the Application

Start the interactive CLI:
```bash
python main.py
```

### Example Usage:
```text
==================================================
Provider-Agnostic LLM Client (Gemini & Ollama)
==================================================
Choose provider (gemini/ollama): gemini
Using Gemini Provider (Model: gemini-2.5-flash)

Enter your question: Explain the concept of recursion in 2 sentences.

Generating response... Please wait.

LLM Response:
--------------------------------------------------
Recursion is a programming technique where a function solves a problem by calling itself with smaller instances of the same problem. It continues until it reaches a base condition that stops the repetition without further recursive calls.
--------------------------------------------------
```
