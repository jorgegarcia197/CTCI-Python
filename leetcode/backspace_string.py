# O(n) T and O(n) space
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for ch in s:
            if ch == "#" and len(s_stack) > 0:
                s_stack.pop()
            else:
                if ch != "#":
                    s_stack.append(ch)
        for ch in t:
            if ch == "#" and len(t_stack) > 0:
                t_stack.pop()
            else:
                if ch != "#":
                    t_stack.append(ch)
        return s_stack == t_stack

    def backspaceCompare2(self, s: str, t: str) -> bool:
        p1 = len(s) - 1
        p2 = len(t) - 1
        while p1 >= 0 or p2 >= 0:
            if s[p1] == "#":
                back_count = 2
                while p1 >= 0 and back_count > 0:
                    p1 -= 1
                    back_count -= 1
                    if s[p1] == "#":
                        back_count += 2
            if t[p2] == "#":
                back_count = 2
                while p2 >= 0 and back_count > 0:
                    p2 -= 1
                    back_count -= 1
                    if t[p2] == "#":
                        back_count += 2
            if s[p1] != t[p2] or p1 < 0 or p2 < 0:
                return False
            p1 -= 1
            p2 -= 1
        return True


if __name__ == "__main__":
    s = "bxj##tw"
    t = "bxj###tw"
    print(Solution().backspaceCompare2(s, t))
