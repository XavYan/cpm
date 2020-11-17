USER_HOME=/home/xavier

if [ -e $USER_HOME/cpm_modules ]; then
  rm -rf $USER_HOME/.cpm_core
fi

mkdir $USER_HOME/.cpm_core
chmod 777 $USER_HOME/.cpm_core

file_list="commands cpm.py makefile.py .env"

for file in $file_list; do
  cp -R $file $USER_HOME/.cpm_core/
done

if [ ! -e $USER_HOME/cpm_modules ]; then
  mkdir $USER_HOME/cpm_modules
fi

pip3 install python-decouple
ln -s $USER_HOME/.cpm_core/cpm.py /usr/local/bin/cpm