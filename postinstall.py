import os

try:
    os.system("pacman -Syu --noconfirm")
except PermissionError:
    print('You must run this script by running "sudo python3 postinstall.py"')
    quit(0)

os.system("pacman -S --noconfirm xdg-utils vim firefox git xorg xorg-server gnome gdm")
os.system("systemctl enable gdm.service")

def install_apps():
    os.system("git clone https://github.com/OrangeOSLE2/PKGBUILDs"
    os.system("pacman -U PKGBUILDs/packages/oosle-shortcuts-1.0-1-any.pkg.tar.zst")
    os.system("pacman -U PKGBUILDs/packages/turbowarp-desktop-bin-1.8.1-1-any.pkg.tar.zst")

print('You can now reboot by running "sudo reboot -h now"')
