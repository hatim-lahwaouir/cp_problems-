class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1  = [0] * 26
        count_s2  = [0] * 26

        for c in s1:
            count_s1[ord('a') - ord(c)] += 1

        r = 0
        l = 0


        while r < len(s2):
            count_s2[ord('a') - ord(s2[r])] += 1
            if r - l + 1 == len(s1) and count_s1 == count_s2:
                return True

            if r - l + 1 == len(s1):
                count_s2[ord('a') - ord(s2[l])] -= 1
                l += 1
            r += 1
        return False


