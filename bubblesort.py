
def sortRowWise(m):
 

 for i in range(len(m)):
  m[i].sort()
  
 for i in range(len(m)):
  for j in range(len(m[i])):
   print(m[i][j], end=" ")
  print()
  
 return 0


m = [[9, 8, 7, 1 ],[7, 3, 0, 2],[9, 5, 3, 2 ],[ 6, 3, 1, 2]]

sortRowWise(m)


