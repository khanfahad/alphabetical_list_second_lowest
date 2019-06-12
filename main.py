pyStudents = []

numStudents = input("Number of students: ")
i = 0
while i < int(numStudents):
    name = input("Name: ")
    score = float(input("Score: "))
    studentSet = []
    studentSet.append(name)
    studentSet.append(float(score))
    pyStudents.append(studentSet)
    i+=1

scores = []
for i in pyStudents:
    scores.append(i[1])
scores.sort(reverse=True)
minScore = min(scores)

shortList = []
for p in scores:
    if p != minScore:
        shortList.append(p)

secondLowest = shortList[-1]

students = []
for j in pyStudents:
    if j[1] == secondLowest:
        students.append(j[0])
students.sort()
for k in students:
    print(k)
