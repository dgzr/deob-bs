# usr/bin/python3
# Bodoamat bro ,cuman tuul ampas gak layak di clone
# Update : selasa Mei 12 2020,- 17:56:55 WIB
from os import system,remove
from sys import argv
import re,argparse

class BashObf(object):
	def __init__(self,file,out):
		self.file = file
		self.out = out
		self.main()
	def main(self):
		try:
			_i = re.sub(r'eval','echo',open(self.file).read())
			with open('tmp.sh','w') as f:
				f.write(_i)
				f.close()
			system(f'sh tmp.sh > {self.out}')
			remove('tmp.sh')
			system('clear')
			print(f'[*] Oke File Saved As => {self.out}')
			_ = input('[*] Print Output ? y/n : ')
			if _.lower() == 'y':
				system(f'cat {self.out}')
			else:
				exit()
		except Exception as eror:
			exit(f'[*] Wrong => {str(eror)}')

try:
	arg = argparse.ArgumentParser(description='Update © 2020 Ezz-Kun\nA Simple Deobfuscated Bash-obfuscate',formatter_class=argparse.RawTextHelpFormatter)
	arg.add_argument('-i','--infile',help='File To Deobfuscated',metavar='')
	arg.add_argument('-o','--output',help='Output File To Save',metavar='')
	gc_ = arg.add_argument_group('Additional')
	gc_.add_argument('-c','--contact',help='contact author',action='store_true')
	gc_.add_argument('-v','--version',help='version tools',action='store_true')
	oo_ = arg.parse_args()
	if oo_.infile and oo_.output:
		BashObf(oo_.infile,oo_.output)
	elif oo_.contact:
		system('xdg-open https://instagram.com/aditiaze_07')
	elif oo_.version:
		print('2.3.0 Update Style © 2020')
	else:
		exit(f"""usage : python {argv[0]} <options>
or python {argv[0]} -h for show all options""")
except EOFError:
	pass
