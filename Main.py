import colorama,requests
from colorama import init
init()
import websocket
import json
import ssl
import time,os
import threading
from datetime import datetime, timezone
import pandas as pd
import numpy as np
import math
import matplotlib
import traceback
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import math
from requests import session


from matplotlib.patches import Rectangle
TOKEN_ = os.environ.get("TELEGRAM_BOT_TOKEN")
print(TOKEN_)
CHAT_ID=os.environ.get("TELEGRAM_CHAT_ID")
print(CHAT_ID)
def AUTO_RELUNCH():
    time.sleep(21000)
    while True:
        try:
            dss={"workflow":".github/workflows/run-bot.yml",
                "branch":"main",
                "show_workflow_tip":""
                }
            headers={
                "accept":"*/*",
              #  "accept-encoding":"gzip, deflate, br, zstd",
                "accept-language":"fr-FR,fr;q=0.9,ar-DZ;q=0.8,ar;q=0.7,en-US;q=0.6,en;q=0.5",
                "baggage":"session.id=7704c922-d471-401a-a49d-341cc347c7c5",
                "content-length":"369",
                "cookie":"_octo=GH1.1.929647033.1783641681; _device_id=90a830c932a17d311d8cc595ca371818; datadome=DloIDqvQsMLo__CffHftNY2G_hhG6ShTEdq75~h_Imub~o~NrfEjcXiPQOcwobdXQFEKVw6fCb7GIRLDkHAfaeHwAg2jGz~g45C~FVZeXep~vhxzvhicRyfLrmnFCdW8; cpu_bucket=lg; preferred_color_mode=light; tz=Africa%2FLagos; saved_user_sessions=211106746%3A1mnBBPD0qWO4O4pZanjvqZDl_he_KkT-_mKM_dBBcQ3sU11I; user_session=1mnBBPD0qWO4O4pZanjvqZDl_he_KkT-_mKM_dBBcQ3sU11I; __Host-user_session_same_site=1mnBBPD0qWO4O4pZanjvqZDl_he_KkT-_mKM_dBBcQ3sU11I; tz=Africa%2FLagos; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=renaiania233; ui_eligible=true; last_write_ms=1792623745691; _gh_sess=HdFXwSmTijhzpL%2BqDh0zQNbnhQI%2FXGUERASbnFLFytrTT1ZtMEmPlSf6HuV6U9NkTe3djHU4vLsw5eeauRf06n4bJRfYfTmjfndwViAUAeRJE276229hKClIrrzKXJd1%2BJHHfSlMnC5nlTL7%2Bn6thK2%2FGLijMeSXbOaKAkl1jzzsf3KUHMKKo79NHCztq%2Fd3FjDIIWCKVYFesdvixC3OIOQuNGKnU1MAfNrTCU2wKiFpLHbyflrDIF%2BNahNZoxC4BFvAENMHUVzBze%2BEOepG0hgCSCaFygTH85Qg3rDvCLdkxli6SUPe%2F4hty69MYBBqgxZXkqI5qLTzMZ%2FskoZzkxG91M6%2Fn%2FKM0J745phgN1QjpzRffUP0uiZ0WP8TsnmwOS83UN14LYoszKDMa0B1B%2Fl90vg6fXZkNO7fj6EmjxuNn95e49HGyNk7EE7Zo8%2BLOfoPa67IWE7Ky%2Bdm451lDrVXvmqCUVyf6uYwD26thjA%2FEHB86azxyrQBwalBYbqPYSSmBWazB09Jqv0bpiDU9nl11xWyrjTVlx2rzVQgKRgbV5y8YLMa07NlSyXEPcLj%2F5%2BQA3AfedvBU2ED7nDtQ87VKgjilhTOUmYL2KVDmFRvUtyHpAoiUT90dIiZjju8NO%2B3JNIVQ4EHYAQg--35In7dNGjCyR0%2B5w--RlV%2FnLUJW7yfJEDmC7eMDw%3D%3D; _dd_s_v2=id=7704c922-d471-401a-a49d-341cc347c7c5&created=1792620998728&expire=1792624749306&c=0",
                "github-verified-fetch":"true",
                "origin":"https://github.com",
                "priority":"u=1, i",
                "referer":"https://github.com/renaiania233/Grambot/actions/workflows/run-bot.yml",
                "sec-fetch-dest":"empty",
                "sec-fetch-mode":"cors",
                "sec-fetch-site":"same-origin",
                "traceparent":"00-000000000000000086ac5083845e1425-12e51a4c09cbb621-01",
                "tracestate":"dd=s:1;o:rum",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
                "x-fetch-nonce":"v2:39bae150-42db-fd29-0b00-7bebd8132511",
                "x-github-client-version":"bbfbb7e891aed5add378e5888804c668fff1c288",
                "x-requested-with":"XMLHttpRequest"


            }
            cxcx = requests.post("https://github.com/renaiania233/Grambot/actions/manual",headers=headers,data=dss,allow_redirects=False)
            if  "actions/runs/" in cxcx.headers["Location"]:
                success=True
                REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n SERVER RUNNING : OK\nRENEWED:NOW  \n")
                return
            else:
                REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n ERROR RELAUNCHING SERVER!, \nUnexpected error occured !  \n")
        except Exception as err:
            print(err)
            time.sleep(30)
            continue
zhk = threading.Thread(target=AUTO_RELUNCH)
zhk.start()
def GITHUB_FILE(update=False,data=None,name=None):
    if update==True:
        try:
            p=session()
            p.headers={}
            p.headers.update({
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             #   "accept-encoding":"gzip, deflate, br, zstd" ,
                "accept-language":"fr-FR,fr;q=0.9,ar-DZ;q=0.8,ar;q=0.7,en-US;q=0.6,en;q=0.5",
                "cache-control":"max-age=0",
                "cookie":"_octo=GH1.1.929647033.1783641681; _device_id=90a830c932a17d311d8cc595ca371818; datadome=DloIDqvQsMLo__CffHftNY2G_hhG6ShTEdq75~h_Imub~o~NrfEjcXiPQOcwobdXQFEKVw6fCb7GIRLDkHAfaeHwAg2jGz~g45C~FVZeXep~vhxzvhicRyfLrmnFCdW8; cpu_bucket=lg; preferred_color_mode=light; tz=Africa%2FLagos; saved_user_sessions=211106746%3A1mnBBPD0qWO4O4pZanjvqZDl_he_KkT-_mKM_dBBcQ3sU11I; user_session=1mnBBPD0qWO4O4pZanjvqZDl_he_KkT-_mKM_dBBcQ3sU11I; __Host-user_session_same_site=1mnBBPD0qWO4O4pZanjvqZDl_he_KkT-_mKM_dBBcQ3sU11I; tz=Africa%2FLagos; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=renaiania233; ui_eligible=true; last_write_ms=1792609408195; _dd_s_v2=isExpired=1&c=0; _gh_sess=ncOWUmds%2F1bnLRX%2BR7gRbFrVwThFK3%2B0FB4LSFkkfUiHQ6WNiGa6sCiifkYfCSJ%2Bwl5pvPyADPrV5uz164j4lN5EYZxKENRoXjqCln0q%2BfxXekPrwKHNQHD28ugqiqpMyWI4OxMpLjPRh%2BEmyOSxTL%2FH74shvAcLNuAK42uYzsMNiDnwPCCDk31wiT0r%2BKp0PwuEq1vuhQJIfANeMDHm9FUev5m%2FM3o%2BQgve9cmeSSH%2F3dGT1fKYDbd9I7Zhl0JFW9OqLrNnnmTAwH%2FsolID%2FKAOUFkE%2Fb6i5Ai6fALJLab9c9G5gOymHrEThEuyuFQ%2Fa%2B3KOSw49RnBhsImsut6z8GG4mYzZvJXNgB4AAaqCvRZKNQsH8EPIrS4LTitw3bYzhjty96NLQ56g1gUTGvjNMNoFlkNrFd9wY0FUXs6qibu7LJ0TukHn9%2Bzdd1ALYn4n9wIXgdSgn7c5b%2Bfj%2FkqRnZHECps4mjckYvWToGQCE%2BqYneR6nPc9O2b6Q%2BEQNAs6ctQ%2F9RibLRkaCpBgmhztNbq6rzgHx6p--puF6E%2BK8I5p1fH%2FI--4ookhcE%2BD21j%2B1KY4ypLmA%3D%3D",
                "priority":"u=0, i",
                "sec-fetch-dest":"document",
                "sec-fetch-mode":"navigate",
                "sec-fetch-site":"none",
                "sec-fetch-user":"?1",
                "upgrade-insecure-requests":"1",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
            })

            html=p.get("https://github.com/renaiania233/Grambot/edit/main/{}.json".format(name)).text
            st=html.find("currentOid")+12
            end =st+40
            token=html[st:end]
            print("TOKENNN : {}".format(token))
            p.headers.update({
                
            "accept":"application/json",
            "accept-encoding":"gzip, deflate, br, zstd",
            "accept-language":"fr-FR,fr;q=0.9,ar-DZ;q=0.8,ar;q=0.7,en-US;q=0.6,en;q=0.5",
            "baggage":"session.id=3078d495-75f9-4034-8eca-a541fe7e8c3b",
            "content-length":"1535",
            #"cookie":"_octo=GH1.1.929647033.1783641681; _device_id=90a830c932a17d311d8cc595ca371818; datadome=DloIDqvQsMLo__CffHftNY2G_hhG6ShTEdq75~h_Imub~o~NrfEjcXiPQOcwobdXQFEKVw6fCb7GIRLDkHAfaeHwAg2jGz~g45C~FVZeXep~vhxzvhicRyfLrmnFCdW8; cpu_bucket=lg; preferred_color_mode=light; tz=Africa%2FLagos; saved_user_sessions=211106746%3A1mnBBPD0qWO4O4pZanjvqZDl_he_KkT-_mKM_dBBcQ3sU11I; user_session=1mnBBPD0qWO4O4pZanjvqZDl_he_KkT-_mKM_dBBcQ3sU11I; __Host-user_session_same_site=1mnBBPD0qWO4O4pZanjvqZDl_he_KkT-_mKM_dBBcQ3sU11I; tz=Africa%2FLagos; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=renaiania233; ui_eligible=true; last_write_ms=1792605199185; _gh_sess=8SnWBxKOIhQDsGf2pDE1%2Fkmylx01qNEZLTSRStdcD%2FsIMPHnP0OKohxIf6H9wnExwruX8EC4M5nrfO68uIFI5gyOnrU37%2F21cB3y1xudxKZW4S%2Fgo48OXuwJ5LF1e6D1mbj27W3l%2FnFJk7FFELe%2BlardovXHQJO14Uoha%2F3v1BA0esuJxwvPL%2BpJHAi5qRtUZeAo2Pad%2B1x%2FeVK%2FOcgprhBROuyZtJaVeknOv11RzN5%2FwNxz%2Fha%2FVdFUUst1h%2FK3bslcibaTNo%2FfwsHqCoGGSscWT2iKsM8cn1MiKRYcC3qvB93zwUgag0%2FD6lZhDcmXgWs4ooVswaiQ0NzBQxewO7KDF73lt30BSUIpKLbd%2FXykim%2Bz14Z3CI30tWdM3kJxCOo7pKTnCKVY%2F8BlPOHQl1PQ51ZW8tUDOMvXsGB0z8Y0Gsjy4CfaEtkWRQr7nz%2Bbk7xeJD5GVNPyDvn1O46IdMdUCKG%2BUV4Q%2BhyKX0iDZkAzbtsw6zgbBfYOi0cgygU8Uf8uRjM4Sm66KekwM3OgjVJy19hd6AaXcQTS%2BjIiLadQySiPithdOY1yFGb%2BbTNqfLMOtQVpTXnWkmnHmjdN6zAaRuz3Bg5J4lM56mIZeqq6GOdQovrVmSSAbs45KELzTv5Kzzx3BKF9kkYsAZ55Z8ppB1yvTAn%2FJ1Fgqesduis1Umivo3nNmyrGDsCO3v9i--AS6Wte4hG26SFn4S--bMp9gfvedQ1yw2FE%2BzkfOg%3D%3D; _dd_s_v2=id=3078d495-75f9-4034-8eca-a541fe7e8c3b&created=1792602651755&expire=1792606119769&c=0",
            "github-verified-fetch":"true",
            "origin":"https://github.com",
            "priority":"u=1, i",
            "referer":"https://github.com/renaiania233/Grambot/edit/main/{}.json".format(name),
            "sec-ch-ua-mobile":"?0",
            "sec-fetch-dest":"empty",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "traceparent":"00-0000000000000000e91f28c7f68afa09-591aba609b8fc7d7-01",
            "tracestate":"dd=s:1;o:rum",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
            "x-fetch-nonce":"v2:b13d9779-3075-420c-a01c-00f2ff2303c7",
            "x-github-client-version":"8025b1b93e54dea8480f99977820ff685f4621d3",
            "x-github-ui-service":"true",
            "x-requested-with":"XMLHttpRequest"

            })
            payload={
            "message":"Update {}.json".format(name),
            "placeholder_message":"Update {}.json".format(name),
            "description":"",
            "commit-choice":"direct",
            "target_branch":"main",
            "quick_pull":"",
            "guidance_task":"",
            "commit":token,
            "same_repo":"1",
            "pr":"",
            "content_changed":"true",
            "filename":"{}.json".format(name),
            "new_filename":"{}.json".format(name),
            "value":data
            }
        
            test= p.post("https://github.com/renaiania233/Grambot/tree-save/main/{}.json".format(name),data=payload).json()["data"]["commitQuorumPollPath"]
            print(test)
            return(True)
        except Exception as e:
            REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n ERROR UPDATING_FILE: {}.json \n{}".format(name,str(e)))
    elif update==False:
        datoss = requests.get("https://raw.githubusercontent.com/renaiania233/Grambot/refs/heads/main/{}.json".format(name)).json()
        return(datoss)


db_manager=[]
db_trades={}
pause=False
RISK_MANAGEMENT_MODES={"V1":"PARTIAL 50% AT 1R + MOVE SL TO BE THEN LET RUNNER TO BE OR TP2.","V2":"PARTIAL 50% AT 1R THEN LET RUNNER TO SL(BE) OR TP2."}
RISK_MANAGMENT_VERSION= "V2"
liss={"1":7050*2,"5":35250*2 ,"15": 450000,"30":211500*2,"60":423000*2,"240":1695609*2 ,"D":10152000*2,"W":71064000*2,"M":284256000*2}

