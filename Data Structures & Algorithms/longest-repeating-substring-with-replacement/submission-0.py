class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_length = 0

        for start in range(n):
            freq = {}
            for end in range(start, n):
                freq[s[end]] = freq.get(s[end], 0) + 1
                window_len = end - start + 1
                max_freq = max(freq.values())
                if window_len - max_freq <= k:
                    max_length = max(max_length, window_len)

        return max_length      