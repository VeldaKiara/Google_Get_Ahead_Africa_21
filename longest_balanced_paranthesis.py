#question
#Given a string of parentheses, find the size of the 
# longest contiguous substring of balanced parentheses. 
# Parentheses are considered
# balanced when there is a valid closing parenthesis for an opening one
# e.g In this string: ())(()), the longest continuous set would be 4 
# characters long (the last 4 characters of the input)
# e.g For )(()))))((((() , the max length would be 4


# everytime we get an opening bracket we pudh it to stack,
# when we get a closing bracket we pop the 1st item on the stack, we
# need to calculate the lenght of
# the string and maximum lenght as we move throught the string.


def longest_balanced(string):
    stack = []
    longest_balanced_paranthesis = 0
    for index, paranthesis in enumerate(string):
        if paranthesis == '(':
            stack.append(index) #stores index of last opening bracket
            
        else:
            if len(stack) > 0:  # gets the lenght between the current closing bracket and last opening bracket
                top = stack.pop() #stores the index of the item that was popped, the top most opening bracket
                length = (index - top) + 1 
                longest_balanced_paranthesis = max( length, longest_balanced_paranthesis)
                
            
    return longest_balanced_paranthesis

 #test   
# print(longest_balanced('())(())'))
# print(longest_balanced(')(()))))((((()'))