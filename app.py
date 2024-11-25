import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Set up the LLM
llm = ChatGroq(temperature=0.7, groq_api_key=st.secrets["groq_api_key"], model_name="llama3-70b-8192")

st.title("AI Beginner Quiz Mentor")
st.write("This app will ask you a beginner-level AI question and provide feedback on your answer.")

question = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Ask the user a basic, beginner-level question about AI that a beginner could answer with some thought. Avoid asking difficult or advanced topics. Provide only the question with no explanations or extra information. Do not include any preamble or introduction.",
        ),
    ]
)

# Button to ask a new question
if st.button('Ask me a question'):
    chain = question | llm
    ai_msg = chain.invoke({})
    st.session_state['question'] = ai_msg.content

# Display the AI-generated question
if 'question' in st.session_state:
    st.write(f"**Question:** {st.session_state['question']}")

# Step 2: Take user input (answer to the question)
reply = st.text_input("Enter your answer:")

# Step 3: Process and display feedback from AI
if st.button("Submit answer"):
    if reply:
        answer = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"Provide a score and constructive feedback on the user's response to the question '{st.session_state['question']}'. Act as a mentor. If the response is incorrect, explain where improvement is needed. If the response is partially correct, acknowledge their effort and suggest improvements. Only give a score and feedback—no preamble, introductions, or extra text.",
                ),
                ("human", reply),
            ]
        )
        chain2 = answer | llm
        ai_msg2 = chain2.invoke({})
        
        # Display the feedback
        st.success(f"**Feedback:** {ai_msg2.content}")
    else:
        st.warning("Please enter an answer before submitting.")
