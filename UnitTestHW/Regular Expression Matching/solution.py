class Solution:
    # 應輸入s、p，輸出bool
    def isMatch(self, s: str, p: str) -> bool:
        # 不須懂
        def sol(s, p, bp):
            if s == "" and p == "":
                return True
            if p == "":
                return False
            if s == "":
                if len(p) > 1 and p[1] == "*":
                    return sol(s, p[2:], "*")
                return False
            if p[0] == ".":
                return sol(s[1:], p[1:], ".")
            elif p[0] == "*":
                if bp == ".":
                    return sol(s[1:], p, bp) or sol(s[1:], p[1:], "*")
                if bp != s[0]:
                    return sol(s, p[1:], "*")
                return sol(s[1:], p, bp) or sol(s[1:], p[1:], "*")
            else:
                if s[0] == p[0]:
                    if len(p) > 1 and p[1] == "*":
                        return sol(s[1:], p[1:], p[0]) or sol(s, p[1:], p[0])
                    return sol(s[1:], p[1:], p[0])
                return sol(s, p[1:], p[0])

        return sol(s, p, "")
