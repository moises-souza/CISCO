from netmiko import ConnectHandler

iosv_12_s1 = {
    'device type': 'cisco_ios',
    'ip': '10.10.100.2',
    'username': 'cisco',
    'password': 'cisco',

}
iosv_12_s2 = {
    'device type': 'cisco_ios',
    'ip': '10.10.100.4',
    'username': 'cisco',
    'password': 'cisco',

}

with open('basci_config1') as f:
    lines = f.read().splitlines()
print lines

all_devices = [iosv_12_s1,iosv_12_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output

    