"""
383. Ransom Note
Given two strings `ransomNote` and `magazine`, return true
if `ransomNote` can be constructed by using the letters from `magazine` and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


def can_construct(ransomNote: str, magazine: str):
    ransom_dict = {}
    for char in ransomNote:
        ransom_dict[char] = ransom_dict.get(char, 0) + 1

    for char in magazine:
        if char in ransom_dict and ransom_dict[char] > 0:
            ransom_dict[char] -= 1

    return all(count == 0 for count in ransom_dict.values())


if __name__ == '__main__':
    assert can_construct("aabb", "aabbb") == True
    assert can_construct("a", "b") == False
    assert can_construct("aa", "ab") == False
