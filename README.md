# AI Feedback System

## Overview

The **AI Feedback System** is a web application that interacts with users to help them learn basic concepts about Artificial Intelligence (AI). The system generates beginner-level questions and provides feedback on user answers. The feedback includes a score and suggestions for improvement, acting as an AI mentor to guide learners through fundamental AI concepts.

## Features

- **AI Question Generation**: Asks a basic, beginner-friendly AI question.
- **Answer Submission**: Users can input their response to the question.
- **Feedback and Scoring**: Provides constructive feedback based on the user's response, including a score and guidance for improvement.

## Tech Stack

- **Streamlit**: Used for building the web application interface.
- **LangChain**: Used for managing AI prompts and templates.
- **ChatGroq**: The language model used to generate questions and provide feedback.
  
## How It Works

1. **Question Generation**: The app generates an AI-related question at a beginner level using a prompt-based system. The question is displayed to the user when they press the "Ask me a question" button.
  
2. **Answer Submission**: Users can submit their answer via a text input field.
  
3. **Feedback**: After submitting an answer, the AI mentor reviews the response and provides a score along with feedback. The feedback highlights correct parts and areas where improvement is needed.

## Usage

### Requirements

- Python 3.x
- Streamlit
- LangChain
- ChatGroq API key (required for using the language model)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/arya-io/ai-feedback-system.git
2. Navigate to the project directory:
   ```bash
   cd ai-feedback-system
3. Install dependencies:
   ```bash
   pip install streamlit langchain_groq
4. Set your Groq API key:

### Running the App

Run the application using Streamlit:
  ```bash
  streamlit run app.py
  ```
This will open the app in your default web browser.

### Example Workflow
1. Press the "Ask me a question" button to generate a beginner-level AI question.
2. Enter your answer in the provided text field.
3. Press "Submit answer" to receive a score and detailed feedback on your answer.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
