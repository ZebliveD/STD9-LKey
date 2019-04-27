from Colors import bcolors
import Global

def Banner():
	print ' _______ '
	print '< STD9-LKey >'
	print ' ------- '
	print '           ffffff'
	print '          f  ff  f'
	print '          f f  f f  -  -  - - --- [STD9-LKey]' 
	print '          f  ff  f   -  -  - -' 
	print '           ff  ff'
        print '            f  f'
        print '            f  f'
        print '            f  f'
        print '            f  f'
        print '             f f'
        print '              f'
        print ' '*10 + '--=' + bcolors.OKBLUE + '[' + bcolors.ENDC + bcolors.BOLD + 'KeyLogger' + bcolors.ENDC
	print ' '*7 + '--+--=' + bcolors.OKBLUE + '[' + bcolors.ENDC + 'Version : ' + bcolors.OKGREEN + bcolors.BOLD + Global.VERSION + bcolors.ENDC + bcolors.ENDC	
	print ' '*7 + '--+--=' + bcolors.OKBLUE + '[' + bcolors.ENDC + 'Coder   : ' + bcolors.OKGREEN + bcolors.BOLD + Global.CODER + bcolors.ENDC + bcolors.ENDC	
	print ' '*10 + '--=' + bcolors.OKBLUE + '[' + bcolors.ENDC + 'github  : ' + bcolors.OKGREEN + bcolors.BOLD + Global.GITHUB + bcolors.ENDC + bcolors.ENDC	
	print ' \n'
