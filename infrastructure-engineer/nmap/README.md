#The Complete Nmap Ethical Hacking Course: Network Security

## 04. Nmap Basics Target Specification & Port States

* Nmap help
```
$ nmap -h
```

### Nmap Basics

* Basic command
```
$ nmap 192.168.0.106
```

* Output
```
Starting Nmap 7.01 ( https://nmap.org ) at 2018-02-05 20:17 -03
Nmap scan report for 192.168.0.106
Host is up (0.000071s latency).
Not shown: 977 closed ports
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
23/tcp   open  telnet
25/tcp   open  smtp
53/tcp   open  domain
80/tcp   open  http
111/tcp  open  rpcbind
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
512/tcp  open  exec
513/tcp  open  login
514/tcp  open  shell
1099/tcp open  rmiregistry
1524/tcp open  ingreslock
2049/tcp open  nfs
2121/tcp open  ccproxy-ftp
3306/tcp open  mysql
5432/tcp open  postgresql
5900/tcp open  vnc
6000/tcp open  X11
6667/tcp open  irc
8009/tcp open  ajp13
8180/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds
```

* Top Port's
```
$ sort -r -k3 /usr/share/nmap/nmap-services | grep tcp | head -n 1000
```

* Run
	- Privilaged (root/admin) = Raw SYN Stealth Scan
	- Unprivilaged = TCP Connect Scan

### Nmap Target Specification

* Can pass hostnames, IP addresses, networks, etc.
```
$ nmap scanme.nmap.org
$ nmap microsoft.com/24 
$ nmap 192.168.0.1
$ nmap 10.0.0-255.1-254
```

* -iL [inputfilename]: Input from list of hosts/networks
```
$ nmap -iL targets.txt
```

* -iR [num hosts]: Choose random targets
```
$ nmap -iR 3 -v
```


### Nmap Port states

* Open: An application is actively accepting TCP connections, UDP datagrams or SCTP associations on this port.
* Closed: A closed port is accessible (it receives and responds to Nmap probe packets), but there is no application listening on it.
* Filtered: Nmap cannot determine whether the port is open because packet filtering prevents its probes from reaching the port.
* Unfiltered: The unfiltered state means that a port is accessible, but Nmap is unable to determine whether it is open or closed.
* Open|Filtered: Nmap places ports in this state when it is unable to determine whether a port is open or filtered.
* Closed|Filtered: This state is used when Nmap is unable to determine whether a port is closed or filtered.

## 05. Nmap Discovery and Ping Scanning

### Nmap Discovery (Part 1)

```
$ nmap 192.168.0.100-106
```

* If no host discovery options, nmap send an:
	- ICMP echo request (ping)
	- TCP SYN packet to port 443
	- TCP ACK packet to port 80
	- ICMP timestamp request

* Exceptions:
	- ARP (for IPv4) and Neighbor Discovery (for IPv6) scans which are used for any targets on a local ethernet network.

### Nmap Discovery (Part 2)

* -sL: list scan, simply list targets to scan.
```
$ nmap facebook.com/24 -sL
$ nmap -iR 300 -sL -vv
```

* -sn: Ping Scan, disable port scan.
```
$ nmap 192.168.0.1/24 -sn
```

* -Pn: Treat all hosts as online, skip host discovery.
```
$ nmap 192.168.0.1/24 -Pn
```

### Nmap Discovery (Part 3)

* -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
```
$ nmap 192.168.0.1-5 -PS22-25,80,113,1050,3500 -v
```

### Nmap Discovery (Part 4)
* -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
```
$ nmap 192.168.1.1-255 -PE -sn -v
```

* -PO [protocol list]: IP Protocol Ping
```
$ nmap 192.168.1.1-255 -PO1,2,4 -sn
```

* -PR: ARP scan (local network)
```
$ nmap 192.168.1.1-255 -PR -sn -vv
```

* --dns-servers: Specify custom DNS servers
```
$ nmap 192.168.1.1-50 -sL --dns-servers 192.168.1.1
```

* --traceroute: Trace hop path to each host
```
$ nmap -iR 3 -sn --traceroute
```

## 06. Nmap Scan Techniques

### Nmap Scan Techniques (Part 1)

* SYN and Connect
	- -sS/sT: TCP SYN/Connect()
		- -sS: SYN scan, quick and default scan

			```
			$ nmap 192.168.0.1 -sS -v
			```

		- -sT: (TCP) Connect(), NMAP establish a connection with the target machine and port.

			```
			$ nmap 192.168.0.1 -sT -v
			```

