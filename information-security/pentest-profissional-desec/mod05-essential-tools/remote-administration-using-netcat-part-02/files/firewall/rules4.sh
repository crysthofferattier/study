#!/bin/bash

# Ativar forward
sysctl -w net.ipv4.ip_forward=1

# Acertar as políticas
iptables -P INPUT DROP
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

# Permintir entrada de tráfego
iptables -A INPUT -i eth0 -p tcp -m tcp --dport 22 -j ACCEPT 
iptables -A INPUT -i eth0 -p tcp -m tcp --dport 80 -j ACCEPT 
iptables -A INPUT -d 172.16.1.5 -i eth0 -p tcp -m tcp --sport 53 --dport 1024:65535 -j ACCEPT 
iptables -A INPUT -d 172.16.1.5 -i eth0 -p tcp -m tcp --sport 80 --dport 1024:65535 -j ACCEPT 
iptables -A INPUT -d 172.16.1.5 -i eth0 -p tcp -m tcp --sport 443 --dport 1024:65535 -j ACCEPT 
iptables -A OUTPUT -o eth0 -p tcp -m tcp --sport 1024:65535 --dport 80 -j ACCEPT 
iptables -A OUTPUT -o eth0 -p tcp -m tcp --sport 1024:65535 --dport 443 -j ACCEPT 
iptables -A OUTPUT -o eth0 -p tcp -m tcp --sport 1024:65535 --dport 53 -j ACCEPT 

# Mascaramento
iptables -t nat -A POSTROUTING -o 172.16.1.1/24 -j MASQUERADE 
