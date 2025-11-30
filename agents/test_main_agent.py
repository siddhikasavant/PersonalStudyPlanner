from agents.main_agent import MainAgent

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Initialize the main agent
agent = MainAgent()

# Add subjects
agent.add_subject("Math")
agent.add_subject("Physics")
agent.add_subject("English")

# Generate study schedule starting from Dec 1, 2025
schedule = agent.create_schedule(["Math", "Physics", "English"], "2025-12-01")
print("Generated Schedule:")
for s in schedule:
    print(s)

# View all stored sessions from DB
sessions = agent.view_schedule()
print("\nStored Sessions in DB:")
for s in sessions:
    print(s)

# Close DB connection
agent.close()
