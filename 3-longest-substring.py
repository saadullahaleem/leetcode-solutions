from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        occurred = dict()
        window_left = window_right = 0
        max = 0

        for i, ch in enumerate(string):
            if ch not in occurred:
                window_right += 1
            else:
                while window_left <= occurred[ch]:
                    window_left += 1
                window_right = i + 1
            occurred[ch] = i
            max = window_right - window_left if (window_right - window_left) > max else max

        return max

