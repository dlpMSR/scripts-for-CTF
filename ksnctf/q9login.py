import re
import requests
import hashlib

url = 'http://ctfq.sweetduet.info:10080/~q9/flag.html'
md5 = lambda x: hashlib.md5(x.encode("ascii")).hexdigest()

# 認証トライ
try_digest_auth = requests.get(url)
t_header = try_digest_auth.headers['WWW-Authenticate']

# 認証パラメータ生成
nonce = re.search(r'(?<=nonce=").*?(?=")', t_header).group()
cnonce = "9691c249745d94fc"
nc = "00000001"
qop = "auth"
a1_md5 = "c627e19450db746b739f41b64097d449"
a2 = "GET:/~q9/flag.html"
resp = a1_md5+":"+nonce+":"+nc+":"+cnonce+":"+qop+":"+md5(a2)
print(resp)
resp = md5(resp)

authorization_header = 'Digest username="q9", realm="secret", nonce="%s", uri="/~q9/flag.html", algorithm=MD5, response="%s", qop=auth, nc=00000001, cnonce="9691c249745d94fc"' % (nonce, resp)
# 認証パラメータを含んだリクエストを送信
headers = {'Authorization':authorization_header}
response = requests.get(url, headers=headers)
print(response.text)
