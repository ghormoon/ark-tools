# Ark-server-pauser

This is tool that helps to automatically slomo empty ARK servers over RCON

## Requirements

Python 3.8 (because of rcon)
python3-rcon
python3-yaml

## Installation

Copy the file somewhere where it can be executed, in my case i did `cp ark-server-pauser.py /usr/local/bin/ark-server-pauser` and make sure it's executable `chmod +x`.

Put the config in place and change accordingly `cp servers.yaml.example /etc/ark-server-pauser/servers.yaml`.

Optionally set up systemd service and edit accordingly (eg. if you're using different user/group than ark/ark. just delete those lines if you want to run under root) `cp ark-server-pauser.service.example /lib/systemd/system/ark-server-pauser.service`. This assumes you're using some recent systemd-based linux os. Reload systemctl config `systemctl daemon-reload`, enable the service `systemctl enable ark-server-pauser.service` and start it `systemctl start ark-server-pauser.service`.

## Configuration

Configuration is simple yaml structure. servername can be any string, it will appear in logs, then you need the host, RCON port and admin password. You can repeat as many block as you want, it will run on all servers in parallel.

```
servername:
    port: 1234
    host: some.host.name
    password: adminpassword
```
