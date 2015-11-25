# Hello PyQt

Steps
* (Open a shell and make sure `python` 2.x and `pip` are in the path)
* `pip install virtualenv` (may need to run as root with sudo)
* `virtualenv --no-site-packages --always-copy env`
* `. env/bin/activate` (replace `bin` with `Scripts` on Windows systems)
* ~~`pip install --allow-external sip --allow-unverified sip sip`~~ (this failed)
* `wget http://sourceforge.net/projects/pyqt/files/sip/sip-4.17/sip-4.17.zip` (download file)
* `unzip sip-4.17.zip` (extract conents)
* `cd sip-4.17`
* `python configure.py --incdir=../env/include/python2.7`
* `make` (at this point I got `"c:\PROGRAM: Interrupt/Exception caught (code = 0xc00000fd, addr = 0x4227d3)` which I blame on Windows, so I switched to my Debian vm)
	```
	gcc -c -pipe -fPIC -O2 -w -DNDEBUG -I. -I/usr/include/python2.7 -o siplib.o siplib.c
	siplib.c:20:20: fatal error: Python.h: No such file or directory
	 #include <Python.h>
						^
	compilation terminated.
	Makefile:29: recipe for target 'siplib.o' failed
	make[1]: *** [siplib.o] Error 1
	make[1]: Leaving directory '/home/user/nerdz/jrq-hello-qt/sip-4.17/siplib'
	Makefile:3: recipe for target 'all' failed
	make: *** [all] Error 2
	```
	I fixed this by running `sudo apt-get install python-dev`
* `make install` (now I can see `env/lib/python2.7/site-packages/sip.so` installed)
* 



  

