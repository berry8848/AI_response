from unmo import Unmo
import morph

DEBUG = True

name = ',/wagahaiwa_nekodearu.txt'

with open(name, encoding='utf-8') as f:
    s = f.read()

s = s.replace('\n', '').replace('。', '。\n')

u = Unmo("tmp")


def learn(u, l):
    if DEBUG:
        print(l)
    u._dictionary.study(l, morph.analyze(l))


[learn(u, l) for l in s.split('\n')]

u.save()
