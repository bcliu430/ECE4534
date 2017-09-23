#!/bin/bash

set -euo pipefail
## based on TAdocs connect_eduroam.pdf

if [ "$EUID" -ne 0 ]; then 
    echo "must be root"
    exit
fi

VTPID="@vt.edu"
NET_PASS=""

cat >> /etc/wpa_supplicant/wpa_supplicant.conf << EOF
ctrl_interface=DIR=/run/wpa_supplicant GROUP=netdev
update_config=1
fast_reauth=1
ap_scan=1
network={
    ssid="eduroam"
    scan_ssid=1
    proto=RSN
    key_mgmt=WPA-EAP
    eap=PEAP
    pairwise=CCMP
    phase1="peaplabel=0"
    phase2="auth=MSCHAPV2"
    anonymous_identity="anonymous@vt.edu"
    identity="$VTPID"
    password="$NETPASS"
}
EOF

service networking stop
wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf

dhcpcd wlan0 || true
dhclient wlan0 || true
service networking start || true

reboot
