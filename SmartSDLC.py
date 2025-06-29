!pip install transformers PyMuPDF


import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        blocks = page.get_text("blocks")
        for block in blocks:
            full_text += block[4] + "\n"  # block[4] is the actual text content
    return full_text


file_path = "/content/KRISHNAVENI RESUME.pdf"
text = extract_text_from_pdf(file_path)

# Check what you got:
print(text[:2000])  # First 2000 chars


from transformers import pipeline

# Load a lightweight code generation model
code_pipeline = pipeline(
    "text-generation",
    model="Salesforce/codegen-350M-mono",
    tokenizer="Salesforce/codegen-350M-mono",
    max_length=512,
    pad_token_id=50256  # Avoids warning
)


def generate_code(prompt):
    """Generate Python code from a natural language prompt."""
    full_prompt = f"# Python function\n# Task: {prompt}\n\ndef "
    output = code_pipeline(full_prompt)[0]["generated_text"]

    # Clean output to avoid trailing junk
    code_start = output.find("def ")
    return output[code_start:].strip()


# ✅ Simulated AI Code Generator
def ai_code_generator(prompt: str) -> str:
    # Hardcoded responses for known prompts
    if "prime" in prompt.lower():
        return '''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True'''

    elif "shoppingcart" in prompt.lower():
        return '''class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def checkout(self):
        return len(self.items)'''

    else:
        return "# Code not available for this prompt."

# ✅ Test cases
print("🔹 Prime Function:\n")
print(ai_code_generator("Write a function is_prime(n) that returns True if n is prime."))

print("\n🔹 Shopping Cart Class:\n")
print(ai_code_generator("Write a class ShoppingCart with add_item(), remove_item(), and checkout() methods."))


# ✅ Simulated AI Bug Fixer (can connect to Watsonx/GPT later)
def bug_fixer(buggy_code: str) -> str:
    # Example hardcoded fix logic
    if "def add(a, b): return a + b +" in buggy_code:
        return "def add(a, b):\n    return a + b"

    if "def is_even(n): return n % 2 = 0" in buggy_code:
        return "def is_even(n):\n    return n % 2 == 0"

    return "# Could not detect specific bug. Please check your code."


bug1 = "def add(a, b): return a + b +"
bug2 = "def is_even(n): return n % 2 = 0"

print("🔧 Fixed Bug 1:\n", bug_fixer(bug1))
print("\n🔧 Fixed Bug 2:\n", bug_fixer(bug2))


# ✅ Simulated AI Test Case Generator
def generate_test_cases(code: str) -> str:
    if "def add(a, b):" in code:
        return '''import unittest

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()'''

    elif "def is_prime(n):" in code:
        return '''import unittest

class TestIsPrime(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(10))

if __name__ == '__main__':
    unittest.main()'''

    else:
        return "# No test cases generated. Unknown function."


code1 = "def add(a, b):\n    return a + b"
code2 = "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5)+1):\n        if n % i == 0:\n            return False\n    return True"

print("🧪 Test Cases for add():\n")
print(generate_test_cases(code1))

print("\n🧪 Test Cases for is_prime():\n")
print(generate_test_cases(code2))


# ✅ Simulated AI-based Code Summarizer
def summarize_code(code: str) -> str:
    if "def is_prime" in code:
        return "This function checks whether a given number `n` is a prime number. It returns `True` if the number is prime, and `False` otherwise."

    elif "def add" in code:
        return "This function returns the sum of two numbers `a` and `b`."

    elif "class ShoppingCart" in code:
        return "This class represents a simple shopping cart with the ability to add and remove items, and compute the total count of items during checkout."

    else:
        return "Summary not available for the given code snippet."


code1 = "def add(a, b):\n    return a + b"
code2 = '''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True'''
code3 = '''class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    def checkout(self):
        return len(self.items)'''

print("🔍 Summary for add():\n", summarize_code(code1))
print("\n🔍 Summary for is_prime():\n", summarize_code(code2))
print("\n🔍 Summary for ShoppingCart class:\n", summarize_code(code3))


def chatbot_response(query):
    query = query.lower()

    if "requirement" in query:
        return "📝 Requirements are gathered from stakeholders to define what the system should do."
    elif "unit test" in query:
        return "🧪 A unit test verifies individual components of code. Use `unittest` or `pytest` in Python."
    elif "deployment" in query:
        return "🚀 Deployment is the process of releasing the software to a production environment."
    elif "design" in query:
        return "📐 Design involves planning the architecture, components, and interfaces of the system."
    elif "write code" in query:
        return "💻 You can write code in any supported language. Use version control tools like GitHub."
    elif "sdlc" in query or "phases" in query:
        return "🔁 SDLC (Software Development Lifecycle) has six main phases: Requirement Gathering, Design, Development, Testing, Deployment, and Maintenance."
    elif "hi" in query or "hello" in query:
        return "👋 Hello! Ask me anything about SDLC like phases, testing, design, etc."
    else:
        return "❓ I'm not sure about that. Please ask something related to SDLC."


# Ask manually
while True:
    question = input("💬 You: ")
    if question.lower() in ["exit", "quit"]:
        print("🤖 Chatbot: Bye!")
        break
    print(f"🤖 Chatbot: {chatbot_response(question)}\n")

