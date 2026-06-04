class CareerSimulator:

    def __init__(self, careers):

        self.careers = careers

    def calculate_scores(self, user_skills_set):

        career_scores = {}

        for career in self.careers:

            required_skills = set(
                self.careers[career]["skills"]
            )

            matched = user_skills_set.intersection(
                required_skills
            )

            score = (
                len(matched)
                / len(required_skills)
            ) * 100

            career_scores[career] = score

        return career_scores

    def find_best_career(self, career_scores):

        return max(
            career_scores,
            key=career_scores.get
        )
    
    def get_missing_skills(
            self,
            best_career,
            user_skills_set):

        required_skills = set(
            self.careers[best_career]["skills"]
        )

        missing_skills = (
            required_skills
            - user_skills_set
        )

        return missing_skills
    
def get_readiness_status(self, best_score):

    if best_score >= 90:
        return "Excellent Match"

    elif best_score >= 70:
        return "Almost Ready"

    elif best_score >= 50:
        return "Good Foundation"

    elif best_score >= 30:
        return "Needs Preparation"

    else:
        return "Beginner"

def generate_roadmap(self, missing_skills):

    month = 1

    print("\nLearning Roadmap:")

    for skill in missing_skills:

        print(
            "Month",
            month,
            "->",
            skill
        )

        month += 1