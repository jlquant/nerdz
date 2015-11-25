# Hello PyQt

## Setup virtual environment
* (Open a shell and make sure `python` 2.x and `pip` are in the path)
* `pip install virtualenv` (may need to run as root with sudo)
* `virtualenv --no-site-packages --always-copy env`
* `. env/bin/activate` (replace `bin` with `Scripts` on Windows systems)

## Install sip
* ~~`pip install --allow-external sip --allow-unverified sip sip`~~ (this failed; pip can't actually install this for us)
* `wget http://sourceforge.net/projects/pyqt/files/sip/sip-4.17/sip-4.17.zip` (can download .tar.gz instead if you like)
* `unzip sip-4.17.zip` (extract conents)
* `cd sip-4.17`
* `python configure.py --incdir=../env/include/python2.7`
* `make` (at this point I got `"c:\PROGRAM: Interrupt/Exception caught (code = 0xc00000fd, addr = 0x4227d3)` which I blame on Windows, so I switched to my Debian vm)
  But then I got this:
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
* `make install` (now I can see `env/lib/python2.7/site-packages/sip.so` installed and running `which sip` shows the path to the binary in the virtualenv)
* `cd ..` (leave build directory -- feel free to move/delete that now as it shouldn't be needed any more since it's now installed in the virtual environment)

## Install Qt5
* `wget http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/PyQt-gpl-5.5.1.tar.gz`
* `tar xf PyQt-gpl-5.5.1.tar.gz`
* `cd PyQt-gpl-5.5.1/`
* `python configure.py` but got the following error due to not having Qt installed yet:
  ```
  Querying qmake about your Qt installation...
  qmake: could not exec '/usr/lib/x86_64-linux-gnu/qt4/bin/qmake': No such file or directory
  Error: PyQt5 requires Qt v5.0 or later. You seem to be using v3. Use the
  --qmake flag to specify the correct version of qmake.
  ```
* `wget http://download.qt.io/official_releases/qt/5.5/5.5.1/qt-opensource-linux-x64-5.5.1.run` (download Qt)
* ` chmod +x ./qt-opensource-linux-x64-5.5.1.run` (make executable)
* `./qt-opensource-linux-x64-5.5.1.run` (run installer -- needed to have X/GUI to run)
* (step through installation wizard -- clicked "skip" during registration part, did not launch QtCreator at the end)
* At this point I ran into a problem due to not having `qmake`.
  I tried to fix this by running `sudo apt-get install libqt4-dev` but that was only for Qt4 not Qt5 and isn't actually the package containing qmake.
  So I tried again (after removing the other) with
  `sudo apt-get install libqt5core5a` which added [some files](https://packages.debian.org/sid/amd64/libqt5core5a/filelist) including a config for Qt5.
  but I also needed `sudo apt-get install qt5-qmake` and finally to actually use Qt5, `export QT_SELECT="qt5"`
* Now when I run `python configure.py ` I get `Error: Failed to determine the detail of your Qt installation. Try again using the --verbose flag to see more detail about the problem.`
  then with `--verbose` I got `qtdetail.cpp:1:28: fatal error: QCoreApplication: No such file or directory` so I think I'm still missing some Qt5 packages. I ran `sudo apt-get install libqt5designer5` (which also caused libqt5gui5 to be installed since it was a dependency)
* It took me a long time to get this working...would've been much easier to just load the PyQt package from apt-get :S
  Since the Qt5 installer put the files in my home directory I had to tell the compiler (g++) and linker (ld) about them.
  I ended up running
  `export CPLUS_INCLUDE_PATH=/home/user/Qt5.5.1/5.5/gcc_64/include/QtCore:/home/user/Qt5.5.1/5.5/gcc_64/include`
  and
  `export LIBRARY_PATH=/home/user/Qt5.5.1/5.5/gcc_64/lib`
  to make it finally configure OK.
* `make && make install` but this failed with `make[1]: /usr/lib/x86_64-linux-gnu/qt5/bin/moc: Command not found`
  so I ran `sudo apt-get install qtbase5-dev-tools` and ran again.
