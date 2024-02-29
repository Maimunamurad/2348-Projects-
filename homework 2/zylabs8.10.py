# MaimunaMurad
# 2065973
def is_palindrome(input_str):
    # Remove spaces from the input string
    input_str = input_str.replace(" ", "")

    # Check if the string is equal to its reverse
    return input_str == input_str[::-1]


if __name__ == '__main__':
    input_word = input()

    if is_palindrome(input_word.lower()):  # Convert to lowercase for case-insensitive comparison
        print(f"{input_word} is a palindrome")
    else:
        print(f"{input_word} is not a palindrome")
