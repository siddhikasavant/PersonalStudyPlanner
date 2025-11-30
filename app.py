import streamlit as st
from agents.main_agent import MainAgent

st.title("Personal Study Planner")

agent = MainAgent()

# ---- Add Subject ----
st.header("Add Subject")
new_subject = st.text_input("Subject Name")
date = st.date_input("Date")
duration = st.number_input("Duration (hours)", min_value=1, max_value=12, value=2)
notes = st.text_area("Notes (optional)")

if st.button("Add Subject"):
    try:
        agent.add_subject(new_subject, str(date), duration, notes)
        st.success(f"Added subject: {new_subject}")
    except ValueError as e:
        st.warning(str(e))

# ---- View Schedule ----
st.header("View Schedule")
if st.button("Show Schedule"):
    sessions = agent.view_schedule()
    if sessions:
        for s in sessions:
            st.write(f"ID:{s[0]} | Subject: {s[1]} | Date: {s[2]} | Duration: {s[3]}h | Completed: {bool(s[4])} | Notes: {s[5]}")
    else:
        st.info("No sessions found!")

# ---- Mark Completed ----
st.header("Mark Session as Completed")
session_id = st.number_input("Enter Session ID", min_value=1)
if st.button("Mark Completed"):
    agent.mark_completed(session_id)
    st.success(f"Session {session_id} marked as completed!")
