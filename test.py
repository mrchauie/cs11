def count_word(paragraph, word): 
    global count
    for i in paragraph.split(" "):
        if i == word:
            count += 1

count = 0
count_word("i love cs11", "love")
print(count)
