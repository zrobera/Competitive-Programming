class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        is_open = False
        output = ""

        for line in source:
            i = 0
            while i < len(line):
                if not is_open:
                    if i + 1 < len(line) and line[i:i+2] == '/*':
                        is_open = True
                        i += 1 
                    elif i + 1 < len(line) and line[i:i+2] == '//':
                        break
                    else:
                        output += line[i]
                elif is_open and i + 1 < len(line) and line[i:i+2] == '*/':
                    is_open = False
                    i += 1 
                i += 1

            if output and not is_open:
                ans.append(output)
                output = ""

        return ans
