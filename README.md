# AI-Powered Personal Study Planner Agent

**Subtitle:** Automating Study Schedules, Tracking Progress, and Boosting Productivity

---

## Project Overview
Students often spend hours manually planning their study schedules, keeping track of subjects, and marking completed sessions. This project is an AI-powered study planner that automates scheduling, tracks progress, and organizes study sessions efficiently.

---

## Features
- **Add Subjects:** Enter subject name, date, duration, and optional notes.  
- **View Schedule:** See all upcoming and completed study sessions.  
- **Mark Sessions Completed:** Track your progress easily.  
- **Persistent Storage:** All data is saved in SQLite, so your schedule is safe even after closing the app.  
- **Streamlit Interface:** Interactive and user-friendly web app.

---

## Project Structure
PersonalStudyPlanner/
├─ agents/
│ ├─ init.py
│ └─ main_agent.py # Main AI agent handling all study tasks
├─ data/
│ └─ memory.db # SQLite database storing sessions
├─ app.py # Streamlit interface
└─  README.md # Project writeup

---

## How It Works
Add Subject: Input the subject, study date, duration, and notes.
View Schedule: Check all upcoming and completed sessions.
Mark Completed: Click to mark a session as done; it updates the SQLite database.
All user data is stored in data/memory.db for persistence

---

## Technologies Used
Python 3.x
Streamlit – Interactive web app interface
SQLite – Persistent database
OOP Concepts – Modular agent design with MainAgent

---

## Working app demo : 
https://siddhikasavant-personalstudyplanner-app-mlhdwi.streamlit.app/
