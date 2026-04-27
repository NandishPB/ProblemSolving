# Right Triangle Pattern (Stars)

## Problem

Print a right triangle pattern of `*` for a given number `n`.

---

## Example

If `n = 5`

```id="k2p8s1"
*
* *
* * *
* * * *
* * * * *
```

---

##  Understanding in Simple Words

Think of this like building steps:

* First step → 1 block
* Second step → 2 blocks
* Third step → 3 blocks

Each row keeps **adding one more star** than the previous row.

---

## What’s Happening?

* Total rows = `n`
* Row 1 → 1 star
* Row 2 → 2 stars
* Row 3 → 3 stars
* and so on...

So stars are **increasing line by line**

---

## 🔄 Logic

* Outer loop → controls rows
* Inner loop → prints stars

But here:

* Number of stars = current row number

So:

```id="m9x2q7"
For each row i:
    Print (i + 1) stars
```

---

## ⚙️ Code

```python id="q7v3nz"
class RightTriangle:
    def pattern(self, n):
        for i in range(n):              # rows
            for j in range(i + 1):      # increasing stars
                print("*", end=" ")
            print()                     # next line

sol = RightTriangle()
sol.pattern(5)
```
---

## 💡 Key Idea

If stars are increasing like:

```id="t8b4y1"
1, 2, 3, 4, ...
```

👉 Use:

```id="c3r6w9"
range(i + 1)
```
Meaning :

```id="c3r6w9"
print (i + 1) times *.
```
---

## 🎯 What to Notice

* Stars increase with each row
* `i + 1` controls the growth
* Nested loops are still the base idea
* `end=" "` keeps output on same line
