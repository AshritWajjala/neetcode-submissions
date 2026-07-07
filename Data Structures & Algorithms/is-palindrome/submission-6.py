class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time --> O(N)
        # Space --> O(1)
        l = 0
        r = len(s) - 1

        while l < r:
            # To ignore non - alpha numeric characters
            while l < r and not self.alpha_numeric(s[l]):
                l += 1
            while l < r and not self.alpha_numeric(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
    # Used this approach to not use builtin method
    def alpha_numeric(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))