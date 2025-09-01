# String manipulation class Tasks

# 1. Reverse string

##text = "Hello"
##reversed_text = text[::-1]
##print(f"Reversed Text: {reversed_text}")


# 2. count vowels in text
##text = "Artificial Intelligence"
##vowels = "aeiouAEIOU"
##count = sum([1 for char in text if char in vowels])
##print(f"Number of vowels: {count}")


# 3. Palindrome
##text = "madam"
##if text == text[::-1]:
##    print(f"'{text}' is palindrome")
##else:
##    print(f"'{text}' is not palindrome")

# 4. Remove spaces from string
##text = "  Machine       Learning  "
##no_spaces = text.replace(" ", "")
##print(no_spaces)

# 5. Find frequency of Each Character
##text = "datascience"
##characters = {}
##for c in text:
##    characters[c] = characters.get(c,0) + 1
##print(characters)
