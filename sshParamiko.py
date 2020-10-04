import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.253.128", username="rushan", password="root", port=22)
chan = ssh.invoke_shell()
#command = "TERM=xterm " + "su"
#TERM_WIDTH = 'terminal width 250\n'

stdin, stdout, stderr = ssh.exec_command("uptime")
stdin.flush()
result = stdout.read().splitlines()
print(result)

stdin, stdout, stderr = ssh.exec_command('sudo ifconfig ens33 192.168.1.14 netmask 255.255.255.0', get_pty = True)
#time.sleep(7)
#chan.send(TERM_WIDTH)
stdin.write("root" + "\n")
stdin.flush()
result = stdout.read().splitlines()
print(result)

#stdin, stdout, stderr = ssh.exec_command("ip a add 192.168.1.14/24 dev ens33")
#stdin.flush()
#result = stdout.read().splitlines()
#print(result)

stdin, stdout, stderr = ssh.exec_command("ip a")
stdin.flush()
result = stdout.read().splitlines()
print(result)
ssh.close()
