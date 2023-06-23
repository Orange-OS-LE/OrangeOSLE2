"""
This program is an installer for Orange OS LE 2, you can find more information in the README
    Copyright (C) 2022 Michael Halpin

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import sys, os
from installClass import installerClass


installer = installerClass()


if sys.argv.__len__() == 2:
    installer.config_file()
else:
    installer.ui()


user_config = open("user_configuration.json", "w")
user_config.write(
    f"""{'{'}
"additional-repositories": "",
"audio": "pipewire",
"bootloader": "grub-install",
"filesystem": "ext4",
"HSM": null,
"config_version": "2.5.0",
"debug": false,
"harddrives": [
    "{installer.hard_drive}"
],
"kernels": [
    "linux"
],
"swap": true,
"keyboard-language": "{installer.keyboard_layout}",
"mirror-region": "{installer.location}",
"hostname": "{installer.host_name}",
"keyboard-layout": "{installer.keyboard_layout}",
"mount_point": null, 
"nic": {'{'}
        "dhcp": true,
        "dns": null,
        "gateway": null,
        "iface": null,
        "ip": null,
        "type": "nm"
{'}'},
"ntp": true,
"plugin": null,
"profile": {'{'}
    "path": "/usr/lib/python3.11/site-packages/archinstall/profiles/minimal.py"
{'}'},
"script": "guided",
"silent": false,
"sys-language": "{installer.language}",
"sys-encoding": "utf-8",
"timezone": "{installer.time_zone}",
"version": "2.5.0",
"packages": ["python3", "neofetch", "wget"],
"custom-commands": []
{'}'}"""
)
user_config.close()
# user creds
print("Now we will setup the disks for you. Unfortunately, we can't offer to let you")
print("do the disk partioning, but we might offer this in the future.")
confirm_installation = input(
    'This will delete all data on the disk you have chosen,\nIf you agree to the conditions, submit with a "Y". Otherwise, submit with any other letter.'
)
if confirm_installation.lower() != "y":
    print("Quitting the script, but run the script again if you change your mind.")
    quit(0)
else:
    print("Here we go...")
user_disks = open("user_disk_layout.json", "w")
user_disks.write(
    f"""{'{'}
    "{installer.hard_drive}": {'{'}
        "partitions": [
            {'{'}
                "boot": true,
                "encrypted": false,
                "filesystem": {'{'}
                    "format": "fat32"
                {'}'},
                "mountpoint": "/boot",
                "size": "{'203MiB' if not os.path.exists("/sys/firmware/efi") else '512MiB'}",
                "start": "{'3MiB' if not os.path.exists("/sys/firmware/efi") else '1MiB'}",
                "type": "primary",
                "wipe": true
            {'}'},
            {'{'}
                "encrypted": false,
                "filesystem": {'{'}
                    "format": "ext4",
                    "mount_options": []
                {'}'},
                "mountpoint": "/",
                "size": "100%",
                "start": "{'206MiB' if not os.path.exists("/sys/firmware/efi") else '513MiB'}",
                "type": "primary",
                "wipe": true
            {'}'}
        ],
        "wipe": true
    {'}'}
{'}'}"""
)
user_disks.close()
if sys.argv.__len__() == 2:
    os.system(
        "sudo archinstall --silent --config ./user_configuration.json --creds ./user_credentials.json --disk_layouts ./user_disk_layout.json"
    )
else:
    os.system(
        "sudo archinstall --silent --config ./user_configuration.json --creds ./user_credentials.json --disk_layouts ./user_disk_layout.json"
    )

print("You can reboot now, if there were no errors.")
print('To reboot run "reboot -h now"')
