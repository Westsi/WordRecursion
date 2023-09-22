import requests
reclim = 5
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def makealpha(w):
    rw = ""
    for c in w:
        if c in alpha:
            rw = rw + c
    return rw

words = [] # words in definitions
lowest_lvl_words = []
def recurse(word, level):
    r = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
    j = r.json()
    try:
        for m in j[0]["meanings"]:
            for d in m["definitions"]:
                for tw in d["definition"].split(" "):
                    w = makealpha(tw)
                    if level >= reclim:
                        lowest_lvl_words.append(w)
                    else:
                        words.append(w)
                        recurse(w, level+1)
    except KeyError as e:
        print(e)
        print(word)

recurse("hello", 1)
print(words)