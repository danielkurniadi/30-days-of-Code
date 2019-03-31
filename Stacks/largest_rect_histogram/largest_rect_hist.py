
class Solution:

    @classmethod
    def largest_rect_area(cls, histogram):
        max_area = 0
        n = len(histogram)
        stack = []
        for i, bar in enumerate(histogram):
            # Checking whether the stack should get going or
            # pop
            if (len(stack) == 0) or (stack[-1][0] <= bar):
                # get going and push if bar height is greater
                # than top (last pushed) item in stack
                stack.append((bar, i))
            elif stack[-1][0] > bar:
                # when bar height is less than top item in stack
                # we unstack items that is less than the bar height
                while(len(stack)>0):
                    height, j = stack.pop()
                    if height > bar:
                        base = (i - stack[-1][1] - 1) if stack else i
                        area = base * height
                        print(i, j, base, height)
                        if max_area < area:
                            max_area = area
                    else:
                        # push back and stop unstacking
                        stack.append((height, j))
                        break
                stack.append((bar, i))

        while len(stack) > 0:
            # finish leftover
            height, j = stack.pop()
            base = (n - stack[-1][1] -1) if stack else n
            area = height * base
            print(j, base, height)
            if max_area < area:
                max_area = area

        print(max_area)
        return max_area

    @classmethod
    def max_area_histogram(cls, histogram): 
          
        # This function calulates maximum  
        # rectangular area under given  
        # histogram with n bars 
      
        # Create an empty stack. The stack  
        # holds indexes of histogram[] list.  
        # The bars stored in the stack are 
        # always in increasing order of  
        # their heights. 
        stack = list() 
      
        max_area = 0 # Initalize max area 
      
        # Run through all bars of 
        # given histogram 
        index = 0
        while index < len(histogram): 
              
            # If this bar is higher  
            # than the bar on top 
            # stack, push it to stack 
      
            if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
                stack.append(index) 
                index += 1
      
            # If this bar is lower than top of stack, 
            # then calculate area of rectangle with  
            # stack top as the smallest (or minimum 
            # height) bar.'i' is 'right index' for  
            # the top and element before top in stack 
            # is 'left index' 
            else: 
                # pop the top 
                top_of_stack = stack.pop() 
      
                # Calculate the area with  
                # histogram[top_of_stack] stack 
                # as smallest bar 
                base = (index - stack[-1] - 1) if stack else index
                area = histogram[top_of_stack] * base
                print(index, base, area)
                
      
                # update max area, if needed 
                max_area = max(max_area, area) 
      
        # Now pop the remaining bars from  
        # stack and calculate area with  
        # every popped bar as the smallest bar 
        while stack: 
              
            # pop the top 
            top_of_stack = stack.pop() 
      
            # Calculate the area with  
            # histogram[top_of_stack]  
            # stack as smallest bar 
            area = (histogram[top_of_stack] * 
                  ((index - stack[-1] - 1)  
                    if stack else index)) 
      
            # update max area, if needed 
            max_area = max(max_area, area) 
      
        # Return maximum area under  
        # the given histogram 
        return max_area 

if __name__ == '__main__':
    hist = [ 6, 2, 5, 4, 5, 1, 6 ]  #12 unit sqr 
    hist = [90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]  #348 unit sqr
    hist = [55, 33]
    max_area = Solution.largest_rect_area(hist)


