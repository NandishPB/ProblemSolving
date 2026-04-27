# Reverse Right Triangle Pattern (Stars)

## Problem

Print a reverse right triangle pattern of `*` for a given number `n`.

---

## Example

If `n = 5`

```
* * * * *
* * * *
* * *
* *
*
```

---

## Understanding in Simple Words

Think of this like removing blocks step by step:

* First row → full (5 stars)
* Next row → remove one star
* Keep removing one star each row

So the pattern **decreases line by line**.

---

## What’s Happening?

* Total rows = `n`
* Row 1 → 5 stars
* Row 2 → 4 stars
* Row 3 → 3 stars
* and so on...

---

## Logic

* Outer loop → controls rows
* Inner loop → controls number of stars

Here:

```
stars = n - i
```

---

## ⚙️ Code

```python
class ReverseRightTriangle:
    def pattern(self, n):
        for i in range(n):              # rows
            for j in range(n - i):      # decreasing stars
                print("*", end=" ")
            print()                     # next line

sol = ReverseRightTriangle()
sol.pattern(5)
```

---

##  Key Idea

If stars are decreasing like:

```
5, 4, 3, 2, 1
```

👉 Use:

```
n - i
```

---

## Note

If you try something like:
*(Reverse Iteration / Decreasing order)*

```python
for j in range(n, i):
```

👉 It will **not run at all**

---

### Why?

```
range(start, end) works only when start < end
```

---

### In this case:

```
range(5, 0), range(5, 1), ...
```

👉 start is always greater than end → so loop is empty

---

### ✅ Fix

* Add step `-1` for reverse iteration:

```python
range(n, i, -1)
```

* OR use:

```
n - i
```

👉 This avoids the empty loop problem

---

## What to Notice

* Stars decrease with each row
* `n - i` controls the reduction
* Nested loops are still the base idea
* `end=" "` keeps output on same line
