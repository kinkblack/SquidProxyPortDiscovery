import sys, signal, requests

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

#Ctrl + C
signal.signal(signal.SIGINT, def_handler)

main_url = "url victima" #url o ip principal de donde proceden la IP por donde corre el servicio  proxy
squid_proxy = {'http': 'http:// <IP y puerto por donde corre el servicio>'}

def portDiscovery():

    common_tcp_ports = {<50 tcp port mas usados por ejemplo>}

    for tcp_port in common_tcp_ports:

        r = request.get(main_url + ':'+ str(tcp_port),proxies=squid_proxy)

        if r.status_code != 503:  #en este caso es 503 el codigo que indica error por eso no nos interesa
            print("\n[+] Port "+ str(tcp_port) + "- OPEN")

if __name__ == '__main__':

    portDiscovery()
