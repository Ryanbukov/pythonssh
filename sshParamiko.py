import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.253.128", username="rushan", password="root", port=22)

stdin, stdout, stderr = ssh.exec_command("uptime")
result = stdout.read().splitlines()
print(result)

stdin, stdout, stderr = ssh.exec_command("sudo ifconfig ens33 192.168.1.14 netmask 255.255.255.0", get_pty = True)
stdin.write("root\n")
result = stdout.read().splitlines()
print(result)

stdin, stdout, stderr = ssh.exec_command("ip a")
result = stdout.read().splitlines()
print(result)
ssh.close()
