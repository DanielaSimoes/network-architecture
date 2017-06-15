import subprocess

cmd = "snmpwalk -v3 -u user1 -A authpass -X encpassword -l authpriv 10.1.190.2 1.3.6.1.2.1.3.1.1.2"
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
