def isMarkovMatrix(m):
   for i in range(len(m)):
       for j in range(len(m[0])):
           if(m[i][j] < 0):
               return False

   for j in range(len(m[0])):
       sum_col = 0
       for i in range(len(m)):
           sum_col += m[i][j]

       if(sum_col != 1.0):
           return False

   return True


mat = []

print("Enter a 3-by-3 matrix row by row:")
mat.append(list(map(float,input().split(" "))))
mat.append(list(map(float,input().split(" "))))
mat.append(list(map(float,input().split(" "))))

markov = isMarkovMatrix(mat)

if(markov):
   print("It is a Markov matrix")
else:
   print("It is not a Markov matrix")