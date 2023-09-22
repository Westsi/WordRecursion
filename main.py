import requests

def writefile(wrd):
    f = open(f"data/{wrd}_recurse{reclim}.txt", 'w')
    for w in words:
        f.write(w+"\n")
    for w in lowest_lvl_words:
        f.write(f"LL: {w}\n")
    f.close()

reclim = 5
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-"
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
    try:
        j = r.json()
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
        try:
            print(f"ERROR: {e}")
            print(f"BROKEN WORD: {word}")
        except:
            pass
    except KeyboardInterrupt:
        writefile(oword)
        exit()
    except:
        pass

oword=input("Enter word: ")
recurse(oword, 1)
print(set(words))
print(set(lowest_lvl_words))
writefile(oword)
