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

class installerClass:
    hard_drive = ""
    host_name = ""
    keyboard_layout = ""
    language = ""
    time_zone = ""
    location = ""


    def ui(self):
        print("Welcome to the Orange OS LE 2 install script.")
        print("We will ask you a few questions to make sure you get a great configuration.")

        self.hard_drive = input("Please input your disk drive file, like /dev/sda: ")
        self.host_name = input(
            "Please enter the name you want to give your computer (a.k.a your hostname): "
        )
        self.keyboard_layout = input("Now enter your keyboard layout, like uk or us: ")

        self.language = input(
            'Now please enter your locale language. This should be something like "en_US": '
        )

        self.time_zone = input(
            "Now we need your timezone, this is usually in the format of <Continent>/<City>, e.g Europe/Paris: "
        )

        self.location = input(
            "Finally, we need to know what country you live in. If you don't want to answer this, enter worldwide."
        ).capitalize()

        print("Okay, now we are going to setup users for you.")
        user_creds = open("user_credentials.json", "w")
        user_creds.write(
            """{
            "!users": ["""
        )
        users_no = int(input("First, how many users do you want the system to hold: "))
        for x in range(0, users_no):
            user_creds.write("{\n")
            username = input(f"Ok what the you want the username of user {x + 1} to be: ")
            password = input(f"Now, what password do you want to give {username}: ")
            superuser = input(
                f"Lastly do you want {username} to be a superuser? Leave blank if you don't: "
            )
            user_creds.write(f'"!password": "{password}",\n')
            if superuser:
                user_creds.write('"sudo": true,\n')
            else:
                user_creds.write('"sudo": false,\n')

            user_creds.write(f'"username": "{username}"\n')
            user_creds.write("}")
            if x == users_no - 1:
                user_creds.write("\n")
            else:
                user_creds.write(",\n")
        user_creds.write("]\n}")
        user_creds.close()


    def config_file(self):
        config = open(sys.argv[1], "r")
        self.hard_drive = config.readline().replace("\n", "")
        self.host_name = config.readline().replace("\n", "")
        self.keyboard_layout = config.readline().replace("\n", "")
        self.language = config.readline().replace("\n", "")
        self.time_zone = config.readline().replace("\n", "")
        self.location = config.readline().capitalize().replace("\n", "")

        user_creds = open("user_credentials.json", "w")
        user_creds.write(
            """{
            "!users": ["""
        )
        users_no = int(config.readline().replace("\n", ""))
        for x in range(0, users_no):
            user_creds.write("{\n")
            username = config.readline().replace("\n", "")
            password = config.readline().replace("\n", "")
            superuser = config.readline().replace("\n", "")
            user_creds.write(f'"!password": "{password}",\n')
            if superuser:
                user_creds.write('"sudo": true,\n')
            else:
                user_creds.write('"sudo": false,\n')

            user_creds.write(f'"username": "{username}"\n')
            user_creds.write("}")
            if x == users_no - 1:
                user_creds.write("\n")
            else:
                user_creds.write(",\n")
        user_creds.write("]\n}")
        user_creds.close()