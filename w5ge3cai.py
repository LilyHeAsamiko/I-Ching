start = [13311,19968,63744,131072,173824,177984,178208,194995]
end = [19893, 40917, 64045, 173782, 177972, 178205,183969, 194998]

def get_stroke(c):
    # 如果返回 0, 则也是在unicode中不存在kTotalStrokes字段
    strokes = []
    with open(strokes_path, 'r') as fr:
        for line in fr:
            strokes.append(int(line.strip()))

    unicode_ = ord(c)

    if 13312 <= unicode_ <= 64045:
        return strokes[unicode_-13312]
    elif 131072 <= unicode_ <= 194998:
        return strokes[unicode_-80338]
    else:
        print("c should be a CJK char, or not have stroke in unihan data.")
        # can also return 0
        
strokes_path = https://github.com/helmz/Corpus/blob/master/zh_dict/strokes.txt
