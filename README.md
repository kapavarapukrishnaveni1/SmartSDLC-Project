# 💡 SmartSDLC – AI-Enhanced SDLC Automation in Google Colab

SmartSDLC is an AI-powered notebook built in **Google Colab** that automates major phases of the Software Development Lifecycle (SDLC) using Natural Language Processing and Hugging Face models.

---

## ✅ Features Implemented

### 📥 1. Requirement Classification from PDF
- Upload a PDF file (e.g., requirement doc or resume).
- Extracts text using `PyMuPDF (fitz)`.
- Classifies each sentence into SDLC phases:
  - Requirements
  - Design
  - Development
  - Testing
  - Deployment

---

### 💻 2. AI Code Generator
- Converts user prompts into Python code using Hugging Face’s `Salesforce/codegen-350M-mono`.

---

### 🐞 3. Bug Fixer
- Accepts buggy Python code.
- Returns optimized or corrected version using AI or logic rules.

---

### ✅ 4. Test Case Generator
- Generates `unittest` test cases automatically for functions like:
  - `add(a, b)`
  - `is_prime(n)`

---

### 📃 5. Code Summarizer
- Provides human-readable explanation for any given code.
- Helpful for understanding unknown logic or documentation.

---

### 💬 6. SmartSDLC Chatbot (Lightweight)
- Chatbot that answers SDLC-related queries.
- Example questions:
  - “What are SDLC phases?”
  - “How to write unit test cases?”
  - “What is requirement analysis?”

---

## ⚙️ Technologies Used
- Python 3.10+
- Google Colab
- Hugging Face Transformers
- PyMuPDF (`fitz`)
- `Salesforce/codegen-350M-mono`
- Lightweight chatbot using `distilgpt2` or `granite-3.3-2b-instruct`

---

