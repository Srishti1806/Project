import sys

def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


def assign_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg <= 89:
        return "A"
    elif 65 <= avg <= 79:
        return "B"
    elif 50 <= avg <= 64:
        return "C"
    elif 40 <= avg <= 49:
        return "D"
    else:
        return "F"


def main():
    name = sys.argv[1]
    department = sys.argv[2]
    semester = sys.argv[3]
    m1 = float(sys.argv[4])
    m2 = float(sys.argv[5])
    m3 = float(sys.argv[6])

    avg = calculate_average(m1, m2, m3)
    grade = assign_grade(avg)

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Average Marks:", avg)
    print("Grade:", grade)


if __name__ == "__main__":
    main()
