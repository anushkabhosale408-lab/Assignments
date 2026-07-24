import streamlit as st
import csv
import os

st.title("🎓 Student Management System")

if "students" not in st.session_state:
    st.session_state.students = []

st.write("Welcome to my first Streamlit Project!")

name = st.text_input("Enter Student Name")
roll_no = st.text_input("Enter Roll Number")

branch = st.selectbox(
    "Select Branch",
    ["AIML", "Computer", "IT", "ENTC", "Mechanical"]
)

marks = st.number_input("Enter Marks", min_value=0, max_value=100)

if st.button("Submit"):
    student = {
        "Name": name,
        "Roll No": roll_no,
        "Branch": branch,
        "Marks": marks
    }

    st.session_state.students.append(student)

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, roll_no, branch, marks])

    st.success(f"Welcome {name}!")

    st.write("### Student Details")
    st.write("Name:", name)
    st.write("Roll Number:", roll_no)
    st.write("Branch:", branch)
    st.write("Marks:", marks)

st.write("### All Students")

for student in st.session_state.students:
    st.write("Name:", student["Name"])
    st.write("Roll No:", student["Roll No"])
    st.write("Branch:", student["Branch"])
    st.write("Marks:", student["Marks"])
    st.write("---------------------------")

st.write("### Search Student")

search_roll = st.text_input("Enter Roll Number to Search")

if st.button("Search"):
    found = False

    for student in st.session_state.students:
        if student["Roll No"] == search_roll:
            st.success("Student Found!")
            st.write("Name:", student["Name"])
            st.write("Branch:", student["Branch"])
            st.write("Marks:", student["Marks"])
            found = True
            break

    if not found:
        st.error("Student Not Found")

st.write("### Delete Student")

delete_roll = st.text_input("Enter Roll Number to Delete")

if st.button("Delete"):
    found = False

    for student in st.session_state.students:
        if student["Roll No"] == delete_roll:
            st.session_state.students.remove(student)
            st.success("Student Deleted Successfully!")
            found = True
            break

    if not found:
        st.error("Student Not Found")