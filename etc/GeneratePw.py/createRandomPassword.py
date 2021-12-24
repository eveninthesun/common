import string
import random
import datetime

# init
LOGO = '''
 _____                      _         _    _            _____               
|  ___|                    (_)       | |  | |          /  ___|              
| |__  __   __  ___  _ __   _  _ __  | |_ | |__    ___ \ `--.  _   _  _ __  
|  __| \ \ / / / _ \| '_ \ | || '_ \ | __|| '_ \  / _ \ `--. \| | | || '_ \ 
| |___  \ V / |  __/| | | || || | | || |_ | | | ||  __//\__/ /| |_| || | | |
\____/   \_/   \___||_| |_||_||_| |_| \__||_| |_| \___|\____/  \__,_||_| |_|

'''
class pwConfig : 
    def onlyUpperCase() : 
        return string.ascii_uppercase
    
    def onlyLowerCase() : 
        return string.ascii_lowercase
    
    def commonCase() : 
        return string.printable.strip()

def generatePW(count, passwordLength, config) : 
    pwList = list()
    
    for i in range(count) : 
        pwTemp = ''
        for j in range(passwordLength) : 
            single = random.choice(config)
            pwTemp += single
        pwList.append(pwTemp)
        
    return pwList

def savefile(pwList, format) : 
    time = datetime.datetime.now()
    f = open('passwordList.{}'.format(format), 'w')
    
    for pw in pwList :
        f.write(pw + '\n')
    
    f.close()
    
    return -1

# main
if __name__ == '__main__' : 
    print(LOGO)
    
    count = int(input('how many create password? : '))
    
    config = input('set password config : ')
    
    if config == '1' : config = pwConfig.commonCase()        
    elif config == '2' : config = pwConfig.onlyUpperCase()
    elif config == '3' : config = pwConfig.onlyLowerCase()
    
    passwordLength = int(input('set password length : '))
    
    fileformat = input('file format(txt, csv) : ')
    
    if fileformat == 'csv' : config.replace(',', ''); print(config)
    
    pwList = generatePW(count, passwordLength, config)
    
    savefile(pwList, fileformat)