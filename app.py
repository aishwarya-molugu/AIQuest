import streamlit as st
import json
import random
import pandas as pd
from datetime import datetime

# -------------------------------
# Load Questions
# -------------------------------
def load_questions(category):
    with open("ai_questions.json", "r") as file:
        data = json.load(file)
    category_questions = [q for q in data if q["category"] == category]
    return random.sample(category_questions, min(5, len(category_questions)))  # 5 random questions

# -------------------------------
# Initialize session variables
# -------------------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "questions" not in st.session_state:
    st.session_state.questions = []
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "name" not in st.session_state:
    st.session_state.name = ""
if "score_saved" not in st.session_state:
    st.session_state.score_saved = False

# -------------------------------
# App Header
# -------------------------------
st.title("🤖 AIQuest: Test Your AI Knowledge!")
st.write("Challenge yourself with fun AI, ML, and Deep Learning questions 🧠")

# Sidebar Fun Fact
st.sidebar.header("💡 AI Fact of the Day")
facts = [
    "The term 'Artificial Intelligence' was coined by John McCarthy in 1956.",
    "Deep Blue, IBM’s chess-playing computer, defeated world champion Garry Kasparov in 1997.",
    "AI can now generate art, code, and even entire books!",
    "Machine Learning is a subset of AI that enables systems to learn from data."
]
st.sidebar.info(random.choice(facts))

# -------------------------------
# Step 1: User Info
# -------------------------------
if not st.session_state.quiz_started:
    st.session_state.name = st.text_input("Enter your name:", key="name_input")
    
    category = st.selectbox(
        "Choose a category:",
        ["AI Basics", "Machine Learning", "Deep Learning", "NLP", "AI Applications"],
        key="category_select"
    )
    
    if st.button("Start Quiz 🚀", key="start_quiz_button"):
        if st.session_state.name.strip() != "":
            st.session_state.questions = load_questions(category)
            st.session_state.quiz_started = True
            st.session_state.score = 0
            st.session_state.q_index = 0
            st.session_state.score_saved = False  # Reset leaderboard flag
        else:
            st.warning("Please enter your name before starting!")

# -------------------------------
# Step 2: Quiz in Progress
# -------------------------------
if st.session_state.quiz_started and st.session_state.q_index < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.q_index]
    st.subheader(f"Question {st.session_state.q_index + 1}: {q['question']}")

    # Radio buttons with unique key per question
    option = st.radio("Select your answer:", q["options"], key=f"q_radio_{st.session_state.q_index}")

    # Track submission status
    submit_key = f"submitted_{st.session_state.q_index}"
    if submit_key not in st.session_state:
        st.session_state[submit_key] = False

    # ---------------- Buttons Side by Side ----------------
    col1, col2 = st.columns(2)

    # Submit button
    with col1:
        if st.button("Submit Answer", key=f"submit_{st.session_state.q_index}", disabled=st.session_state[submit_key]):
            # Evaluate answer
            if option == q["answer"]:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! Correct answer: {q['answer']}")
                st.info(f"💬 Explanation: {q['explanation']}")
            st.session_state[submit_key] = True  # Enable Next button

    # Next button
    with col2:
        if st.button("Next Question ➡️", key=f"next_{st.session_state.q_index}", disabled=not st.session_state[submit_key]):
            st.session_state.q_index += 1

    # ---------------- Progress Bar ----------------
    submitted_count = sum(
        1 for i in range(len(st.session_state.questions))
        if st.session_state.get(f"submitted_{i}", False)
    )
    progress = submitted_count / len(st.session_state.questions)
    st.progress(progress)

# -------------------------------
# Step 3: Quiz Complete
# -------------------------------
if st.session_state.quiz_started and st.session_state.q_index >= len(st.session_state.questions):
    st.success("🎉 Quiz Completed!")
    st.balloons()
    st.write(f"**Your Final Score:** {st.session_state.score}/{len(st.session_state.questions)}")

    percentage = (st.session_state.score / len(st.session_state.questions)) * 100
    if percentage == 100:
        st.success("Perfect! You're an AI Genius 🤖🔥")
    elif percentage >= 60:
        st.info("Good job! You know your AI basics well 🧠")
    else:
        st.warning("Keep learning! AI mastery takes practice 📚")

    # Save to leaderboard only once
    if not st.session_state.score_saved:
        data = {
            "Name": [st.session_state.name],
            "Score": [st.session_state.score],
            "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        }
        df = pd.DataFrame(data)
        
        try:
            leaderboard = pd.read_csv("leaderboard.csv")
            leaderboard = pd.concat([leaderboard, df], ignore_index=True)
        except FileNotFoundError:
            leaderboard = df

        leaderboard.to_csv("leaderboard.csv", index=False)
        st.session_state.score_saved = True

    # Show leaderboard
    st.write("---")
    st.subheader("🏆 Leaderboard (Top 5)")
    top_players = leaderboard.sort_values(by="Score", ascending=False).head(5)
    st.table(top_players)

    # Play Again button
    if st.button("Play Again 🔁", key="play_again_button"):
        st.session_state.quiz_started = False
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.questions = []
        st.session_state.name = ""
        st.session_state.score_saved = False
