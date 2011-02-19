  oe-build-essentials
=======

A simple meta-package to install the OE requirements for OpenEmbedded 
development on an Ubuntu workstation.

There is an accompanying python script to check the installed packages on
your workstation.

Tested with Ubuntu 10.10

Checkout
-------

Checkout the project from github or just copy the files you want.

    $ git clone git://github.com/scottellis/oe-build-essentials-project.git
    

Usage
-------

If you just want to check for missing packages, you can use the check-installed.py
script. Just run it with no arguments. You should hopefully get a listing like this.

	scott@quad:~/examples/oe-build-essentials-project$ ./check-installed.py 

	Packages found:

	ii  git                1:1.7.1-1.1ubuntu0.1        fast, scalable, distributed revision control system
	ii  git-doc            1:1.7.1-1.1ubuntu0.1        fast, scalable, distributed revision control system (documentation)
	ii  subversion         1.6.12dfsg-1ubuntu1.1       Advanced version control system
	ii  gcc                4:4.4.4-1ubuntu2            The GNU C compiler
	ii  g++                4:4.4.4-1ubuntu2            The GNU C++ compiler
	ii  make               3.81-8                      An utility for Directing compilation.
	ii  libc6-dev          2.12.1-0ubuntu10.2          Embedded GNU C Library: Development Libraries and Header Files
	ii  dpkg-dev           1.15.8.4ubuntu3.1           Debian package development tools
	ii  patch              2.6-2ubuntu1                Apply a diff file to an original
	ii  help2man           1.38.2                      Automatic manpage generator
	ii  diffstat           1.53-1                      produces graph of changes introduced by a diff file
	ii  texi2html          1.82-1                      Convert Texinfo files to HTML
	ii  texinfo            4.13a.dfsg.1-5ubuntu1       Documentation system for on-line information and printed output
	ii  libncurses5-dev    5.7+20100626-0ubuntu1       developer's libraries and docs for ncurses
	ii  cvs                1:1.12.13-12ubuntu1         Concurrent Versions System
	ii  gawk               1:3.1.7.dfsg-5              GNU awk, a pattern scanning and processing language
	ii  python-dev         2.6.6-2ubuntu2              header files and a static library for Python (default)
	ii  python-pysqlite2   2.6.0-1                     Python interface to SQLite 3
	ii  unzip              6.0-4                       De-archiver for .zip files
	ii  chrpath            0.13-2build2                Tool to edit the rpath in ELF binaries
	ii  ccache             2.4-17ubuntu2               Compiler results cacher, for fast recompiles

	Packages missing:

	<none>


The meta-package oe-build-essentials.deb can be used to install all or just the
missing packages on your Ubuntu system. 

If you did a git checkout of this project, the you could also customize the
package by editing the oe-build-essentials/DEBIAN/control file and rebuilding
the deb file.

If you are customizing, then after your edits, run the following command to 
rebuild the deb.

    $ cd oe-build-essentials-project
    $ dpkg-deb -b oe-build-essentials

To install the oe-build-essentials.deb run the following:

    $ sudo dpkg -i oe-build-essentials.deb
    $ sudo apt-get -f install

The apt-get call does the real installation and will give you a list of what's
going to happen and a chance to abort before it does anything.

Package List
-------

The list of packages come from the Gumstix recommendations here
http://www.gumstix.org/software-development/open-embedded/61-using-the-open-embedded-build-system.html

Here's the list

    git
    git-doc
    subversion
    build-essential (gcc, g++, make, libc6-dev, dpkg-dev)
    patch
    help2man
    diffstat
    texi2html
    texinfo
    libncurses5-dev
    cvs
    gawk
    python-dev
    python-pysqlite2
    unzip
    chrpath
    ccache

I also added ckermit as a RECOMMENDS because that's what I use.