dbass={"1":"1 m","5":"5 m","15":"15 m","30":"30 m","60":"1 H","240":"4 H","D" :"1 D","W":"1 W","M":"1 M"}

higher_time_frames = {"1":"5:5","5":"15:3","15":"30:2","30":"60:2","60":"240:4"}

# Your request
os.system("cls")
os.system("clear")
#db_manager={}
ALREADY_ALERTED_TRADES=[]
indexed_db={"last_message":None}


##################################
balance = 0
win_trades=0
loss_trades=0
counter=0
buy_trades=0
sell_trades=0
draw_counter=0
max_drawdown=0
max_profit=0
profit_counter=0
duplicated_drawdown =0
r1_trades =0
r2_trades=0
total_profit=0
total_losses=0
be_trades=0
###########################################################
def EXECUTE_TRADE_V1(candles,trade_type,entry,sl,tp1,tp2,capital):# WITH SL MOVING 
                    global balance, win_trades, loss_trades ,counter ,buy_trades, sell_trades, draw_counter, max_profit, max_drawdown ,profit_counter ,duplicated_drawdown ,r1_trades,r2_trades, total_profit ,total_losses , be_trades
                    counter+=1
                    r1_reached=False
                    if trade_type=="SELL_TRADE":
                        r1_reached=False
                        sell_trades+=1
                        for c in candles:
                          #  if float(c["low"]) <=tp1 and float(c["high"]) >= entry:
                           #    # multiple_values+=1  # same candl touched tp and entry on the same candle
                                

                            if float(c["low"])<= tp1 and r1_reached==False:
                                r1_reached=True
                                r1_trades+=1
                            if r1_reached ==True and float(c["high"]) >= entry:
                                win_trades+=1
                                total_profit+=(capital*1/100)#25
                                balance+=(capital*1/100)#25
                                profit_counter+=1
                                if max_profit<=profit_counter:
                                    max_profit=profit_counter
                                draw_counter=0    
                                #break
                                return
                            if float(c["high"])>=sl and r1_reached==False:
                               # print("  SELL SL -50$")
                                balance-=(capital*1/100)
                                loss_trades+=1
                                total_losses+=(capital*1/100)
                                profit_counter=0
                                draw_counter+=1
                                if max_drawdown<draw_counter:
                                    max_drawdown=draw_counter
                                #break
                                return
                            if float(c["low"])<=tp2:
                               # print("  SELL TP +75$")
                                balance+=(capital*2/100)#75
                                win_trades+=1
                                r2_trades+=1
                                r1_trades-=1
                                total_profit+=(capital*2/100)#75
                                profit_counter+=1
                                if max_profit<=profit_counter:
                                    max_profit=profit_counter
                                    #duplicated_drawdown+=1
                                draw_counter=0
                                #break
                                return
                        sell_trades-=1
                        counter-=1
                    elif trade_type=="BUY_TRADE":
                        buy_trades+=1 
                        r1_reached=False
                        for c in candles:
                      #      if float(c["high"]) >=tp1 and float(c["low"]) <= entry:
                       #         print("\033[35m* buy TRADE ENTERED AT CANDLE : \033[36m{}\033[37m".format(c["ctm"]))
                        #        multiple_values+=1# same candl touched tp and entry on the same candle
                            if float(c["high"])>= tp1 and r1_reached==False:
                                r1_reached=True
                                r1_trades+=1
                            if r1_reached ==True and float(c["low"]) <= entry:
                                win_trades+=1
                                total_profit+=(capital*1/100)#25
                                balance+=(capital*1/100)#25
                                profit_counter+=1
                                if max_profit<=profit_counter:
                                    max_profit=profit_counter
                                draw_counter=0    
                                #break
                                return
                            if float(c["low"])<=sl and r1_reached==False:
                               # print("  BUY SL -50$")
                                balance-=(capital*1/100)
                                loss_trades+=1
                                total_losses+=(capital*1/100)
                                profit_counter=0
                                draw_counter+=1
                                if max_drawdown<draw_counter:
                                    max_drawdown=draw_counter
                                #break
                                return
                            if float(c["high"])>=tp2:
                                #print("  BUY TP +75$")
                                balance+=(capital*2/100)
                                win_trades+=1
                                r2_trades+=1
                                r1_trades-=1
                                total_profit+=(capital*2/100)
                                profit_counter+=1
                                if max_profit<=profit_counter:
                                    max_profit=profit_counter
                                #    duplicated_drawdown+=1
                                draw_counter=0    
                                #break
                                return
                        buy_trades-=1 
                        counter-=1

################################
def EXECUTE_TRADE_V2(candles,trade_type,entry,sl,tp1,tp2,capital):#without sl moving 
                    global balance, win_trades, loss_trades ,counter ,buy_trades, sell_trades, draw_counter, max_profit, max_drawdown ,profit_counter ,duplicated_drawdown ,r1_trades,r2_trades, total_profit ,total_losses ,be_trades
                    counter+=1
                    r1_reached=False
                    if trade_type=="SELL_TRADE":
                        r1_reached=False
                        sell_trades+=1
                        for c in candles:
                          #  if float(c["low"]) <=tp1 and float(c["high"]) >= entry:
                           #    # multiple_values+=1  # same candl touched tp and entry on the same candle
                                

                            if float(c["low"])<= tp1 and r1_reached==False:
                                r1_reached=True
                                r1_trades+=1
                            if r1_reached ==True and float(c["high"]) >= sl:
                                be_trades+=1
                                return
                            if float(c["high"])>=sl and r1_reached==False:
                               # print("  SELL SL -50$")
                                balance-=(capital*1/100)
                                loss_trades+=1
                                total_losses+=(capital*1/100)
                                profit_counter=0
                                draw_counter+=1
                                if max_drawdown<draw_counter:
                                    max_drawdown=draw_counter
                                #break
                                return
                            if float(c["low"])<=tp2:
                               # print("  SELL TP +75$")
                                balance+=(capital*1.5/100)#75
                                win_trades+=1
                                r2_trades+=1
                                r1_trades-=1
                                total_profit+=(capital*1.5/100)#75
                                profit_counter+=1
                                if max_profit<=profit_counter:
                                    max_profit=profit_counter
                                    #duplicated_drawdown+=1
                                draw_counter=0
                                #break
                                return
                        sell_trades-=1
                        counter-=1
                    elif trade_type=="BUY_TRADE":
                        buy_trades+=1 
                        r1_reached=False
                        for c in candles:
                      #      if float(c["high"]) >=tp1 and float(c["low"]) <= entry:
                       #         print("\033[35m* buy TRADE ENTERED AT CANDLE : \033[36m{}\033[37m".format(c["ctm"]))
                        #        multiple_values+=1# same candl touched tp and entry on the same candle
                            if float(c["high"])>= tp1 and r1_reached==False:
                                r1_reached=True
                                r1_trades+=1
                            if r1_reached ==True and float(c["low"]) <= sl:
                                be_trades+=1
                                return
                            if float(c["low"])<=sl and r1_reached==False:
                               # print("  BUY SL -50$")
                                balance-=(capital*1/100)
                                total_losses+=(capital*1/100)
                                loss_trades+=1
                                profit_counter=0
                                draw_counter+=1
                                if max_drawdown<draw_counter:
                                    max_drawdown=draw_counter
                                #break
                                return
                            if float(c["high"])>=tp2:
                                #print("  BUY TP +75$")
                                balance+=(capital*1.5/100)
                                win_trades+=1
                                r2_trades+=1
                                r1_trades-=1
                                total_profit+=(capital*1.5/100)
                                profit_counter+=1
                                if max_profit<=profit_counter:
                                    max_profit=profit_counter
                                #    duplicated_drawdown+=1
                                draw_counter=0    
                                #break
                                return
                        buy_trades-=1 
                        counter-=1
def REQUEST_(url,headers=None,payload=None,json=None):
    for i in range(0,50):
        try:
           # print(json)
            req = requests.get(url,timeout=30,headers=headers,json=json)
          #  print(req)
            if "Too Many Requests" in req.text:print("Too Many Requests");time.sleep(3);continue
            return req
        except Exception as e :
            print(e)
            time.sleep(5)
            continue


def BLOCK_MESSAGES():
    payl= {'chat_id': -1004324675339, 'permissions': {'can_send_messages': False, 'can_send_audios': False, 'can_send_documents': False, 'can_send_photos': False, 'can_send_videos': False, 'can_send_video_notes': False, 'can_send_voice_notes': False, 'can_send_polls': False, 'can_send_other_messages': False, 'can_add_web_page_previews': False}}
    a = REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/setChatPermissions",json=payl)
	#if a.text=='{"ok":true,"result":true}':
    return
def UNBLOCK_MESSAGES():
    payl= {'chat_id': -1004324675339, 'permissions': {'can_send_messages': True, 'can_send_audios': True, 'can_send_documents': True, 'can_send_photos': True, 'can_send_videos': True, 'can_send_video_notes': True, 'can_send_voice_notes': True, 'can_send_polls': True, 'can_send_other_messages': True, 'can_add_web_page_previews': True}}
    a = REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/setChatPermissions",json=payl)
	#if a.text=='{"ok":true,"result":true}':
    return

UNBLOCK_MESSAGES()

def MAIN_TELEGRAM_RESPONDER():
    global RISK_MANAGMENT_VERSION ,pause , balance, win_trades, loss_trades ,counter ,buy_trades, sell_trades, draw_counter, max_profit, max_drawdown ,profit_counter ,duplicated_drawdown ,r1_trades,r2_trades, total_profit ,total_losses ,be_trades

   # global pause
    while True:
        try:
            with open("db.json","w") as w :
                w.write(json.dumps(db_manager))
            ####################################
            updx= GITHUB_FILE(update=True,data=json.dumps(db_manager),name="db")
