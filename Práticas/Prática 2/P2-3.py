minor = 17
adult = 64
senior = 110

age = int(input("Age: "))
if age <= minor:
    print("\nYou are a minor")
elif age <= adult:
    print("\nYou are an adult")
elif age <= senior:
    print("\nYou are a senior")
else:
    print("\nYou are not from this world!")