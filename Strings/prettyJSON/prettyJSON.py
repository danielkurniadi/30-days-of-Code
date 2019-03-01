class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, json):
        json = "%r"%json
        length = len(json)
        tabs, is_outer_dict = 0, True
        is_newline = True
        pretty_json = ""
        i = 0
        while i < length:
            ch = json[i]
            if (ch == '{') or  (ch == '['):
                if not is_outer_dict:
                    pretty_json += '\n'
                is_outer_dict = False
                pretty_json += '\t'*tabs + ch+ '\n'
                tabs += 1
                i+=1
                is_newline = True
                continue
            if (ch == '}') or (ch == ']'):
                tabs -= 1
                pretty_json += '\n' + '\t'*tabs + ch + '\n'
                i+=1
                is_newline = True
                continue
            if is_newline:
                pretty_json += '\t'*tabs
                is_newline = False
            pretty_json += ch
            if ch == ',':
                pretty_json += '\n'
                is_newline = True
            i +=1
        pretty_json += '\n'
        print([line for line in pretty_json.split('\n') if line and (line not in "\"\'")] )

if __name__ == '__main__':
    solver = Solution()
    solver.prettyJSON(r'["foo", {"bar":["baz",null,1.0,2]}]')
    solver.prettyJSON(r'{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}')
    solver.prettyJSON('{"id":100,"firstName":"Jack","lastName":"Jones","age":12}')
            
