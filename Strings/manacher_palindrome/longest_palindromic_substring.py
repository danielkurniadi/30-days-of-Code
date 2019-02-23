class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, _s):
        s =  "#".join('#'+_s+'#')
        n = len(s)
        
        C, R = 0, 0
        P = [0]*n
        
        n_palin, idmax = 0, 0
        
        for i in range(n):
            mirr = 2*C - i
            if i < R:
                P[i] = min(R-i, P[mirr])
            while (i-P[i] > 0) and (i+P[i] < n-1) and (s[i+P[i]+1]==s[i-P[i]-1]):
                P[i] += 1
            if (i+P[i]<R):
                C, R = i, P[i] + i
            if P[i] > n_palin:
                n_palin, idmax = P[i], i
        
        i, j = idmax-(n_palin//2)*2, idmax+(n_palin//2)*2
        return s[i:j+1].replace('#', '')