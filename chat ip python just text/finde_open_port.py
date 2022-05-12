import subprocess

def ports():
    open_ports=subprocess.getoutput('Netstat')
    open_ports=int(open_ports[open_ports.index(':')+1:open_ports.index(':')+5])

    return open_ports
