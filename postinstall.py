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

os.system("pacman -S vim --noconfirm")

os.system("pacman -S firefox --noconfirm")
os.system("pacman -S git")


def install_app_links():
    os.system("git clone https://github.com/OrangeOSLE2/PKGBUILDs"
    os.system("pacman -U PKGBUILDs/packages/oosle-shortcuts-1.0-1-any.pkg.tar.zst")

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

    os.system(f"wget -O {name}.AppImage {appimagelink}")
    os.system(f"cp {name}.AppImage /opt/")
    os.system(f"chmod +x /opt/{name}.AppImage")
)

install_app_appimage(
    "turbowarp",
    "https://github.com/TurboWarp/desktop/releases/download/v1.7.1/TurboWarp-linux-arm64-1.7.1.AppImage",
)

print('You can now reboot by running "sudo reboot -h now"')
