import streamlit as st
from langgraph.types import Command
from graph import app  #import LangGraph workflow

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = None
if "thread_config" not in st.session_state:
    st.session_state.thread_config = {"configurable": {"thread_id": "1"}}
if "approved" not in st.session_state:
    st.session_state.approved = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

st.title("💬 SQL Agent")

# Query input
query = st.text_input("Enter your query")

if query and st.session_state.messages is None:
    if query.lower() == "exit":
        st.warning("Conversation ended.")
    else:
        # Initial user query
        initial_state = {"messages": [("user", query)]}
        st.session_state.messages = app.invoke(initial_state, st.session_state.thread_config)
        st.session_state.approved = False

# Show generated SQL query (latest message)
if st.session_state.messages and not st.session_state.approved:
    with st.expander("🧠 Generated SQL Query", expanded=True):
        final_query = st.session_state.messages["messages"][-1].content
        st.code(final_query, language="sql")

    # Feedback input
    st.session_state.feedback = st.text_input("Approve or give feedback:", key="feedback_box")

    # Buttons for interaction
    col1, col2 = st.columns(2)
    if col1.button("✅ Approve"):
        # Continue workflow
        st.session_state.messages = app.invoke(
            Command(resume="yes"),
            config=st.session_state.thread_config,
        )
        st.session_state.approved = True

    if col2.button("🔁 Send Feedback"):
        if st.session_state.feedback.strip():
            st.session_state.messages = app.invoke(
                Command(resume=st.session_state.feedback),
                config=st.session_state.thread_config,
            )
            st.session_state.feedback = ""  # Reset feedback
            st.rerun()  # ✅ Trigger UI update to show new query


# Show final result
if st.session_state.messages and st.session_state.approved:
    st.success("✅ Final Result:")
    st.markdown(st.session_state.messages["messages"][-1].content)

# Reset to start new query
if st.session_state.approved:
    if st.button("Start New Query"):
        st.session_state.messages = None
        st.session_state.approved = False
        st.session_state.feedback = ""
