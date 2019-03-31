class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        expression = A.strip()
        operators = ['+', '-', '*', '/', '%', '^', '%', ':']
        right_paren = ['(', '{', '[']
        left_paren = [')', ']', '}']
        stack = []
        
        for c in expression:
            # switch case for each char input
            if c in left_paren:
                # Pop all the items until we see a 
                # right bracket
                is_redundant = True
                while (len(stack) > 0):
                    # while unstacking/popping items, we check
                    # if there is operator in between in current braces pair
                    item = stack.pop()
                    if item in right_paren:
                        # stop if we see the right braces
                        break
                    elif item in operators:
                        # mark as non redundant
                        is_redundant = False

                if is_redundant:
                    # an expression is redundant if
                    # no operators involved in a braces pair
                    return 1
            
            else:
                # otherwise, we threat other char as the same
                stack.append(c)

        return 0
                
if __name__ == '__main__':
    exp1 = "(a)" #redundant
    exp2 = "((a+b))" #redundant
    exp3 = "(((a+b)+(c+d)+(e+f)))" #also redundant
    exp4 = "((a+b)+(c+d)+(e+f))+g" #ok 

    is_redundant = Solution().braces(exp2)
    print(is_redundant)           
        
