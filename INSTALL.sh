#!/usr/bin/bash

if [ -n "$SUDO_USER" ]; then
  USER_HOME=/home/$SUDO_USER
else
  USER_HOME=/home/$USER
fi

if [ -e $USER_HOME/cpm_modules ]; then
  rm -rf $USER_HOME/.cpm_core
fi

mkdir $USER_HOME/.cpm_core
chmod 777 $USER_HOME/.cpm_core

file_list="commands cpm.py makefile.py"

for file in $file_list; do
  cp -R $file $USER_HOME/.cpm_core/
done

while IFS= read -r line
do
  if [[ $line == *DIR_PATH* ]]; then
    echo -e "DIR_PATH = \"$USER_HOME/cpm_modules\"" >> $USER_HOME/.cpm_core/.env
  else
    echo $line >> $USER_HOME/.cpm_core/.env
  fi
done < .env

if [ ! -e $USER_HOME/cpm_modules ]; then
  mkdir $USER_HOME/cpm_modules
  chmod 777 $USER_HOME/cpm_modules
fi

pip3 install -r requirements.txt
ln -s $USER_HOME/.cpm_core/cpm.py /usr/local/bin/cpm

echo "Installed successfully! Try cpm -h"
