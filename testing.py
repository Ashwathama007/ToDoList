import streamlit as st
# Set the title of the app
st.title("📝 To DO or NOT to DO?")

# Initialize an empty list to store tasks
if 'my_lst' not in st.session_state:
    st.session_state['my_lst'] = []

# Input for new tasks
task_input = st.text_input("Enter your task", placeholder="Type your task here...")

# Insert button to add new tasks
if st.button("Insert"):
    if task_input:
        st.session_state['my_lst'].append(task_input)

# Display the list of tasks or a message if the list is empty
if len(st.session_state['my_lst']) == 0:
    st.write("### 😞 Oops! The list is empty.")
else:
    st.write("## 📋 Tasks To Be Performed:")
    for i, t in enumerate(st.session_state['my_lst']):
        st.write(f"{i+1}. {t}")
    st.write("## 🗑️ Tasks To Be Deleted:")
    st.write("Double click on the tasks you want to delete")
    for i, t in enumerate(st.session_state['my_lst']):
        if st.checkbox(f"{i+1}. {t}"):
            st.session_state['my_lst'].remove(t)


# Add some spacing at the bottom of the app
st.write("\n" * 2)

















    