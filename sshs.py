from pexpect import pxssh

s = pxssh.pxssh()
hostname = '192.168.253.128'
username = 'rushan'
password = 'root'
s.login(hostname, username, password)

s.sendline('su')
s.sendline('root')
s.sendline('sudo ifconfig ens33 192.168.1.15 netmask 255.255.255.0')

s.prompt()
print(s.before)