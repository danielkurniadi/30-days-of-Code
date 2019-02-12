
class BacktrackSolution:
    """
    Generate all possible (unique) permutations of sequence.
    Uses Backtracking with dictionary as Hashset data structure. 

    Time Complexity:
        T = O(n**n), where n is number of element in a given sequence/array to permute
    """
    def permute(self, Arr):
        """Generate/permute all possible permutations of sequence
        """
        # Initialize hashset to track unique permutation using dictionary
        self.track_permutes = {}
        # Begin recursive permutation
        self.permute_recursive([], Arr)

    def permute_recursive(self, choosen, remaining):
        """Permutation helper function that does the recursion
        """
        # terminating recursive condition
        if (len(remaining) == 0):
            # save permutation result
            self.track_permutes[tuple(choosen)] = 1
            return
        # iterate and recursive call to itself
        for i,e in enumerate(remaining):
            choosen.append(e)
            # explore recursively
            remaining.pop(i)
            self.permute_recursive(choosen, remaining)
            # pop last choosen element from [choosen] after recursion and restore [remaining]
            remaining.insert(i, choosen.pop())

if __name__ == '__main__':
    # data to play with
    arr = [1, 1, -2, 3, 5]
    solution = BacktrackSolution()
    solution.permute(arr)

    permutations_results = solution.track_permutes
    
    for result in permutations_results.keys():
        print(result)
    print(len(permutations_result.keys())) 
