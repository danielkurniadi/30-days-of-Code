class Solution:
    def romanToInt(self, roman):
    roman_dic = {
        'I':1, 
        'V': 5, 
        'X': 10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    N, integer = len(roman), 0
    for i in range(N):
        n = roman_dic[roman[i]]
        if i<N-1:
        nex = roman_dic[roman[i+1]]
        if nex > n:
            n = -n
        integer += n
    return integer