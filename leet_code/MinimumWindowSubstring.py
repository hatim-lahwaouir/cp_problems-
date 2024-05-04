class Solution:
    def help(self, t, s):
        i  = 0
        for c in t:
            if t[c] <= s.get(c, 0):
                i += t[c]
        return i
    
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        s_count =  {}
        l = 0 
        r = 0
        ans = [0, 0]
        minLen = int(1e10)

        need = len(t)
        while r < len(s) and l <= r:
            s_count[s[r]] = s_count.get(s[r], 0) + 1
            have = self.help(t_count, s_count)
            
            print(have, need)
            if have == need:
                while have == need:
                    s_count[s[l]] = s_count.get(s[l], 0) - 1
                    l += 1
                    have = self.help(t_count, s_count)
                if r - (l - 1) + 1 < minLen:
                    minLen = r - (l - 1) + 1
                    ans[0] = r + 1
                    ans[1] = l - 1
            r += 1
        return s[ans[1]:ans[0]]
