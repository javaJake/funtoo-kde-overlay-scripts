#!/bin/bash

set -e
eval `keychain --eval --agents ssh id_rsa`
cd /home/jacob/funtoo-git/gentoo && git pull
cd /home/jacob/funtoo-git/gentoo-kde-overlay && git pull
/home/jacob/kde-funtoo-scripts/scripts/merge-kde-staging.py
