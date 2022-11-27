def solution(m, musicinfos):
    musics = []
    for i in musicinfos:
        start, end, name, info = map(str, i.split(","))
        info = replace_info(info)
        start_hour, start_minute = map(int, start.split(":"))
        end_hour, end_minute = map(int, end.split(":"))
        time = (end_hour - start_hour) * 60 + (end_minute - start_minute)
        real_info = info * (time // len(info)) + info[:(time % len(info))]
        musics.append((name, real_info))
    answer = []
    target = replace_info(m)
    for name, real_info in musics:
        if target in real_info:
            answer.append((name, real_info))
    answer.sort(key=lambda x: (-len(x[1]), name, musics.index((name, real_info))))
    if answer:
        return answer.pop(0)[0]
    return "(None)"


def replace_info(string: str):
    for old, new in [("C#", "c"), ("D#", "d"), ("F#", "f"), ("G#", "g"), ("A#", "a")]:
        string = string.replace(old, new)
    return string

