# agents/assessment_agent.py

import time
from agents.question_generator import generate_question

def ask_questions(skill, difficulty, count):
    correct = 0
    logs = []
    for _ in range(count):
        q_data = generate_question(skill, difficulty)
        print("\n" + q_data)
        start = time.time()
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        end = time.time()
        correct_ans = q_data.split("Answer:")[-1].strip().upper()[0]
        is_correct = (answer == correct_ans)
        if is_correct:
            correct += 1
        logs.append({
            'Skill': skill,
            'Question': q_data.split("\n")[0],
            'Difficulty': difficulty,
            'User Answer': answer,
            'Correct Answer': correct_ans,
            'Is Correct': is_correct,
            'Time Taken (s)': round(end - start, 2)
        })
    return correct, logs

def conduct_adaptive_assessment(user_data, matched_skills, max_questions=25):
    results = []
    total_asked = 0
    difficulty_time = {'basic': 0, 'medium': 0, 'scenario': 0}
    difficulty_counts = {'basic': 0, 'medium': 0, 'scenario': 0}

    for skill in matched_skills:
        print(f"\nAssessing skill: {skill.upper()}")

        correct_basic, basic_qs = ask_questions(skill, 'basic', 3)
        for q in basic_qs:
            difficulty_time['basic'] += q['Time Taken (s)']
            difficulty_counts['basic'] += 1

        total_asked += len(basic_qs)
        results.extend(basic_qs)

        if correct_basic >= 2 and total_asked < max_questions:
            correct_medium, medium_qs = ask_questions(skill, 'medium', 2)
            for q in medium_qs:
                difficulty_time['medium'] += q['Time Taken (s)']
                difficulty_counts['medium'] += 1

            total_asked += len(medium_qs)
            results.extend(medium_qs)

            if correct_medium == 2 and total_asked < max_questions:
                _, scenario_qs = ask_questions(skill, 'scenario', 2)
                for q in scenario_qs:
                    difficulty_time['scenario'] += q['Time Taken (s)']
                    difficulty_counts['scenario'] += 1

                total_asked += len(scenario_qs)
                results.extend(scenario_qs)
        else:
            print(f"  Need improvement in {skill}, skipping advanced levels.")

        if total_asked >= max_questions:
            print("Reached maximum question limit.")
            break

    total_time = sum(difficulty_time.values())
    total_correct = sum(1 for r in results if r['Is Correct'])
    total_wrong = len(results) - total_correct

    correct_topics = list(set([r['Skill'] for r in results if r['Is Correct']]))
    wrong_topics = list(set([r['Skill'] for r in results if not r['Is Correct']]))

    metadata = {
        'Total Questions': len(results),
        'Correct Answers': total_correct,
        'Wrong Answers': total_wrong,
        'Correct Topics': correct_topics,
        'Wrong Topics': wrong_topics,
        'Difficulty Stats': difficulty_counts,
        'Time Stats': difficulty_time,
        'Total Time (s)': round(total_time, 2)
    }

    return results, metadata
