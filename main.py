import random ,os ,threading ,random #line:1
import requests #line:2
token =input ("Token User >>> : ")#line:4
def add ():#line:6
    for OO00OOO00O0000O00 in range (int (20 )):#line:7
        O0O000000O00OO0O0 =['8499','1231','1238','4583','8124','3048','5679','9785','4396','8459',]#line:18
        try :#line:19
            O0OOOO0000OOOOO00 =requests .post (f"https://discord.com/api/v9/users/@me/relationships",headers ={"authorization":token },json ={"username":"user","discriminator":random .choice (O0O000000O00OO0O0 )});#line:27
            print (O0OOOO0000OOOOO00 .text )#line:28
        except :pass #line:29
add ()