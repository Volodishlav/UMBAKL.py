# UMBAKL.py - Python keylogger PoC by Volodishlav

This tool is a keylogger for Linux-based operating systems. Just run the ".py" file and the keylogger will start.

## Set up the tool:

```bash
cp umbakl.py /usr/umbakl/umbakl.py
```

- The tool monitors keyboard input and stores captured data in a local file located at: **/usr/umbakl/umbakl.txt**.
- Just press the keys "umbakl" all at once on the computer and the program will copy **/usr/umbakl/umbakl.txt** to the default USB path.
- The default USB path in which it will copy the ".txt" file to is **/media/usuario/3FB6-9A53**.
- To enable persistence across system reboots, copy the systemd service file: **python3ubuntu.service** to **/etc/systemd/system/**.

```bash
cp python3ubuntu.service /etc/systemd/system/
```

Then enable it with:

```bash
sudo systemctl enable python3ubuntu.service
sudo systemctl start python3ubuntu.service
```

## All variables can (and should) be modified to suit your preferences. Enjoy :)
