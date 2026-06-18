password = input("Enter your password: ")

special_chars = "@#$%&!"

has_digits = False
has_uppercase = False
has_lowercase = False
has_alpha = False
has_special_chars = False

for i in password:

    if i.isdigit():
        has_digits = True

    if i.isupper():
        has_uppercase = True

    if i.islower():
        has_lowercase = True

    if i.isalpha():
        has_alpha = True

    if i in special_chars:
        has_special_chars = True

# Decide strength AFTER the loop

if (len(password) >= 12 and
    has_uppercase and
    has_lowercase and
    has_digits and
    has_special_chars):

    print("Strength : Strong")

elif len(password) >= 8 and has_digits and has_alpha:

    print("Strength : Medium")

else:

    print("Strength : Weak")

print("\nPassword Analysis")
print("Contains digits :", has_digits)
print("Contains uppercase :", has_uppercase)
print("Contains lowercase :", has_lowercase)
print("Contains special chars :", has_special_chars)
