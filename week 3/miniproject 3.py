"""
RECORD CHECK  -  my version
===========================

Name  :Yuvesh Devason
Lane  :  AI 
Date  :11/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
def check(value, limit):
    difference = value - limit
    percent = (value/limit) * 100
    return difference, percent
def print_report(label, value, limit, difference, percent, status):
    print(f"  Label: {label}")
    print(f"  Value: {value}")
    print(f"  limit: {limit}")
    print(f"  Difference: {difference}")
    print(f"  Percentage: {percent:2f}%")
    print(f"  Status: {status}")


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Enter label: ")
value = float(input("Enter value: "))
limit = float(input("Enter limit: "))


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
difference, percent = check(value, limit)
status = status_of(percent)

difference = value - limit
percent = (value/limit) * 100
status = status_of(percent)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f" Value: {value:>10.2f}")
print(f" Limit: {limit:>10.2f}")
print(f" Difference: {difference:>10.2f}")
print(f" Percentage: {percent:>10.2f}%")
print(f" Status: {status:>10}")
print_report(label, value, limit, difference, percent, status)

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
