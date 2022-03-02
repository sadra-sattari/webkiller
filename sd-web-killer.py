import os
from tkinter import W
from turtle import clear 
import requests
from colorama import Fore , init 
import time

init()

def logo() :
    print(Fore.CYAN + """
    
    5@@@&#G:    .       P&@@@@#&.                                                                       
    Y#@@@@Y            :77G#&&&B                                                                        
    .^~  ~            .~7?5?.                                                                        
            .:   ^^                                                                                    
        .~ :JY~  :.   .                                                                                
        ?:  .                                                                                          
                    .                                                                                   
        :?!. :.                                                                                         
    :7YPYJYY:     .                                                                                    
    :Y5J!7JP5.    .                                                                                    
    .?7~75JPY         .                                                                               
        !?5J~.   .                                                                                      
        :.                                                                                             
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
              ...                                 ..                                                
          .Y#&&@@: ?PPPPGPY:                  :5#&&@& .GGGGGGGG7.GGGGGGGG7 YP555J!:   !#BBG         
         .&@@@@&#: B@@@BG@@@7                :&@@@@&B :@@@@@@@@P^@@@@@@@@P &@@@##@@B  J@@@@.        
         ^@@@@Y    G@@@J^@@@&                ?@@@@7   .G#@@@@BG?.G#@@@@BG7 &@@@::@@@: J@@@&         
         .&@@@&G^  G@@@J^@@@@.               :@@@@&P.   :@@@@:    :@@@@.   &@@@B&@@#  J@@@&         
          :B@@@@@! G@@@?~@@@&.                ^#@@@@@:  :@@@@:    :@@@@.   &@@@@@@@^  ?@@@&         
         .  ^&@@@G G@@@?Y@@@B :##&J          .  !@@@@J  :@@@@.    :@@@&.   #@@@Y&@@#. 7@@@&         
         ~@&&@@@@^ G@@@&@@@&: :@@@# .??????^ J@&&@@@&.  :@@@@.    :@@@&    #@@@~:@@@J ~@@@&         
         .B&&&#P:  !GPPGPY!   .&&&B !@@@@@@# :#&&&#Y.   .PGGP     .GGG5    7GP5. ~G^  :#GGY         
                                    ~@&&&&@B                                                        
                                     ......                                                 sd sttri web killer tool        
                                                                                                    
                                                                                            follow me on instagram : sd._sttri         
                                                                                                    
                                                                                            version : 1.0.0       
                                                                                .~                  
                                                                                 .         ~^    ::.
                                                                                           .    ^&&#
                                                                                                J&&#
                                                                             .??7!^   :         Y##&
                                                                          . .7?J5Y^              .:^
                                                                              .^!^                  
                                                                              .    .    ..:. :!     
                                                                                    ^~JP&&&J::.     
                                                                           .^      :Y#@@@@&5G:      
                                                                                    ~G@@@@&#GG.     
                                                                                 ^BJ !B@#YGP?J..!?P7
                                                                            ..         ::.     :7~7J
                                                                                                 :7?
                                                                          .^^.            7~        

    """)

def clear() :
    os.system("cls")


logo()
print("welcome .......")
time.sleep(1)

os.system("puase")

clear()

logo()

def web_killer() :
  search = [
    'robots.txt',
    'search/',
    'admin/',
    'login/',
    'sitemap.xml',
    'sitemap2.xml',
    'config.php',
    'wp-login.php',
    'log.txt',
    'update.php',
    'INSTALL.pgsql.txt',
    'user/login/',
    'INSTALL.txt',
    'profiles/',
    'scripts/',
    'LICENSE.txt',
    'CHANGELOG.txt',
    'themes/',
    'inculdes/',
    'misc/',
    'user/logout/',
    'user/register/',
    'cron.php',
    'filter/tips/',
    'comment/reply/',
    'xmlrpc.php',
    'modules/',
    'install.php',
    'MAINTAINERS.txt',
    'user/password/',
    'node/add/',
    'INSTALL.sqlite.txt',
    'UPGRADE.txt',
    'INSTALL.mysql.txt'
    'robots.txt',
    'search/',
    'admin/',
    'login/',
    'sitemap.xml',
    'sitemap2.xml',
    'config.php',
    'wp-login.php',
    'log.txt',
    'update.php',
    'INSTALL.pgsql.txt',
    'user/login/',
    'INSTALL.txt',
    'profiles/',
    'scripts/',
    'LICENSE.txt',
    'CHANGELOG.txt',
    'themes/',
    'inculdes/',
    'misc/',
    'user/logout/',
    'user/register/',
    'cron.php',
    'filter/tips/',
    'comment/reply/',
    'xmlrpc.php',
    'modules/',
    'install.php',
    'MAINTAINERS.txt',
    'user/password/',
    'node/add/',
    'INSTALL.sqlite.txt',
    'UPGRADE.txt',
    'INSTALL.mysql.txt' ,
    'administrator/account.brf',
    'administrator.brf','acceso.brf',
    'admin_area/admin.html',
    'pages/admin/admin-login.brf',
    'admin/admin-login.brf',
    'admin-login.brf',
    'bb-admin/index.html',
    'bb-admin/login.html',
    'bb-admin/admin.html',
    'admin/home.html',
    'login.brf'
    ,'modelsearch/login.brf',
    'moderator.brf','moderator/login.brf',
    'moderator/admin.brf',
    'account.brf',
    'pages/admin/admin-login.html',
    'admin/admin-login.html',
    'admin-login.html',
    'controlpanel.brf',
    'admincontrol.brf',
    'modelsearch/admin.brf',
    'admincontrol/login.brf',
    'adm/admloginuser.brf','admloginuser.brf',
    'admin2.brf',
    'admin2/login.brf',
    'admin2/index.brf',
    'usuarios/login.brf',
    'adm/index.brf',
    'adm.brf',
    'affiliate.brf',
    'adm_auth.brf',
    'memberadmin.brf',
    'administratorlogin.brf',
    'cpanel',
    'cpanel.php',
    'cpanel.html',
    ]
  url = input("\r\nEnter your URL: ")
  for page in search:
        req = requests.get( "https://"+ url + "/" + page)
        if req.status_code == 200:
            print( Fore.GREEN + " [+] " + Fore.BLUE + "   page is ok " +url + "/"+ page )
            with open('test.txt' , W ) as f:
                f.write(url)
        else:
            print( Fore.RED+ " [-]" +  Fore.RED + "   page is not ok " +url + "/" + page )

web_killer()

os.system("puase ")