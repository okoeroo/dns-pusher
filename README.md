Start in virtual environment.
```
python3 -m venv .venv
source .venv/bin/activate 
python3 -m pip install --upgrade dnspython
```


Get it from log file:
```
grep Answer /var/log/syslog | egrep 'rcode="0"' | cut -d" " -f 21-23 | sort -u
```
                        
Accepted format:
```
qname="02bb573ca7a7fbef75f05186b520adcf.safeframe.googlesyndication.com" qtype="HTTPS" rcode="0"
qname="02fa32d46675b50def6386d87537ec36.safeframe.googlesyndication.com" qtype="AAAA" rcode="0"
qname="z-p42-instagram.c10r.instagram.com" qtype="AAAA" rcode="0"
qname="z-p42-instagram.c10r.instagram.com" qtype="A" rcode="0"
```