import os
from time import sleep

import requests

# 国家代码列表
codes = """
ae
sg
es
my
be
lu
fr
dk
de
se
nl
fi
it
ch
gr
pt
at
no
ie
kr
jp
mt
pl
hu
lv
ro
si
cz
hr
sk
bg
ee
cy
lt
nz
gb
ca
li
au
is
us
mc
hk
br
ar
cl
ad
sm
bb
bn
il
bs
uy
mx
va
kn
sc
pe
vc
ag
cr
ua
mo
py
tt
mu
gd
lc
pa
sb
dm
co
rs
sv
gt
mk
ge
me
ws
hn
ki
tv
tw
mh
to
ru
al
ba
md
ni
ve
fm
pw
tr
qa
kw
za
tl
bz
mv
ec
sa
bh
jm
fj
gy
th
om
vu
xk
cn
by
kz
id
bo
nr
pg
sr
bw
ma
az
do
ls
am
sz
na
mn
ph
mw
ke
tz
cv
tn
gh
zm
gm
rw
cu
kg
in
ug
uz
st
zw
vn
bj
mz
ga
mg
sl
tj
dz
kh
sn
bf
gq
tg
ci
ao
ne
mr
bt
la
jo
ml
gn
eg
km
ht
tm
cf
dj
gw
lr
td
cg
cm
bi
lk
lb
mm
cd
np
ng
et
ly
ir
sd
ss
er
kp
bd
ps
ye
so
pk
iq
sy
af
""".split()

# 保存目录
SAVE_DIR = "."
os.makedirs(SAVE_DIR, exist_ok=True)

BASE_URL = "https://img.passportindex.org/countries/{}.png"

# ✅ 关键：伪装浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0)",
    "Referer": "https://www.passportindex.org/",
    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}

session = requests.Session()
session.headers.update(headers)

for code in codes:
    url = BASE_URL.format(code)
    file_path = os.path.join(SAVE_DIR, f"{code}.png")

    try:
        print(f"Downloading {code}...")
        resp = session.get(url, timeout=10)

        if resp.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(resp.content)
        else:
            print(f"❌ Failed: {code} ({resp.status_code})")

        sleep(0.3)

    except Exception as e:
        print(f"❌ Error: {code} - {e}")

print("✅ Done!")
