# Copying the current path (pwd) in the Shell without using the mouse

Those who work a lot in front of the terminal eventually develop the skill of not using the mouse. A good part of my work time is spent in front of the terminal (whether a Linux terminal or OS X), and I rarely use the mouse for anything, except to interact with the graphical interface (like dragging windows or similar tasks). But one situation that always forced me to use the mouse at the terminal was simply copying the current directory path and pasting it into the vi (or vim) editor or somewhere else. To do this, I always used the `pwd` command and used the mouse to copy and paste. Realizing that this was practically the only action that made me take my hands off the keyboard while working with the terminal, I decided to look for a solution. I found one, and it's quite simple. There are basically two commands that can be used for this function. One of them is `pbcopy`, which can be used on OS X, and the other is `xclip`, which can be used on Linux.

## pbcopy on OS X

In the OS X terminal, I found the `copypath` command. This command is built-in, meaning it's part of OS X's toolset, so there's no need to install it.

### Usage

An example of its use is as follows:

```bash
$ pwd | pbcopy
```

Using the keyboard shortcut `CMD+v`, I can paste the path indicated by the `pwd` command into the terminal (or anywhere else):

```bash
/Users/carlos
```

Very simple and functional.

## xclip on Linux

Since I didn't know that `pbcopy` was an internal command on OS X, I tried it in the Linux terminal, and it didn't work. I searched and found the `xclip` command, which has the same function and works very well. However, on the machine I was working on, this command wasn't installed, but nothing prevented me from installing it locally.

### Installation

To install the `xclip` command on a machine from the program's source code, just follow the steps below:

```bash
$ wget -c https://github.com/astrand/xclip/archive/master.zip
$ unzip master.zip
$ cd master/
$ ./bootstrap
$ ./configure --prefix=${PWD}
$ make
$ make install
```

With these commands, you will install `xclip` in the same directory as the program's source code. Two new directories, `bin` and `share`, will be created. The `xclip` executables should be in the first one, and the manuals should be in the second. To add the new commands and manuals to the shell's PATH, just configure your `~/.bashrc` (or `~/.bash_profile` or even `~/.profile`) file by adding the following lines at the end of the file:

```bash
export PATH="/path/to/xclip/bin/directory":${PATH}
export MANPATH="/path/to/xclip/share/man/directory":${MANPATH}
```

With that done, just source the modified file (e.g., `source ~/.bashrc`) or open a new tab in the terminal.

### Usage

Using the `xclip` command in the Linux shell is quite simple. For example, copying the current path and redirecting the output to a text file (`arq.txt`):

```bash
$ pwd | xclip
$ xclip -o > arq.txt
```

To paste the path copied with xclip into the vim editor, just type `SHIFT+p`.

That's it!

## References

* [https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/](https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/)
* [https://langui.sh/2010/11/14/pbpaste-pbcopy-in-mac-os-x-or-terminal-clipboard-fun/](https://langui.sh/2010/11/14/pbpaste-pbcopy-in-mac-os-x-or-terminal-clipboard-fun/)
