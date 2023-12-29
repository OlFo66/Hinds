![Maintenance](https://img.shields.io/maintenance/yes/2030)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/datetime)
![](https://img.shields.io/badge/License-Beerware-yellow)

<img src="https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0b5061df29d55a92d945_full_logo_blurple_RGB.svg" data-canonical-src="https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0b5061df29d55a92d945_full_logo_blurple_RGB.svg" width="600" height="100" />

# 
# :warning: Disclaimer :warning:
:warning:Alfred is for educational purpose only!<br>
:warning:️I am not responsible for any damage caused by the usage of this tool.<br>
# What?
alfred.py is a data exfiltration tool using Discord channel webhook.
# How to use it?
* Rename .webhook.sample as .webhook & write the url of the channel's webhook the script sends data to.
* You can call the script with 2 different options:
  * -f \<FULLPATH/FILENAME2> \<FULLPATH/FILENAME2> ... : will send base64 encoded filename1, filename2, etc.
  * -c \<COMMANDLINE>              : will send stdout of the provided commandline if return code is 0.

Note: if you send file(s), the script first send the number of chunks then send the encoded file.

![discord-discussion2.png](./discord-discussion.png)

# To do
- :black_square_button: Add proxy HTTP configuration
- :black_square_button: Add more control (variable)
- :white_square_button: Take a beer.<br>
- :black_square_button: Repeat.

## License
```
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * I wrote this file.  As long as you retain this notice you
 * can do whatever you want with this stuff (for educational purpose!). 
 * If we meet some day, and you think this stuff is worth it, you can buy me a beer in return.   
 * Olivier FONT
 * ----------------------------------------------------------------------------
 */
```
