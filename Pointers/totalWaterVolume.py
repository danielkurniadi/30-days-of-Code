
class BaseSolution():

    @classmethod
    def get_water_volume(cls, barriers):
        pass

class MySolution(BaseSolution):
    """My solution
    """
    @classmethod
    def get_water_volume(cls, barriers):
        n = len(barriers)
        total_vol = 0

        i = 0
        while(i < n):
            current = 0
            height = barriers[i]
            j = i+1
            while (j < n) and (barriers[j] < height):
                current += height-barriers[j]
                j += 1
            if j == n:
                current = 0
                i += 1
            else:
                total_vol += current
                i = j

        return total_vol

class GFGSolution(BaseSolution):
    """Geeks for Geeks's solution
    """
    @classmethod
    def get_water_volume(cls, barriers):
        i, j = 0, len(barriers)-1
        left_max, right_max = 0, 0
        total_vol = 0
        while(i <= j):
            if barriers[i]<barriers[j]:
                if barriers[i] > left_max:
                    # When current barrier is taller than left_max
                    # volume water trapped is 0 due to overflow. 
                    # and update the left_max also
                    left_max = barriers[i]
                else:
                    # When current barrier is shorter than left_max
                    # vol water trapped at that point is below:
                    total_vol += left_max - barriers[i]
                i += 1
                continue
            else:
                if barriers[j] > right_max:
                    # When current barrier is taller than right_max
                    # volume water trapped is 0 due to overflow. 
                    # and update the right_max also
                    right_max = barriers[j]
                else:
                    # When current barrier is shorter than left_max
                    # vol water trapped at that point is below:
                    total_vol += right_max - barriers[j]
                j -= 1

        return total_vol

if __name__ == '__main__':
    barriers = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    my_answer = MySolution.get_water_volume(barriers)
    gfg_answer = GFGSolution.get_water_volume(barriers)

    print("My Solution is : ", my_answer)
    print("Geek for geek solution is: ", gfg_answer)
