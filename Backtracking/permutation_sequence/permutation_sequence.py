
class BacktrackSolution:
    def permute(self, Arr):
        # Initialize data structure to track unique permutation
        self.track_permutes = {}
        # Begin recursive permutation
        self.permute_recursive([], Arr)

    def permute_recursive(self, choosen, remaining):
        # terminating recursive condition
        if (len(remaining) == 0):
            # save permutation result
            self.track_permutes[tuple(choosen)] = 1
            return
        # iterate and recursive call to itself
        for e in remaining:
            choosen.append(e)
            # explore recursively
            self.permute_recursive(choosen, remaining[:-1])
            # pop back to restore [choosen] after recursion, in cpp we will need to manually restore [remaining]
            choosen.pop()

if __name__ == '__main__':
    # data to play with
    arr = [1, 1, -2, 3, 5, -19, 20, 111, 68, 89, 17, 12, 9, 17, 91]
    solution = BacktrackSolution()
    
    permutations_results = solution.permute(arr)
    for result in permutations_results.key():
        print(result)
