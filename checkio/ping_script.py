import subprocess
with open('C:\Python27\log.txt') as limbo:
    links = limbo.readlines()
    address = [i.strip() for i in links]
    for ping in address:
        res = subprocess.Popen(["ping", "-n", "1", "-w", "200", ping], stdout=limbo, stderr=limbo).wait()
        if res == 0:
            print "ping to", ping, "Active"
        elif res == 2:
            print "no response from", ping
        else:
            print "ping to", ping, "Inactive"
