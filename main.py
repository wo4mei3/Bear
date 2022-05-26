import sys
import copy
import MeCab

arg = sys.argv

if len(arg) < 2:
    print('例文が渡されていません。強制終了します。')
    sys.exit()
sentence = arg[1]

tagger = MeCab.Tagger()
bunkai = tagger.parse(sentence).split("\n")
new = []
kuma = ['くま', 'クマ', 'クマ', 'くま', '語尾', '', '', '']
for s in bunkai:
    tmp = s.split("\t")
    new.append(tmp)

rev = copy.deepcopy(new)
rev.reverse()
def contains(a,b):
    flag = True
    if len(a) < len(b):
        return False
    for i, c in enumerate(b):
        if a[i] != c:
            flag = False
    return flag

for i, l in enumerate(reversed(new)):
    if len(l) < 8:
        pass
    #elif l[4] == "助詞-終助詞" or contains(l[4],"名詞"):
    #    rev.insert(i,kuma)
    #    break   
    elif contains(l[4],"助詞") or contains(l[4],"名詞"):
        rev.insert(i,kuma)
        break

    elif contains(l[6],"終止形") or contains(l[6],"命令形"):
        rev.insert(i,kuma)
        break

result = ""
for l in reversed(rev):
    if len(l) < 8:
        pass
    else:
        result += l[0]

print(result)