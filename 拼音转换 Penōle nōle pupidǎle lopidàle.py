dic = {"a": "da", "a1": "dā", "a2": "dá", "a3": "dǎ", "a4": "dà",
       "b": "ha", "b1": "hā", "b2": "há", "b3": "hǎ", "b4": "hà",
       "c": "la", "c1": "lā", "c2": "lá", "c3": "lǎ", "c4": "là",
       "ĉ": "na", "ĉ1": "nā", "ĉ2": "ná", "ĉ3": "nǎ", "ĉ4": "nà",
       "d": "pa", "d1": "pa", "d2": "pá", "d3": "pǎ", "d4": "pà",
       "e": "sa", "e1": "sā", "e2": "sá", "e3": "sǎ", "e4": "sà",
       "f": "do", "f1": "dō", "f2": "dó", "f3": "dǒ", "f4": "dò",
       "g": "ho", "g1": "hō", "g2": "hó", "g3": "hǒ", "g4": "hò",
       "h": "lo", "h1": "lō", "h2": "ló", "h3": "lǒ", "h4": "lò",
       "i": "no", "i1": "nō", "i2": "nó", "i3": "nǒ", "i4": "nò",
       "j": "po", "j1": "pō", "j2": "pó", "j3": "pǒ", "j4": "pò",
       "k": "so", "k1": "sō", "k2": "só", "k3": "sǒ", "k4": "sò",
       "l": "de", "l1": "dē", "l2": "dé", "l3": "dě", "l4": "dè",
       "m": "he", "m1": "hē", "m2": "hé", "m3": "hě", "m4": "hè",
       "n": "le", "n1": "lē", "n2": "lé", "n3": "lě", "n4": "lè",
       "o": "ne", "o1": "nē", "o2": "né", "o3": "ně", "o4": "nè",
       "p": "pe", "p1": "pē", "p2": "pé", "p3": "pě", "p4": "pè",
       "q": "se", "q1": "sē", "q2": "sé", "q3": "sě", "q4": "sè",
       "r": "di", "r1": "dī", "r2": "dí", "r3": "dǐ", "r4": "dì",
       "s": "hi", "s1": "hī", "s2": "hí", "s3": "hǐ", "s4": "hì",
       "ŝ": "li", "ŝ1": "lī", "ŝ2": "lí", "ŝ3": "lǐ", "ŝ4": "lì",
       "t": "ni", "t1": "nī", "t2": "ní", "t3": "nǐ", "t4": "nì",
       "u": "pi", "u1": "pī", "u2": "pí", "u3": "pǐ", "u4": "pì",
       "v": "si", "v1": "sī", "v2": "sí", "v3": "sǐ", "v4": "sì",
       "w": "du", "w1": "dū", "w2": "dú", "w3": "dǔ", "w4": "dù",
       "x": "hu", "x1": "hū", "x2": "hú", "x3": "hǔ", "x4": "hù",
       "y": "lu", "y1": "lū", "y2": "lú", "y3": "lǔ", "y4": "lù",
       "z": "nu", "z1": "nū", "z2": "nú", "z3": "nǔ", "z4": "nù",
       "ẑ": "pu", "ẑ1": "pū", "ẑ2": "pú", "ẑ3": "pǔ", "ẑ4": "pù",
       "ŋ": "su"}
lis = ["bo", "de", "de", "ge", "ji", "po", "te", "ke", "qi", "mo",
 "ne", "fo", "he", "xi", "le", "wu"]
while True:
    s = input("Hipī dipì penōle nōle：")
    s = s.replace("ng", "ŋ")
    s = s.replace("zhi", "ẑ")
    s = s.replace("chi", "ĉ")
    s = s.replace("shi", "ŝ")
    s = s.replace("zh", "ẑ")
    s = s.replace("ch", "ĉ")
    s = s.replace("sh", "ŝ")
    s = s.replace("ri", "r")
    s = s.replace("zi", "z")
    s = s.replace("ci", "c")
    s = s.replace("si", "s")
    s = s.replace("yi", "i")
    s = s.replace("yu", "v")
    s = s.replace("yv", "v")
    s = s.replace("ju", "jv")
    s = s.replace("qu", "qv")
    s = s.replace("xu", "xv")
    i = 0
    while i < len(s) - 1:
        if s[i: i+2] in lis and (s[i+2] == " " or s[i+2].isdigit()):
            s = s[:i+1] + s[i+2:]
        i += 1
    t = ""
    i = 0
    while i < len(s):
        if s[i: i+2] in dic:
            t += dic[s[i: i+2]]
            i += 2
        elif s[i] in dic:
            t += dic[s[i]]
            i += 1
        else:
            t += s[i]
            i += 1
    print(t)
