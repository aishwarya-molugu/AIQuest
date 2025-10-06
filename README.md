# AIQuest: Test Your AI Knowledge! 🤖

AIQuest is an interactive quiz application built with Streamlit. It allows users to test their knowledge of Artificial Intelligence (AI), Machine Learning (ML), Deep Learning, and related topics. The app features a leaderboard to track top scores and provides fun facts about AI to keep users engaged.

---

## Features

- **Interactive Quiz**: Users can answer multiple-choice questions from categories like AI Basics, Machine Learning, Deep Learning, NLP, and AI Applications.
- **Randomized Questions**: Each quiz session presents a random set of questions from the selected category.
- **Leaderboard**: Tracks and displays the top 5 scores, allowing users to compete for the highest rank.
- **Progress Tracking**: A progress bar shows how far the user has progressed in the quiz.
- **AI Fun Facts**: Displays a random AI fact in the sidebar to educate and entertain users.
- **Dynamic Feedback**: Provides immediate feedback on answers, including explanations for incorrect responses.

---

## How It Works

### 1. **User Info**
- Users enter their name and select a category to start the quiz.
- Categories include:
  - AI Basics
  - Machine Learning
  - Deep Learning
  - NLP
  - AI Applications

### 2. **Quiz in Progress**
- The app displays one question at a time with multiple-choice options.
- Users can submit their answer and receive immediate feedback.
- A progress bar updates as the quiz progresses.

### 3. **Quiz Completion**
- At the end of the quiz, the app displays the user's final score and a personalized message based on their performance.
- The score is saved to a leaderboard, which shows the top 5 players.

### 4. **Play Again**
- Users can restart the quiz to try again and improve their score.

---

## Installation

Follow these steps to set up and run the app locally:

### 1. **Clone the Repository**
```bash
git clone https://github.com/aishwarya-molugu/AIQuest.git
cd AIQuest
```

### 2. **Install Dependencies**
Make sure you have Python installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 3. **Run the App**
Start the Streamlit app:
```bash
streamlit run app.py
```

### 4. **Access the App**
Open your browser and go to:
```
http://localhost:8501
```

---

## File Structure

```
AIQuest_ProjectUsingStreamLit/
│
├── app.py                # Main Streamlit app
├── ai_questions.json     # JSON file containing quiz questions
├── leaderboard.csv       # CSV file to store leaderboard data (auto-generated)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## JSON File Format (ai_questions.json)

The ai_questions.json file contains the quiz questions. Each question is structured as follows:

```json
[
  {
    "category": "AI Basics",
    "question": "What does AI stand for?",
    "options": ["Artificial Intelligence", "Automated Interface", "Advanced Integration"],
    "answer": "Artificial Intelligence",
    "explanation": "AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines."
  },
  ...
]
```

---

## Leaderboard

The leaderboard is stored in leaderboard.csv and contains the following columns:
- **Name**: The name of the user.
- **Score**: The user's score.
- **Date**: The date and time the score was recorded.

---

## Customization

### Adding New Questions
To add new questions, update the ai_questions.json file with the desired category, question, options, answer, and explanation.

### Changing the Number of Questions
By default, the app selects 5 random questions per quiz. To change this, modify the `load_questions` function in app.py:
```python
return random.sample(category_questions, min(5, len(category_questions)))
```
Replace `5` with the desired number of questions.

---

## Deployment

To deploy the app, follow these steps:

### 1. **Push to GitHub**
Ensure your code is pushed to a GitHub repository.

### 2. **Deploy on Streamlit Community Cloud**
1. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
2. Log in with your GitHub account.
3. Select your repository and branch.
4. Specify app.py as the entry point.
5. Click **Deploy**.
