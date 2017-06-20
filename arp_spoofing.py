import subprocess
from prettytable import PrettyTable

cmd = "snmpwalk -v3 -u user1 -A authpass -X encpassword -l authpriv 10.1.190.2 1.3.6.1.2.1.3.1.1.2"
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()

route_arptable = {}

for i in range(0, len(output.split("="))-1):
    ip = ".".join([x.strip(' ') for x in output.split("=")[i].split(".")[-4:]])

    if output.split("=")[i+1].replace(" Hex-STRING: ", "").split(" ")[-1] == "":
        mac = ":".join(output.split("=")[i+1].replace(" Hex-STRING: ", "").split(" ")[-8:-2])
    else:
        mac = ":".join(output.split("=")[i+1].replace(" Hex-STRING: ", "").split(" ")[-8:-1])

    if ip in route_arptable:
        print "ARP Spoofing detected!"
        print ("new ip: ", ip, " ; ", "new mac: ", mac)
        print ("current ip: ", ip, " ; ", "current mac: ", route_arptable[ip])
        exit(1)

    route_arptable[ip] = mac

    i += 2

print "ARP Spoofing not detected!"
print ""

t = PrettyTable(["IP", "MAC"])

for key in route_arptable:
    t.add_row([key, route_arptable[key]])

print(t)

# print output.split("=")[0].split(".")[-4:]