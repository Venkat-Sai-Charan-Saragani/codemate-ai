# 💻 CodeMate AI

An AI-powered Coding Assistant built with **Python**, **Streamlit**, and the **Groq API**. CodeMate AI helps developers generate code, explain programming concepts, debug errors, and optimize solutions through a simple and interactive chat interface.

---

## 🚀 Features

* 🤖 AI-powered coding assistant
* 💬 Interactive chat interface
* 🐍 Generate code in multiple programming languages
* 🐞 Debug and fix programming errors
* 📖 Explain code and programming concepts
* ⚡ Fast responses powered by the Groq API
* 📝 Markdown support with syntax-highlighted code blocks
* 🧠 Maintains conversation history during the session
* 🗑️ Clear chat functionality

---
## Live Demo
https://codemeta.streamlit.app/

---

## 🛠️ Tech Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Backend                         |
| Streamlit         | User Interface                  |
| Groq API          | Large Language Model            |
| OpenAI Python SDK | API Integration                 |
| python-dotenv     | Environment Variable Management |

---

## 📂 Project Structure

```text
codemate-ai/
│
├── assistant.py         # Handles communication with the Groq API
├── main.py              # Streamlit application
├── prompts.py           # System prompt for the AI
├── requirements.txt     # Project dependencies
├── .gitignore           # Files ignored by Git
├── README.md            # Project documentation
└── .env                 # API key (not tracked by Git)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Venkat-Sai-Charan-Saragani/codemate-ai.git
cd codemate-ai
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

The application will open in your browser automatically.

---

## 💡 Example Prompts

Try asking:

* Write a Python function to reverse a linked list.
* Explain the Sliding Window algorithm.
* Fix this Python error.
* Optimize this code for better performance.
* Convert this Java code to Python.
* Explain the time complexity of Merge Sort.

---

## 📸 Screenshot

<img width="1907" height="917" alt="image" src="https://github.com/user-attachments/assets/76192112-9222-42bb-8159-098edfe2f0ee" />


## result
<img width="1907" height="920" alt="image" src="https://github.com/user-attachments/assets/fea55909-551b-4c40-a786-96eae20d9348" />


```

---

## 📌 Future Improvements

* 📂 Upload and analyze source code files
* 📄 Generate README files automatically
* 🧪 Generate unit tests
* 🔍 Code review and optimization
* 🌙 Improved UI and themes
* 📋 Copy generated code
* 💾 Save conversation history
* 🤖 Multiple AI model selection
* 📝 Export chat history

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

If you have ideas for improvements, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Venkat Sai Charan Saragani**

GitHub: https://github.com/Venkat-Sai-Charan-Saragani

---

⭐ If you found this project useful, consider giving it a star!
