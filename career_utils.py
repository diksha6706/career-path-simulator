#readiness status
def get_readiness_status(best_score):
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
#roadmap
def generate_roadmap(missing_skills):
    month = 1
    print("\nLearning Roadmap:")
    for skill in missing_skills:
        print("Month", month, "->", skill)
        month += 1
#score calculations
def calculate_scores(careers, user_skills_set):
    career_scores = {}

    for career in careers:
        required_skills = set(careers[career]["skills"])
        matched = user_skills_set.intersection(required_skills)
        score = (len(matched)/len(required_skills))*100
        career_scores[career] = score
    return career_scores

##missing skills
def get_missing_skills(careers, best_career, user_skills_set):
    required_skills = set(careers[best_career]["skills"])
    missing_skills = required_skills - user_skills_set
    return missing_skills

##best career
def find_best_career(career_scores):
     return max(career_scores, key=career_scores.get)
