
""" Longest Consecutive Sequence Problem

 @definition: 
   Given an unsorted array of integer, find the longest consecutive elements sequence,
   that can be created from the element in the array.

 @solution: 
   There is a simple way to approach this problem. It uses the power of hashing or memoization. 
   The implementation can be done using simply an array to cache and retrieve in O(1) manner for each element
   Or we can use a more suitable built-in data structure in cpp called hashSet, a hashmap that replicates the behavior of set (mathematically).
   Hashset in C++ is called `std::unordered_set`.

"""

class Solution:
    # @param A : tuple/list of integers
    # @return an integer
    def longestConsecutive(self, A):
        minz, maxz = min(A), max(A)
        length = maxz - minz +1
        
        binslist = [-1]*length
        for n in A:
            binslist[n-minz] = 1
        
        count, maxcount = 0, 1
        for i in range(length):
            if binslist[i] == 1:
                count+=1
                continue
            else:
                if count>maxcount:
                    maxcount = count
                count = 0
        return maxcount