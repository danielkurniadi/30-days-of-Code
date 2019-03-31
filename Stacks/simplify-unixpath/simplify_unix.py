
class Solution:
    @classmethod
    def simplify_unix(cls, path):
        files = path.split('/')
        simplified = []

        for item in files: 
            if item == "..":
                simplified.pop()
            elif (not item) or (item == "."):
                continue
            else:
                simplified.append(item)
        
        print(simplified)
        print("/".join(simplified))


if __name__ == '__main__':
    path = "/a/./b/../../c/"
    Solution.simplify_unix(path)

