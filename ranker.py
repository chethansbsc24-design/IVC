def find_largest(a, b, c):
    return max(a, b, c)

if __name__ == "__main__":
    a = float(input("Enter data stream 1: "))
    b = float(input("Enter data stream 2: "))
    c = float(input("Enter data stream 3: "))
    print(f"Dominant Value: {find_largest(a, b, c)}")
