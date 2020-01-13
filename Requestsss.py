import requests

r=requests.get('https://xkcd.com/353/')
print(r)#<Response [200]>
print(dir(r))#all objects
print(help(r))#more elaborate

print(r.text)#text of website

s=requests.get('https://imgs.xkcd.com/comics/star_wars_voyager_1.png')
#print(s.content)

with open('comic.png','wb') as f:
    f.write(s.content)#getting image b as byte

print(s.status_code)#200 is ok ,300 redirects , 400 clients error ,500 servers error (site crashes)
print(s.ok)#True

print(s.headers)#headers

payload={'page':2,'count':25}
t=requests.get('https://httpbin.org/get',params=payload)
print(t.text)
print(t.url)

payload={'username':'satyam','password':'testing'}
u=requests.post('https://httpbin.org/post',data=payload)
print(u.text)

u_dict = u.json()
print(u_dict['form'])

v=requests.get('http://httpbin.org/basic-auth/satyam/testing',auth=('satyam','testing'),timeout=3)


print(v)#<Response [200]>
print(v.text)#{
 # "authenticated": true,
 # "user": "satyam"
#}


v=requests.get('https://httpbin.org/delay/6',timeout=3)# raise ReadTimeout(e, request=request)
print(v)












