# Analytical Thinking and Boelan Logic

# Movie Theater  Entery checker
---
## 1. Identify the components

###  1.1 Inputs
 - Age (13 or 13>)
 - Accompanied by an adult (True/False)
 - Valid ticket (True/False)

 ### 1.2 Process
 
 1. Check if the user is older than 13.
 2. If not, check weahter the user is accompanied by an adult. 
 3. Check if the user has a valid ticket.
 4. If `(Age >= 13 OR AccompaniedByAdult)` AND `ValidTicket` is true, allow entry.
 5. Otherwise, deny entry.

 ### 1.3 Output

 - Allowed to Enter
 - Entry Denied
---
 # 2. Design the Algorithm
```text
Start
 |
input Age, Adult, Ticket
 |
(Age >= 13 OR Adult?)
 |
 No -------> Deny Entry
 |
Yes
 |
Valid ticket?
 |
 No -------> Deny Entry
 |
Yes
 |
Allowed Entry
 |
End
```
---

### 2.2 Truth Table

| Age >= 13 | Adult | Ticket | Entry |
| --------- | ----- | ------ | ----- |
| False | False | False | False |
| False | False | True | False |
| False | True | False | False |
| False | True | True | True |
| True | False |False |False |
| True | False | True | True |
| True | True | False | False |
| True | True | True | True |

### 2.3 Step-by-step  Algorithm

1. Start
2. Input age
3. Input accompanied by adult
4. Input valid ticket
5. Check if age >= 13 OR accompanied by an adult
6. If false, deny entry
7. If true, check tikcet validity
8. If ticket is valid, allow entry
9. Otherwise deny entry
10. End

### 2.4 Pseudocode

```text
BEGIN

Input age
Input accompaniedByadult
Input validTicket

If (age >= 13 OR accompaniedByadult = TRUE) AND validTicket = TRUE THEN
    PRINT "Allowed Entry"
ELSE
    PRINT "Entry Denied"
ENDIF

END
```

---

# Evaluate Expression

### Test Case 1

| Input | Value |
| ----- | ----- |
| Age | 15 |
| Adult | False |
| Ticket | True |

Result: **Allowed to Enter**

### Test Case 2

| Input | Value |
| ----- | ----- |
| Age | 10 |
| Adult | True |
| Ticket | True |

Result: **Allowed to Enter**

### Test Case 3

| Input | Value |
| ----- | ----- |
| Age | 10 |
| Adult | False |
| Ticket | True |

Result: **Entry Denied**

### Test Case 4

| Input | Value |
| ----- | ----- |
| Age | 16 |
| Adult | False |
| Ticket | False |

Result: **Entry Denied**