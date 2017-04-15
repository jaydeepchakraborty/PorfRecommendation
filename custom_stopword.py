custom_stop_lst = ["al","et",
                   "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                   "s1","s2","s2\"","can","use","show","one","two","use","will","ear","php","pp","sm","ri","vq","wkh","edg","epoch","r1","qwip","ldcm","r1",
                   "m1","follow","number","output","m2","hold","size","case","problem","different","kc","time","example","step","work","also","given","figure",
                   "base","also","may","new","effort","work","table","time","warmbase","x1","xn","xi","tir","landsat"]


def isEnglish(s):
    try:
        s.encode().decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
