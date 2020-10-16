from pexpect import pxssh

s = pxssh.pxssh()
hostname = '192.168.253.128'
username = 'rushan'
password = 'root'
s.login(hostname, username, password)

s.sendline('sudo ifconfig ens33:0 192.168.1.21 netmask 255.255.255.0')
s.prompt()
print(s.before)
s.sendline('root')
s.prompt()
print(s.before)

s.sendline('ip a')
s.prompt()
print(s.before)