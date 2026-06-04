from career_data import careers
from file_handler import *
from career_simulator import CareerSimulator

simulator = CareerSimulator(careers)
#main code
print("1. Career Analysis")
print("2. View Previous Reports")
print("3. Compare Careers")
print("4. Career Analytics")

choice = input("Enter Choice: ")

if choice == "2":
    view_reports()
    exit()

if choice == "3":

    career1 = input("Enter First Career: ")

    career2 = input("Enter Second Career: ")

    if career1 not in careers or career2 not in careers:
        print("Invalid Career Name")
        exit()

    skills1 = careers[career1]["skills"]
    skills2 = careers[career2]["skills"]

    print("\n" + career1)


    for skill in skills1:
        print(skill)

    print("\n" + career2)
    print("-" * 20)

    for skill in skills2:
        print(skill)

    skills1_set = set(skills1)
    skills2_set = set(skills2)

    common_skills = skills1_set.intersection(skills2_set)

    print("\nCommon Skills:")
    print("-" * 20)

    if len(common_skills) == 0:
        print("No Common Skills")
    else:
        for skill in common_skills:
            print(skill)

    only_career1 = skills1_set - skills2_set
    only_career2 = skills2_set - skills1_set

    print("\nOnly in", career1)
    print("-" * 20)

    for skill in only_career1:
        print(skill)

    print("\nOnly in", career2)
    print("-" * 20)

    for skill in only_career2:
        print(skill)

    # Personalized Comparison

    user_skills = input(
        "\nEnter Your Skills (comma separated): "
    )

    skills_list = []

    for skill in user_skills.split(","):
        skills_list.append(skill.strip())

    user_skills_set = set(skills_list)

    matched1 = user_skills_set.intersection(skills1_set)

    score1 = (
        len(matched1)
        / len(skills1_set)
    ) * 100

    matched2 = user_skills_set.intersection(skills2_set)

    score2 = (
        len(matched2)
        / len(skills2_set)
    ) * 100

    print("\nCareer Match Scores")
    print("-" * 20)

    print(career1, ":", round(score1, 2), "%")
    print(career2, ":", round(score2, 2), "%")

    if score1 > score2:

        print(
            "\nRecommended Career:",
            career1
        )

    elif score2 > score1:

        print(
            "\nRecommended Career:",
            career2
        )

    else:

        print(
            "\nBoth careers are equally suitable."
        )

    exit()

if choice == "4":
    show_analytics()
    exit()



for career in careers:
    print(career)

user_skills = input("\nEnter your skills (comma separated): ")
#print(user_skills)

skills_list = []
for skill in user_skills.split(","):
    skills_list.append(skill.strip())

user_skills_set = set(skills_list)
#print(user_skills_set)

# career_scores = calculate_scores(careers, user_skills_set)
career_scores = simulator.calculate_scores(
    user_skills_set
)

best_career = simulator.find_best_career(career_scores)
print("\nCareer scores:")
for career, score in career_scores.items():
    print(career, ":" , score)

print("Best Career:", best_career)
print("Matched Score:", career_scores[best_career])

missing_skills = simulator.get_missing_skills(best_career, user_skills_set)

print("\nMissing Skills:")
for skill in missing_skills:
    print(skill)

simulator.generate_roadmap(missing_skills)

best_score = career_scores[best_career]
status = simulator.get_readiness_status(best_score)
print("\nCareer Readiness level:")
print(status)

name = input("Enter Your Name: ")
save_report(name, best_career, best_score, status, missing_skills)

