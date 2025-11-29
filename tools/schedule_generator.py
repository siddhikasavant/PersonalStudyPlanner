from datetime import datetime, timedelta

def generate_schedule(subjects, start_date, study_hours_per_day=2):
    schedule = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    
    for i, subject in enumerate(subjects):
        session = {
            "subject": subject,
            "date": current_date.strftime("%Y-%m-%d"),
            "duration": study_hours_per_day
        }
        schedule.append(session)
        current_date += timedelta(days=1)
    
    return schedule

