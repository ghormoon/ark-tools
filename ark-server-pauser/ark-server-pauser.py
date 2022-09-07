#!/usr/bin/env python3

from rcon.source import Client
import time
import multiprocessing
import yaml

def monitor(server, config):
    state = "unknown"
    print("Started monitoring server {0}.".format(server), flush=True)
    
    while True:
        try:
            with Client(config['host'], config['port'], passwd=config['password']) as client:
                response = client.run('ListPlayers')
                if "No Players Connected" in response:
                    if "slow" not in state:
                        print("Slowing down server {0}.".format(server), flush=True)
                        response = client.run('slomo', '0.00000001')
                        state = "slow"
                else:
                    if "normal" not in state:
                        print("Setting speed to normal on server {0}.".format(server), flush=True)
                        response = client.run('slomo', '1')
                        state = "normal"
            time.sleep(5)
        except Exception:
            time.sleep(5)

if __name__ == '__main__':
    config = {}
    with open("/etc/ark-server-pauser/servers.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            exit(1)

    for (server, conf) in config.items():
        p = multiprocessing.Process(target=monitor,args=[server, conf])
        p.start()
