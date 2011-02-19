#!/usr/bin/env python
#
# Checks the dpkg status of the OE required packages for an Ubuntu workstation.
#

import subprocess

package_list = [ 'git', 'git-doc', 'subversion', 'gcc', 'g++', 'make', 'libc6-dev',
		'dpkg-dev', 'patch', 'help2man', 'diffstat', 'texi2html', 'texinfo', 
		'libncurses5-dev', 'cvs', 'gawk', 'python-dev', 'python-pysqlite2',
		'unzip', 'chrpath', 'ccache' ]


not_found = []

print '\nPackages found:\n'

for tool in package_list:
	p = subprocess.Popen(['dpkg', '-l', tool], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	lines = p.stdout.readlines()

	if len(lines) == 6:
		print lines[5],
	else:
		not_found.append(tool)

print '\nPackages missing:\n'

if len(not_found) == 0:
	print '<none>\n'
else:
	for tool in not_found:
		print tool

	print '\n'






	
