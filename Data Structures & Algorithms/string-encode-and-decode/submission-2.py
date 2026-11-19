class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = []

        for s in strs:
            s_len = len(s)
            res.append(f"{s_len}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return list()
        i = 0
        res = []
        while i < len(s):
            digit = ""
            while i < len(s) and s[i].isdigit():
                digit += s[i]
                i += 1
            if s[i] == '#':
                i += 1

            res.append(s[i:i+int(digit)])
            i = i + int(digit)

        return res