from pexpect import pxssh

try:
    s = pxssh.pxssh()
    hostname = '192.168.253.128'
    username = 'rushan'
    password = 'root'
    s.login(hostname, username, password)
    s.sendline('uptime')
    s.prompt()
    print(s.before)
    s.sendline('su')
    s.prompt()
    print(s.before)
    s.sendline('root')
    s.prompt()
    print(s.before)
    s.sendline('sudo ifconfig ens33 192.168.1.18 netmask 255.255.255.0')
    s.prompt()
    print(s.before)

except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)