#####################################
            ssd = REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/getUpdates?offset=-1").json()
            #print(ssd)
            #print("--------------------------------------------")
            try:
                checkpoint = (ssd["result"][-1]["message"]["date"])
            except:
                print("currently there is no recent message on thrr group ")
                time.sleep(10)
                continue
            #print(str(checkpoint) +"  "+ssd["result"][-1]["message"]["text"])
            #print(indexed_db["last_message"])
            if indexed_db["last_message"]==None:indexed_db["last_message"]=checkpoint; time.sleep(10);continue
            elif indexed_db["last_message"]!=checkpoint:
                indexed_db["last_message"]=checkpoint
                #BLOCK_MESSAGES()
                try:
                    msg=ssd["result"][-1]["message"]["text"]
                    #print(msg)
                except :msg=""
                if "/is_bot_online" in msg:
                    ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n BOT-STATUS : RUNNING ONLIGNE ✅")
                    time.sleep(2)
                #    UNBLOCK_MESSAGES()
                elif "/take_picture_from" in msg :
               #     BLOCK_MESSAGES()
                    try:
                        paire = msg.split()[1]
                        timeframe= str(msg.split()[2])
                        
                        j = dbass[timeframe]
                        sti=liss[timeframe]
                        starter = GET_CNDLSTICKS_CHART(timeframe,j,int(time.time())-sti,int(time.time())+ 3600*8,paire,PARAM=None)
                        sti = threading.Thread(target=starter.CHECK_FVG_AVAILABILITY,args=(db_manager,0,True))
                        sti.start()
                    except KeyError :
                        ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n🚫 INVALID TIME FRAME ,PLEASE USE THIS FORMAT <PAIRE> <TIMEFRAME(min)> \n-AUTHORIZED TIMEFRAMES : [1,3,5,15,30,60,240,D,W,M] .")
                    except Exception as e :
                        print(e)
                        ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n🚫   CHECK THIS COMMAND FORMAT:  COMMAND <PAIRE> <TIMEFRAME> \n {}  ".format(e))
              #      UNBLOCK_MESSAGES()
                    
                elif "/start_new_listenner_on" in msg :
                 #   BLOCK_MESSAGES()
                    if len(msg.split()) < 5 :
                        ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n🚫  NO ENOUGH PARAMETERS ,CHECK THIS FORM:  COMMAND <PAIRE> <TIMEFRAME> <PARAM> <SL-DISTANCE> <REFRESH(sec)>\n  ")
                	    #UNBLOCK_MESSAGES()
                	    #continue
                    else:
                        paire = msg.split()[1]
                        timeframe= str(msg.split()[2])
                        param = float(msg.split()[3])
                        min_stop_distance= float(msg.split()[4])
                        timing_ = int(msg.split()[5])
                        j = dbass[timeframe]
                        sti=liss[timeframe]
                        di = {"PAIRE":paire,"RUNNING":True,"TF-NAME":j,"TIMEFRAME":timeframe,"TIMING":timing_,"SETTINGS":param,"MIN-SL":min_stop_distance}
                        print(di)
                        print(db_manager)
                        print(type(di))
                        print(type(db_manager))
                        if di not in db_manager:
                            
                            starter = GET_CNDLSTICKS_CHART(timeframe,j,int(time.time())-sti,int(time.time())+8*3600,paire,param,min_stop_distance)
                            sti = threading.Thread(target=starter.CHECK_FVG_AVAILABILITY,args=(di,timing_,False,False,True))
                            sti.start()

    	        				#starter.CHECK_FVG_AVAILABILITY()
                        else:
                            ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n🚫  REQUESTED RUNNER WAS ALREADY RUNING ON THE DB ! \n  ")
                  #  UNBLOCK_MESSAGES()
                elif "/show_current_listenners" in msg :
                    print("listenner")
                    msg = ""#json.dumps(db_manager)#.replace('}, "','}, \n\n"')
                    for index , runner in enumerate(db_manager):
                        msg+="{})  {} \n\n".format(index,runner)

                    if msg=="":msg="\n\nNO LISTENNER CURRENTLY ON !, DB EMPTY"
                    ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n 🆗 THIS IS THE CURRENT DB-STATUS: \n{}  ".format(str(msg)))
                 #   print(ssd.text)
                    #UNBLOCK_MESSAGES()
                elif "/kill_listenner" in msg : 

                   # BLOCK_MESSAGES()

                    if len(msg.split()) < 2 :
                        ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n🚫  NO ENOUGH PARAMETERS ,CHECK THIS FORM:  COMMAND <INDEX[0,1,2,3,4,5,6,....]> \n  ")
                    else:
                        index = int(msg.split()[-1])
                        try:
                                targetted= db_manager[index]
                            #if targetted["RUNNING"]==True:
                                del db_manager[index]
                                ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n  🚫 {} KILLED FROM DB-LISTENNERS \n  ".format(str(targetted)))
                        
                        except IndexError :
                            ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n  ❌ ({}) NOT IN DB-LISTENNERS | INVALID SELECTION !\n  ".format(str(index)))

                    #UNBLOCK_MESSAGES()
                        

                elif "show_result_for_trade_id" in msg :
                    try:
                        
                        trade_id=str(int(msg.split()[1]))
                        print(trade_id)
                        if trade_id in list(db_trades.keys()) :
                            j = dbass[str(db_trades[trade_id]["TIME-FRAME"])]
                            print(j)
                            sti=liss[str(db_trades[trade_id]["TIME-FRAME"])]
                            print(sti)
                            paire=str(db_trades[trade_id]["PAIRE"])
                            print(paire)
                        
                            starter = GET_CNDLSTICKS_CHART(db_trades[trade_id]["TIME-FRAME"],j,str(trade_id),str(int(trade_id)+sti),paire,0)
                            sti = threading.Thread(target=starter.CHECK_FVG_AVAILABILITY,args=(db_manager,0,False,True))
                            sti.start()
                        else:
                            print(db_trades)
                            ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n  ❌ {} NOT ALREADY REGISTERED AS TRADE ON THE DB !  \n  FAILED TO CHECK TRADE RESULT FOR THIS TRADE-ID".format(str(trade_id)))



                    except Exception as e :
                        print("erroiii"+str(e))
                        ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n  ❌ INVALID COMMAND/ARGUMENTS : COMMAND <TRADE-ID>  ")
                elif "pause_all_listenners" in msg :
                    for listener_ in db_manager:
                        listener_["RUNNING"]=False
                    pause=True
                    ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n✅ ALL CURRENT ACTIVE LISTENNERS ARE CURRENTLY SUSPENDED ! ")
                elif "resume_all_listenners" in msg:
                    for listener_ in db_manager:
                        listener_["RUNNING"]=True
                    pause=False
                    ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n✅ ALL CURRENT ACTIVE LISTENNERS ARE CURRENTLY RELUNCHED SUCCESSFULLY ! ")
                elif "execute_all_trades_with_stats" in msg:
                    if len(db_trades)==0:
                        REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n DB TRADES WAS EMPTY ! \nUNABLE TO START SIMULATION .")
                        continue
                    factor = 10**2
                    balance = 0
                    win_trades=0
                    loss_trades=0
                    counter=0
                    buy_trades=0
                    sell_trades=0
                    draw_counter=0
                    max_drawdown=0
                    max_profit=0
                    profit_counter=0
                    duplicated_drawdown =0
                    r1_trades =0
                    r2_trades =0
                    total_profit=0
                    total_losses=0
                    be_trades=0
                    if len(msg.split())==3 or len(msg.split())==4 :
                        try:
                            list(db_trades.keys())[int(msg.split()[1])]
                            list(db_trades.keys())[int(msg.split()[2])]
                            
                            new_db_trades_ranges_keys=list(db_trades.keys())[int(msg.split()[1]):int(msg.split()[2])]
                            if len(msg.split())==4:
                                capital=int(msg.split()[3])
                            else:
                                capital = 1000
                        except Exception as e : #IndexError:
                            print(e)
                            ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n INVALID TRADES RANGE FROM {} TO {} ❌\n COMMAND <start> <end> <capital[DEFAULT =1000$]>".format(msg.split()[1],msg.split()[2]))
                            continue
                    else:       
                        print(4444444444444444444444444444444444)
                        new_db_trades_ranges_keys=db_trades
                        capital=1000#defaut capital if no specified 



                    new_db_trades_ranges=db_trades.copy()
                    message_id= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n PLEASE WAIT WHILE EXECUTING ...").json()["result"]["message_id"]
                    time.sleep(2)

                    print(new_db_trades_ranges_keys)
                    processor = 0
                    for indx ,  t in enumerate(new_db_trades_ranges_keys):
                        processor=  int((indx/len(new_db_trades_ranges_keys))*100)/100 
                        updated_msg= "- PROCESSING SIMULATION {}%" .format(processor*100)
                        updates____= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/editMessageText?chat_id="+CHAT_ID+"&message_id={}&text={}".format(message_id,updated_msg))
                        entry=new_db_trades_ranges[t]["ENTRY"]
                        trade_type=new_db_trades_ranges[t]["TRADE-TYPE"]
                        tp1=new_db_trades_ranges[t]["TP1"]
                        tp2=new_db_trades_ranges[t]["TP2"]
                        sl=new_db_trades_ranges[t]["STOP-LOSS"]
                        sym=new_db_trades_ranges[t]["PAIRE"]
                        tf = new_db_trades_ranges[t]["TIME-FRAME"]
                        sti=liss[str(new_db_trades_ranges[t]["TIME-FRAME"])]
                        starter = starter = GET_CNDLSTICKS_CHART(tf,None,str(t),str(int(t)+sti),sym,None)
                        starter.PREPARE_REQUEST()
                        NEW_DB_RESULT= starter.db
                        time.sleep(1)
                        if RISK_MANAGMENT_VERSION=="V2":
                            EXECUTE_TRADE_V2(candles=NEW_DB_RESULT,trade_type=trade_type,entry=entry,sl=sl,tp1=tp1,tp2=tp2,capital=capital)
                        #print(balance)
                        elif RISK_MANAGMENT_VERSION=="V1":
                            EXECUTE_TRADE_V1(candles=NEW_DB_RESULT,trade_type=trade_type,entry=entry,sl=sl,tp1=tp1,tp2=tp2,capital=capital)
                    sell_trades=(counter-buy_trades)
                    try:
                        average_win= int((total_profit/win_trades)*100)/100
                    except:
                        average_win=0
                    try:  
                        average_loss= int((total_losses/loss_trades)*100)/100  
                    except:
                        average_loss=0


                    win_rate=(int((win_trades/(counter-be_trades))*100)*100) /100
                    loss_rate=(int((loss_trades/(counter-be_trades))*100)*100)/100
                        
                    expectency=int((((win_rate/100)*average_win)-((loss_rate/100)*average_loss))*100)/100  
                    profit_factor = int((total_profit/total_losses)*100)/100

                    message="""\n
     💹VIRTUAL EXECUTION STATESTICS💹
-------------------------------------------------------------
NET BALANCE AFTER {} TRADES : {}$\n
WINS: {} | LOSSES: {} | BE: {} \n
1R-TRADES  : {} | 2R-TRADES : {}\n
BUY-TRADES : {} | SELL-TRADES : {} \n
WIN-RATE : {}%  | LOSS-RATE : {}%  \n
MAX-WIN : {} | MAX-LOSS : {}\n
PROFIT-FACTOR : {}  \n
EXPECTENCY : {} \n
AVERAGE-WIN : {} | AVERAGE-LOSS {}
--------------------------------------------------------
        *USED RISK MANAGEMENT {}*
--------------------------------------------------------
                        """.format(counter,balance,win_trades,loss_trades,be_trades,r1_trades,r2_trades,buy_trades,sell_trades,win_rate,100-win_rate,max_profit,max_drawdown,profit_factor,expectency,average_win,average_loss,RISK_MANAGMENT_VERSION)
                    print(message)
                    updates____= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/editMessageText?chat_id="+CHAT_ID+"&message_id={}&text={}".format(message_id,"- PROCESSING SIMULATION 100%"))
                    print(updates____.text)
                    time.sleep(1)
                    statestics = REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/editMessageText?chat_id="+CHAT_ID+"&message_id={}&text={}".format(message_id,message))
                    print(statestics.text)
                elif "show_previous_trades" in msg:
                    msg=""
                    for index,trade in enumerate(db_trades.keys()):
                        msg+="{}) [{}] {} | {} | {}\n".format(index,datetime.fromtimestamp(int(trade)),db_trades[trade]["PAIRE"],dbass[str(db_trades[trade]["TIME-FRAME"])],db_trades[trade]["TRADE-TYPE"])
                    print(msg)
                    temp__=""
                    lisd = []
                    for line in msg.split("\n"):
                        lisd.append(line)
                        print(line)
                        if len(lisd)==60:
                            #print(len(lisd))
                            for ln in lisd :
                                temp__+=ln
                                temp__+="\n"
                            ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n {}  ".format(temp__.replace("_","-",9999)))
                            temp__=""
                            lisd=[]

                    #if msg.split()
                    if lisd != []:
                        for ln in lisd :
                            temp__+=ln
                            temp__+="\n"
                        ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n {}  ".format(temp__.replace("_","-",9999)))
                    #print(ssd.text)
                elif "set_risk_management" in msg:
                    if len(msg.split())==2:
                        version_=msg.split()[1]
                        if version_ in RISK_MANAGEMENT_MODES:
                            
                            if RISK_MANAGMENT_VERSION==version_:
                                ssd= REQUEST_('https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n RISK MANAGEMENT MODE WAS ALREADY SET TO :  "{}" ✅'.format(version_))
                                print(ssd.json())
                            else : 
                                RISK_MANAGMENT_VERSION=version_
                                ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n RISK MANAGEMENT MODE SET TO  {} ✅".format(version_))
                                print(ssd.json())
                        else:
                            msg_= "           RISK MANAGEMENT MODES  \n"
                            for md in RISK_MANAGEMENT_MODES:
                                msg_+="{} : {}\n\n ".format(md, RISK_MANAGEMENT_MODES[md])
                            msg_+='RISK MANAGMENT CURRENT MODE : "{}"'.format(RISK_MANAGMENT_VERSION)
                            print(msg_)
                            ssd= REQUEST_('https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n "{}" INVALID RISK MANAGEMENT MODE! ❌\n\n {} '.format(version_,str(msg_)))
                    else:
                        msg_= "           *RISK MANAGEMENT MODES*  \n"
                        for md in RISK_MANAGEMENT_MODES:
                            msg_+="{} : {}\n\n ".format(md, RISK_MANAGEMENT_MODES[md])
                        msg_+='RISK MANAGMENT CURRENT MODE : "{}"'.format(RISK_MANAGMENT_VERSION)
                        print(msg_)
                        ssd= REQUEST_('https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n {} '.format(msg_))
                        print(ssd.json())

                else:
                    ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n {} : WAS AN INVALID COMMAND ❌".format(msg))
                indexed_db["last_message"]=checkpoint
                #UNBLOCK_MESSAGES()
        except ZeroDivisionError :
            REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n ❌CURRENTLY UNABLE TO CALCULATE STATS ! \nPlease wait/try again after some time!")
        except Exception as e :
            error = traceback.format_exc()
            print("err "+str(error))
            REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n {} : WAS AN INVALID COMMAND/ARGUMENT ❌".format(str(e)))
        print("sleeping for 10sec....")
        time.sleep(10)
class GET_CNDLSTICKS_CHART():
    def __init__(self,TIME_FRAME,TF_TO_STR,START,END,SYMBOL,PARAM=0,min_sl=0):
        self.tf=TIME_FRAME
        self.tfcc =TF_TO_STR 
        print(self.tfcc)
        print(self.tf)
        self.start=START
        self.end=END
        self.symbol=SYMBOL
        self.db = []
        self.param=PARAM
        self.result_byID=False
        self.min_sl=min_sl
    def PREPARE_REQUEST(self,confirmation=False):
        try:
            payload = {
                "period": self.tf,
                "from": self.start,
                "to": self.end,
                "cmd": "history",
                "symbol": self.symbol
                    }
            headers= {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    #"accept-encoding":"gzip, deflate, br, zstd",
    "sec-ch-ua":'"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":'"Windows"',
    "accept-language":"en-US,en;q=0.9",
    #"cache-control":"max-age=0",
    #"cookie":"__cf_bm=V08hjYevqvjCfYIuCib4ScQsU3AsYIpLToYAUgfs6oU-1783044267.9888048-1.0.1.1-gH2DTRW5t4gJa0CAi1.J4_t_xbAVa2IYNdfh94dxy8bFA28HFB1RH7g2YRo8eZI9yUZYuOmGZHMCYBlOHtBcZsMtadIgHWY.es0rCVVOYemxLy8y.OQ8kqKbxqbSEfc3.UQJrPBD8QgLwr1yDnwxQQ",
    "priority":"u=0, i",
    "sec-fetch-dest":"document",
    "sec-fetch-mode":"navigate",
    "sec-fetch-site":"none",
    "sec-fetch-user":"?1",
    "upgrade-insecure-requests":"1",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
            }
            proxies = proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080",
    }       
            
            self.response= REQUEST_("https://my.litefinance.org/chart/get-history?symbol={}&resolution={}&from={}&to={}".format(self.symbol,self.tf,self.start,self.end),headers=headers).json()#,proxies=proxies,verify=False)
            #print(self.response)
            try:
                self.response["data"]
            except KeyError:
                if str("empty") in str(self.response) or "EMPTY" in str(self.response):
                    time.sleep(10)
                    self.PREPARE_REQUEST(confirmation=confirmation)
                    return
                ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n {}  ".format(str(self.response).replace("_"," " ,999)))
                return False
            except Exception as err:
               # print(err)
                return None
            print("##################")
            if confirmation==True:
                self.db2=[]
                for i in range(0,len(self.response["data"]["t"])):
                    self.db2.append({"time":self.response["data"]["t"][i],"open":self.response["data"]["o"][i],"close":self.response["data"]["c"][i],"high":self.response["data"]["h"][i],"low":self.response["data"]["l"][i]})
                return True
            for i in range(0,len(self.response["data"]["t"])):
                    self.db.append({"time":self.response["data"]["t"][i],"open":self.response["data"]["o"][i],"close":self.response["data"]["c"][i],"high":self.response["data"]["h"][i],"low":self.response["data"]["l"][i]})
            print(len(self.db))
            print("START TIME : ",str(self.start))
            print("END TIME : ",str(self.end))
            print(self.tf)
            print("##################")
            return True
        except Exception as e :
            print(e)
            print("errornni")
            self.PREPARE_REQUEST(confirmation=confirmation)
    def PREPARE_REQUEST3(self):
        #https://lightcharts.ifxdb.com/?server_type=5&language=en&symbol=xauusd&compact_menu=1&shrink_corners&timeframe=60
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            #"Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "datafeed.ifxdb.com",
            "Pragma": "no-cache",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0",
            "sec-ch-ua": '"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
            }
        proxies={"https":None}
        while True:
            try:
                self.response= requests.get("https://datafeed.ifxdb.com/chart/history?symbol={}&resolution={}&from={}&to={}&server=europe".format(self.symbol,self.tf,self.start,self.end,self.tf),headers=headers,proxies=proxies)
                print("+"+str(self.response.text)+"+")
                if str("IP address is temporarily blocked") in str(self.response.text):
                    print("TRUE TRUE TRUE ")
                    requests.get("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \nERROR : RECIVED RESPONSE : \nIP address is temporarily blocked")
                    proxies={"https":"http://oyymhzrz-rotate:a23d27ck5y6u@p.webshare.io:80"}
                    continue
                else:
                    #self.response.json()
                    proxies={"https":None}
                    break
            except Exception as e :
                print("un error por aqui : "+str(e))
                time.sleep(10)
                continue
        for i in range(0,len(self.response.json()["t"])):
                self.db.append({"time":self.response.json()["t"][i],"open":self.response.json()["o"][i],"close":self.response.json()["c"][i],"high":self.response.json()["h"][i],"low":self.response.json()["l"][i]})

        print("READY")
    def PREPARE_REQUEST2(self):
        payload = {
            "period": self.tf,
            "from": self.start,
            "to": self.end,
            "cmd": "history",
            "symbol": self.symbol
                }
        print(payload)
        ws = websocket.create_connection(
             "wss://q.ifccd.net/",
        header={
             "Connection": "Upgrade",
             "Pragma":"no-cache",
             "Cache-Control": "no-cache",
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
             "Upgrade": "websocket",
             "Origin": "https://www.ifcm.co.uk",
             "Sec-WebSocket-Version": "13",
             "Accept-Language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
             "Sec-WebSocket-Key": "u3uhLY+x2mOhtfaqKFqMaA=="
                  },
    sslopt={"cert_reqs": ssl.CERT_NONE},
    skip_utf8_validation=True,
    enable_multithread=True
                                  )
