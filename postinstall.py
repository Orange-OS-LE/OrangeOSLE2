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

os.system("pacman -S vim")


def install_app_link(name):
    os.system(
        f"curl https://raw.githubusercontent.com/Orange-OS-LE/OrangeOSLE2/main/apps/{name}/{name}.png > {name}.png"
    )
    os.system(f"cp {name}.png /opt/{name}.png")
    os.system(f"rm {name}.png")

    os.system(
        f"curl https://raw.githubusercontent.com/Orange-OS-LE/OrangeOSLE2/main/apps/{name}/{name}.desktop > {name}.desktop"
    )
    os.system(f"cp {name}.desktop /usr/share/applications/")
    os.system(f"rm {name}.desktop")


def install_app_appimage(name, appimagelink):
    os.system(
        f"curl https://raw.githubusercontent.com/Orange-OS-LE/OrangeOSLE2/main/apps/{name}/{name}.png > {name}.png"
    )
    os.system(f"cp {name}.png /opt/{name}.png")
    os.system(f"rm {name}.png")

    os.system(
        f"curl https://raw.githubusercontent.com/Orange-OS-LE/OrangeOSLE2/main/apps/{name}/{name}.desktop > {name}.desktop"
    )
    os.system(f"cp {name}.desktop /usr/share/applications/")
    os.system(f"rm {name}.desktop")

    os.system(f"curl {appimagelink} > {name}.AppImage")
    os.system(f"cp {name}.AppImage /opt/")
    os.system(f"chmod u+x /opt/{name}.AppImage")


install_app_link("ocular")
install_app_link("scratchstats")
install_app_link("aviate")
install_app_link("itinerary")

install_app_appimage(
    "turbowarp",
    "https://github.com/TurboWarp/desktop/releases/download/v1.7.1/TurboWarp-linux-arm64-1.7.1.AppImage",
)

print('You can now reboot by running "sudo reboot -h now"')
