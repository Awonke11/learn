import random as r

list_of_alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                   "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Function that will remove spaces from input string
def remove_spaces_from_string(string : str) -> str:
    list_of_strings = string.split(" ")
    return "".join(list_of_strings).upper()

# Returns len of string
def get_string_length(string : str) -> int:
    return len(string)

# Generate secrete key
def generate_secret_key(length : int) -> str:
    list_of_letters = []
    for i in range(0, length):
        random_number : int = r.randint(0, 25)
        char : str = list_of_alphabets[random_number]
        list_of_letters.append(char)

    return "".join(list_of_letters)

def get_numbers_from_string(string: str):
    string_len = len(string)
    list_of_numbers = [] # Stores all the numbers

    for i in range(0, string_len):
        char = string[i]
        for j in range(0, len(list_of_alphabets)):
            if char == list_of_alphabets[j]:
                list_of_numbers.append(j)

    return list_of_numbers

def encrypt(message: str, secrete_key: str) -> str:
    message_list = get_numbers_from_string(message)
    secrete_key_list = get_numbers_from_string(secrete_key)

    list_of_addition = []
    for msg, secret in zip(message_list, secrete_key_list):
        sum : int = msg + secret
        if (sum >= 26):
            new_value = sum - 26
            list_of_addition.append(new_value)
        else:
            list_of_addition.append(sum)

    list_of_char = []
    for num in list_of_addition:
        get_char = list_of_alphabets[num]
        list_of_char.append(get_char)

    return "".join(list_of_char)

def encrypt_main(message):
    # Remove spaces from message
    removed_spaces_message = remove_spaces_from_string(message)

    # Get message length
    message_length = get_string_length(removed_spaces_message)

    # Generate secret key
    secrete_key_string : str = generate_secret_key(message_length)

    # Implementation
    encrypted_message : str = encrypt(removed_spaces_message, secrete_key_string)

    # Output
    return encrypted_message

if __name__ == "__main__":
    encrypt_main()