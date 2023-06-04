import os

try:
    os.system("pacman -Syu")
except PermissionError:
    print('You must run this script by running "sudo python3 postinstall.py"')
    quit(0)

os.system("pacman -S --noconfirm xorg xorg-server")
os.system("pacman -S --noconfirm gnome")
os.system("systemctl enable gdm.service")

os.system("pacman -S --noconfirm xdg-utils")
os.system(
    "curl https://raw.githubusercontent.com/Orange-OS-LE/OrangeOSLE2/main/apps/ocular/ocular.png > ocular.png"
)
os.system("cp ocular.png /opt/ocular.png")
os.system("rm ocular.png")

os.system(
    "curl https://raw.githubusercontent.com/Orange-OS-LE/OrangeOSLE2/main/apps/ocular/Ocular.desktop > Ocular.desktop"
)
os.system("cp Ocular.desktop /usr/share/applications/")
os.system("rm Ocular.desktop")

print('You can now reboot by running "sudo reboot -h now"')
