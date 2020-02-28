def suma_kolokviumi(resultStudents):
    for student in resultStudents:
        firstP = student["Prv Kolokvium"]
        secondP = student["Vtor Kolokvium"]
        totalK = firstP + secondP
        student.pop("Prv Kolokvium")
        student.pop("Vtor Kolokvium")

        student["Vkupno od kolokviumi"] = totalK

    return resultStudents # Return the list

if __name__ == "__main__":
    n = int(input())
    resultStudents = []  # List of dictionaries
    for i in range(0, n):
        student = {}  # Dictionary for one student
        noIndex = input()
        noPointsFirst = float(input())
        noPointsSecond = float(input())
        # Adding info to dictionary. Then adding to dictionary to list of dictionaries
        student = {
            "indeks": noIndex,
            "Predmet": "Veshtachka inteligencija",
            "Prv Kolokvium": noPointsFirst,
            "Vtor Kolokvium": noPointsSecond,
        }
        resultStudents.append(student) # Adding one student to the list

    print(suma_kolokviumi(resultStudents))