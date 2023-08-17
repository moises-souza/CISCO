import getpass
import sys
import telnetlib

host = "10.10.100.2"
usuario = raw_input("Entre com o seu usuário: ")
password = getpass.getpass()

executar_telnet = telnetlib.Telnet(host)

executar_telnet.read_until("username: ")
executar_telnet.write(usuario + "\n")

if password:
    executar_telnet.read_until("Password: ")
    executar_telnet.write(password +"\n")

executar_telnet.write("enable\n")
executar_telnet.write("cisco\n")
executar_telnet.write("conf t\n")

for numerovlans in range (2,149):
    executar_telnet.write("vlan" + str(numerovlans) + "\n")
    executar_telnet.write("name Python_VLAN_" + str(numerovlans) + "\n")     

executar_telnet.write("end\n")
executar_telnet.write("exit\n")

print executar_telnet.read_all()