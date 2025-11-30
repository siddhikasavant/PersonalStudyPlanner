from schedule_generator import generate_schedule

subjects = ["Math", "Physics", "English"]
start_date = "2025-12-01"

schedule = generate_schedule(subjects, start_date)
for s in schedule:
    print(s)