#        print("✅ Connected, sending request...")
        ws.send(json.dumps(payload))
 #       print("📤 Request sent!, Waiting for response ")
        ws.settimeout(10)  # 10 second timeout
        self.response = ws.recv()
        print(self.response)
        self.db= json.loads(self.response)["list"]
        #print(self.response)
        ws.close()
        #print(self.response)
    def CALCULATE_RSI(self,prices,period=10):
        prices = np.array(prices)
        momentum = np.full_like(prices, np.nan, dtype=float)
        
        for i in range(period, len(prices)):
            momentum[i] = prices[i] - prices[i - period]
        
        return momentum
    def calculate_sma(self, length=15):
        highs=[]
        lows=[]
        for candle in self.db:
            highs.append(float(candle["high"]))
            lows.append(float(candle["low"]))
        hl2 = [(h + l) / 2.0 for h, l in zip(highs, lows)]

        sma = []
        for i in range(len(hl2)):
            if i < length - 1:
                sma.append(None)
            else:
                window = hl2[i - length + 1 : i + 1]
                sma.append(sum(window) / float(length))
        self.sma_values = sma 
#        return sma
    def calculate_sma2(self, length=5):
        highs=[]
        lows=[]
        for candle in self.db:
            highs.append(float(candle["high"]))
            lows.append(float(candle["low"]))
        hl2 = [(h + l) / 2.0 for h, l in zip(highs, lows)]

        sma = []
        for i in range(len(hl2)):
            if i < length - 1:
                sma.append(None)
            else:
                window = hl2[i - length + 1 : i + 1]
                sma.append(sum(window) / float(length))
        self.sma_values2 = sma
    def calculate_hma_base4 (self,periode=5):
        highs=[]
        lows=[]
        for candle in self.db:
            highs.append(float(candle["low"]))
            lows.append(float(candle["low"]))
        self.hma_values4 = self.calculate_hma(highs, lows, length=5)
    def calculate_hma_base3 (self,periode=15):
        highs=[]
        lows=[]
        for candle in self.db:
            highs.append(float(candle["high"]))
            lows.append(float(candle["low"]))
        self.hma_values3 = self.calculate_hma(highs, lows, length=15)
    def calculate_hma_base2 (self,periode=20):
        highs=[]
        lows=[]
        for candle in self.db:
            highs.append(float(candle["high"]))
            lows.append(float(candle["low"]))
        self.hma_values2 = self.calculate_hma(highs, lows, length=20)

#25 28 5 min  52%win rate dd8 mp12 $26501365 trades
    def calculate_hma_base (self,periode=9):
        highs=[]
        lows=[]
        for candle in self.db:
            highs.append(float(candle["high"]))
            lows.append(float(candle["low"]))
        self.hma_values = self.calculate_hma(highs, lows, length=9)

 
    def calculate_wma(self,data, length):
        """Calculates Weighted Moving Average using pure Python lists."""
        result = []
        weight_denom = (length * (length + 1)) / 2.0

        for i in range(len(data)):
            if i < length - 1:
                result.append(None)
            else:
                window = data[i - length + 1 : i + 1]
                if None in window:
                    result.append(None)
                else:
                    weighted_sum = sum(
                        (j + 1) * val for j, val in enumerate(window)
                    )
                    result.append(weighted_sum / weight_denom)

        return result


    def calculate_hma(self,highs, lows, length=5):
        """Calculates Hull Moving Average (HMA) on (High + Low) / 2 source without external libraries."""
        # 1. Compute hl2 source: (High + Low) / 2
        hl2 = [(h + l) / 2.0 for h, l in zip(highs, lows)]

        half_length = int(length / 2)
        sqrt_length = int(math.sqrt(length))

        # 2. Calculate WMAs for half length and full length
        wma_half = self.calculate_wma(hl2, half_length)
        wma_full = self.calculate_wma(hl2, length)

        # 3. Calculate Raw HMA: (2 * WMA_half) - WMA_full
        raw_hma = []
        for h_val, f_val in zip(wma_half, wma_full):
            if h_val is None or f_val is None:
                raw_hma.append(None)
            else:
                raw_hma.append(2 * h_val - f_val)

        # 4. Smooth Raw HMA over sqrt(length)
        final_hma = self.calculate_wma(raw_hma, sqrt_length)

        return final_hma


    def calculate_adx(self, period=9):
        """Calculates ADX (Average Directional Index) using pure Python math (Wilder's Smoothing)."""
        highs=[]
        lows=[]
        closes = []
        for candle in self.db:
            highs.append(float(candle["high"]))
            lows.append(float(candle["low"]))
            closes.append(float(candle["close"]))
        n = len(highs)
        if n < (2 * period):
            return [None] * n

        # 1. Compute True Range (TR) and Directional Movement (+DM, -DM)
        tr = [highs[0] - lows[0]]
        plus_dm = [0.0]
        minus_dm = [0.0]

        for i in range(1, n):
            up_move = highs[i] - highs[i - 1]
            down_move = lows[i - 1] - lows[i]

            p_dm = up_move if (up_move > down_move and up_move > 0) else 0.0
            m_dm = down_move if (down_move > up_move and down_move > 0) else 0.0

            tr_val = max(
                highs[i] - lows[i],
                abs(highs[i] - closes[i - 1]),
                abs(lows[i] - closes[i - 1]),
            )

            tr.append(tr_val)
            plus_dm.append(p_dm)
            minus_dm.append(m_dm)

        # 2. Smooth TR, +DM, -DM using Wilder's Smoothing
        smoothed_tr = [None] * n
        smoothed_p_dm = [None] * n
        smoothed_m_dm = [None] * n

        # First smoothed value is the simple sum over the first 'period'
        smoothed_tr[period] = sum(tr[1 : period + 1])
        smoothed_p_dm[period] = sum(plus_dm[1 : period + 1])
        smoothed_m_dm[period] = sum(minus_dm[1 : period + 1])

        for i in range(period + 1, n):
            smoothed_tr[i] = (
                smoothed_tr[i - 1] - (smoothed_tr[i - 1] / period) + tr[i]
            )
            smoothed_p_dm[i] = (
                smoothed_p_dm[i - 1] - (smoothed_p_dm[i - 1] / period) + plus_dm[i]
            )
            smoothed_m_dm[i] = (
                smoothed_m_dm[i - 1]
                - (smoothed_m_dm[i - 1] / period)
                + minus_dm[i]
            )

        # 3. Compute +DI, -DI, and DX
        dx = [None] * n
        for i in range(period, n):
            if smoothed_tr[i] is None or smoothed_tr[i] == 0:
                continue

            p_di = 100.0 * (smoothed_p_dm[i] / smoothed_tr[i])
            m_di = 100.0 * (smoothed_m_dm[i] / smoothed_tr[i])

            di_sum = p_di + m_di
            dx[i] = 100.0 * (abs(p_di - m_di) / di_sum) if di_sum != 0 else 0.0

        # 4. Compute ADX (Wilder's Smoothing of DX)
        adx = [None] * n
        start_idx = 2 * period - 1

        if start_idx < n:
            valid_dx = dx[period : start_idx + 1]
            if None not in valid_dx:
                adx[start_idx] = sum(valid_dx) / period

                for i in range(start_idx + 1, n):
                    if adx[i - 1] is not None and dx[i] is not None:
                        adx[i] = ((adx[i - 1] * (period - 1)) + dx[i]) / period

        return adx




    def calculate_smi(self,candles, period=10, smooth=3):
        """
        TradingView Stochastic Momentum Index (SMI)

        candles = [
            {"high": ..., "low": ..., "close": ...},
            ...
        ]

        Returns:
            list of SMI values
            None until enough historical data is available
        """

        n = len(candles)
        smi = [None] * n

        if n < period:
            return smi

        high = [float(c["high"]) for c in candles]
        low = [float(c["low"]) for c in candles]
        close = [float(c["close"]) for c in candles]

        # EMA that starts only when the required data exists
        def ema(values, length):
            result = [None] * len(values)
            alpha = 2 / (length + 1)

            first = next(
                (i for i, x in enumerate(values) if x is not None),
                None
            )

            if first is None:
                return result

            result[first] = values[first]

            for i in range(first + 1, len(values)):
                if values[i] is not None:
                    result[i] = (
                        alpha * values[i]
                        + (1 - alpha) * result[i - 1]
                    )

            return result

        # TradingView ta.highest() / ta.lowest()
        highest = [None] * n
        lowest = [None] * n

        for i in range(period - 1, n):
            highest[i] = max(high[i - period + 1:i + 1])
            lowest[i] = min(low[i - period + 1:i + 1])

        # relativeRange and highestLowestRange
        relative_range = [None] * n
        highest_lowest_range = [None] * n

        for i in range(period - 1, n):
            relative_range[i] = (
                close[i] - (highest[i] + lowest[i]) / 2
            )

            highest_lowest_range[i] = (
                highest[i] - lowest[i]
            )

        # emaEma(relativeRange, smooth)
        rr_ema1 = ema(relative_range, smooth)
        rr_ema2 = ema(rr_ema1, smooth)

        # emaEma(highestLowestRange, smooth)
        range_ema1 = ema(highest_lowest_range, smooth)
        range_ema2 = ema(range_ema1, smooth)

        # TradingView SMI
        for i in range(n):
            if rr_ema2[i] is not None and range_ema2[i] is not None:
                if range_ema2[i] != 0:
                    smi[i] = 200 * rr_ema2[i] / range_ema2[i]
        self.smi = smi 
        return smi
    def is_sl_vulnerable(self,entry,sl,direction,fvgs,current_index,atr,min_fvg_atr=5,max_age=50):
        """
        Check whether there is a significant FVG beyond the SL.

        LONG:
            FVG must be below SL.

        SHORT:
            FVG must be above SL.

        Returns:
            True  -> SL may be vulnerable
            False -> no relevant FVG beyond SL
        """

        for fvg in fvgs[::-1]:

            # Ignore future FVGs
            if fvg["index"] > current_index:
                continue

            # Ignore old FVGs
            if current_index - fvg["index"] > max_age:
                continue

            # Ignore small FVGs
          #  if atr is not None:
           #     if fvg["size"] < atr * min_fvg_atr:
            #        continue

            # =========================
            # LONG
            # =========================
            if direction == "long":

                # FVG completely below SL
                if fvg["high"] < sl:
                    return True
                else:return False

            # =========================
            # SHORT
            # =========================
            elif direction == "short":

                # FVG completely above SL
                if fvg["low"] > sl:
                    return True
                else:return False


        return False
    def is_tp_blocked(self,entry,tp, direction,fvgs,current_index,atr,min_fvg_atr=5,max_age=50):
        """
        Returns True if a significant, recent opposing FVG
        is located between entry and TP.
        """

        for fvg in fvgs[::-1]:

            # Ignore future FVGs
            if fvg["index"] > current_index:
                continue

            # Ignore old FVGs
            if current_index - fvg["index"] > max_age:
                continue

            # Ignore small FVGs
     #       if atr is not None:
      #          if fvg["size"] < atr * min_fvg_atr:
       #             continue

            # LONG → bearish FVG can block TP
            if direction == "long" and fvg["type"] == "bearish":

                if fvg["high"] >= entry and fvg["low"] <= tp:
                    return True
                else : return False

            # SHORT → bullish FVG can block TP
            elif direction == "short" and fvg["type"] == "bullish":

                if fvg["high"] >= tp and fvg["low"] <= entry:
                    return True
                else: return False

        return False
    def detect_fvgs(self,candles):
        """
        Detect 3-candle Fair Value Gaps.

        Returns:
            list of FVG dictionaries.
        """

        fvgs = []

        for i in range(2, len(candles)):

            c0 = candles[i - 2]
            c2 = candles[i]

            # Bullish FVG
            if float(c2["low"]) > float(c0["high"]):
                if (float(c2["low"]) - float(c0["high"])) <2:continue
              #  input("<<<<<")
                fvgs.append({
                    "index": i,
                    "type": "bullish",
                    "low": float(c0["high"]),
                    "high": float(c2["low"]),
                    "size": float(c2["low"]) - float(c0["high"])
                })
            # Bearish FVG
            elif float(c2["high"]) < float(c0["low"]):
                if (float(c0["low"]) - float(c2["high"])) <2:continue
                #input("<<<<<")
                fvgs.append({
                    "index": i,
                    "type": "bearish",
                    "low": float(c2["high"]),
                    "high": float(c0["low"]),
                    "size": float(c0["low"]) - float(c2["high"])
                })

        return fvgs
    def stochastic_rsi(self,db, rsi_length=14, stoch_length=14,
                       smooth_k=3, smooth_d=3):
        """
        db: list of candle dictionaries containing 'close'

        Returns:
            k_line: list of %K values
            d_line: list of %D values

        TradingView default settings:
            RSI Length = 14
            Stochastic Length = 14
            K Smoothing = 3
            D Smoothing = 3
        """


        close = pd.Series(
            [float(c["close"]) for c in db],
            dtype="float64"
        )

        # 1. Calculate RSI using Wilder's RMA
        delta = close.diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.ewm(
            alpha=1 / rsi_length,
            min_periods=rsi_length,
            adjust=False
        ).mean()

        avg_loss = loss.ewm(
            alpha=1 / rsi_length,
            min_periods=rsi_length,
            adjust=False
        ).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        # Handle zero-loss and zero-gain edge cases
        rsi = rsi.mask((avg_loss == 0) & (avg_gain > 0), 100.0)
        rsi = rsi.mask((avg_gain == 0) & (avg_loss > 0), 0.0)

        # 2. Stochastic applied to RSI
        lowest_rsi = rsi.rolling(
            window=stoch_length,
            min_periods=stoch_length
        ).min()

        highest_rsi = rsi.rolling(
            window=stoch_length,
            min_periods=stoch_length
        ).max()

        rsi_range = highest_rsi - lowest_rsi

        stoch_rsi = (
            (rsi - lowest_rsi) / rsi_range.replace(0, np.nan)
        ) * 100

        # 3. Smooth %K and %D using SMA
        k_line = stoch_rsi.rolling(
            window=smooth_k,
            min_periods=smooth_k
        ).mean()

        d_line = k_line.rolling(
            window=smooth_d,
            min_periods=smooth_d
        ).mean()

        return k_line.tolist(), d_line.tolist()
    def GET_MANUAL_PICTURE(self,type,signal,candles, entry_index, entry_price, tp_price, sl_price,rectangle_width=10,take_picture_only=False,price_min_=None,price_max_=None):
      try:
        print("hello inside")
        fig, ax = plt.subplots(figsize=(16, 9))

        # --------------------------------------------------
        # Background
        # --------------------------------------------------
        fig.patch.set_facecolor("#131722")
        ax.set_facecolor("#131722")

        # --------------------------------------------------
        # Draw candles
        # --------------------------------------------------
        candle_width = 0.65
        print(len(candles))
        print("-------------")
        for i, candle in enumerate(candles):

            o = float(candle["open"])
            h = float(candle["high"])
            l = float(candle["low"])
            c = float(candle["close"])

            # Bullish / bearish
            if c >= o:
                color = "#26a69a"
            else:
                color = "#ef5350"

            # ---------------------------
            # Wick
            # ---------------------------
            ax.plot(
                [i, i],
                [l, h],
                color=color,
                linewidth=1.2,
                zorder=1
            )

            # ---------------------------
            # Body
            # ---------------------------
            body_bottom = min(o, c)
            body_height = abs(c - o)

            # Prevent zero-height candle bodies
            if body_height == 0:
                body_height = 0.000000000000000000001

            ax.add_patch(
                Rectangle(
                    (i - candle_width / 2, body_bottom),
                    candle_width,
                    body_height,
                    facecolor=color,
                    edgecolor=color,
                    linewidth=1,
                    zorder=2
                )
            )

        # --------------------------------------------------
        # TP / SL rectangle
        # --------------------------------------------------

        # Rectangle extends from entry candle into future
        x_start = entry_index - 0.5
       # x_end = entry_index + rectangle_width
        x_end = min(entry_index + rectangle_width,len(candles) - 1)

        # ---------------------------
        # TP rectangle
        # ---------------------------
        if take_picture_only==False:

            tp_top = max(tp_price, entry_price)
            tp_bottom = min(tp_price, entry_price)

            ax.add_patch(
            Rectangle(
                (x_start, tp_bottom),
                x_end - x_start,
                tp_top - tp_bottom,
                facecolor="#00ff00",
                edgecolor="#b000ff",
                linewidth=2,
                alpha=0.45,
                zorder=3
            )
        )

        # ---------------------------
        # SL rectangle
        # ---------------------------
            sl_top = max(sl_price, entry_price)
            sl_bottom = min(sl_price, entry_price)

            ax.add_patch(
            Rectangle(
                (x_start, sl_bottom),
                x_end - x_start,
                sl_top - sl_bottom,
                facecolor="#ff5555",
                edgecolor="#b000ff",
                linewidth=2,
                alpha=0.45,
                zorder=3
            )
        )

        # --------------------------------------------------
        # Entry line
        # --------------------------------------------------
            calc =entry_price+(tp_price-entry_price)/2
            ax.hlines(
            float(calc),
            x_start,
            x_end,
            colors="white",
            linestyles="--",
            linewidth=1,
            alpha=0.7
        )
           
