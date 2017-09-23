#!/bin/bash
## modified based on Lewiscowles1986/rPi3-ap-setup.sh and raspi_APconfig.txt
## To get a Raspberry Pi configured as an Access Point from a fresh Raspbian Jessie install:

## Make sure you are connected to the internet, and open a terminal

if [ "$EUID" -ne 0 ]
    then echo "Must be root"
    exit
fi
APSSID="Team16"
APPASS=

apt-get remove --purge hostapd -yqq
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install dnsmasq hostapd


cat > /etc/hostapd/hostapd.conf <<EOF
interface=wlan0
ssid=your_ssid_here
channel=6
hw_mode=g
ignore_broadcast_ssid=0
wpa=2
ieee80211n=1
macaddr_acl=0
auth_algs=1
wpa_key_mgmt=WPA-PSK
wpa_passphrase=your_password_here
wpa_group_rekey=86400
rsn_pairwise=CCMP
wme_enabled=1
EOF

echo "" > /etc/network/interfaces
cat > /etc/hostapd/hostapd.conf <<EOF
allow-hotplug wlan0
iface wlan0 inet static
	address 192.168.1.100
	netmask 255.255.255.0
	network 192.168.1.0
	broadcast 192.168.1.100
	gateway 192.168.1.100
EOF

sudo service dhcpcd restart
sudo ifdown wlan0
sudo ifup wlan0

## * Find the line with '#DAEMON_CONF=""' and replace it with:
## DAEMON_CONF="/etc/hostapd/hostapd.conf"
sed -i -- 's/#DAEMON_CONF=""/DAEMON_CONF="\/etc\/hostapd\/hostapd.conf"/g' /etc/default/hostapd


## * Find the line with "DAEMON_CONF=" and replace it with:
## DAEMON_CONF=/etc/hostapd/hostapd.conf
sed -i -- 's/#DAEMON_CONF=""/DAEMON_CONF="\/etc\/hostapd\/hostapd.conf"/g' /etc/init.d/hostapd
sudo mv -r /etc/dnsmasq.conf /etc/dnsmasq.conf.orig

## sudo nano /etc/dnsmasq.conf
## * Put the following in the file:
sudo touch /etc/dnsmasq.conf
cat > /etc/dnsmasq.conf << EOF
interface=wlan0
dhcp-range=192.168.1.100,192.168.1.110,12h
bind-interfaces
EOF

sudo service hostapd start
sudo service dnsmasq start

## * The following will make the services run automatically on boot:
sudo update-rc.d hostapd enable
sudo update-rc.d dnsmasq enable

## * Finally, reboot with "sudo reboot" and you should be able to connect to the Pi with a properly configured Wifly
## * Download the server_echo.py file from Canvas and run it, and it will echo whatever is sent to it via the Wifly
