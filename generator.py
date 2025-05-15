import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)  # Replace with your actual key
model = genai.GenerativeModel('gemini-2.0-flash')

# Prompt for how to generate the mcq
def generate_mcqs(topic, difficulty, count):
    prompt = f"""
    You are an excellent mcq generator.
    Generate exactly {count} multiple-choice questions on the topic '{topic}' at '{difficulty}' difficulty.
    Format each question like:
    1. What is...?
    a. Option A
    b. Option B
    c. Option C
    d. Option D
    Correct answer: b
    Do not include any introduction or explanation.
    Only return the questions in the format above.
    """
    response = model.generate_content(prompt)
    return response.text

# Parse Gemini response into structured format
def parse_mcqs(text):
    mcqs = []
    questions = text.strip().split('\n')
    
    i = 0
    while i < len(questions):
        line = questions[i].strip()
        if line and line[0].isdigit() and '.' in line:
            q_text = line.split('.', 1)[1].strip()
            options = []
            for j in range(1, 5):
                if i + j < len(questions):
                    opt = questions[i + j].strip()
                    if len(opt) >= 3 and opt[1] == '.':
                        options.append(opt)
            answer_line = questions[i + 5].strip() if i + 5 < len(questions) else "Correct answer: a"
            correct = answer_line[-1].lower() if answer_line.startswith("Correct answer") else "a"

            mcqs.append({
                "question": q_text,
                "options": options,
                "answer": correct
            })
            i += 6 
        else:
            i += 1
    return mcqs

# Streamlit UI
st.set_page_config(page_title="MCQ Generator", layout="wide")
st.title("🧠 MCQ Generator using Gemini")

topic = st.text_input("📚 Enter a Topic")
difficulty = st.selectbox("🎯 Select Difficulty", ["easy", "medium", "hard"])
num_questions = st.number_input("🔢 Number of MCQs", min_value=1, max_value=10, value=3)

# Initialize session state
if "mcqs" not in st.session_state:
    st.session_state.mcqs = []
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Generate questions
if st.button("Generate MCQs"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating questions..."):
            raw = generate_mcqs(topic, difficulty, num_questions)
            st.session_state.mcqs = parse_mcqs(raw)
            st.session_state.answers = {}

# Display questions and options
if st.session_state.mcqs:
    st.markdown("## 📝 Answer the questions:")

    for i, mcq in enumerate(st.session_state.mcqs):
        st.markdown(f"### ❓ Q{i+1}: {mcq['question']}")
        st.session_state.answers[i] = st.radio(
            "Choose your answer:",
            options=[opt for opt in mcq["options"]],
            key=f"q{i}"
        )
        st.markdown("---")

    # Submit all at once
    if st.button("✅ Submit All Answers"):
        st.markdown("## 🧾 Results")
        correct_count = 0
        for i, mcq in enumerate(st.session_state.mcqs):
            user_opt = st.session_state.answers.get(i, "")
            user_ans = user_opt[0].lower() if user_opt else ""
            correct_ans = mcq["answer"]

            if user_ans == correct_ans:
                st.success(f"✅ Q{i+1}: Correct")
                correct_count += 1
            else:
                st.error(f"❌    Q{i+1}: Incorrect. Correct answer: {correct_ans.upper()}")
        st.info(f"🎯 Final Score: {correct_count}/{len(st.session_state.mcqs)}")
