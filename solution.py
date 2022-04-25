def solution(number):
    
  i = 0
  suma = 0

  while i < number:
    if i % 5 == 0:
      suma = suma + i
    elif i % 3 == 0:
      suma = suma + i
    
    i += 1
  
  return suma
