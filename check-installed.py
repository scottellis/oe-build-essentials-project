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
misconfigured = []

print '\nPackages found:\n'

for tool in package_list:
	p = subprocess.Popen(['dpkg', '-l', tool], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	lines = p.stdout.readlines()

	if len(lines) == 6:
		fields = lines[5].split(None, 3)

		if fields[0] == 'ii':
			print lines[5],
		else:
			misconfigured.append(lines[5])
	else:
		not_found.append(tool)


if len(misconfigured) > 0:
	print '\n\nPackages misconfigured:\n'

	for tool in misconfigured:
		print tool,


print '\n\nPackages missing:\n'

if len(not_found) == 0:
	print '<none>\n'
else:
	for tool in not_found:
		print tool

	print '\n'





	
