def calculate_average(scores):
    return sum(scores) / len(scores)

def percentage_distribution(scores):
    bins = {"90-100": 0, "80-89": 0, "70-79": 0, "60-69": 0, "<60":0}
    for score in scores:
        if score >= 90:
            bins["90-100"] += 1
        elif score >= 80:
            bins["80-89"] += 1
        elif score >= 70:
            bins["70-79"] += 1
    return bins