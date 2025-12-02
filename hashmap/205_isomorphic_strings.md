# **205. Isomorphic Strings**

**Category:** Hash Map

---

### 🔍 **Pattern & Intuition**

**Core Insight:**
Two strings are *isomorphic* if characters in `s` can be replaced to form `t` **with consistent, one-to-one character mapping**.

* Each character in `s` must always map to the *same* character in `t`
* No two different characters in `s` may map to the *same* character in `t`
* Order must remain preserved

👉 This is a **bijection check**, meaning we need to ensure both:

* `s → t` mapping is consistent
* `t → s` reverse mapping is also consistent

**Pattern recognized:** Use **two hash maps** to ensure one-to-one correspondence.

---

### ✅ **Optimized Solution (O(n))**

```python
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for cs, ct in zip(s, t):
        # Forward mapping must be consistent
        if cs in s_to_t and s_to_t[cs] != ct:
            return False
        
        # Reverse mapping must also be consistent
        if ct in t_to_s and t_to_s[ct] != cs:
            return False

        s_to_t[cs] = ct
        t_to_s[ct] = cs

    return True
```

---

### ⏱️ **Time & Space Complexity**

| **Complexity** | **Analysis**                                           |
| -------------- | ------------------------------------------------------ |
| **Time**       | **O(n)** — one pass through the strings                |
| **Space**      | **O(1)** — bounded by character set size (≤ 256 chars) |

---

### 💡 *Brute-Force or Incorrect Idea (Why It Fails)*

**Bad Idea:** Try to assign mappings without tracking both directions.
This fails because:

* You may allow multiple chars to map to the same target (violates injective rule).
* Without reverse mapping, `"ab"` and `"cc"` falsely appear valid.

**Correctness requires two-way validation.**

---

### 🧪 **Critical Edge Cases**

| **Test Case**              | **Expected** | **Why It Matters**                      |
| -------------------------- | ------------ | --------------------------------------- |
| `s = "egg", t = "add"`     | `True`       | Standard valid mapping.                 |
| `s = "foo", t = "bar"`     | `False`      | 'o' cannot map to both 'a' *and* 'r'.   |
| `s = "paper", t = "title"` | `True`       | Pattern matches; mapping is consistent. |
| `s = "a", t = "a"`         | `True`       | Character can map to itself.            |
| `s = "ab", t = "aa"`       | `False`      | Two chars cannot map to same char.      |

---

### 💎 **Why This Pattern Works**

* The problem requires **consistent** mapping → hash maps enforce that.
* The mapping must be **one-to-one** → reverse map prevents collisions.
* Using the pair of dictionaries ensures both **injectivity** and **surjectivity**.
* This is the standard pattern for isomorphic-like string problems (`word pattern`, `pattern matching`, etc.).

> ✨ **Pro Tip:** In bijection problems, always create **two hash maps** unless constraints explicitly allow one-directional mapping.

---
