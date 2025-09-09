def rem(l, word):
    if word in l:
        l.remove(word)
    return l

l = ["Roshan", "Shubham", "John", "Lucky", "an"]

print(rem(l, "Lucky"))
