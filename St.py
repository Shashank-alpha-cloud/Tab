import streamlit as st

st.title("Simple Chatbot")

st.session_state.messages=[]

a=st.text_input("Enter a command:")

if st.button("Run Command"):

	if a.lower() == "hi":

		st.session_state.messages.append("Hello!")

	elif a.lower() == "bye": 

		st.session_state.messages.append("Goodbye!")

	else: 

		st.session_state.messages.append("Unknown command. Try 'hi', 'bye' ")

st.subheader("Output:")

for msg in st.session_state.messages:


	st.text(msg)

