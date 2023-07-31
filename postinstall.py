import os, string

try:
    os.system("pacman -Syu --noconfirm")
except PermissionError:
    print('You must run this script by running "sudo python3 postinstall.py"')
    quit(0)

with open('postinstall.pkgs') as pkgs:
    while pkgs.readable():
        for line in pkgs:
            os.system(f'pacman -S {line.strip()}')

with open('postinstall.srvcs') as srvcs:
    while srvcs.readable():
        for line in pkgs:
            os.system(f'sudo systemctl enable {line.strip()}')

def install_apps():
    os.system("git clone https://github.com/OrangeOSLE2/PKGBUILDs")
    os.system("pacman -U PKGBUILDs/packages/oosle-shortcuts-1.0-1-any.pkg.tar.zst")
    os.system("pacman -U PKGBUILDs/packages/turbowarp-desktop-bin-1.8.1-1-any.pkg.tar.zst")

print('You can now reboot by running "sudo reboot -h now"')
