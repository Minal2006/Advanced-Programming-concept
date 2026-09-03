

def attendance_percentage(present, total):
    return (present / total) * 100


def eligibility(percentage):
    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"