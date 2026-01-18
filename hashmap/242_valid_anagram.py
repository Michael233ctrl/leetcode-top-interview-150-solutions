"""
242. Valid Anagram

Given two strings s and t, return true if t is an of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}

    # Count characters in s
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Decrease counts using t
    for char in t:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False

    return True

if __name__ == '__main__':
    assert is_anagram(s="anagram", t="nagaram") == True
    assert is_anagram(s="rat", t="car") == False
