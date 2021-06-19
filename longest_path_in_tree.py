# Write a function that computes the length of the longest path of consecutive integers in a tree. 
# A node in the tree has a value and a set of children nodes. 
# A tree has no cycles and each node has exactly one parent. 
# A path where each node has a value 1 greater than its parent is a path of consecutive integers (e.g. 1,2,3 not 1,3,5). 
# A few things to clarify:
# Integers are all positive
# Integers appear only once in the tree

"""
suggested solution
class Tree:
    def __init__(self, value, *children):
        self.value = value
        self.children = children
# It's Python, so we walk the tree by iterating through it, yielding the length of
# the path ending at each node we encounter, then take the max of that.    
def longest_path(tree):
    
    def rec(current, parent_value=0, parent_path_length=0):
        # Length of the longest chain this node is a part of.
        current_path_length = (parent_path_length + 1
            if current.value == parent_value + 1 else 1)
        # Emit the length for this node 
        yield current_path_length
        # Recurse into the children
        for child in current.children:
            # For each of the descendant nodes, emit their lengths as well
            for value in rec(child, current.value, current_path_length):
                yield value
    # Take the overall maximum length.
    return max(*rec(tree))



# "Tests"
if __name__ == '__main__':
    
    assert longest_path(
        Tree(1,
             Tree(2,
                  Tree(4)),
             Tree(3))
    ) == 2
    assert longest_path(
        Tree(5,
             Tree(6),
             Tree(7,
                  Tree(8,
                       Tree(9,
                            Tree(15),
                            Tree(10))),
                  Tree(12)))
    ) == 4
    
    
print( longest_path(
        Tree(1,
             Tree(2,
                  Tree(4)),
             Tree(3))
    ) )
print( longest_path(
        Tree(5,
             Tree(6),
             Tree(7,
                  Tree(8,
                       Tree(9,
                            Tree(15),
                            Tree(10))),
                  Tree(12)))
    ))

"""
#my variation of the solution to be updated
