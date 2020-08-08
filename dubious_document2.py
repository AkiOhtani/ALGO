def cmpStr(S1, S2):
    for i in range(len(S2)):
        if S1[i] == S2[i] or S1[i] == '?':
            yield S2[i]
        else:
            break

Sp = input()
T = input()
res = []
for i in range(len(Sp)-len(T), -1, -1):
    if Sp[i] == '?' or Sp[i] == T[0]:
        substr = ''.join(list(cmpStr(Sp[i:i+len(T)], T)))

        if len(substr) == len(T):
            res.append(Sp[:i]+T+Sp[i+len(T):])
            res[-1] = res[-1].replace('?', 'a')
            break
if res:
    res.sort()
    print(res[0])
else:
    print("UNRESTORABLE")