from datetime import datetime, timedelta

def generate_schedule(subjects, start_date, study_hours_per_day=2):
    """
    Generates a simple daily study schedule.
    
    :param subjects: List of subject names
    :param start_date: Start date in "YYYY-MM-DD" format
    :param study_hours_per_day: Hours per subject per day
    :return: List of session dictionaries
    """
    schedule = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    
    for i, subject in enumerate(subjects):
        session = {
            "subject": subject,
            "date": current_date.strftime("%Y-%m-%d"),
            "duration": study_hours_per_day
        }
        schedule.append(session)
        current_date += timedelta(days=1)  # Next subject/day
    
    return schedule
