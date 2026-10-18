text = input("Enter a string: ")
digits = "".join(ch for ch in text if ch.isdigit())
print(digits)