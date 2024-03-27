# Maimuna Murad
# 2065973
# Lab 11.22 Word frequencies

words = input()

Word_List = words.split()

for i in range(len(Word_List)):

    print(Word_List[i], Word_List.count(Word_List[i]))