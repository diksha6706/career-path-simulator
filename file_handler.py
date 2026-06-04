##file read

from datetime import datetime

def view_reports():
    try:
        file = open("reports.txt", "r")

        content = file.read()

        print(content)

        file.close()
    except:
        print("No Reports Found")
#file write
def save_report(name, best_career, best_score, status, missing_skills):
    missing_text = ""
    for skill in missing_skills:
        missing_text += skill + "\n"

    current_time = datetime.now()
    date = current_time.strftime("%d-%m-%Y")
    time = current_time.strftime("%I:%M %p")

    report = f"""
    Date: {date}
    Time: {time}
    Name: {name}
    Best Career: {best_career}
    Matched Score: {best_score}
    Career Readiness level: {status}
    Missing Skills: {missing_text}
    """

    file = open("reports.txt", 'a')
    file.write(report)
    file.close()

    print("\nReport Saved Successfully!")

def show_analytics():
    
    try:

        file = open("reports.txt", "r")

        data = file.read()

        file.close()

        lines = data.split("\n")

        career_count = {}

        total_reports = 0

        scores = []

        for line in lines:

            if "Best Career:" in line:

                career = line.replace(
                    "Best Career:",
                    ""
                ).strip()

                total_reports += 1

                if career in career_count:

                    career_count[career] += 1

                else:

                    career_count[career] = 1

            if "Matched Score:" in line:

                score = line.replace(
                    "Matched Score:",
                    ""
                ).strip()

                score = float(score)

                scores.append(score)

        print("\nCareer Analytics")
        print("-" * 25)

        print(
            "Total Reports:",
            total_reports
        )

        print("\nCareer Popularity:")

        for career, count in career_count.items():

            print(
                career,
                ":",
                count
            )

        if len(career_count) > 0:

            most_popular = max(
                career_count,
                key=career_count.get
            )

            print(
                "\nMost Popular Career:",
                most_popular
            )

        if len(scores) > 0:

            average_score = (
                sum(scores)
                / len(scores)
            )

            print(
                "\nAverage Match Score:",
                round(average_score, 2)
            )

            highest_score = max(scores)

            print(
                "Highest Match Score:",
                highest_score
            )

            lowest_score = min(scores)

            print(
                "Lowest Match Score:",
                lowest_score
            )

    except:

        print("No Reports Found")