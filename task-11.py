#takes two strings as input, and outputs the common characters/letters that they share
def common_letters(str1, str2):
    char_list = []
    for char in str1:
        if(str2.find(char) != -1):
            char_list.append(char)
    return "common letters: " + ", ".join(char_list)

print(common_letters("house", "computers"))
