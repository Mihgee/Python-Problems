#this question was so confusing, the wording made me unsure what to do.
f= open('score', 'r')
data = f.readlines()
count= 0
marks=[]
for line in data:
    count+=1
    if(count!=1):

        marks.append(int(line))
print("The highest score is:", max(marks))



'''
studentNumber = ""
studentScore = 0
maxS = -1
maxName = ""
count=0
while True:
    studentNumber = input("Student Number (type stop to calculate):")
    count += 1
    if studentNumber.lower() == "stop"+"":
        break
    studentScore = eval(input("Enter a Student Score: "))

    if studentScore > maxS:
        maxS = studentScore
        maxName = studentNumber

print("Top Student is student number",maxName,"with a test score of",maxS,"out of",count,"students")'''
