class Solution:
    def isPalindrome(self, s: str) -> bool:
        # First converting input string to lower case while ignoring non-alpha numeric characters
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
            
        return new_str == new_str[::-1]