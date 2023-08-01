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
    f"""
{'{'}
    "config_version": "2.5.2",
    "additional-repositories": [],
    "archinstall-language": "English",
    "audio_config": {'{'}"audio": "pipewire"{'}'},
    "bootloader": "Systemd-boot",
    "debug": false,
    "disk_config": {'{'}
        "config_type": "default_layout",
        "device_modifications": [
            {'{'}
                "device": "{installer.hard_drive}"
                "partitions": [
                    {'{'}
                        "btrfs": [],
                        "flags": [
                            "Boot"
                        ],
                        "fs_type": "fat32",
                        "length": {'{'}
                            "sector_size": null,
                            "total_size": null,
                            "unit": "MiB",
                            "value": 512
                        {'}'},
                        "mount_options": [],
                        "mountpoint": "/boot",
                        "obj_id": "2c3fa2d5-2c79-4fab-86ec-22d0ea1543c0",
                        "start": {'{'}
                            "sector_size": null,
                            "total_size": null,
                            "unit": "MiB",
                            "value": 1
                        {'}'},
                        "status": "create",
                        "type": "primary"
                    {'}'},
                    {'{'}
                        "btrfs": [],
                        "flags": [],
                        "fs_type": "ext4",
                        "length": {'{'}
                            "sector_size": null,
                            "total_size": null,
                            "unit": "GiB",
                            "value": 20
                        {'}'},
                        "mount_options": [],
                        "mountpoint": "/",
                        "obj_id": "3e7018a0-363b-4d05-ab83-8e82d13db208",
                        "start": {'{'}
                            "sector_size": null,
                            "total_size": null,
                            "unit": "MiB",
                            "value": 513
                        {'}'},
                        "status": "create",
                        "type": "primary"
                    {'}'},
                    {'{'}
                        "btrfs": [],
                        "flags": [],
                        "fs_type": "ext4",
                        "length": {'{'}
                            "sector_size": null,
                            "total_size": {'{'}
                                "sector_size": null,
                                "total_size": null,
                                "unit": "B",
                                "value": 250148290560
                            {'}'},
                            "unit": "Percent",
                            "value": 100
                        {'}'},
                        "mount_options": [],
                        "mountpoint": "/home",
                        "obj_id": "ce58b139-f041-4a06-94da-1f8bad775d3f",
                        "start": {'{'}
                            "sector_size": null,
                            "total_size": null,
                            "unit": "GiB",
                            "value": 20
                        {'}'},
                        "status": "create",
                        "type": "primary"
                    {'}'}
                ],
                "wipe": true
            {'}'}
        ]
    {'}'},
    "hostname": "{installer.host_name}",
    "kernels": [
        "linux"
    ],
    "keyboard-layout": "{installer.keyboard_layout}",
    "mirror-region": {'{'}
        "Worldwide": {'{'}
            "https://geo.mirror.pkgbuild/$repo/os/$arch": true
        {'}'}
    {'}'},
    "nic": {'{'}
        "dhcp": true,
        "dns": null,
        "gateway": null,
        "iface": null,
        "ip": null,
        "type": "nm"
    {'}'},
    "no_pkg_lookups": false,
    "ntp": true,
    "offline": false,
    "packages": [],
    "parallel downloads": 0,
    profile_config" : {'{'}
        "gfx-driver": null,
        "greeter": null,
        "profile": {'{'}
            "custom_settings": {'{'}{'}'},
            "details": [],
            "main": "Minimal"
        {'}'}
    {'}'},
    "script": "guided",
    "silent": false,
    "swap": true,
    "sys-encoding": "utf-8",
    "sys-language": "{installer.language}",
    "timezone": "{installer.time_zone}",
    "version": "2.5.2"
{'}'}
"""
)
user_config.close()
# user creds
confirm_installation = input(
    'This will delete all data on the disk you have chosen,\nIf you agree to the conditions, submit with a "Y". Otherwise, submit with any other letter.'
)
if confirm_installation.lower() != "y":
    print("Quitting the script, but run the script again if you change your mind.")
    quit(0)
else:
    print("Here we go...")
if sys.argv.__len__() == 2:
    os.system(
        "sudo archinstall --silent --config ./user_configuration.json --creds ./user_credentials.json"
    )
else:
    os.system(
        "sudo archinstall --silent --config ./user_configuration.json --creds ./user_credentials.json"
    )

print("You can reboot now, if there were no errors.")
print('To reboot run "reboot -h now"')
