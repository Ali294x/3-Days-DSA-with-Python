

# 🚀 3-Day Python DSA Revision Bootcamp


![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![DSA](https://img.shields.io/badge/Data_Structures-Algorithms-FF6F00?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active_Revision-success?style=for-the-badge)

Welcome to the **3-Day Python DSA Revision Guide**! This repository is designed to help you rapidly review core algorithmic patterns, optimize your problem-solving intuition, and master high-yield techniques over a condensed 72-hour period.

---

## 🗓️ Day 1: Array Mastery & Advanced Manipulation

Focus on linear data structures, sliding windows, and advanced array transformations. Arrays are foundational, and mastering their built-in operations will speed up your execution.

### 🧠 Core Concepts & Techniques
- **Prefix Sums:** Quickly calculating range sums. Use Python's built-in `itertools.accumulate` for optimal and elegant implementations.
- **Difference Array Technique:** Handling multiple range updates efficiently in $O(1)$ time per query before computing the final state.
- **Frequency Maps:** Utilizing `collections.Counter` to quickly find element frequencies and solve subarray matching problems.
- **Searching in Modified Spaces:** Binary search applications like the **Shifted Array Search** (searching efficiently in a rotated sorted array).

### 💻 Python Quick Snippet: Prefix Sum
```python
from itertools import accumulate

nums = [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
prefix_sums = list(accumulate(nums)) 
```

### 🎯 Practice Checklist
- [ ] Implement Shifted Array Search (Binary Search variation).
- [ ] Solve Subarray Sum Equals K (Prefix Sum + Hash Map).
- [ ] Apply the Difference Array technique to a range-addition problem.

---

## 🗓️ Day 2: Bit Manipulation & Low-Level Optimization

Shift focus to bitwise operations, an essential tool for $O(1)$ space optimizations and solving complex filtering problems efficiently.

### 🧠 Core Concepts & Techniques
- **XOR Magic:** Understanding how `a ^ a = 0` and `a ^ 0 = a` can be leveraged to find missing or unique elements.
- **Bitmasking:** Representing sets and states using integers.
- **Isolating Bits:** Extracting the rightmost set bit using `x & ~(x - 1)` or `x & -x`.

### 💻 Python Quick Snippet: Single Number III (Two Unique Elements)
```python
def singleNumber(nums):
    xor_all = 0
    for num in nums: xor_all ^= num
    
    # Find the rightmost set bit
    diff_bit = xor_all & -xor_all
    
    a = b = 0
    for num in nums:
        if num & diff_bit:
            a ^= num
        else:
            b ^= num
    return [a, b]
```

### 🎯 Practice Checklist
- [ ] Single Number I (Find the one element that appears once).
- [ ] Single Number II (Find the element appearing once when others appear thrice).
- [ ] Single Number III (Find two elements appearing once).

---

## 🗓️ Day 3: Advanced Patterns - Game Theory & Dynamic Programming

Tackle competitive programming patterns involving optimal play, decision-making, and state caching. 

### 🧠 Core Concepts & Techniques
- **Game Theory Algorithms:** Building intuition for "optimal play" scenarios. Analyze states to determine if a winning strategy exists.
- **Minimax Pattern:** Simulating worst-case optimal moves for opponents using recursion and memoization.
- **Prefix Sums in Games:** Often, game theory on arrays requires fast access to remaining sums, combining Day 1 skills with DP.

### 💻 Python Quick Snippet: Memoization Blueprint for Games
```python
from functools import cache

@cache
def dp(index, current_state):
    # Base cases (end of game)
    if index >= len(stones): return 0
    
    # Calculate optimal move by simulating choices
    # return max(take_one, take_two...)
    pass
```

### 🎯 Practice Checklist
- [ ] Analyze the "Sum Game" pattern (Greedy / Math strategies).
- [ ] Solve "Stone Game VIII" or similar array-based game theory problems (DP + Prefix Sums).
- [ ] Review Line-by-Line executions of your DP solutions to solidify intuition.

---

## 🛠️ Essential Python Libraries for DSA
Make sure you are comfortable with these built-in modules:
- `collections` (`Counter`, `deque`, `defaultdict`)
- `itertools` (`accumulate`, `permutations`, `combinations`)
- `functools` (`cache`, `lru_cache`)
- `heapq` (Min/Max heaps via `heappush`, `heappop`)
- `math` and `bisect` (Binary search utilities)
