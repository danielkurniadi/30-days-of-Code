

"""
Problem Statement:
    Implement pow(X, n) % M.
    In other words given X, n and M; Calculate (X^n) % M as fast as possible!
Solution Approach:
    Combine power of modular computation and memoization.
    - modular computation:
        Since (a . b) % m = {(a % m).(b % m)} % m;
        Then x . x .... x % m = { [x^(n/2) % m] . [x^(n/2) % m] }
    - memoization:
        So as to avoid computing same thing twice.
"""

class Solution:
	# @param X : operand
	# @param n : exponent
	# @param M : modulus
	# @return an integer
	def Mod(self, X, n, M):
	    self.hashSet = {(2, 1, 3): 1}
        result = self.ModRecursive(X, n, M)
        return result
        
    def ModRecursive(self, x, n, m):
        if (x==0) or (x == m):
            return 0
        if n == 0:
            return 1
        r = self.hashSet.get((x, n, m))
        if r is None:
            if n%2 == 0:
                r = self.ModRecursive(x, n//2, m)
                self.hashSet[(x, n//2, m)] = r
                return self.ModRecursive(r*r, 1, m)
            else:
                r1 = x%m
                r2 = self.ModRecursive(x, n-1, m)
                self.hashSet[(x, 1, m)] = r1
                self.hashSet[(x, n-1, m)] = r2
                return self.ModRecursive(r1*r2, 1, m)
        else:
            return r