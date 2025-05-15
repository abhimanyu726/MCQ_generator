# 🧠 MCQ Generator using Gemini & Streamlit

This project is a web-based Multiple Choice Question (MCQ) generator using Google Gemini (Generative AI) and Streamlit. It allows users to input a **topic**, select a **difficulty level**, and specify the **number of questions**. The app then generates and displays MCQs, lets users choose their answers, and shows immediate feedback.

---

## 🚀 Features

- ✅ Automatically generates topic-based MCQs using Google Gemini
- 📚 Difficulty selection: easy, medium, hard
- 🔢 Custom number of questions (up to 10)
- 🧪 Interactive answer selection and validation

---

## 📦 Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mcq-generator.git
cd mcq-generator

### 2. Create and activate a conda environment

```bash
conda create -n mcqenv python=3.10 -y
conda activate mcqenv

### 3. Install required dependencies
```bash
pip install -r requirements.txt

### 4. Create a .env file and add your Gemini API key
```env
GEMINI_API_KEY=your_google_gemini_api_key_here

### 🚦 How to Run the App
```bash
streamlit run generator.py

## 🧠 How It Works
User enters a topic, selects a difficulty level, and chooses the number of questions

The app builds a prompt and sends it to Google Gemini using the GenerativeModel

Gemini returns formatted MCQs (question, 4 options, correct answer)

Streamlit displays each question interactively, and validates user responses instantly

## 🧩 Tech Stack
🧠 Google Gemini (Pro / 1.5-flash) – LLM used for generating MCQs

📘 Python 3.10+ – Programming language

🌐 Streamlit – Lightweight Python web framework for the user interface

🔒 python-dotenv – For securely managing API keys via .env


## 💡 Example Use Cases
- AI-based tutoring assistants
- Interview preparation tools
- Classroom quiz generators
- Personalized learning platforms

