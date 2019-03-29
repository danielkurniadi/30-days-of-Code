class Solution:
	# @param A : list of strings
	# @return a strings
	@classmethod
	def longestCommonPrefix(cls, Arr):
	    all_dic = {}
	    for word in Arr:
	        m = len(word)
	        for i in range(1, m+1):
	            prefix = word[:i]
            	if prefix not in all_dic:
                    # if the prefix has not been seen,
                    # make a key value pair for it
                    all_dic[prefix] = 1 
                else:
                    # if the prefix has been seen. just add += 1 to it
                    all_dic[prefix] += 1
        
        longest_prefixes = ""
        for k, v in all_dic.items():
            if v == len(Arr):
                if len(k) > len(longest_prefixes):
                    longest_prefixes = k
        
        return k

if __name__ == '__main__':
	Arr = [
		"abcdefgh",
		"aefghijk",
		"abcefgh"
	]

	lngst_pref = Solution.longestCommonPrefix(Arr)
	print(lngst_pref)

