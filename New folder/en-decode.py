def encode(text,key):
    shift = key % 26
    right_left_shift = 26 - shift
    encoded_text = ""
    for i in text:
        if i.islower():
            if ord(i) + shift < 123  :
                encoded_text += chr(ord(i) + shift)
            else:
                encoded_text += chr(ord(i) - right_left_shift )
        if i.isupper():
            if ord(i) + shift < 91 :
                encoded_text += chr(ord(i) + shift)
            else:
                encoded_text += chr(ord(i) - right_left_shift)

    print("Encoded : ",encoded_text)
    return encoded_text

def decode(encoded_text,key):
    shift = key % 26
    right_left_shift = 26 - shift
    decoded_text = ""
    for i in encoded_text:
        if i.islower():
            if ord(i) - shift > 96  :
                decoded_text += chr(ord(i) - shift)
            else:
                decoded_text += chr(ord(i) + right_left_shift )
        if i.isupper():
            if ord(i) - shift > 64 :
                decoded_text += chr(ord(i) - shift)
            else:
                decoded_text += chr(ord(i) + right_left_shift)

    print("Decoded : ",decoded_text)

text = input()
key = int(input("K : "))
encoded_text = encode(text,key)
decode(encoded_text,key)





