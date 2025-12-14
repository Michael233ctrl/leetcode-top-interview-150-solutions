# **290. Word Pattern**

**Category:** Hash Map / String

---

### 🔍 **Pattern & Intuition**

**Core Insight:**
This problem is a **bijection validation** between:

* characters in `pattern`
* words in the string `s`

To satisfy the pattern:

* Each letter must map to **exactly one unique word**
* Each word must map back to **exactly one unique letter**
* Order must be preserved

This is conceptually identical to **Isomorphic Strings**, except:

* one side is characters
* the other side is **words split by spaces**

**Pattern recognized:** Bidirectional mapping using **two hash maps**.

---

### **Optimized Solution (O(n))**

```python
def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    
    # Length mismatch → cannot form bijection
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for ch, word in zip(pattern, words):
        # Forward mapping must be consistent
        if ch in char_to_word and char_to_word[ch] != word:
            return False
        
        # Reverse mapping must be consistent
        if word in word_to_char and word_to_char[word] != ch:
            return False

        char_to_word[ch] = word
        word_to_char[word] = ch

    return True
```

---

### **Time & Space Complexity**

| **Complexity** | **Analysis**                                             |
| -------------- | -------------------------------------------------------- |
| **Time**       | **O(n)** — one pass through pattern and words            |
| **Space**      | **O(n)** — stores mappings for pattern letters and words |

---

### *Common Incorrect Approach (Why It Fails)*

**Mistake:**
Only mapping `pattern → words` without checking the reverse mapping.

**Why it fails:**
Example:

```
pattern = "ab"
s = "dog dog"
```

* Forward map looks valid (`a → dog`, `b → dog`)
* But two letters map to the same word → **violates bijection**

👉 Reverse mapping is **mandatory**.

---

### 🧪 **Critical Edge Cases**

| **Test Case**                              | **Expected** | **Why It Matters**                           |
| ------------------------------------------ | ------------ | -------------------------------------------- |
| `pattern = "abba", s = "dog cat cat dog"`  | `True`       | Perfect bijection in both directions.        |
| `pattern = "abba", s = "dog cat cat fish"` | `False`      | Last mapping breaks consistency.             |
| `pattern = "aaaa", s = "dog cat cat dog"`  | `False`      | One letter cannot map to multiple words.     |
| `pattern = "ab", s = "dog dog"`            | `False`      | Two letters mapping to same word is invalid. |
| `pattern = "a", s = "dog"`                 | `True`       | Single valid mapping.                        |

---

### 💎 **Why This Pattern Works**

* The problem requires a **full bijection**, not just matching counts or order.
* Two hash maps enforce:

  * **Injective mapping** (no collisions)
  * **Surjective mapping** (full coverage)
* Splitting `s` first simplifies the logic into a clean linear scan.

> ✨ **Pro Tip:**
> If a problem mentions *bijection*, *isomorphic*, or *one-to-one mapping*, immediately think **two hash maps**.

---