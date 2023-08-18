# -*- coding: utf-8 -*-
import getpass
import sys
import telnetlib

host = "10.10.100.2"
usuario = raw_input("Entre com o seu usuário: ")
password = getpass.getpass()

executar_telnet = telnetlib.Telnet(host)

executar_telnet.read_until("username: ")
executar_telnet.write(usuario + "\n")

for n in range (2,21):
    print ("Vlan" + str(n))
    print ("name Vlan_script_" + str())


