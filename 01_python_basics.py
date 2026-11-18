# 01. Python - Data Structures and Basic Testing

def get_student_info():
    return {
        "name": "Hariom Gupta",
        "branch": "AIML",
        "skills": ["Python", "Data Structures", "Problem Solving"]
    }

if __name__ == "__main__":
    data = get_student_info()
    assert data["branch"] == "AIML"
    print("01 Python Test Passed:", data)
