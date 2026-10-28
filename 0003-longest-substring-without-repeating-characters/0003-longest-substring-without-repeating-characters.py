class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]

            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right

            longest = max(longest, right - left + 1)

        return longest