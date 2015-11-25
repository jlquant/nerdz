# Hello PyQt

Steps
* (Open MinGW/shell/terminal and make sure python is in the path)
* `pip install virtualenv`
* `virtualenv --no-site-packages --always-copy env`
* `. env/Scripts/activate` (`Scripts` may be `bin` on non-Windows systems)
* ~~`pip install --allow-external sip --allow-unverified sip sip`~~ (this failed)
* `wget http://sourceforge.net/projects/pyqt/files/sip/sip-4.17/sip-4.17.zip` (download file)
* `unzip sip-4.17.zip` (extract conents)
* `cd sip-4.17`
* `python configure.py --incdir=../env/include/python2.7`
* `make` (at this point I got `"c:\PROGRAM: Interrupt/Exception caught (code = 0xc00000fd, addr = 0x4227d3)` which I blame on Windows, so I switched to my Debian vm)
* `make install`

  

