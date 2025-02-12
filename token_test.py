import time
import ollama

model = "deepseek-r1:1.5b"
prompt = """whrite code for java factor of a number '"""

start_time = time.time()
response = ollama.generate(model=model, prompt=prompt)
end_time = time.time()

tokens = response.get("eval_count", 1)  # Default to 1 to avoid division by zero
elapsed_time = end_time - start_time

print(f"Tokens per second: {tokens / elapsed_time:.2f}")
