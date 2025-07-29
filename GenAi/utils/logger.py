import csv
from datetime import datetime
import os


def save_assessment_report(user_data, results, metadata):
    user_id = user_data['name'].replace(" ", "_").lower()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{user_id}_{timestamp}_assessment.csv"
    folder_path = "data/assessments"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)

    with open(file_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write metadata
        writer.writerow(["User ID", user_data['name']])
        writer.writerow(["Total Questions", metadata['Total Questions']])
        writer.writerow(["Correct Answers", metadata['Correct Answers']])
        writer.writerow(["Wrong Answers", metadata['Wrong Answers']])
        writer.writerow(["Correct Topics", ", ".join(metadata['Correct Topics'])])
        writer.writerow(["Wrong Topics", ", ".join(metadata['Wrong Topics'])])
        writer.writerow(["Total Time (s)", metadata['Total Time (s)']])
        writer.writerow([])
        writer.writerow(["Difficulty", "Questions", "Time Spent (s)"])
        for level in ['basic', 'medium', 'scenario']:
            writer.writerow([
                level.capitalize(), 
                metadata['Difficulty Stats'].get(level, 0), 
                metadata['Time Stats'].get(level, 0)
            ])
        
        writer.writerow([])
        writer.writerow(["Skill", "Question", "Difficulty", "User Answer", "Correct Answer", "Is Correct", "Time Taken (s)"])
        
        # Write question-level data
        for r in results:
            writer.writerow([
                r['Skill'],
                r['Question'],
                r['Difficulty'],
                r['User Answer'],
                r['Correct Answer'],
                "Yes" if r['Is Correct'] else "No",
                r['Time Taken (s)']
            ])

    print(f"\nReport saved to: {file_path}")


def print_assessment_summary(user_data, results, metadata):
    print("\ Assessment Summary")
    print("-" * 30)
    print(f" User: {user_data['name']}")
    print(f"Total Questions: {metadata['Total Questions']}")
    print(f" Correct: {metadata['Correct Answers']} | ❌ Wrong: {metadata['Wrong Answers']}")
    print(f" Total Time: {metadata['Total Time (s)']}s")

    print("\n Topic-wise Analysis")
    print(f" Correct Topics: {metadata['Correct Topics']}")
    print(f" Weak Topics: {metadata['Wrong Topics']}")

    print("\n Difficulty Breakdown")
    for level in ['basic', 'medium', 'scenario']:
        count = metadata['Difficulty Stats'].get(level, 0)
        time_spent = metadata['Time Stats'].get(level, 0)
        print(f"🔹 {level.capitalize()}: {count} questions | {round(time_spent, 2)}s spent")