### Nmap Scan Techniques (Part 2)

* UDP scan
	- -sU: UDP Scan (root)

		```
		$ nmap 192.168.0.106 -sU -v
		```

		- UDP and TCP scan:

		```
		$ nmap 192.168.0.106 -sU -sS -v
		```
* STCP scan
	* -sY/sZ: SCTP INIT/COOKIE-ECHO scans (mobile cellular network)

		```
		$ nmap 192.168.0.106 -sY -v
		```

* Extras
	- UDP and TCP scan:

		```
		$ nmap 192.168.0.106 -sU -sS -v
		```
	- -sV: version detection

		```
		$ nmap 192.168.0.106 -sU -sV -v
		```
	- --host-timeout:

		```
		$ nmap 192.168.0.106 -sU -sV -v --host-timeout 2m
		```

### Nmap Scan Techniques (Part 3)
* TCP ACK scan
	* -sA: ACK scan (map firewall rules), run as root

			```
			$ nmap 192.168.0.1 -sA -v
			```

	* -sW: Window scan

		```
		$ nmap 192.168.0.1 -sW -v
		```

### Nmap Scan Techniques (Part 4)

* -sN/sF/sX: TCP Null, FIN, and Xmas scans
	- Exactly the same in behavior, except for the TCP flags set in the probe packets. Exploit a subtle lopp hole to differentiate between open and closed ports.

		```
		$ nmap 192.168.0.1 -sN
		$ nmap 192.168.0.1 -sF
		$ nmap 192.168.0.1 -sX
		```

* -sM: Maimon scans

```
$ nmap 192.168.0.1 -sM
```

