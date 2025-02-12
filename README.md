# 🚀 LLM Speed Test  

Measure the **token generation speed** of your **local LLM** running via **Ollama**. This script tests how many **tokens per second** your model generates using **DeepSeek-R1:1.5B**.  

---

## 🛠️ Installation  

### 🔹 Install Dependencies  
```sh
pip install ollama
```

### 🔹 Clone the Repository & Run the Test  
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/llm-speed-test.git
cd llm-speed-test
python token_test.py
```

---

## 🚀 Usage  
Run the script to test your **LLM's token generation speed**:  
```sh
python token_test.py
```

---

## 📜 Script Explanation  
The script sends a **Java factorization prompt** to the LLM and measures how many **tokens per second** it generates.  

```python
import time
import ollama

model = "deepseek-r1:1.5b"
prompt = "Write a Java program to find the factors of a number."

start_time = time.time()
response = ollama.generate(model=model, prompt=prompt)
end_time = time.time()

tokens = response.get("eval_count", 1)  # Default to 1 to avoid division by zero
elapsed_time = end_time - start_time

print(f"Tokens per second: {tokens / elapsed_time:.2f}")
```

---

## 📊 Example Output  
```sh
Tokens per second: 35.67
```

---

## 🤝 Contributing  
Feel free to **fork the repository**, make improvements, and submit a **pull request**.  

---

## 📜 License  
This project is licensed under the **GPL-3.0 license**.  

---

🌟 **Star this repo if you find it useful!** 🚀  

