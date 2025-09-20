import streamlit as st
from database import init_db
from models import add_task, get_tasks, mark_complete, delete_task

# Initialize DB
init_db()

st.set_page_config(page_title="SmartOrganizer", page_icon="✅", layout="centered")

st.title("📌 SmartOrganizer")
st.write("A simple task management app built with Python & Streamlit.")

menu = ["Add Task", "View Tasks", "Mark Complete", "Delete Task"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Task":
    st.subheader("➕ Add a New Task")
    with st.form("task_form"):
        title = st.text_input("Task Title")
        description = st.text_area("Description")
        priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        deadline = st.date_input("Deadline")
        submitted = st.form_submit_button("Add Task")
        if submitted:
            add_task(title, description, priority, str(deadline))
            st.success(f"Task '{title}' added!")

elif choice == "View Tasks":
    st.subheader("📋 All Tasks")
    tasks = get_tasks()
    if tasks:
        for task in tasks:
            st.write(f"**{task[0]} - {task[1]}** | {task[2]} | Priority: {task[3]} | Deadline: {task[4]} | Status: {task[5]}")
    else:
        st.info("No tasks available.")

elif choice == "Mark Complete":
    st.subheader("✅ Mark Task as Complete")
    tasks = get_tasks()
    task_ids = [t[0] for t in tasks]
    task_id = st.selectbox("Select Task ID", task_ids)
    if st.button("Mark Complete"):
        mark_complete(task_id)
        st.success("Task marked as complete!")

elif choice == "Delete Task":
    st.subheader("🗑️ Delete a Task")
    tasks = get_tasks()
    task_ids = [t[0] for t in tasks]
    task_id = st.selectbox("Select Task ID", task_ids)
    if st.button("Delete Task"):
        delete_task(task_id)
        st.warning("Task deleted!")