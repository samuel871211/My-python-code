Given_array = [1,2,3,4,5]

def stupid_Function(Given_array):
  total = 0
return total

#In this function, it doesn't matter whether the length of the Given_array gets longer, line 4 and 5 will only be executed by 1 time.
#So here we can say the time complexity of this function is O(1). #"O(1)" we read "big oh of one"

def find_Sum(Given_array)
  total = 0
  for each element in Given_array:
    total = total + element
return total

#As the size of the Given_array gets bigger, the for loop will be executed by more time.
#If we have n(n is a constant) elements inside the Given_array, the for loop will be executed by n time.
#So here we can say the time complexity of this function is O(n). #"O(n)" we read "big oh of n"

array_2d = [[1,2,3],
            [4,5,6],    
            [7,8,9]]
            
def find_Sum_2d(array_2d):
  total = 0
  for each row in array_2d:
    for each element in row:
      total = total + element
  return total
  
#line 26 will be executed by 3 times, and line 27 as well.
#Totally, line 26 and line 27 will be executed by 3 squared times.
#If we have n(n is a constant) rows inside array_2d, each row has n elements, the double for loop will be executed by n square times.
#So here we can say the time complexity of this function is O(n2). #"O(n2)" we read "big oh of n square"
