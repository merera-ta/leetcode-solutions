class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)

            length = max(len1, len2)

            if length > max_len:
                max_len = length
                start = i - (length - 1) // 2

        return s[start:start + max_len]