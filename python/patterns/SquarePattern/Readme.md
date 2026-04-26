# Square Pattern in Python

## Problem Statement

Print a square pattern of stars (*) of size `n`.

## Example Output (n = 5)

```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```
##  Real-Life Analogy

Think of this like arranging chairs in a classroom:

* Each **row** = one line
* Each **column** = number of chairs in that row
* Every row has the **same number of chairs**

So if there are 5 rows and 5 chairs per row → it's a square.

##  Step-by-Step Logic

1. We need **5 rows** → so we run a loop 5 times
2. Inside each row:

   * Print 5 stars
3. After printing one row:

   * Move to the next line

So:

* Outer loop → controls rows
* Inner loop → controls columns


## ⚙️ Code Explanation

```python
for i in range(n):          # runs 5 times → rows
    for j in range(n):      # runs 5 times → columns
        print("*", end=" ") # print star without new line
    print()                 # move to next line
```

### Important:

* `end=" "` → prevents newline after each star
* `print()` → moves to next row(by Default 1 print statement - 1 New Line )

---

## 💻 Final Code

```python
class Square:
    def pattern(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()

sol = Square()
sol.pattern(5)
```
## 🎯 Key Learning

* Nested loops = Core Idea Behind Patterns
* Outer loop → Controls Rows
* Inner loop → Controls Columns
* `end=" "` → Keeps printing on same line.
