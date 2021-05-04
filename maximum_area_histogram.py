#question
#Given an array of non-negative integers that represent the bars (y value) 
# in a histogram (with the array index being the x value), 
# find the rectangle with the largest area under the curve 
# and above the x-axis (i.e. the largest rectangle that fits 
# inside the histogram). Return the pair of array indices that
# represent the rectangle.
#divide and conquer method
def find_maximum_rectangle(histogram, start, end ):
    #best case scenario
    if (end - start) < 0:
        return 0, (-1,-1)
    
    minimum_index = start
    
    for i in range(start, end + 1):
        if histogram[i] < histogram[minimum_index]:
            minimum_index = i
    
    current_value = (end - start + 1) * histogram[minimum_index], (start, end)
    left = find_maximum_rectangle(histogram, start, minimum_index - 1)
    right = find_maximum_rectangle(histogram, minimum_index + 1, end)
    return max(current_value, left, right)

def maximum_rectangle(histogram):
    return find_maximum_rectangle(histogram, 0, len(histogram) - 1)[1]

histogram = [2,4,2,1,10,6,10]
print(maximum_rectangle(histogram))

#output 
#the largest area is 18,
# with height 6 and width from indices 4 to 6



    
      
    
  
  
    
      
  
  
  
  


  
  
