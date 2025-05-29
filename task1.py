with open("sample.txt","r",encoding="utf-8")as myfile:
    lines=myfile.readlines()

line_count=len(lines)
word_count=0
char_count=0

for line in lines:
    words=line.split()
    word_count+=len(words)
    char_count+=len(line)

print("Total number of lines=",line_count)
print("Total number of words=",word_count)
print("Total number of characters=",char_count)
