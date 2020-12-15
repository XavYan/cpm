#!/usr/bin/bash

if [ -n "$SUDO_USER" ]; then
  USER_HOME=/home/$SUDO_USER
else
  USER_HOME=/home/$USER
fi

pip3 uninstall cpm

rm -rf $USER_HOME/.cpm_core
rm /usr/local/bin/cpm

echo "Removed successfully"