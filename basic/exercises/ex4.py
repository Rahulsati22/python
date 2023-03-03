word = input("Enter the word you want to use in your secret language\n")

# writing encode function start


def reverse(word):
    return word[::-1]


def append(word):
    return "abc" + word[1:len(word)] + word[0] + "mne"
# writing encode function start

# writing decode function start


def reverseDecode(word):
    return word[::-1]


def appendDecode(word):
    helper1 = word[3:len(word)]
    helper2 = helper1[0:len(helper1)-3]
    return helper2[len(helper2)-1] + helper2[0:len(helper2)-1]
# writing decode function end


encode = ""
decode = ""
if (len(word) < 3):
    encode = reverse(word)

else:
    encode = append(word)


if (len(encode) < 3):
    decode = reverseDecode(encode)
else:
    decode = appendDecode(encode)


print(f"The encoded word is {encode} and the decoded word is {decode}")


# writing encode word
