import streamlit as st
import openai
import datetime

# Set your OpenAI API key here
openai.api_key = 'sk-QMTZolSHhzqbSUCejaOwT3BlbkFJq8we8gvQaVUUhHa1pepAs'

# Example data for TechSolutions
data_context = """
TechSolutions is an innovative technology firm based in Bangalore, India, specializing in software development, AI solutions, and IT consulting. Founded in 2010, TechSolutions has grown into a leading IT service provider with a strong emphasis on delivering cutting-edge technology solutions to clients globally. Our services include custom software development, AI and machine learning solutions, cloud services, and IT strategy consulting. With a team of over 500 dedicated professionals, we strive to empower businesses through technology and innovation. TechSolutions is committed to sustainability and corporate social responsibility, actively participating in community development and green initiatives.
"""

# Example questions
example_questions = [
    "What services does TechSolutions offer?",
    "When was TechSolutions founded?",
    "How many employees does TechSolutions have?",
    "What is TechSolutions' commitment to sustainability?",
    "Where is TechSolutions based?"
]

def get_answer(question, context):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{context}\n\nQuestion: {question}"},
            ],
            temperature=0.5,
            max_tokens=100,
            top_p=1.0,
            stop=["\n"]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

def schedule_appointment():
    st.subheader("Schedule an Appointment")
    date = st.date_input("Choose the date for your appointment:")
    time = st.time_input("Choose your time:")
    if st.button("Schedule Appointment"):
        st.success(f"Appointment scheduled for {date} at {time}!")

def live_chat():
    st.subheader("Live Chat Support")
    user_message = st.text_input("How can we help you today?")
    if st.button("Send Message"):
        st.text_area("Chat", value="Thank you for reaching out. Our support team will contact you soon.", height=100, disabled=True)

def collect_feedback():
    st.subheader("Feedback")
    feedback = st.text_area("Please share your feedback to help us improve:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

def knowledge_base_search():
    st.subheader("Search Our Knowledge Base")
    query = st.text_input("Enter your query:")
    if st.button("Search"):
        st.write("Results for your query will appear here...")

def main():
    st.title("TechSolutions Q&A Chatbot")

    menu = ["Q&A", "Schedule Appointment", "Live Chat Support", "Feedback", "Knowledge Base"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Q&A":
        st.subheader("Ask a question about TechSolutions:")
        question = st.selectbox("Select an example question", [""] + example_questions)
        user_question = st.text_input("...or type your own question here:")
        final_question = user_question if user_question else question
        if st.button("Get Answer"):
            if final_question:
                answer = get_answer(final_question, data_context)
                st.write(answer)
            else:
                st.warning("Please select a question or enter your own.")
    elif choice == "Schedule Appointment":
        schedule_appointment()
    elif choice == "Live Chat Support":
        live_chat()
    elif choice == "Feedback":
        collect_feedback()
    elif choice == "Knowledge Base":
        knowledge_base_search()

if __name__ == "__main__":
    main()
