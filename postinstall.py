import os

try:
    os.system("pacman -Syu --noconfirm")
except PermissionError:
    print('You must run this script by running "sudo python3 postinstall.py"')
    quit(0)

os.system("pacman -S --noconfirm xorg xorg-server")
os.system("pacman -S --noconfirm gnome")
os.system("systemctl enable gdm.service")

os.system("pacman -S --noconfirm xdg-utils")


def install_app(name):
    os.system(
        f"curl https://raw.githubusercontent.com/Orange-OS-LE/OrangeOSLE2/main/apps/{name}/{name}.png > {name}.png"
    )
    os.system("cp {name}.png /opt/{name}.png")
    os.system("rm {name}.png")

    os.system(
        "curl https://raw.githubusercontent.com/Orange-OS-LE/OrangeOSLE2/main/apps/{name}/{name}.desktop > {name}.desktop"
    )
    os.system("cp {name}.desktop /usr/share/applications/")
    os.system("rm {name}.desktop")


install_app("ocular")
install_app("scratchstats")
install_app("aviate")

print('You can now reboot by running "sudo reboot -h now"')
