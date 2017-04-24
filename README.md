# TechLab - Maggiordomo setup doc

## Format SD
Used Windows SD-formatter with a Kingston 16GB HC Class 10

## Install Raspbian Lite to the SD
Used Windows Win32 Disk Imager

## Put SD inside Raspberry
Used Raspberry Pi 3 Model B V1.2

## Remote access to the raspberry
Turn ON the raspberry with a 2A - 5V power supply. Ethernet-link with the LAN router.
Install fing (search for it)
      
      sudo fing

Look for IP raspberry, something like:

      14:44:41 > Host is up:   192.168.1.8
           HW Address:   B8:27:EB:58:3E:B4 (Raspberry Pi Foundation)

Connect to raspberry:

      ssh pi@192.168.1.8

standard password:

      raspberry

Resize to the max size
      sudo raspi-config
      --resize

update

      apt-get update
      apt-get upgrade
      apt-get dist-upgrade
      rpi-update
      dpkg-reconfigure tzdata

change password for pi

      passwd

add password for root

      sudo passwd root

reboot the machine and login again

      ssh pi@192.168.1.8

became root

      sudo su

install python 3.5

      apt-get install build-essential libncursesw5-dev libgdbm-dev libc6-dev 
      apt-get install zlib1g-dev libsqlite3-dev tk-dev
      apt-get install libssl-dev openssl
      cd /root/
      wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz
      tar -zxvf Python-3.5.0.tgz
      cd Python-3.5.0
      ./configure
      make #long command! ~30min
      make install
      python3.5 --version

install telepot

      pip3.5 install telepot datetime requests asyncio selenium PyVirtualDisplay 

install firefox

	  sudo nano /etc/apt/sources.list
	  --add-- deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu trusty main 
	  --add-- deb-src http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu trusty main

	  sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F && sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9BDB3D89CE49EC21 && sudo apt-get update && sudo apt-get install firefox

	  sudo apt-get install openssl gem ruby xvfb

	  sudo apt-get install iceweasel
	  


configure git

      apt-get install git-core
      ssh-keygen -t rsa -b 4096 -C "paolo.cavagnolo@gmail.com"
      eval "$(ssh-agent -s)"
      ssh-add ~/.ssh/id_rsa
      tail ~/.ssh/id_rsa.pub
      --copy and paste it to github/settings--
      git config --global user.email "paolo.cavagnolo@gmail.com"
      git config --global user.name "Paolo Cavagnolo"









      