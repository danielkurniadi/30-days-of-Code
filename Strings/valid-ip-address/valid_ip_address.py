class Solution():
    def restoreIpAddresses(self, s):
        self.solution = []
        self.recursive(["", "", "", ""], s, 0)
        print(self.solution)
        return [".".join(ip) for ip in self.solution]
    
    def recursive(self, chosens, remainings, n):
        if n >= 4:
            return
        if self.is_valid(chosens):
            if not remainings:
                non_empty = True
                for ip in chosens:
                    if not ip:
                        non_empty = False
                if non_empty:
                    self.solution.append(chosens)
                return
            if chosens[n]:
                self.recursive(chosens[:], remainings[:], n+1)
            chosens[n] = chosens[n]+remainings[0]
            self.recursive(chosens[:], remainings[1:], n)
    
    def is_valid(self, ipv4):
        valid = True
        for ip in ipv4:
            if not ip:
                continue
            if len(ip) > 3:
                return False
            x = int(ip)
            if x >255:
                return False
            if (ip[0]=="0") and len(ip)>1:
                return False
        return True

if __name__ == '__main__':
    solver = Solution()
    # solver.restoreIpAddresses("25525511135")
    # sln = solver.restoreIpAddresses("25525511135")
    sln = solver.restoreIpAddresses("0100100")
    print(sln)

