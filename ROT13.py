from string import ascii_letters


def rot13(message):
    result = ""
    for character in message:
        is_upper = character.isupper()
        if character in ascii_letters:
            character_position = ascii_letters.find(character)
            character_rot13 = ascii_letters[character_position - 13]
            result += character_rot13.upper() if is_upper else character_rot13.lower()
        else:
            result += character
    return result


def rot13_2(message):
    from codecs import encode

    return encode(message, "rot13")


print(rot13("EBG13 rknzcyr."))
print(rot13("This is my first ROT13 excercise!"))
print(
    rot13(
        "How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."
    )
)
print(rot13("123"))
print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"))
print(rot13("@[`{"))
