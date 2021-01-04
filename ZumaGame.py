import functools
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        codes = {"R": 10000, "Y": 1000, "B": 100, "G": 10, "W": 1}
        def encode(char_count):
            result = 0
            for c in char_count:
                result += codes[c] * char_count[c]
            return result
        def decode(value):
            chars = "WGBYR"
            idx = 0
            result = {"W": 0, "G": 0, "B": 0, "Y": 0, "R": 0}