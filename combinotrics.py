import itertools

elements = ['a', 'b', 'c']

# All permutations of the list:

permutations = list(itertools.permutations(elements))

print("Permutations of ['a', 'b', 'c']:", permutations)

# All combinations of 2 elements:

combinations = list(itertools.combinations(elements, 2))

print("Combinations of 2 from ['a', 'b', 'c']:", combinations)

"""
### 📝 **Summary: Permutations vs Combinations (Toy Analogy)**

* You have 3 toys: `'a'` (🚗), `'b'` (⚽), `'c'` (🧊)

---

### 🔄 **Permutations** = All **possible orders** of the toys

> 👉 Rearranging them every way

Example:

```python
itertools.permutations(elements)
```

Gives:

```
('a', 'b', 'c'), ('a', 'c', 'b'), ...
```

✅ **Order matters**

---

### 🤝 **Combinations** = All **unique groups** (no repeats)

> 👉 Just picking toys, **order doesn't matter**

Example:

```python
itertools.combinations(elements, 2)
```

Gives:

```
('a', 'b'), ('a', 'c'), ...
```

❌ **Order doesn’t matter**

---

### 🧠 TL;DR:

| Action           | Concept     | Example               | Order matters? |
| ---------------- | ----------- | --------------------- | -------------- |
| Rearranging toys | Permutation | (a, b, c) → (c, a, b) | ✅ Yes          |
| Picking toys     | Combination | (a, b), (b, c)        | ❌ No           |



Explanation: Permutations and combinations illustrate counting principles underpinning many algorithmic problems, where understanding the possible configurations is crucial.
"""