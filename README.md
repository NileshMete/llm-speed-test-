🚀 Installation & Usage
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/YOUR_GITHUB_USERNAME/llm-speed-test.git
cd llm-speed-test
2️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Script
sh
Copy
Edit
python token_test.py
📜 Script Overview (token_test.py)
python
Copy
Edit
import time
import ollama

model = "deepseek-r1:1.5b"
prompt = """Write Java code to find the factors of a number."""

start_time = time.time()
response = ollama.generate(model=model, prompt=prompt)
end_time = time.time()

tokens = response.get("eval_count", 1)  # Default to 1 to avoid division by zero
elapsed_time = end_time - start_time

print(f"Tokens per second: {tokens / elapsed_time:.2f}")
🎯 How It Works
1️⃣ Sends a prompt to the LLM.
2️⃣ Measures time taken for the response.
3️⃣ Calculates tokens per second and displays the result.

