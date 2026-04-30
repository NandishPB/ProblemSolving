# Two Sum Problem

## Problem

Given an array of integers and a target value, return the **indices of the two numbers** such that they add up to the target.

You can assume:

* Each input has exactly one solution
* You cannot use the same element twice

---

## Example

```id="k9f3ms"
nums = [2, 7, 11, 15]
target = 9
```

### Output:

```id="m2x7qp"
[0, 1]
```

👉 Because:

```id="d8v1zt"
nums[0] + nums[1] = 2 + 7 = 9
```

---

## Understanding in Simple Words

Think of this like finding a pair of numbers:

👉 For every number, ask:

```id="v4n2qx"
"What number do I need to reach the target?"
```

Example:

* If current number = 2
* Target = 9

👉 Needed number = `7`

Now just check:
👉 “Have I already seen 7?”

---

## DSA Used in This Problem

### Data Structure: Hash Map (Dictionary)

A **hash map** is used to store values along with their indices.

👉 Why use it?

* It allows **fast lookup in O(1) time**
* Helps avoid checking every pair (which is slow)

### 🔧 How It Is Used

* Store each number as a **key**
* Store its index as the **value**

```id="hashmap_example"
hashmap[number] = index
```

👉 While iterating:

* Check if the required number already exists in the hashmap
* If yes → we found the pair
* If no → store current number for future checks

---

## 🔍 What’s Happening?

For each number:

```id="p6z3rw"
required = target - current_number
```

Then:

* If required number already exists → answer found
* Otherwise → store current number for future use

---

## 🔄 Logic

```id="q1n7kc"
Loop through array:
    Calculate required = target - current number
    
    If required exists:
        return indices
    
    Else:
        store current number with its index
```

---

## ⚙️ Code (Optimized Approach)

```python
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            required = target - nums[i]

            if required in hashmap:
                return [hashmap[required], i]

            hashmap[nums[i]] = i

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
```

---

## 💡 Key Idea

```id="c5v8zn"
Instead of checking every pair,
store values and check in one pass
```

👉 This reduces time complexity significantly

---

## ⚠️ Note

If you try checking all pairs:

```python
for i in range(n):
    for j in range(i+1, n):
```

👉 It works, but:

```id="u7x3pl"
Time Complexity = O(n²)
```

---

### ✅ Optimized Approach

Using hashmap:

```id="y5n8vd"
Time Complexity = O(n)
Space Complexity = O(n)
```

👉 Much faster for large inputs

---

## 🎯 What to Notice

* Use of hashmap for fast lookup
* `target - current` is the key idea
* Single loop instead of nested loops
* Stores value → index mapping
