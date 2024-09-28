"""https://leetcode.com/problems/simplify-path/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        way = path.split("/")
        lst = []
        for x in way:
            if x not in [".", "", ".."]:
                lst.append(x)
            elif lst and x == "..":
                lst.pop()

        return "/" + "/".join(lst)
