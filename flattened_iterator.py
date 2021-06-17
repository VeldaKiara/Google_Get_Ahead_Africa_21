# Given a list of iterators, implement a FlattenedIterator class which incrementally iterates over the integers from all the iterators in an interleaved fashion. 

# Example:

# Iterators[0] = [1,2,3]
# Iterators[1] = [4,5]
# Iterators[2] = [6,7,8]

# FlattenedIterator = [1, 4, 6, 2, 5, 7, 3, 8]
# An iterator implements the next() and hasNext() interface. You're free to use them, and you will implement them on the FlattenedIterator class.

# You're free to initialize FlattenedIterator with any data structure of your choice for the iterators. 

class FlattenedIterator:
    def __init__(self, subiterators):
        self.subiterators = []
        self.res_index = 0
        self.getValue(subiterators)
     
    def getValue(self,Subiterators):
        for item in Subiterators:
            if item.hasNext():
                self.subiterators.append(item)
     
    def ridValue(self):
        self.subiterators.pop(self.res_index)
        
    
    def moveNext(self):
        res_index = self.res_index
        if not self.subiterators[res_index].hasNext():
            self.ridValue()
        else:
            res_index = self.res_index + 1
        
        if res_index <= len(self.subiterators) - 1:
            self.res_index = res_index
        else:
            self.res_index = 0    
            
    def hasNext(self):
        if (self.subiterators):
            return True
        return False

    def next(self):
      if self.hasNext():
            next_value = self.subiterators[self.res_index].next()
            self.moveNext()
            return next_value
 

