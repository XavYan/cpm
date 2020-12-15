# C++ Project Manager
A simple program who lets you to concentrate more in coding
but less in project structure.

- Create projects with basic structure using `cpm --init PROJECT_NAME`.
- Add classes with `cpm -a CLASS`, both templates and non templates.
- Remove classes you don't need with `cpm -R CLASS`.
- Run the project without leave the executable after it. Run `cpm -r` to test all your project like an interpreter!
- If you want to make an executable, with `cpm -b` is all done!

All of this with a Makefile auto-configuration!

## Dependencies
To use this program, you need:

- Python 3.8.5 or upper.
- pip 20.0.2 or upper.

## Installation
To install this project, simply clone this repository:
```bash
$ git clone https://github.com/XavYan/cpm
```
Go inside `cpm` folder and execute:
```bash
$ sudo ./INSTALL.sh
```
Just that! Now you can verify the installation making `cpm --version`.

## Updating
If you want to update this project, clone again this repository, and execute `sudo ./UNINSTALL`
and `sudo ./INSTALL` respectively. This will remove and install the new version.

Full commands:
```bash
$ git clone https://github.com/XavYan/cpm /tmp/cpm_cloned
$ cd /tmp/cpm_cloned
$ sudo ./UNINSTALL.sh
$ sudo ./INSTALL.sh
```

Test new version with:
```bash
$ cpm --version
```

## Uninstallation
If you want to uninstall this project, use:
```bash
$ sudo ./UNINSTALL.sh
```
It will do all work for you!

## Usage
All usage of this program is with a terminal a `cpm` command! To see full functionality use `cpm -h`.

## Contributing
If you think this is a cool tool and want to **contribute** your grain of sand, feel free to make an issue with possible
enhancenments or even with a PR of your ideas.

In the same way, if you have found **problems or bugs** using this program I would be so thankful if you make an issue
explaining what happened.