# Right Triangle Pattern (Numbers – Same Number per Row)

## Problem

Print a right triangle pattern where each row contains the **same number**, increasing row by row.

---

## Example

If `n = 5`

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

## Understanding in Simple Words

Think of this like writing row numbers:

* First row → write **1 one time**
* Second row → write **2 two times**
* Third row → write **3 three times**

So:

* Number = row number
* Times = how many times it repeats

---

## What’s Happening?

* Row 1 → print `1` → 1 time
* Row 2 → print `2` → 2 times
* Row 3 → print `3` → 3 times

So both:

```
value = i
count = i
```

---

## Logic

* Outer loop → controls rows
* Inner loop → controls how many times to print

Here:

```
print number i → i times
```

---

## ⚙️ Code

```python
class RytTriNum:
    def numPattern(self, n):
        for i in range(1, n + 1):      # rows start from 1
            for j in range(i):         # print i times
                print(i, end=" ")
            print()                   # next line

sol = RytTriNum()
sol.numPattern(5)
```

---

## Key Idea

If pattern looks like:

```
1
2 2
3 3 3
```

👉 Then:

```
print i → i times
```

---

## ⚠️ Note

If your loop starts from 0:

```python
for i in range(n):
```

Then:

* First row → i = 0 → prints 0 (not useful)

👉 So you must adjust:

```
value = i + 1
count = i + 1
```

OR simply start loop from 1:

```python
range(1, n + 1)
```

👉 This keeps things clean and avoids confusion

---

## 🎯 What to Notice

* Value printed = row number
* Count of numbers = row number
* Both depend on `i`
* Nested loops still control structure
