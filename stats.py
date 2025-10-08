import sys, pathlib
def stats(p):
    s = pathlib.Path(p).read_text(encoding='utf-8')
    return len(s), len(s.split()), s.count('\n')+1
for p in sys.argv[1:]:
    c,w,l = stats(p); print(f"{p}: chars={c} words={w} lines={l}")
