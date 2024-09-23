def single_root_words(a, *other_words):
    same_words = []
    for i in other_words:
        if a.lower() in i.lower():
            same_words.append(i)
    return same_words

root = "Lol"
lol = "Lolkek"
kek = "kek"
keklol = "kekloL"
lolan = "lolan"
tir = "tir"

print(single_root_words(root, lol, kek, keklol, lolan, tir))