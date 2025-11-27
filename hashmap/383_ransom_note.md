# 383. Ransom Note

**Category:** Hash Map

---

### 🔍 **Pattern & Intuition**
**Core Insight**:  
*Use a hash table to track **remaining required characters** in `ransomNote` while scanning `magazine`.*  
- **Why hash table?** Not just "presence check" → needs **frequency matching** (e.g., `ransomNote="aa"` requires *two* 'a's from `magazine`).
- **Key trick**: Decrement counts in the hash table as you "use" characters from `magazine`. If any count drops below zero → invalid.

**Pattern recognized:** Counting occurrences → common hash map usage.

---

### ✅ **Optimized Solution (O(n))**
```python
def can_construct(ransomNote: str, magazine: str) -> bool:
    # Build frequency counter for ransomNote (O(n))
    freq = {}
    for char in ransomNote:
        freq[char] = freq.get(char, 0) + 1
    
    # Check magazine against frequency counter (O(m))
    for char in magazine:
        if char in freq and freq[char] > 0:
            freq[char] -= 1
    
    # Verify all counts are 0 (O(1) since max 26 letters)
    return all(count == 0 for count in freq.values())
```

---

### ⏱️ **Time & Space Complexity**
| **Complexity** | **Analysis**                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Time**       | **O(n + m)**<br>(n = len(ransomNote), m = len(magazine))<br>→ One pass for each string. |
| **Space**      | **O(1)**<br>(Max 26 keys in hash table for English letters)                |

---

### 💡 *O(n²) solution*  

```python
def can_construct(ransomNote: str, magazine: str):
    ransomNote_dict = dict([[letter, ransomNote.count(letter)] for letter in ransomNote])

    for i in magazine:
        if i in ransomNote_dict:
            if ransomNote_dict[i]:
                ransomNote_dict[i] -= 1

    return False if any(ransomNote_dict[i] > 0 for i in ransomNote_dict) else True
```

`ransomNote.count()` is O(n²) → **fails on large inputs**.

---

### 🧪 **Critical Edge Cases**
| **Test Case**               | **Expected** | **Why It Matters**                                      |
|-----------------------------|--------------|---------------------------------------------------------|
| `ransomNote = "", magazine = "abc"` | `True`       | Empty ransom note is always valid.                      |
| `ransomNote = "a", magazine = ""`   | `False`      | Magazine must have *all* characters.                    |
| `ransomNote = "aa", magazine = "ab"` | `False`      | Magazine has only *one* 'a' (needs two).                |
| `ransomNote = "a", magazine = "a"`   | `True`       | Exact match.                                            |
| `ransomNote = "a", magazine = "aab"` | `True`       | Extra characters in magazine are ignored.               |

---

### 💎 **Why This Pattern Works**
- **Hash table = Frequency tracker**: Tracks *how many more* of each character are needed.
- **No extra loops**: Scans `magazine` once to "satisfy" requirements from `ransomNote`.
- **Space-efficient**: Only stores counts for characters *actually in `ransomNote`*.

> ✨ **Pro Tip**: In interviews, always clarify if the problem involves *frequency* (not just presence) before choosing a data structure. Hash tables are your go-to for frequency matching.