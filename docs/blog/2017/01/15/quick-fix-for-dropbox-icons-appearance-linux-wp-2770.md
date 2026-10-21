---
title: Quick fix for dropbox icons appearance (Linux)
date: '2017-01-15 20:26:00'
tags:
- Linux
- Tudo
- dropbox
- hardcode-tray
- icons
- inkscape
- papirus
categories:
- Linux
- Tudo
- dropbox
- hardcode-tray
- icons
- inkscape
- papirus
wordpress_id: 2770
original_url: https://craftmind.wordpress.com/2017/01/15/quick-fix-for-dropbox-icons-appearance-linux/
---

# Quick fix for dropbox icons appearance (Linux)

If you tried to use the [hardcode-tray](https://github.com/bil-elmoussaoui/Hardcode-Tray) script to fix the appearance of the tray icons under Linux desktops, you may have noticed that dropbox icons still look the same. This might happen if you install dropbox from [here](https://www.dropbox.com/install-linux), instead from your linux official repository. If this is your case, you can use this easy fix to get the correct icons:

1. First you need to locate the correct dropbox icons within your icon theme installation. In my case, I am using the [Papirus](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme) icon theme. On my Linux, they are located at "/usr/share/icons/Papirus/";
2. Under the Papirus directory, you will find a folder named "22x22/panel", where are the target dropbox icons. Note that I'm using the "22x22" size. Copy the following icons to "~$USER/.dropbox-dist/dropbox-lnx.x86_64-20.3.15/images/hicolor/16x16/status". Note that your dropbox version might be different!
3. Convert the SVG icons to PNG (it got to be PNG, otherwise dropbox will show no icons in the system tray). Use the following command to convert the icons properly:



```plain
inkscape -z -e output.png -w 22 -h 22 input.svg
```

This command will get the job done. But as dropbox use several icons to indicate each state, then you have to use the same command to convert each icon. To get all icons converted at once, use a modified version of this command:

```plain
for i in $(ls *svg); do j=$(echo $i | sed "s,.svg,,g"); inkscape -z -e $j.png -w 22 -h 22 $i; done
```

This command list all SVG files, strip the ".svg" extension; run the inkscape command and done! Note that the icons will be converted to 22px x 22px. If this is not your case, just change the output size accordingly.

Images:

**Before**
![img-alternative-text](../../../../assets/wordpress/2017/01/1484246670.png)
**After**
![img-alternative-text](../../../../assets/wordpress/2017/01/1484246685.png)

Thats all!
