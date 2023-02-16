# Task 1
def encrypt(input_text,shift_number, shift_direction):
    input_encrypted = ""
    input_length = len(input_text)  # length of input
    reversed_input = input_text[input_length::-1]  # input is reversed
    split_reversed = [*reversed_input]  # reversed input is split into a list of characters

    for letter in split_reversed:  # for each letter in reversed input
        if( letter == " " or letter =="!"):  # if the letter is ever a space ot !, the input is invalid
            print("Input is invalid")

        if(shift_direction == -1):  # shift left
            ascii_value = (ord(letter) - shift_number) # ascii(letter)-shift# = shifted ascii value
            difference = 34 - ascii_value
            if(difference > 0):  # if the shift results in an ascii value less than 34
                ascii_value = 127 - difference  # subtract 127 by difference
            ascii_character = chr(ascii_value)  # save ascii value

        if(shift_direction == +1):
            ascii_value = ord(letter) + shift_number
            value = ascii_value + shift_number
            # print(value)
            difference = ascii_value -126
            if(difference > 0):
                ascii_value = difference + 33
            ascii_character = chr(ascii_value)

        input_encrypted = input_encrypted + ascii_character
    return input_encrypted

# Task 2
def decrypt(input_text,shift_number, shift_direction):
    input_decrypted=""
    input_length = len(input_text)  # length of input
    reversed_input = input_text[input_length::-1]  # input is reversed
    split_reversed = [*reversed_input]  # input is split into a list of characters
    # print(split_reversed)
    for letter in split_reversed:
        if(letter == " " or letter =="!"):
            print("Input is invalid")

        if(shift_direction == -1):
            ascii_value = ord(letter) + shift_number
            value = ascii_value + shift_number
            # print(value)
            difference = ascii_value - 126
            if (difference > 0):
                ascii_value = difference + 33
            ascii_character = chr(ascii_value)

        if(shift_direction == +1):
            ascii_value = (ord(letter) - shift_number)
            # print(ascii_value)
            difference = 34 - ascii_value
            if (difference > 0):
                ascii_value = 127 - difference
            ascii_character = chr(ascii_value)


        input_decrypted = input_decrypted + ascii_character
    return input_decrypted

# def main():
#
#     value = decrypt('~}|',1,+1)
#     print(value)
#
#
# main()