* --sI [zombie host[:port]]: Idle scan [link](https://nmap.org/book/idlescan.html)

```
$ nmap 192.168.0.1 -sI 10.0.0.1:80
```	

* --scanflags [flags]: Customize TCP scan flags

```
$ nmap 192.168.0.1 --scanflags
```

* -sO: IP protocol scan (root)

```
$ nmap 192.168.0.1 -sO
$ nmap 192.168.0.1 -sO -p 1,2,3,4,5,6,17

Result:

Starting Nmap 7.01 ( https://nmap.org ) at 2018-02-06 19:40 -03
Warning: 192.168.0.106 giving up on port because retransmission cap hit (10).
Nmap scan report for 192.168.0.106
Host is up (0.030s latency).
Not shown: 250 closed protocols
PROTOCOL STATE         SERVICE
1        open          icmp
2        open|filtered igmp
6        open          tcp
17       open          udp
136      open|filtered udplite
201      open|filtered unknown

```



## 07. Nmap Port Specification Service Version & OS Detection

### Nmap Port Specification
* -p [port ranges]: Only scan specified ports	
```
$ nmap 192.168.0.106 -v -p 21-1000
$ nmap 192.168.0.106 -v -p http,https,ftp
```

- U:/T: UDP ports and TCP ports
```
$ nmap 192.168.0.106 -v -p U:53,111,137,5353,T:21-25,80,139,8080 -sU -sS

Result:
PORT     STATE  SERVICE
21/tcp   open   ftp
22/tcp   open   ssh
23/tcp   open   telnet
24/tcp   closed priv-mail
25/tcp   open   smtp
80/tcp   open   http
139/tcp  open   netbios-ssn
8080/tcp closed http-proxy
53/udp   open   domain
111/udp  open   rpcbind
137/udp  open   netbios-ns
5353/udp closed zeroconf
```

- -p-: All ports
```
$ nmap 192.168.0.106 -v -p-
$ nmap 192.168.0.106 -v -p-65535 (1 to 65535)
$ nmap 192.168.0.106 -v -p0-  (0 to 65535)
```

* -F: Fast mode, scan fewer ports than the default scan (100 ports)
```
$ nmap 192.168.0.106 -v -F
```

* --top-ports [number]: Scan [num] most common ports
```
$ nmap 192.168.0.106 -v --top-ports 2000
```

* --exclude-ports [port ranges]: Exclude the specified ports from scanning
```
$ nmap 192.168.0.106 -v --top-ports 2000 --exclude-ports 80,21,8080,5353,123-456
```

* -r: Scan ports consecutively - don't randomize
```
$ nmap 192.168.0.106 -v -r
```

### Nmap Service and Version Detection
* Nmap service probes:
```
cat /usr/share/nmap/nmap-service-probes
```

* -sV: Version detectation
```
$ nmap 192.168.0.106 -v -sV
$ nmap 192.168.0.106 -v -sV -p 80,22
$ nmap 192.168.0.106 -v -sV --allports
```

* --version-intensity [level]: Set from 0 (light) to 9 (try all probes) (default is 7)
```
$ nmap 192.168.0.106 -sV --version-intensity 6
```

* --version-light: Limit to most likely probes (intensity 2)
```
$ nmap 192.168.0.106 -sV --version-light -v
```

* --version-all: Try every single probe (intensity 9)
```
$ nmap 192.168.0.106 -sV --version-all -v
```

* --version-trace: Show detailed version scan activity (for debugging)
```
$ nmap 192.168.0.106 -sV --version-trace
```

### Nmap OS Detection

* Info:
```
$ cat /usr/share/nmap/nmap-os-db
```

* -O: OS information
```
$ nmap 192.168.0.106 -O
$ nmap 192.168.0.106 -O -v
```

```
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.9 - 2.6.33
Uptime guess: 0.089 days (since Wed Feb  7 17:56:48 2018)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=198 (Good luck!)
IP ID Sequence Generation: All zeros
```

--osscan-limit: Limit OS detection to promising targets
```
$ nmap 192.168.0.1-40 -O -Pn -v --osscan-limit
```

--fuzzy: guess more agrecive
```
$ nmap 192.168.0.106 -O --fuzzy
```

-max-os-tries [num]: Max detection tries
```
$ nmap 192.168.0.106 -O --fuzzy -max-os-tries 1
```

--osscan-guess: Guess OS more aggressively
```
$ nmap 192.168.0.106 -O -Pn -v --osscan-limit
```


## 08. Nmap Scripting Engine (NSE)

### Nmap Scripting Engine (NSE) Part 1 - Categories

* [NSE Documentation](https://nmap.org/nsedoc/index.html)
* Categories:
	- [auth](https://nmap.org/nsedoc/categories/auth.html)
	- [broadcast](https://nmap.org/nsedoc/categories/broadcast.html)
	- [brute](https://nmap.org/nsedoc/categories/brute)
	- [default](https://nmap.org/nsedoc/categories/default.html)
	- [discovery](https://nmap.org/nsedoc/categories/discovery.html)
	- [dos](https://nmap.org/nsedoc/categories/dos.html)
	- [exploit](https://nmap.org/nsedoc/categories/exploit.html)
	- [external](https://nmap.org/nsedoc/categories/external.html)
	- [fuzzer](https://nmap.org/nsedoc/categories/fuzzer.html)
	- [intrusive](https://nmap.org/nsedoc/categories/intrusive.html)
	- [malware](https://nmap.org/nsedoc/categories/malware.html)
	- [safe](https://nmap.org/nsedoc/categories/safe.html)
	- [version](https://nmap.org/nsedoc/categories/version.html)
	- [vuln](https://nmap.org/nsedoc/categories/vuln.html)

* Script's (/usr/share/nmap/scripts)
```
$ locate *.nse
$ locate *auth*.nse
$ locate smb*.nse
$ locate *ip-geolocation-*
```

* -sC: equivalent to --script=default
```
$ nmap -sC scanme.nmap.org -v
```

### Nmap Scripting Engine (NSE) Part 2 - Usage and Cool Scripts

* Rules:
	- prerule()
	- hostrule(host)
	- portrule(host, port)
	- postrule()

### Script's usage:
* --script [categories/script.nse]: Run script
```
$ nmap 192.168.0.106 --script default,safe

$ nmap -vvv --script=banner 192.168.0.106
$ nmap -Pn --script=http-xssed scanme.nmap.org
$ nmap -Pn --script=http-sitemap-generator scanme.nmap.org
$ nmap -v --script "http-*" 192.168.0.106
$ nmap -n -Pn -p 80 --open -sV -v  --script http-method-tamper 192.168.0.106
$ nmap -n -Pn -p 80 --open -sV -vvv  --script banner,http-title -iR 100
$ nmap -Pn --script=dns-brute facebook.com
$ nmap --script= smb-os-discovery -vv 192.168.1.81
$ nmap -n -Pn -vv -O -sV --script smb-enum*,smb-ls,smb-mbenum,smb-os-discovery,smb-s*,smb-vuln*,smbv2* -vv 192.168.0.106
$ nmap --script broadcast -v
$ nmap --script "broadcast and not targets*" -v
$ nmap --script "broadcast and not targets*" -v --script-trace
$ nmap --script "not intruse" -vv 192.168.0.106
$ nmap --script "vuln,exploit" -vv 192.168.0.106 -sV -O
$ nmap --script ip-geolocation-* facebook.com
$ nmap --script whois* facebook.com
```

* Obs:
	- ip-geolocation-maxmind.nse: Download database
		* [Maxmind database](http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz) 
	- ip-geolocation-ipinfodb.nse: register API key
		* [API key](http://ipinfodb.com/register.php)

## Nmap Scripting Engine (NSE) Part 4 - Usage and Cool Scripts

### vulscan:
* Vulscan is a module which enhances nmap to a vulnerability scanner.
	- [Documentation](http://www.computec.ch/projekte/vulscan/?s=documentation) 
	- [Downlaod](http://www.computec.ch/projekte/vulscan/download/nmap_nse_vulscan-2.0.tar.gz)

* Installation
	Please install the files into the following folder of your Nmap installation:
```
$ cd /usr/share/nmap/scripts/
$ wget http://www.computec.ch/projekte/vulscan/download/nmap_nse_vulscan-2.0.tar.gz
$ tar xvfz nmap_nse_vulscan-2.0.tar.gz
$ cd vulscan/
$ ls -l
```

* Usage
	You have to run the following minimal command to initiate a simple vulnerability scan:
```
$ nmap -sV --script=vulscan/vulscan.nse www.example.com
```

### Script args and help

* --script-args=<n1=v1,[n2=v2,...]>: provide arguments to scripts
```
$ nmap -sV --script=vulscan/vulscan.nse --script-args vulscaninteractive=1 192.168.0.106
```

* --script-help=[Lua scripts]: Show help about scripts. [script-name] is a comma-separated list of script-files or
           script-categories.
```
$ nmap --script-help [scaript-name] snmp-sysdescr
$ nmap --script-help snmp-sysdescr
```

### Script
```
$ nmap --script http-open-proxy -p8080 192.168.0.100-106
$ nmap -p80 --script http-brute --script-args http-brute.path=/admin/ scanme.nmap.org
$ nmap -p80 --script http-brute --script-args userdb=/var/usernames.txt,passdb=/var/pwd.txt scanme.nmap.org
$ nmap -p80 --script http-brute --script-args brute.firstOnly
$ nmap -p80 --script http-wordpress-brute --script-args http-wordpress-brute.threads=5 scanme.nmap.org
$ namp -p25 --script smtp-brute scanme.nmap.org
$ namp -p80 --script http-waf-defect scanme.nmap.org
$ namp -p80 --script http-unsafe-output-escaping scanme.nmap.org
$ namp -p80 --script http-sql-injection scanme.nmap.org
$ namp -p3306 --script mysql-databases --script-args mysqluser=[user-name],mysqlpassword=[user-password] scanme.nmap.org
$ namp -sV --script smtp-open-relay -v -iR 100 -p 25 -n -Pn
```

### Update nmap script database
```
$ namp -p80 --script-updatedb
```

## Writing Nmap Scripting Engine (NSE) Scripts

### Script
* Lua Base language
	- Lua v5.3 documentation [here](https://www.lua.org/manual/5.3/)
	- Nmap Script Engine Documentatio [here](https://media.blackhat.com/bh-us-10/whitepapers/Vaskovitch/BlackHat-USA-2010-Fyodor-Fifield-NMAP-Scripting-Engine-wp.pdf)
	- Script  Example [here](https://svn.nmap.org/nmap/scripts/rpcinfo.nse)

## 09. Nmap Performance Firewall and IDS Evasion

### Nmap Timing and Performance

* -T[0-5]: Set timing template (higher is faster)]
	- -T0: paranoid (slow)
	- -T1: sneaky (slow)
	- -T2: polite
	- -T3: normal/default
	- -T4: aggressive (reasonably fast (local network))
	- -T5: insane
```
$ nmap -v -T0 192.168.0.106
$ nmap -v -T1 192.168.0.106
$ nmap -v -T2 192.168.0.106
$ nmap -v -T3 192.168.0.106
$ nmap -v -T4 192.168.0.106
$ nmap -v -T5 192.168.0.106
```

### Nmap Firewall IDS Evasion and Spoofing (Part 1)

* -f, --mtu [val]: fragment packets (optionally w/given MTU)
```
$ nmap -f 192.168.0.106
$ nmap -mtu 16 192.168.0.106
```

* -D [decoy1,decoy2[,ME],...]: Cloak a scan with decoys
```
$ nmap -n -D 192.168.101,192.168.102,192.168.103,192.168.104 192.168.1.1
```

* -S [IP_Address]: Spoof source address
	Here we are scanning facebook as if we-re coming from Microsoft.
```
$ nmap -S www.microsoft.com www.facebook.com
```

* -e [iface]: Use specified interface
```
$ nmap -S www.microsoft.com www.facebook.com -e eth0 -Pn
```

* -g/--source-port [portnum]: Use given port number
```
$ nmap -n -T4 -g 53 192.168.0.106
```

### Nmap Firewall IDS Evasion and Spoofing (Part 2)
* --proxies [url1,[url2],...]: Relay connections through HTTP/SOCKS4 proxies
```
$ nmap --proxies http://192.168.0.100:8080, http://192.168.0.101:8080 192.168.0.100
```

* --data-length [num]: Append random data to sent packets
```
$ nmap --data-length 200 192.168.0.100
```

* --data [hex string]: Append a custom payload to sent packets
```
$ namp --data 0xAABBCC 192.168.0.106
```

* --data-string [string]: Append a custom ASCII string to sent packets
```
$ namp --data-string "Will scanned your system!" 192.168.0.100
```

```
$ nmap -f -T0 -n -Pn --data-length 200 -D 192.168.0.106
```

## 10. Nmap Output and Extras
Output scan in normal, XML, s|<rIpt kIddi3, and Grepable format, respectively, to the given filename.

### Nmap Output

* -oN: normal output
```
$ nmap 192.168.0.104 -oN normal.file
```

* -oX: xml file
```
$ nmap 192.168.0.104 -oX files/xml.file
```

* -oG: grep file
```
$ nmap 192.168.0.104 -oG files/grep.file
```

* -oS: scriptkiddie file
```
$ nmap 192.168.0.104 -oG files/scriptkiddie.file
```

* -oA: all types (xml, grep, normal)
```
$ nmap 192.168.0.104 -oG files/results
```

* - (dash): nmap is not going to create a output file, bu the output is going  to screen in a grep format.
```
$ nmap -p80 -sV -oG - --open 192.168.0.1/24
$ nmap -p80 -sV -oG - --open 192.168.0.1/24 | grep open
```

* List of live hosts:
```
$ nmap 192.168.0.1-100 -n -oX out.xml | grep "Nmap" | cut -d " " -f5 > files/live-hosts.txt
```

* --append-output:
```
$ nmap 192.168.0.1 -T4 -oN file.file --append-output
$ nmap 192.168.0.2 -T4 -oN file.file --append-output
```

### Nmap Output & Miscellaneous Options

* -v: Increase verbosity level (use -vv or more for greater effect)
```
$ nmap -v 192.168.0.1
$ nmap -vv 192.168.0.1
$ nmap -vvv 192.168.0.1
```

* -d: Increase debugging level (use -dd or more for greater effect)
```
$ nmap -d 192.168.0.1
$ nmap -dd 192.168.0.1
```

* -h: help
```
$ nmap -h
```

* --reason: Display the reason a port is in a particular state
```
$ nmap --reason 192.168.0.1
$ nmap --reason 192.168.0.1 --open
$ nmap --reason 192.168.0.1 --open --packet-trace
```

* --packet-trace: Show all packets sent and received
```
$ nmap --reason 192.168.0.1 --open --packet-trace
```

* --source-port: equal -g
```
$ nmap 192.168.0.1 -T4 --packet-trace --source-port 53
```

* --iflist: Print host interfaces and routes (for debugging)
```
$ nmap --iflist
```

* --resume [file-name]: Resume aborted scan
```
$ nmap --resume hosts.txt
```

* -6 [IPv6-address]: IPv6
```
$ nmap -6 2607:f0d0:1002:51::4
```

* -A (all): Enable OS detection, version detection, script scanning, and traceroute
```
$ nmap 192.168.0.104 -A -T4
$ nmap -O -sV -sC -traceroute -T4 192.168.0.104
```

## Extras

* ndiff: Compare scan with
```
$ ndiff out-put-scan1.xml out-put-scan2.xml
```

* xlstproc: Convert xml to html
```
$ xsltproc out-put.xml -o out-put.html
```

* xlstproc: Convert xml to html
```
$ xsltproc out-put.xml -o out-put.html
```

* filters
```
$ grep " open " results.nmap | sed -r 's/ +/ /g' | sort | uniq -c | sort -rn | less
```

* Online web scaner:
	* [Pentest-Tools.com](https://pentest-tools.com/network-vulnerability-scanning/tcp-port-scanner-online-nmap)
	* [Nmap online scanner](http://nmap.online-domain-tools.com/)