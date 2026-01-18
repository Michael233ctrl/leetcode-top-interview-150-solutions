# **242. Valid Anagram**

**Category:** Hash Map / String / Counting

---

### 🔍 **Pattern & Intuition**

**Core Insight:**
Two strings are **anagrams** if they contain the **same characters with the same frequencies**, regardless of order.

This is **not** a positional problem — it’s a **frequency matching** problem.

Key observations:

* If lengths differ → impossible
* Every character in `s` must appear the **same number of times** in `t`
* Order does not matter

👉 This naturally leads to **character counting using a hash map**.

**Pattern recognized:** Frequency counting with hash tables.

---

### ✅ **Optimized Solution (O(n))**

```python
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
```

**Why this is optimal:**

* Uses a **single hash map**
* Avoids building two dictionaries
* Early exits on mismatch

---

### ⏱️ **Time & Space Complexity**

| **Complexity** | **Analysis**                                           |
| -------------- | ------------------------------------------------------ |
| **Time**       | **O(n)** — single pass over both strings               |
| **Space**      | **O(1)** — max 26 lowercase letters (English alphabet) |

---

This still runs in **O(n)** time and passes all cases.

---

### 🧪 **Critical Edge Cases**

| **Test Case**                  | **Expected** | **Why It Matters**                |
| ------------------------------ | ------------ | --------------------------------- |
| `s = "anagram", t = "nagaram"` | `True`       | Same letters, same frequencies.   |
| `s = "rat", t = "car"`         | `False`      | Different character sets.         |
| `s = "", t = ""`               | `True`       | Empty strings are valid anagrams. |
| `s = "a", t = "a"`             | `True`       | Single character match.           |
| `s = "a", t = "aa"`            | `False`      | Frequency mismatch.               |

---

### 💎 **Why This Pattern Works**

* **Hash maps track frequencies**, not positions
* Decrementing counts while scanning `t` simulates “using” characters
* Any negative count or missing key means mismatch
* No sorting needed → faster and cleaner

> ✨ **Pro Tip:**
> When a problem asks *“same characters, different order”*, always think **frequency map first**, sorting second.