####################
            ax.hlines(
            entry_price,
            x_start,
            x_end,
            colors="white",
            linestyles="--",
            linewidth=1,
            alpha=0.7
        )
            ax.text(
            x_end ,#+ 0.2,
            entry_price,
            f"BE {entry_price:.6f}",
            color="white",
            fontsize=10,
            verticalalignment="center"
        )
            ##################

        # --------------------------------------------------
        # TP / SL labels
        # --------------------------------------------------
            ax.text(
            x_end ,#+ 0.2,
            tp_price,
            f"TP {tp_price:.6f}",
            color="white",
            fontsize=10,
            verticalalignment="center"
        )

            ax.text(
            x_end ,#+ 0.2,
            sl_price,
            f"SL {sl_price:.6f}",
            color="white",
            fontsize=10,
            verticalalignment="center"
        )

        # --------------------------------------------------
        # Formatting
        # --------------------------------------------------

        ax.set_xlim(-1, len(candles) + 2)

        # Price range
        all_prices = []

        for c in candles:
            all_prices.extend([
                float(c["high"]),
                float(c["low"])
            ])
        if take_picture_only==False:
            all_prices.extend([
                tp_price,
                sl_price,
                entry_price
            ])

        if self.result_byID ==True:
           # all_prices.append(price_min_)
            #all_prices.append(price_max_)

            price_min = min(all_prices)
            price_max = max(all_prices)
        else :
            price_min = min(all_prices)
            price_max = max(all_prices)
            self.price_min=price_min
            self.price_max=price_max

        padding = (price_max - price_min) * 0.05

        ax.set_ylim(
            price_min - padding,
            price_max + padding
        )
        print("hihihihi")

        # Grid
        ax.grid(
            True,
            color="#2a2e39",
            linewidth=0.8,
            alpha=0.8
        )

        # Remove unnecessary borders
        ax.spines["top"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(False)

        # Tick colors
        ax.tick_params(
            colors="#b2b5be",
            labelsize=10
        )

        # Price axis on right
        ax.yaxis.tick_right()
        # Remove x labels
        ax.set_xticks([])
        ax.set_title(
        "{} - {} |  {}".format(self.symbol,self.tfcc,type),
        color="white",
        fontsize=16,
        fontweight="bold",
        pad=15
    )

        plt.tight_layout()

        plt.savefig(
        "{}.png".format(signal),
        dpi=300,
        bbox_inches="tight"
    )
        return(True)
  #  plt.show()
      except Exception as e :print(e)
    def GET_TRADE_PICTURE_FROM_CHART(self,signal,details,start_timing):
      #  if self.tf>=60:
       #     calculator= (self.tf * 60)*8
        #else:
        #    calculator= (self.tf*60)*8
        end_timing=start_timing+8*3600
        end_timing=str(datetime.fromtimestamp(end_timing)).replace(" ","T")+".000Z"

        api_keys=["GN475exYnc1OcuNWQWgzI7oNbVRfU3OB9M0Di4HR"]#["bQfMOpcms22KQzrnw53kl9sy6f1sLSFl89IoV4IM","SzssIc7mPD2eIr8zKVkep7VXna3keg0Y6JGb2FLr","U70bTRRbyD3vlD2JnINjgdhQ0XDH8Th5C40RlxM2"]
        start_timing=str(datetime.fromtimestamp(start_timing)).replace(" ","T")+".000Z"
        url = "https://api.chart-img.com/v2/tradingview/advanced-chart"
       # if  self.tf==60 :v_tf="1h"
        if self.tf<60: v_tf="{}m".format(str(self.tf)) 
        elif self.tf>=60:v_tf="{}h".format(str(int(self.tf/60)))

        payload = {
            "symbol": "FX:{}".format(self.symbol),
            "interval": v_tf,
            "theme": "dark",
            "style": "candle",
            "drawings": [
                 {
              "name": "Rectangle",
              "input": {
                "startDatetime": start_timing,
                "startPrice": (float(details[0])),
                "endDatetime": end_timing,
                "endPrice": (float(details[1])),
                "text": "RECTANGLE ZONE",
              },
              "override": {
                "backgroundColor": "rgba(243,155,155,1)",
                "transparency": 100,
                "borderColor": "rgb(255,255,255)",
                "lineWidth": 2
              }},




              {
              "name": "Rectangle",
              "input": {
                "startDatetime": start_timing,
                "startPrice": (float(details[1])),
                "endDatetime": end_timing,
                "endPrice": (float(details[2])),
                "text": "RECTANGLE ZONE",
                
              },
              "override": {
                "backgroundColor": "rgba(117,239,117,1)",
                "transparency": 100,
                "borderColor": "rgb(255,255,255)",
                "lineWidth": 2
              }}
            ]
        }
        print(payload)
        proxies={"https":None}
        while True:
            for key in api_keys:
                try:
                    headers = {
                        "x-api-key": key,
                        "Content-Type": "application/json"
                    }
                    response = requests.post(url, headers=headers, json=payload,proxies=proxies)
                    print("oki"+str(response.text)+"oka")#{"message":"Limit Exceeded"}
                    if str("IP address is temporarily blocked") in str(self.response.text):
                        proxies={"https":"http://oyymhzrz-rotate:a23d27ck5y6u@p.webshare.io:80"}
                        continue
                except Exception as err:
                    print(err)
                    continue
                if len(response.content)>1000:
                    with open("{}.png".format(signal), "wb") as f:
                        f.write(response.content)
                        return True
            time.sleep(10)
    def count_range_intersections(self,ranges):
        intersection_count = 0
        n = len(ranges)
        
        # Compare every unique pair (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                start1, end1 = ranges[i]
                start2, end2 = ranges[j]
                
                # Check if range i and range j overlap
                if start1 <= end2 and start2 <= end1:
                    intersection_count += 1
                    
        return intersection_count
    
    def CHECK_FVG_AVAILABILITY(self,management,timing___,pic,result_byID=False,send_confirmation=False):
      already_alerted_started_ok =False
      while True:
       try:
        while pause ==True:
            time.sleep(5)
            continue
        self.db=[]
        print("running iteration ....")
        
        #if management[self.symbol]==False:return
        #self.tf=60
        
        ssxx = self.PREPARE_REQUEST()
        ################################
       # fvgaps=  self.detect_fvgs(self.db)

        self.calculate_hma_base()
        self.calculate_hma_base2()
        self.calculate_hma_base3()
		self.calculate_hma_base4()
        self.calculate_sma()
        adxdb = self.calculate_adx()
        #k_line, d_line = self.stochastic_rsi(self.db)

       # self.calculate_hma_base2()
        #self.calculate_hma_base3()
        #self.calculate_hma_base4()
        #self.calculate_sma2()
        #######################
        if ssxx==False:
            time.sleep(5)
            return 
        elif ssxx== True:
            if send_confirmation==True:
                if already_alerted_started_ok==False:
                    ssd= REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \n✅LISTENNER STARTED ON :\nPAIRE: {}\nTIME-FRAME: {}\nPARAM: {}\nMIN-SL: {}\nREFRESH(sec): {}".format(self.symbol,self.tf,self.param,self.min_sl,timing___))
                    already_alerted_started_ok=True
                    di = {"PAIRE":self.symbol,"RUNNING":True,"TF-NAME":self.tfcc,"TIMEFRAME":self.tf,"TIMING":timing___,"SETTINGS":self.param,"MIN-SL":self.min_sl}
                    if di not in db_manager:
                        db_manager.append(di)
        else:
            time.sleep(30)
            continue

        print("HOHO")
        time.sleep(timing___)
        if pic ==True:
            print("lets execute ")
            spp = self.GET_MANUAL_PICTURE(type="CHART",signal="pic_{}".format(self.symbol),candles=self.db[len(self.db)-80:],entry_index=len(self.db[len(self.db)-80:]),entry_price=0,tp_price=0,sl_price=0,take_picture_only=True)
            print(spp)
            if spp==True:
                                    
                              #      TOKEN = "8953744107:AAGT84f18dCY4Lwxnam1P_TixecJ9LHDuU8"
                                 #   CHAT_ID = "-1004324675339"
                                    while True:
                                        try:
                                            url = f"https://api.telegram.org/bot{TOKEN_}/sendPhoto"  
                                            with open("pic_{}.png".format(self.symbol), "rb") as photo:
                                                r = requests.post(
                                                    url,
                                                    data={
                                                        "chat_id": CHAT_ID,
                                                        "caption":"{} - {} | INSTANT LIVE-CHART.".format(self.symbol,self.tfcc)# "     🔴➖ SELL SIGNAL DETECTED ➖🔴 \n\n * ENTRY: {} \n\n * STOP_LOSS: {} \n\n * TAKE_PROFIT1: {} \n\n * TAKE_PROFIT2: {} \n\n * RUNNER? :  AFTER TP2 \n\n➖➖➖➖(ID: {})➖➖➖➖".format(round(st,5),round(sl,5),round(tp1,5),round(tp2,5),str(id__)),
                                                        # "parse_mode": "Markdown"
                                                    },
                                                    files={
                                                        "photo": photo
                                                    }
                                                ).json()
                                                if r["ok"]==True:

                                                        #ALREADY_ALERTED_TRADES.append(id__)
                                                        break
                                        except Exception as e :  print("RECIVED RSP" +str(e));time.sleep(10)

            else:
                REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \nERROR OCCURED WHEN TRYING TO GENERTE THE PICTURE , PLEASE RETRY AGAIN !")
            return 
        ##############################################################################################################################################################
        if result_byID==True:
            self.result_byID=True
            print("ehlo")
           # ind = self.db.index(self.start)
            #print(ind)
            entry= db_trades[self.start]["ENTRY"]
            tp2= db_trades[self.start]["TP2"]
            sl = db_trades[self.start]["STOP-LOSS"]
            trade_closed =False
            for cndl in self.db[0:80]:
                if db_trades[self.start]["TRADE-TYPE"]=="BUY_TRADE" :
                    if float(cndl["high"]) >= tp2:
                        ind = self.db.index(cndl)
                        print(float(cndl["high"]))
                        print(ind)
                        print(cndl)
                        print("-----")
                        trade_closed=True
                        break
                    elif float(cndl["low"])<=sl:
                        ind = self.db.index(cndl)
                        trade_closed=True
                        break
                    else:
                        ind = self.db.index(cndl)
                else:
                    if float(cndl["low"]) <= tp2:
                        ind = self.db.index(cndl)
                        trade_closed=True
                        break
                    elif float(cndl["high"])>=sl:
                        ind = self.db.index(cndl)
                        trade_closed=True
                        break
                    else:
                        ind = self.db.index(cndl)
            #if ind <10:
            #    ind =10 
            ind =ind
            print(ind)


            #tt__ = len(self.db)
            #result_counter = 80-tt__
            try:
                end_trade_cndl=self.db[ind]
                ind=ind#+1
                print("validated_with +1 ")
                print(end_trade_cndl)
            except:
                end_trade_cndl=self.db[ind]
                print("validated normally ")
                print(end_trade_cndl)
                pass

            old_start=self.start
            print(len(self.db))
            #if len(self.db)<80:
            #    cbi =  liss[self.tf]
             #   self.start= int(old_start)-cbi
             #   self.end=int(self.db[ind]["time"])
            #    self.db=[]
            #    self.PREPARE_REQUEST()
            #    self.db=self.db
            #    ind = self.db.index(end_trade_cndl)
            #    print("++++++++++++++++++++++++++++++")
             #   print(len(self.db))
             #   new_indox_final=len(self.db)#self.db.index(self.db[ind])
             #   for i in self.db :
             #       if str(i["time"]) ==str(old_start):
             ##           print("ehkiiiiiii")
             #           new_indox_start=self.db.index(i)
              #          print(new_indox_start)
              #          break
            if True : 
                cbi =  liss[self.tf]
                self.start= int(old_start)-cbi
                self.end=int(self.db[ind]["time"])
                self.db=[]
                self.PREPARE_REQUEST()
                self.db=self.db
                ind = len(self.db)#self.db.index(end_trade_cndl)
                print(ind)
                print("ehlolaaaaaaaaaaaaaaaaaaaaa")
                self.db=self.db[0:ind]
                self.db=self.db[len(self.db)-80:]
                print(len(self.db))
                self.db[-1]=end_trade_cndl
                print("Pppppppppppppppppppppp")
                print(self.db[-1])
                new_indox_final=len(self.db)#self.db.index(end_trade_cndl)
                for i in self.db:
                    if str(i["time"]) == str(old_start):
                        new_indox_start=self.db.index(i)
                        break
                self.start=old_start




               


                










            print("hiiiihahahahhahiiihahahah")
            print(ind)
            pp = self.GET_MANUAL_PICTURE(type=db_trades[old_start]["TRADE-TYPE"],signal="{}_{}".format(self.symbol,db_trades[old_start]["TRADE-TYPE"]),candles=self.db,entry_index=new_indox_start,entry_price=entry,tp_price=tp2,sl_price=sl,rectangle_width=new_indox_final,take_picture_only=False,price_min_=None,price_max_=None)
            if pp==True:
                                #    TOKEN = "8953744107:AAGT84f18dCY4Lwxnam1P_TixecJ9LHDuU8"
                              #      CHAT_ID = "-1004324675339"
                                    while True:
                                        try:

                                            url = f"https://api.telegram.org/bot{TOKEN_}/sendPhoto"
                                            with open("{}_{}.png".format(self.symbol,db_trades[self.start]["TRADE-TYPE"]), "rb") as photo:
                                                if db_trades[self.start]["TRADE-TYPE"]=="SELL_TRADE":
                                                    data={
                                                        "chat_id": CHAT_ID,
                                                        "caption": "🔴 TRADING RESULT FOR THE TRADE (ID: {}) SELL {} | {} ".format(self.start,self.symbol,self.tfcc),
                                                        # "parse_mode": "Markdown"
                                                        }
                                                else :
                                                    data={
                                                        "chat_id": CHAT_ID,
                                                        "caption": "🟢 TRADING RESULT FOR THE TRADE (ID: {}) BUY {} | {} ".format(self.start,self.symbol,self.tfcc),
                                                        # "parse_mode": "Markdown"
                                                        }
                                                r = requests.post(
                                                    url,
                                                    data=data,
                                                    files={
                                                        "photo": photo
                                                    }
                                                ).json()
                                                if r["ok"]==True:
                                                       # with open("TRADES.json","w") as w :         
                                                        #    db_trades[id__]={"TRADE-TYPE":"BUY_TRADE","PAIRE":self.symbol,"TIME-FRAME":self.tf,"ENTRY":round(,5),"STOP-LOSS":round(sl,5),"TP1":round(tp1,5),"TP2":round(tp2,5)}
                                                         #   w.write(json.dumps(db_trades))
                                                        #ALREADY_ALERTED_TRADES.append(id__)
                                                        break
                                        except Exception as e : print("RECIVED RSP" +str(e))

                                    return



        ##################################################################################################################

        if management not in db_manager:return
     #   self.calculate_hma_base()
        #self.calculate_sma()
     #   self.calculate_hma_base2()#update thehre 
     #   self.calculate_sma2()
    #    adxdb = self.calculate_adx()
       # print(adxdb)
      #  print(self.hma_values)
      #  print(self.sma_values)

        ################################
#        base_tf= self.tf
#        self.tf=higher_time_frames[base_tf].split(":")[0]
#        self.synctf=int(higher_time_frames[base_tf].split(":")[1])
#        print("motherfucker")
#        print(self.synctf)
#        print(self.tf)
#        self.PREPARE_REQUEST(confirmation=True)
#        self.calculate_hma_base2()
#        self.calculate_sma2()
#        self.tf=base_tf


        #################################
        balance = 0
        win_trades=0
        loss_trades=0
        counter=0
        self.first_trade_timestamp=None
        #######################
        checkpoint=22
        prev_checkpoint=None
        #######################
        buy_trades=0
        sell_trades=0
        draw_counter=0
        max_drawdown=0
        max_profit=0
        profit_counter=0
        duplicated_drawdown =0
        r1_trades =0
        #------------------
        total_profit=0
        total_losses=0
        #-------------------
        be25=0
        BE =0
    #-----------------------------SELLLLLLLLLLL------------------------
        #while True:
        buffer=0
        check_buffer=None
        win_signature=[{21: 6}, {19: 10}, {18: 10}, {26: 25}, {27: 16}, {12: 8}, {15: 13}, {13: 7}, {23: 7}, {27: 9}, {13: 8}, {26: 18}, {15: 7}, {18: 14}, {14: 6}, {16: 8}, {10: 8}, {26: 12}, {11: 7}, {12: 7}, {14: 6}, {27: 11}, {13: 10}, {18: 14}, {18: 12}, {15: 12}, {17: 7}, {15: 11}, {11: 6}, {11: 7}, {21: 16}, {12: 8}, {27: 18}, {25: 14}, {24: 15}, {29: 20}, {17: 6}, {12: 7}, {22: 8}, {20: 17}, {24: 13}, {27: 9}, {15: 6}, {25: 7}, {16: 8}, {16: 11}, {21: 9}, {21: 18}, {24: 6}, {15: 8}, {11: 6}, {12: 6}, {12: 9}, {16: 9}, {10: 9}, {20: 15}, {20: 17}, {16: 12}, {26: 14}, {17: 11}, {17: 14}, {25: 25}, {13: 7}, {28: 15}, {11: 9}, {14: 8}, {14: 10}, {10: 6}, {10: 6}, {14: 14}, {22: 7}, {14: 11}, {19: 10}, {20: 17}, {14: 11}, {24: 14}, {11: 6}, {15: 9}, {11: 8}, {16: 14}, {18: 6}, {16: 10}, {17: 8}, {10: 8}, {20: 14}, {12: 6}, {17: 6}, {14: 10}, {19: 20}, {24: 7}, {18: 6}, {24: 11}, {11: 8}, {20: 17}, {17: 6}, {24: 9}, {15: 8}, {24: 15}, {15: 12}, {14: 12}, {15: 7}, {16: 7}, {23: 15}, {19: 8}, {11: 7}, {14: 12}, {16: 9}, {15: 8}, {17: 12}, {10: 8}, {16: 10}, {22: 10}]
                #2024 gg [{12: 6}, {23: 17}, {23: 21}, {16: 11}, {10: 7}, {14: 6}, {25: 24}, {20: 19}, {13: 8}, {17: 14}, {10: 6}, {14: 12}, {15: 11}, {17: 10}, {12: 7}, {16: 6}, {14: 7}, {26: 7}, {19: 15}, {13: 6}, {21: 21}, {19: 7}, {11: 9}, {12: 8}, {10: 10}, {21: 6}, {19: 10}, {18: 10}, {26: 25}, {27: 16}, {15: 13}, {13: 7}, {23: 7}, {27: 9}, {26: 18}, {15: 7}, {18: 14}, {16: 8}, {10: 8}, {26: 12}, {11: 7}, {27: 11}, {13: 10}, {18: 12}, {15: 12}, {17: 7}, {11: 6}, {21: 16}, {27: 18}, {25: 14}, {24: 15}, {29: 20}, {17: 6}, {22: 8}, {20: 17}, {24: 13}, {15: 6}, {25: 7}, {21: 9}, {21: 18}, {24: 6}, {15: 8}, {28: 11}, {17: 11}, {16: 9}, {17: 9}, {20: 6}, {27: 12}, {25: 15}, {24: 9}, {22: 6}, {19: 6}, {15: 9}, {18: 8}, {29: 6}, {18: 7}, {16: 7}, {23: 18}, {11: 8}, {21: 13}, {28: 21}, {13: 9}, {18: 9}, {23: 15}, {25: 12}, {12: 12}, {10: 9}, {15: 14}, {12: 9}, {20: 15}, {16: 12}, {26: 14}, {25: 25}, {28: 15}, {14: 8}, {14: 10}, {14: 14}, {22: 7}, {14: 11}, {24: 14}, {16: 14}, {18: 6}, {16: 10}, {17: 8}, {20: 14}, {19: 20}, {24: 7}, {24: 11}, {27: 13}, {19: 8}, {22: 10}, {17: 12}, {13: 19}, {18: 39}, {24: 19}, {21: 14}, {26: 16}, {29: 14}, {20: 9}, {28: 26}, {21: 10}, {17: 28}, {20: 8}, {13: 52}, {17: 15}, {21: 8}, {25: 18}, {29: 10}, {27: 8}, {23: 13}, {23: 8}, {24: 10}, {14: 9}, {21: 49}, {27: 17}, {13: 11}, {18: 15}, {26: 9}, {28: 14}, {29: 23}, {17: 16}, {25: 17}, {28: 9}, {16: 13}, {24: 16}]
        #2022loss_times=[{14: 13}, {24: 15}, {15: 6}, {12: 6}, {11: 7}, {14: 11}, {16: 11}, {18: 8}, {25: 18}, {24: 17}, {12: 6}, {11: 6}, {10: 7}, {22: 16}, {28: 27}, {13: 8}, {24: 19}, {11: 9}, {13: 12}, {24: 6}, {13: 8}, {13: 9}, {13: 11}, {12: 6}, {23: 17}, {23: 21}, {16: 11}, {10: 7}, {14: 6}, {25: 24}, {20: 19}, {13: 8}, {17: 14}, {10: 6}, {14: 12}, {15: 11}, {17: 10}, {12: 7}, {16: 6}, {14: 7}, {26: 7}, {19: 15}, {13: 6}, {10: 7}, {21: 21}, {19: 7}, {12: 6}, {11: 9}, {12: 8}, {10: 10}, {21: 6}, {19: 10}, {18: 10}, {26: 25}, {27: 16}, {12: 8}, {15: 13}, {13: 7}, {23: 7}, {27: 9}, {13: 8}, {26: 18}, {15: 7}, {18: 14}, {14: 6}, {16: 8}, {10: 8}, {26: 12}, {11: 7}, {12: 7}, {14: 6}, {27: 11}, {13: 10}, {18: 14}, {18: 12}, {15: 12}, {17: 7}, {15: 11}, {11: 6}, {11: 7}, {21: 16}, {12: 8}, {27: 18}, {25: 14}, {24: 15}, {29: 20}, {17: 6}, {12: 7}, {22: 8}, {20: 17}, {24: 13}, {27: 9}, {15: 6}, {25: 7}, {16: 8}, {16: 11}, {21: 9}, {21: 18}, {24: 6}, {15: 8}, {28: 11}, {17: 11}, {16: 9}, {17: 9}, {20: 6}, {13: 6}, {21: 9}, {27: 12}, {25: 15}, {24: 9}, {22: 6}, {14: 7}, {19: 10}, {16: 8}, {19: 6}, {15: 9}, {15: 7}, {18: 8}, {29: 6}, {17: 14}, {18: 7}, {14: 6}, {11: 6}, {16: 7}, {17: 6}, {18: 7}, {23: 18}, {11: 8}, {21: 13}, {24: 6}, {28: 21}, {22: 8}, {22: 8}, {10: 6}, {19: 6}, {11: 8}, {20: 7}, {22: 18}, {24: 19}, {13: 11}, {18: 11}, {11: 8}, {14: 11}, {22: 11}, {11: 6}, {18: 7}, {21: 7}, {11: 8}, {14: 8}, {16: 12}, {10: 6}, {10: 8}, {12: 6}, {15: 10}, {15: 12}, {11: 7}, {16: 11}, {21: 17}, {10: 6}, {19: 17}, {12: 10}, {13: 9}, {18: 9}, {23: 15}, {11: 6}, {11: 8}, {11: 9}, {25: 12}, {12: 12}, {14: 7}, {10: 9}, {11: 8}, {11: 6}, {10: 8}, {12: 7}, {15: 14}, {11: 6}, {12: 6}, {12: 9}, {16: 9}, {10: 9}, {20: 15}, {20: 17}, {16: 12}, {26: 14}, {17: 11}, {17: 14}, {25: 25}, {13: 7}, {28: 15}, {11: 9}, {14: 8}, {14: 10}, {10: 6}, {10: 6}, {14: 14}, {22: 7}, {14: 11}, {19: 10}, {20: 17}, {14: 11}, {24: 14}, {11: 6}, {15: 9}, {11: 8}, {16: 14}, {18: 6}, {16: 10}, {17: 8}, {10: 8}, {20: 14}, {12: 6}, {17: 6}, {14: 10}, {19: 20}, {24: 7}, {18: 6}, {24: 11}, {11: 8}, {20: 17}, {17: 6}, {24: 9}, {15: 8}, {24: 15}, {15: 12}, {14: 12}, {15: 7}, {16: 7}, {23: 15}, {27: 13}, {19: 8}, {22: 10}, {17: 10}, {11: 7}, {14: 12}, {16: 9}, {15: 11}, {15: 8}, {17: 12}, {10: 8}, {16: 10}, {22: 10}, {13: 19}, {18: 39}, {24: 19}, {12: 7}, {21: 14}, {26: 16}, {14: 6}, {29: 14}, {20: 9}, {26: 16}, {28: 26}, {15: 11}, {15: 11}, {21: 10}, {18: 10}, {17: 28}, {20: 8}, {13: 52}, {21: 18}, {14: 11}, {13: 9}, {17: 15}, {27: 11}, {17: 7}, {21: 8}, {17: 10}, {11: 7}, {15: 7}, {12: 6}, {20: 19}, {27: 11}, {25: 18}, {29: 10}, {27: 8}, {18: 14}, {23: 13}, {23: 8}, {23: 15}, {24: 10}, {10: 10}, {15: 8}, {23: 18}, {17: 6}, {17: 10}, {12: 6}, {24: 13}, {14: 9}, {10: 7}, {21: 49}, {27: 16}, {27: 17}, {13: 11}, {18: 15}, {26: 9}, {28: 14}, {10: 6}, {11: 8}, {29: 23}, {12: 9}, {17: 8}, {11: 8}, {20: 15}, {28: 15}, {17: 16}, {25: 17}, {28: 9}, {17: 6}, {13: 7}, {16: 13}, {24: 16}, {13: 6}]
        #win_times=[]
        for candle in self.db[checkpoint:]:
            checkpoint = self.db.index(candle)
            if self.hma_values[checkpoint]<self.hma_values[checkpoint-1] and  self.hma_values[checkpoint-1]> self.hma_values[checkpoint-2] and  self.hma_values[checkpoint-4]> self.hma_values[checkpoint-5]:
            #if counter ==0 :
#            if self.sma_values[checkpoint-1]<self.hma_values[checkpoint-1] and self.sma_values[checkpoint]>self.hma_values[checkpoint]:#sell signal
#                if  self.sma_values2[-1]>self.hma_values2[-1]:#sell signal higher time frame
#                    if prev_checkpoint==None: prev_checkpoint=  checkpoint;continue 
                  #  ind =self.db.index(candle)
                 #   if float(candle["close"]) > self.sma_values2[ind]:continue


#                    if adxdb[checkpoint] ==None or d_line[checkpoint]==None : continue
#                    if adxdb[checkpoint]>20  and  d_line[checkpoint]<20:continue
                    if self.hma_values3[checkpoint] > self.hma_values2[checkpoint] and adxdb[checkpoint] > 45: continue
                    if adxdb[checkpoint] < 20 : continue
					if  self.hma_values4[checkpoint] > self.hma_values4[checkpoint-1]:continue


#                    engulf =None 
#                    wicks = None  
#                    wicks_nbr = 0
#                    temp_lisst = []
#                    for k in self.db[checkpoint-5:checkpoint]:
#                        if (float(k["open"])-float(k["close"])) < 0 :#bullich cndl = True
#
#                            start1 = float(k["close"])
#                            end1 = float(k["high"])
#                            temp_lisst.append((start1,end1))
#                        else:#sell_cndl = True
#                            start1=float(k["open"])
#                            end1=float(k["high"])
#                            temp_lisst.append((start1,end1))#
###
#
#                        #if abs(float(candle["high"])-float(candle["close"])) > abs(float(candle["open"])-float(candle["close"])) :
#                            #wicks =True 
#                            #wicks_nbr+=1
#                    check= self.count_range_intersections(temp_lisst)
                   # print("CHECKER = {}".format(check))
                  #  if checkpoint - prev_checkpoint<5:continue
                    entry = float(self.db[checkpoint]["close"])
                    #if adxdb[checkpoint] < 20 :continue
                    temp_lst =[]
                    for k in self.db[checkpoint-5:checkpoint+1]:
                        temp_lst.append(float(k["high"])) 
                   # try:
                    sl = max (temp_lst)
                   # except ValueError : print("SELL TRADE SKIPPED SELF SL");break
                    stop_distance = abs (entry-sl)
                  #  if stop_distance >=5:continue
             #       prev_checkpoint=  checkpoint  ########may be should be deletted after confiroming useless
                   # if stop_distance >45:continue
                    tp1 = (entry-stop_distance)

                    tp2 = (entry-stop_distance*2)
                    ##########################################
                   # if int(entry)==int(sl):print("TRADE AVOIDED");continue
                    if abs(float(entry) -  float(sl)) >self.min_sl:print("SELL TRADE SKIPPED DUE TO SL-DISTANCE");continue
                    ############# FVG AVOIDING ###############
                    ############# FVG AVOIDING ###############
                    if (entry) == (sl): continue    ################################newly added for buy and sell 
                  #  blocked = self.is_tp_blocked(entry=entry,tp=tp2,direction="short",fvgs=fvgaps,current_index=checkpoint,atr=1)
                  #  vulnerable = self.is_sl_vulnerable(entry=entry,sl=sl,direction="short",fvgs=fvgaps,current_index=checkpoint,atr=1)
                  #  if blocked ==True : continue

                    ####################################################
 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                    start_range = None
#                    for it in range(0,50):
#                            ccv = self.db[checkpoint-it]
#                        #if ccv:
#                          #  print (ccv)
#                            if   float(ccv["close"])<=tp1:
#                                start_range=it+1
#                                #print(it)
#                                break
#                    #print(start_range)
#                    if start_range==None : continue
#                    avoid_trade=False
#                    for ci in self.db[checkpoint-start_range:checkpoint] :  
#                       # print("hoho "+ str(ci))
#                        main_indx = self.db[checkpoint-start_range:checkpoint].index(ci)#-1
#                        if main_indx==0:continue
#                      #  print("new iterrr " + str(main_indx))
#                        if (float(self.db[checkpoint-start_range:checkpoint][main_indx]["close"])-float(self.db[checkpoint-start_range:checkpoint][main_indx]["open"])) >0 :
#                          try:
#                            end=float(self.db[checkpoint-start_range:checkpoint][main_indx-1]["high"])
#                            st = float(self.db[checkpoint-start_range:checkpoint][main_indx+1]["low"])
#                            #print(abs(st-end))
#                            if abs(st-end) >= self.param: 
#                                #print("end : " +str(self.db[checkpoint-start_range:checkpoint][main_indx-1]))
#                                avoid_trade=True
#                                #print("st : " +str(self.db[checkpoint-start_range:checkpoint][main_indx+1]))
#                               # print ("start range : " +str(start_range))
#                              #  print(abs(st-end))
#                             #   print(self.db[checkpoint-start_range:checkpoint][main_indx])######
#
#                            #    print(candle["ctm"])
#                                break
#                          except Exception as e :
#                           # print("errrr"+str(e))
#                            continue
#                    if avoid_trade==True:prev_checkpoint=  checkpoint  ; continue
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    ##########################################

                    ########avoiding range trading #########

                  #  if abs(self.hma_values[checkpoint]-self.sma_values[checkpoint])<0.5:continue
                    ########################################
                    trade_entered =True 
                    counter+=1
                    sell_trades+=1
                    ################################################sell picture ##############
                  #  print("\033[33m-----------------------------------------------------------------")
                   # print("\033[31m* SELL TRADE ENTERED AT CANDLE : \033[36m{}\033[37m".format(candle["time"]))
                   # print("  ENTRY AT : {}".format(entry ))
                   # print("  STOPLOSS AT : {}".format(sl))
                   # print("  TP1 AT : {}".format(tp1))
                   # print("  TP2 AT : {}".format(tp2))
                    ###########################################################################
                    if  self.db[-1]!=candle :continue
                    print("BOOOOM")
                    indox = self.db.index(candle)
                    id__ =str(self.db[indox]["time"]) #int(float(candle["open"])+float(candle["close"])+float(candle["high"])+float(candle["low"]))
                    if id__ in ALREADY_ALERTED_TRADES:continue
                    print("COUNTER OF DB ")
                    print(len(self.db))
                    REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \nSELL SIGNAL DETECTED")

                 #   pp = self.GET_TRADE_PICTURE_FROM_CHART(signal="SELL_{}".format(self.symbol),details=[sl,entry,tp2],start_timing=int(candle["time"]))
                    #print(pp)
                    
                    pp = self.GET_MANUAL_PICTURE(type="SELL TRADE",signal="SELL_{}".format(self.symbol),candles=self.db[len(self.db)-80:],entry_index=len(self.db[len(self.db)-80:])-8,entry_price=entry,tp_price=tp2,sl_price=sl)
         
                    if pp==True:
                                 #   TOKEN = "8953744107:AAGT84f18dCY4Lwxnam1P_TixecJ9LHDuU8"
                                 #   CHAT_ID = "-1004324675339"
                                    while True:
                                        try:
                                            url = f"https://api.telegram.org/bot{TOKEN_}/sendPhoto"  
                                            with open("SELL_{}.png".format(self.symbol), "rb") as photo:
                                            #    if result_byID==True:
                                             #       data={
                                              #          "chat_id": CHAT_ID,
                                               #         "caption": "🔴 TRADING RESULT FOR THE TRADE (ID: {}) SELL {} | {} ".format(self.start,self.symbol,self.tfcc),
                                                #        # "parse_mode": "Markdown"
                                                 #       }
                                            #    else:
                                                factor =10**6
                                                data={
                                                        "chat_id": CHAT_ID,
                                                        "caption": "     🔴➖ SELL SIGNAL DETECTED ➖🔴 \n\n * ENTRY: {} \n\n * STOP_LOSS: {} \n\n * TAKE_PROFIT1: {} \n\n * TAKE_PROFIT2: {} \n\n * RUNNER? :  AFTER TP2 \n\n➖➖➖➖(ID: {})➖➖➖➖".format(math.trunc(entry*factor)/factor,math.trunc(sl*factor)/factor,math.trunc(tp1*factor)/factor,math.trunc(tp2*factor)/factor,str(id__)),
                                                        # "parse_mode": "Markdown"
                                                        }
                                                r = requests.post(
                                                    url,
                                                    data=data,
                                                    files={
                                                        "photo": photo
                                                    }
                                                ).json()
                                                print(r)
                                                if r["ok"]==True:
                                                        with open("TRADES.json","w") as w :         
                                                            db_trades[id__]={"TRADE-TYPE":"SELL_TRADE","PAIRE":self.symbol,"TIME-FRAME":self.tf,"ENTRY":math.trunc(entry*factor)/factor,"STOP-LOSS":math.trunc(sl*factor)/factor,"TP1":math.trunc(tp1*factor)/factor,"TP2":math.trunc(tp2*factor)/factor,"PR_min":self.price_min,"PR_max":self.price_max}
                                                            w.write(json.dumps(db_trades))
                                                        GITHUB_FILE(update=True,data=json.dumps(db_trades),name="TRADES")
                                                        ALREADY_ALERTED_TRADES.append(id__)
                                                        break
                                        except Exception as e :  print("RECIVED RSP" +str(e))



                    ###########################################################################
                    
                    continue
                    for c in self.db[len(self.db)-80:][checkpoint:]:
                        
                        if float(c["high"])>=sl:
                
                            print("  SELL SL -50$")
                            balance-=50
                            loss_trades+=1
                            total_losses+=50
                            profit_counter=0
                            draw_counter+=1
                            if max_drawdown<draw_counter:
                                max_drawdown=draw_counter
                            break
                        if float(c["low"])<=tp2:
                            print("  SELL TP +100$")
                            balance+=100
                            win_trades+=1
                            total_profit+=100
                            profit_counter+=1
                            if max_profit<=profit_counter:
                                max_profit=profit_counter
                                duplicated_drawdown+=1
                            draw_counter=0
                            break
                    prev_checkpoint=  checkpoint   
                    #print("\033[31m* SELL TRADE CLOSED AT CANDLE : \033[36m{}\033[37m".format(c["time"])) 
                    #print("\033[33m-----------------------------------------------------------------")  
            if self.hma_values[checkpoint]>self.hma_values[checkpoint-1] and  self.hma_values[checkpoint-1]<self.hma_values[checkpoint-2] and  self.hma_values[checkpoint-4]<self.hma_values[checkpoint-5]: 
#            if self.sma_values[checkpoint-1]>self.hma_values[checkpoint-1] and self.sma_values[checkpoint]<self.hma_values[checkpoint]:#buy signal
#                if  self.sma_values2[-1]<self.hma_values2[-1]:#buy signal higher time frame 2 
#                    if prev_checkpoint==None: prev_checkpoint=  checkpoint;continue
                   # ind =self.db.index(candle)
                    #if float(candle["close"]) < self.sma_values2[ind]:continue
                    #if adxdb[checkpoint] ==None or adxdb[checkpoint]<20 : continue

#                    if adxdb[checkpoint] ==None or d_line[checkpoint]==None : continue
#                    if adxdb[checkpoint]>20  and  d_line[checkpoint]>80:continue
                    if self.hma_values3[checkpoint] < self.hma_values2[checkpoint] and adxdb[checkpoint] > 45: continue
                    if adxdb[checkpoint] < 20 : continue
					if  self.hma_values4[checkpoint] < self.hma_values4[checkpoint-1]:continue


#                    engulf =None 
#                    wicks = None  
#                    wicks_nbr = 0
#                    temp_lisst = []
#                    for k in self.db[checkpoint-5:checkpoint]:
#                        if (float(k["open"])-float(k["close"])) < 0 :#bullich cndl = True
#
#                            start1 = float(k["low"])
#                            end1 = float(k["open"])
#                            temp_lisst.append((start1,end1))
#                        else:#sell_cndl = True
#                            start1=float(k["low"])
#                            end1=float(k["close"])
#                            temp_lisst.append((start1,end1))
#
#
#                        #if abs(float(candle["high"])-float(candle["close"])) > abs(float(candle["open"])-float(candle["close"])) :
#                            #wicks =True 
#                            #wicks_nbr+=1
#                    check= self.count_range_intersections(temp_lisst)
#                    #print("CHECKER = {}".format(check))
               #     if  checkpoint - prev_checkpoint<2 :continue

                    entry = float(self.db[checkpoint]["close"])
                    #if adxdb[checkpoint] < 20 :continue
                    temp_lst =[]
                    for k in self.db[checkpoint-5:checkpoint+1]:
                        temp_lst.append(float(k["low"])) 
                    #try:
                    sl = min (temp_lst)
                    #except ValueError : print("BUY TRADE SKIPPED SELF SL");break
                    stop_distance = abs (entry-sl)
                  #  if stop_distance >=5:continue
                    #prev_checkpoint=  checkpoint###################may should be removed !
                  #  if stop_distance >45:continue
                    tp1 = (entry+stop_distance)
                    tp2 = (entry+stop_distance*2)
                    ##########################################
                    if (entry) == (sl): continue 
                    if abs(float(entry) -  float(sl)) >self.min_sl:print("BUY TRADE SKIPPED DUE TO SL-DISTANCE");continue
                    ############# FVG AVOIDING ###############
                 #   if int(entry) == int(sl): continue    ################################newly added for buy and sell 
           #         blocked = self.is_tp_blocked(entry=entry,tp=tp2,direction="long",fvgs=fvgaps,current_index=checkpoint,atr=1)
            #        vulnerable = self.is_sl_vulnerable(entry=entry,sl=sl,direction="long",fvgs=fvgaps,current_index=checkpoint,atr=1)
             #       if blocked ==True : continue
  
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                    start_range = None
#                    for it in range(0,50):
#                            ccv = self.db[checkpoint-it]
#                        #if ccv:
#                            if float(ccv["close"])>=tp1:
#                                start_range=it+1
#                                break
#                    if start_range==None : continue
#                    avoid_trade=False
#                    #print(self.db[checkpoint-start_range:checkpoint])
#                    for ci in self.db[checkpoint-start_range:checkpoint] :
#                        main_indx = self.db[checkpoint-start_range:checkpoint].index(ci)
#                        if main_indx==0:continue
#                        if (float(self.db[checkpoint-start_range:checkpoint][main_indx]["close"])-float(self.db[checkpoint-start_range:checkpoint][main_indx]["open"])) <0 :
#                          try:
#                            end=float(self.db[checkpoint-start_range:checkpoint][main_indx-1]["low"])
#                            st = float(self.db[checkpoint-start_range:checkpoint][main_indx+1]["high"])
#                            #print (start_range)
#                            #print(abs(st-end))
#                            if abs(st-end) >= self.param: 
#                               # print (start_range)
#                               # print(abs(st-end))
#                               # print(candle["ctm"])
#                                avoid_trade=True
#                                break##
#
#                          except Exception as e :continue
#                        
#                    if avoid_trade==True: prev_checkpoint=  checkpoint  ;continue
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    ##########################################
                    ###LETS AVOID THE RANGE TRADING ######

                  #  if abs(self.hma_values[checkpoint]-self.sma_values[checkpoint])<0.5:continue
                    #############################################################################
                #    print("\033[33m-----------------------------------------------------------------")
               #     print("\033[32m* BUY TRADE ENTERED AT CANDLE : \033[36m{}\033[37m".format(candle["time"]))
              #      print("  ENTRY AT : {}".format(entry ))
             #       print("  STOPLOSS AT : {}".format(sl))
            #        print("  TP1 AT : {}".format(tp1))
           #         print("  TP2 AT : {}".format(tp2))
                    trade_entered =True
                    buy_trades+=1    
                    counter+=1
                    ##########################################
                    #print(candle)
                    #print(self.db[-1])
                    if  self.db[-1]!=candle :continue
                    print("BOOOOM")
                    indox = self.db.index(candle)
                    id__ = str(self.db[indox]["time"])  #int(time.time()) candle["ctm"] #int(float(candle["open"])+float(candle["close"])+float(candle["high"])+float(candle["low"]))
                    if id__ in ALREADY_ALERTED_TRADES:continue
                    REQUEST_("https://api.telegram.org/bot"+TOKEN_+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=Markdown&text=[········🔥MARKETS_TRACKER_BOT🔥········](https://t.me/MARKETS_SIGNALS) \nBUY SIGNAL DETECTED")
                    print("COUNTER OF DB ")
                    print(len(self.db))
                    ########################################## picture ##########################   
         # v1          #pp = self.GET_TRADE_PICTURE_FROM_CHART(signal="BUY_{}".format(self.symbol),details=[sl,entry,tp2],start_timing=int(candle["time"]))
                    
                    pp = self.GET_MANUAL_PICTURE(type="LONG TRADE",signal="BUY_{}".format(self.symbol),candles=self.db[len(self.db)-80:],entry_index=len(self.db[len(self.db)-80:])-8,entry_price=entry,tp_price=tp2,sl_price=sl)
                
                    if pp==True:
                                 #   TOKEN = "8953744107:AAGT84f18dCY4Lwxnam1P_TixecJ9LHDuU8"
                                #    CHAT_ID = "-1004324675339"
                                    while True:
                                        try:

                                            url = f"https://api.telegram.org/bot{TOKEN_}/sendPhoto"
                                            with open("BUY_{}.png".format(self.symbol), "rb") as photo:
                                        #        if result_byID==True:
                                         #           data={
                                          #              "chat_id": CHAT_ID,
                                           #             "caption": "🟢 TRADING RESULT FOR THE TRADE (ID: {}) BUY {} | {} ".format(self.start,self.symbol,self.tfcc),
                                            #            # "parse_mode": "Markdown"
                                             #           }
                                              #  else :
                                                factor =10**6
                                                data={
                                                        "chat_id": CHAT_ID,
                                                        "caption": "     🟢➖ BUY SIGNAL DETECTED ➖🟢 \n\n * ENTRY: {} \n\n * STOP_LOSS: {} \n\n * TAKE_PROFIT1: {} \n\n * TAKE_PROFIT2: {} \n\n * RUNNER? :  AFTER TP2 \n\n➖➖➖➖(ID: {})➖➖➖➖".format(math.trunc(entry*factor)/factor,math.trunc(sl*factor)/factor,math.trunc(tp1*factor)/factor,math.trunc(tp2*factor)/factor,str(id__)),
                                                        # "parse_mode": "Markdown"
                                                    }
                                                r = requests.post(
                                                    url,
                                                    data=data,
                                                    files={
                                                        "photo": photo
                                                    }
                                                ).json()
                                                print(r)
                                                if r["ok"]==True:
                                                        with open("TRADES.json","w") as w :         
                                                            db_trades[id__]={"TRADE-TYPE":"BUY_TRADE","PAIRE":self.symbol,"TIME-FRAME":self.tf,"ENTRY":math.trunc(entry*factor)/factor,"STOP-LOSS":math.trunc(sl*factor)/factor,"TP1":math.trunc(tp1*factor)/factor,"TP2":math.trunc(tp2*factor)/factor,"PR_min":self.price_min,"PR_max":self.price_max}
                                                            w.write(json.dumps(db_trades))
                                                        GITHUB_FILE(update=True,data=json.dumps(db_trades),name="TRADES")
                                                        ALREADY_ALERTED_TRADES.append(id__)
                                                        break
                                        except Exception as e : print("RECIVED RSP" +str(e))





                    continue
                    for c in self.db[checkpoint:]:
                        if float(c["low"])<=sl:
                            print("  BUY SL -50$")
                            balance-=50
                            loss_trades+=1
                            profit_counter=0
                            draw_counter+=1
                            if max_drawdown<draw_counter:
                                max_drawdown=draw_counter
                            break
                        if float(c["high"])>=tp2:
                            print("  BUY TP +100$")
                            balance+=100
                            win_trades+=1
                            total_profit+=100
                            profit_counter+=1
                            if max_profit<=profit_counter:
                                max_profit=profit_counter
                                duplicated_drawdown+=1
                            draw_counter=0    
                            break
                   # prev_checkpoint=  checkpoint   
                  #  print("\033[32m* BUY TRADE CLOSED AT CANDLE : \033[36m{}\033[37m".format(c["time"])) 
                  #  print("\033[33m-----------------------------------------------------------------")  
       except Exception as e :
        error = traceback.format_exc()
        print("hihi "+str(error))
        #if 


                

                














       # sell_trades+=(counter-buy_trades)
     #   average_win=total_profit/win_trades
      #  average_loss=total_losses/loss_trades
        #win_rate=(win_trades/counter)*100
        #loss_rate=(loss_trades/counter)*100
        #expectency=((win_rate/100)*average_win)-(average_loss*(loss_rate/100))
        #profit_factor = (100*win_trades)/(50*loss_trades)
#################################################################################
        #print("\033[33m|--------------------------------\033[36mSTATS OF THE BACKTEST\033[33m ---------------------")
                                                                                                              
       # print("\033[37m|TOTAL BALANCE AFTER \033[32m{} \033[37mTRADES  WAS \033[32m{} $".format(str(counter),str(balance)))
       # print("\033[37m|RATIO GAIN/PERTE : \033[32m{} \033[37mWINNERS | \033[32m{} \033[37mLOSSERS IN TOTAL OF\033[33m {} \033[37m| BE : \033[32m{}".format(str(win_trades),str(loss_trades),str(counter),str(be25)))
       # print("\033[37m|ASSET/TIME-FRAME : \033[32m{}/{} TF".format(self.symbol,self.tf))
       # print("\033[37m|BUY-TRADES : \033[32m{} \n\033[37m|SELL-TRADES: \033[32m{} ".format(str(buy_trades),str(sell_trades)))
       # print("\033[37m|WIN RATE : \033[32m"+str(int(win_rate))+ "%")
        #print("\033[37m|MAX_DRAWDOWN : \033[31m{} \033[37mTRADES".format(max_drawdown))
        #print("\033[37m|MAX_PROFIT \033[32m{} \033[37mTRADES".format(str(max_profit)))
        #print("\033[37m|PROFIT_FACTOR \033[32m{}".format(str(profit_factor)))
       # print("\033[37m|EXPECTENCY : \033[36m{}".format(expectency))
   #     print("\033[37m|AVERAGE_WIN : \033[36m{}".format(average_win))
    #    print("\033[37m|AVERAGE_LOSS: \033[36m{}".format(average_loss))


       # print("\033[37m|1R-TRADES : \033[36m{}".format(r1_trades))
        #print("\033[37m|2R-TRADES : \033[36m{}".format(counter-r1_trades-loss_trades))
    #    print("\033[37m|NUMBER OF BE: \033[36m{} | {}$".format(be25,be25*25))
    #    print("\033[37m|BACKTEST FROM :  \033[32m{}  \033[37mTO :  \033[32m{}\033[37m".format(str(self.first_trade_timestamp),str(end_trade_timestamp) ))
   #     print("\033[33m-----------------------------------------------------------------------------\033[37m")

       # print(buffer)
        #print(loss_times)
        #print(win_signature)









         #print("STARTING BALANCE : 0$ FINAL BALANCE AFTER ALL TRADES WAS : "+str(total_balance)+"$")
         #win_rate=(win_trades/counter)*100
         #print(win_rate)
        # print("TOTAL-TRADES:"+str(counter)+" | WINNERS:"+str(win_trades)+" | LOSSERS:"+str(loss_trades )+" | WINRATE: "+str(win_rate))
         #print("DRAWDOWN : {} : WITH TOTAL PERPETUAL LOSS OF {} $ ".format(max_drawdown/50,max_drawdown))
         #print("MOYENNE DE BODY DES WINING TRADES WAS : ",moy/tt)
         #print(tt)
           # if stop_distance>0:

            #space = round((abs((float(i["open"])-float(i["close"]))/float(i["open"]))*100),2)
#            
  
#                     input()
#                     print("\033[0m_____________________________________________________") 
 #                    print(st)
#                     print(end)
#                     input()
#                     print(i)
#                       print("semi fvg")
 #                       if  total_db[next_cndl]["high"] not in rng: 
  #                          print ("FVG FOUND : ",i)

timeframes=[
{"name":"30M","value":60},
#{"name":"30M","value":30},
#{"name":"1H","value":1*60},
#{"name":"4H","value":4*60}
]
#xauusd >=12:3       1754065205   307 trades  61%/70%  4 drawdown of 200$ 
#XAG 0.5|0.1    bad    >>    <=0.7|0.1        59%/73%  261 trades    1754065205
#eurusd <=0.00180:0.00030     1754065205  364 TRADES  56%|71%
#usdjpy <=0.450| 0.1   1754065205 239 trades / 76% |57% 
#with open("config.json","r") as r :
 #    paires =json.loads(r.read())
#paires =["XAUUSD"] #,"NZDJPY","USDCAD","USDCHF","USDMXN","USDGBP"]
#for pair in paires:
#    for tf in timeframes :
#        print("\033[37m----------------- \033[36m| \033[33m\033[41m{}\033[40m \033[36m|\033[33m\033[41m {} \033[36m\033[40m|\033[40m\033[37m ---------------".format(pair,tf["name"]))
      #  print("STARTING WITH TF  ",tf)
 #       starter = GET_CNDLSTICKS_CHART(tf["value"],1704114000,int(time.time()),pair)
      #  starter.PREPARE_REQUEST()
  #      starter.CHECK_FVG_AVAILABILITY()
   # break
#1704114000: 2024
#1754065205 1 ans august

try:
    open("db.json","r")
except FileNotFoundError:
    with open("db.json","w") as w :
        w.write("[]")
#######################
response0= GITHUB_FILE(update=False,data=None,name="TRADES")
with open("TRADES.json","w") as w :
        w.write(json.dumps(response0))
#######################
try:
    open("TRADES.json","r")
except FileNotFoundError:
    with open("TRADES.json","w") as w :
        w.write("{}")
with open("TRADES.json","r") as r :
    db_trades =json.loads(r.read())
    #db_trades={1788310620: {"TRADE-TYPE":"BUY_TRADE","PAIRE":"XAUUSD","TIME-FRAME":1,"ENTRY":round(4317.74,5),"STOP-LOSS":round(4314.59,5),"TP1":round(4313.38,5),"TP2":round(4323.35,5)}}
    #print(db_trades)
####################################
response1= GITHUB_FILE(update=False,data=None,name="db")
with open("db.json","w") as w :
        w.write(json.dumps(response1))
#####################################
with open("db.json","r") as r :
    dito =json.loads(r.read())
    db_manager=dito
    print(db_manager)
    for runner  in dito :
            sti=liss[runner["TIMEFRAME"]]
            starter = GET_CNDLSTICKS_CHART(runner["TIMEFRAME"],runner["TF-NAME"],int(time.time())-sti,int(time.time())+8*3600,runner["PAIRE"],runner["SETTINGS"],runner["MIN-SL"])
            sti = threading.Thread(target=starter.CHECK_FVG_AVAILABILITY,args=(runner,runner["TIMING"],False))
            sti.start()

MAIN_TELEGRAM_RESPONDER()




