def ledger _operations(a, b) :
total = a + b
difference = a - b
return total, difference
if
_name__ == "main_":
num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value: "))
total, diff = ledger_operations(num1, num2)
print(f"Total Combined Value : {total}")
print(f"Difference           : {diff}")



