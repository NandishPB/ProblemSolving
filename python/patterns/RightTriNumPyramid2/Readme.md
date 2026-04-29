# Right Triangle Pattern (Increasing Numbers)

## Problem

Print a right triangle pattern where numbers increase from `1` up to the row number.

---

## Example

If `n = 5`

```id="h3k9wq"
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

## Understanding in Simple Words

Think of this like counting numbers in each row:

* First row → count till 1
* Second row → count till 2
* Third row → count till 3

Each row **starts from 1** and goes up to the row number.

---

## What’s Happening?

* Row 1 → `1`
* Row 2 → `1 2`
* Row 3 → `1 2 3`

So:

```id="8r4vyt"
start = 1
end = i
```

---

## 🔄 Logic

* Outer loop → controls rows
* Inner loop → prints numbers

Here:

```id="m5x8as"
for each row i:
    print numbers from 1 to i
```

---

## ⚙️ Code

```python id="w2n7cz"
class RightTriangleNumPyramid:
    def numPattern(self, n):
        for i in range(1, n + 1):        # rows start from 1
            for j in range(1, i + 1):    # numbers from 1 to i
                print(j, end=" ")
            print()                      # next line

sol = RightTriangleNumPyramid()
sol.numPattern(5)
```

---

## 💡 Key Idea

If pattern looks like:

```id="g7v2km"
1
1 2
1 2 3
```

👉 Then:

```id="9b1xrd"
print numbers from 1 → i
```

---

## ⚠️ Note

If you use:

```python id="p4z6nx"
for i in range(n + 1):
```

👉 First iteration:

```id="y8n3qs"
i = 0
```

Then:

```id="c1r7va"
range(1, i + 1) → range(1, 1) → empty
```

👉 So first row will be blank

---

### ✅ Fix

Start loop from 1:

```python id="t9k5lm"
range(1, n + 1)
```

👉 This avoids the empty row and keeps output clean

---

## 🎯 What to Notice

* Numbers always start from `1`
* End value depends on row (`i`)
* Inner loop controls the sequence
* Nested loops define the structure
