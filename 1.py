#0

# print(2**38)

#1


new_Alphabet = {

    "A":"c",
    "B":"d",
    "C":"e",
    "D":"f",
    "E":"g",
    "F":"h",
    "G":"i",
    "H":"j",
    "I":"k",
    "J":"l",
    "K":"m",
    "L":"n",
    "M":"o",
    "N":"p",
    "O":"q",
    "P":"r",
    "Q":"s",
    "R":"t",
    "S":"u",
    "T":"v",
    "U":"w",
    "V":"x",
    "W":"y",
    "X":"z",
    "Y":"a",
    "Z":"b"
}

string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

str = ""
for i in string:
    if i.upper() in new_Alphabet:
        # print(new_Alphabet[i.upper()])
        str += new_Alphabet[i.upper()]
    else:
        str += i

print(str)

a = "abcdefghijklmnopqrstuvwxyz"
b = "cdefghijklmnopqrstuvwxyzab"

x = string.maketrans(a,b)
print(x)
print(string.translate(x))
print("map".translate(x))

# data = page_content.find_all(class_='intro')