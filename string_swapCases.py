# 1st way
def swap_string_cases(text):
    new_text = ""
    for t in text:
        if t.islower():
            new_text += t.upper()
        else:
            new_text += t.lower()
    return new_text

print(swap_string_cases("UPPERCASE lowercase 45"))
print(swap_string_cases("Special @Characters!"))



# 2nd way
# short way to do string swapCases using a string method
def swap_string_cases(text):
    return text.swapcase()

print(swap_string_cases("UPPERCASE lowercase 45"))
print(swap_string_cases("Special @Characters!"))
