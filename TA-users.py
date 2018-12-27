import urllib2
import os, re, sys, glob, time, random

def print_logo():
    clear = "\x1b[0m"
    colors = [34 , 37]

    x = '''
	==================================
	|       TA-Checker Emailes       |
	|     Greetz to n00b's Teams     |
	|--------------------------------|
	|   CoDeD By TA Hacker (@391F)   |
	|--------------------------------|
	'''
    for N , line in enumerate ( x.split ( "\n" ) ):
        sys.stdout.write ( "\x1b[1;%dm%s%s\n" % (random.choice ( colors ) , line , clear) )
        time.sleep ( 0.03 )

def self():
    self.r = '\033[31m'
    self.g = '\033[32m'
    self.y = '\033[33m'
    self.b = '\033[34m'
    self.m = '\033[35m'
    self.c = '\033[36m'
    self.w = '\033[37m'

def Twitter():
    self.m = '\033[35m'
    self.g = '\033[32m'
    userList = raw_input ( self.m + "Enter your users list  ==> " )
    user = open ( userList ).read ( ).splitlines ( )
    for user in user:
        try:
            self.r = '\033[31m'
            self.g = '\033[32m'
            req = "https://twitter.com/users/username_available?username="+user+""
            urllib2.Request ( req )
            response = urllib2.urlopen ( req )
            content = response.read ( )
            if 'Available!' in content:
                print ( self.g + "Available! => {}".format ( user ) )
                with open ( 'USERS.txt' , 'a' ) as Available:
                    Available.write ( user + '\n' )
            else:
                print ( self.r + "Not Available! {}".format ( user ) )
        except:
            pass



if __name__ == '__main__':
    print_logo()
    Twitter()
    self()



