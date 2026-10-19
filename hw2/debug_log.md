# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
NameError: name 'count' is not defined. Did you mean: 'counts'?

### 2. What I thought it meant
I though I wrote the count formula incorecctly

### 3. What it actually meant
I typed count instead of counts so it couldn't find the variable

### 4. The fix
counts[a] = counts.get(a, 0) + 1

## Entry 2

### 1. Error message
TypeError: 'list' object is not callable

### 2. What I thought it meant
I wasn't sure why it's unable to call / just unable to run back

### 3. What it actually meant
I'm supposed to use .append() to add a title to the list

### 4. The fix
titles.append(artwork.get("title", "Unknown"))