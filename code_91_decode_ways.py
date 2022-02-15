class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        if n == 1:
            return 0 if s == '0' else 1

        previous = 1
        previous_previous = 0

        for i in range(n-1,-1,-1):
            ni = int(s[i])
            current = 0 if int(s[i]) == 0 else previous
            if i < n-1 and (ni == 1 or (ni == 2 and int(s[i+1]) < 7)):
                current += previous_previous
            previous_previous = previous
            previous = current
        
        return previous