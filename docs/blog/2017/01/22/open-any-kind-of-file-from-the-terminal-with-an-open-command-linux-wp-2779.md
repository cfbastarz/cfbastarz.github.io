---
title: Open any kind of file from the terminal with an “open” command (Linux)
date: '2017-01-22 11:36:37'
tags:
- .bash_aliases
- BASH
- Linux
- Tudo
- Tutoriais
categories:
- Linux
- Tudo
- Tutoriais
wordpress_id: 2779
original_url: https://craftmind.wordpress.com/2017/01/22/open-any-kind-of-file-from-the-terminal-with-an-open-command-linux/
---

# Open any kind of file from the terminal with an “open” command (Linux)

Mac OS X has a handy script called "open" that lets you open basically any kind of file from command line inside it's default application. For example, if you are navigantig through the terminal and there is a file called "document.pdf" and you need to open it, you can simply do: "open document.pdf" and it will open the document inside the Preview app. Another example is: "open picture.png" and the open command will do the same thing. As simple as that.

But as a Linux user, I was wondering if there is such a command to use from the terminal emulator under my Linux box. If you try the "open" command, it will probably not work, unless the word "open" is an alias pointing to whathever program/script you have. But it happens that we do have the command "xdg-open" built-in the Linux shell that will get the job done. You can invoke, from the command line, the very same commands (but using the "xdg-open” command instead). For example: "xdg-open document.pdf" and it will open the document inside eg., Evince (it will depend on your desktop environment). You can do "xdg-open picture.png" and it will open the picture inside the Eye of Gnome or whaterever picture viewer you have as a default.

If you want to keep things common between the two systems, specially if you are a command line user in both, just make an alias called “open" pointing to "xdg-open”:


```
$ alias open="/usr/bin/xdg-open"
```


In fact, almost every desktop environment has its built-in "open" command, but "xdg-open" is more generic.

That's it!

**Reference:**
<http://https://budts.be/weblog/2011/07/xdf-open-vs-exo-open>
