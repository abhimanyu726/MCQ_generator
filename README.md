# 🧠 MCQ Generator using Gemini & Streamlit
This project is a web-based **Multiple Choice Question (MCQ)** generator powered by **Google Gemini** (Generative AI) and **Streamlit**. It enables users to input a topic, select a difficulty level, and specify the number of questions. The app generates MCQs, allows users to select answers, and provides immediate feedback.
## 🚀 Features
- ✅ Automatically generates topic-based MCQs using Google Gemini
- 📚 Difficulty levels: Easy, Medium, Hard
- 🔢 Customizable number of questions (up to 10)
- 🧪 Interactive answer selection with immediate feedback
## 📋 Prerequisites
Before setting up the project, ensure you have the following installed:
1. **Python 3.10+**
2. **Conda** (for environment management)
3. **Git** (for cloning the repository)
4. A **Google Gemini API key** (obtainable from [Google Cloud Console](https://cloud.google.com/))
## 📦 Installation
1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/mcq-generator.git
    cd mcq-generator
    ```
2. **Create and Activate a Conda Environment**
    ```bash
    conda create -n mcqenv python=3.10 -y
    conda activate mcqenv
    ```
3. **Install Dependencies**
    Install the required Python packages listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
4. **Set Up Environment Variables**
    Create a `.env` file in the project root and add your Google Gemini API key:
    ```env
    GEMINI_API_KEY=your_google_gemini_api_key_here
    ```
## 🚦 Running the App
1. **Run the Streamlit App**
    To launch the MCQ Generator, run the following command:
    ```bash
    streamlit run generator.py
    ```
2. **Access the App**
    The app will start a local web server, accessible in your browser at `http://localhost:8501`.
## 🧩 Tech Stack
- **Google Gemini (Pro / 1.5-flash)**: Large Language Model for generating MCQs
- **Python 3.10+**: Core programming language
- **Streamlit**: Lightweight web framework for building the user interface
- **python-dotenv**: Secure management of API keys and environment variables
## 🧠 How It Works
1. The user inputs a **topic**, selects a **difficulty level** (Easy, Medium, Hard), and specifies the **number of MCQs** (up to 10).
2. The app constructs a prompt and sends it to **Google Gemini** using the `GenerativeModel` API.
3. Gemini generates structured MCQs with questions, options, and correct answers.
4. **Streamlit** renders the MCQs interactively, allowing users to select answers.
5. The app validates the user's answers and provides immediate feedback.
## 💡 Example Use Cases
- **Education**: Create quizzes for classroom learning or self-study.
- **Interview Preparation**: Generate practice questions for technical or general interviews.
- **Tutoring**: Build AI-powered tutoring tools for personalized learning.
- **Content Creation**: Develop quiz content for e-learning platforms.
