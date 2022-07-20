class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = {n} # s equals to set n
        while n != 1: 
            tmp = sum([int(c) ** 2 for c in str(n)])
            if tmp in s: # if this number has been saved in s, then there's a loop
                return False
            s.add(tmp)
            n = tmp
        return True
if __name__ == "__main__":
    print(Solution().isHappy(19))
    print(Solution().isHappy(2))
