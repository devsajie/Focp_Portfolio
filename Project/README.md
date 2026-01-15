# Portfolio: Python Problem Solving

This repository features two Python implementations designed to solve practical problems using structured logic and user interaction.

---

## Task 1: Beckett Pizza Plaza Offer (4-for-3)

### Overview
This utility calculates the optimal price for a "4-for-3" pizza promotion. It ensures the customer receives the cheapest pizza for free, maximizing the value of the deal.

### Operational Logic
1.  **Data Collection**: Prompts the user for the price of four distinct pizzas.
2.  **Validation**: Enforces positive numeric input to ensure calculation accuracy.
3.  **Optimization**: Identifies the lowest-priced item.
4.  **Calculation**: Computes the final payable amount by subtracting the cheapest item from the subtotal.
5.  **Reporting**: Displays the discounted total and the effective percentage saved.

### Usage Example
*Inputs:*
- Pizza A: £12.00
- Pizza B: £15.00
- Pizza C: £10.00
- Pizza D: £13.00

*Result:*
The system identifies Pizza C (£10.00) as the free item.
**Final Cost:** £40.00 (Original: £50.00)
**Savings:** 20%

### Key Features
- **Robust Input Handling**: Rejects non-numeric and negative values.
- **Currency Formatting**: Outputs clearly formatted monetary values.

---

##  Task 2: Password Verification System

### Overview
A security simulation that authenticates a user by verifying random characters from their password, adding a layer of protection against simple observation.

### Operational Logic
1.  **Setup**: User defines a password.
2.  **Constraint Check**: Validates that the password meets the minimum length requirement (9+ characters).
3.  **Challenge-Response**: The system randomly selects three distinct index positions.
4.  **Verification**: The user must correctly identify the character at each requested position.
5.  **Access Control**: Access is strictly granted only if all three checks are successful; otherwise, the process terminates immediately.

### Usage Example
*Setup:*
- Password: `MySecurePassword!`

*Challenge:*
- "Enter character at position 1" -> User types `M`
- "Enter character at position 3" -> User types `S`
- "Enter character at position 10" -> User types `d`

*Result:*
If all match, **Security Check Passed**.

### Key Features
- **Length Enforcement**: Mandates strong, long passwords.
- **Randomized Challenges**: Ensures dynamic and unpredictable verification steps.
- **Immediate Failure**: Enhances security by stopping at the first incorrect entry.

---

## Execution Instructions

Run the scripts directly from the terminal:

**Task 1 (Pizza Calculator):**
```bash
python Task1.py
```

**Task 2 (Security Check):**
```bash
python Task2.py
```
