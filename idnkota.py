import requests, json
from bs4 import BeautifulSoup
from time import sleep
import os


url = "https://ugg.idkota.com/User/User/user"
urlread1 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17595&lang=indonesian&device_id=b271bb989de4cbec"
urlread2 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17603&lang=indonesian&device_id=b271bb989de4cbec"
urlread3 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17602&lang=indonesian&device_id=b271bb989de4cbec"
urlread4 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17601&lang=indonesian&device_id=b271bb989de4cbec"
urlread5 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17600&lang=indonesian&device_id=b271bb989de4cbec"
urlread6 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17594&lang=indonesian&device_id=b271bb989de4cbec"
urlread7 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17593&lang=indonesian&device_id=b271bb989de4cbec"
urlread8 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17592&lang=indonesian&device_id=b271bb989de4cbec"
urlread9 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17591&lang=indonesian&device_id=b271bb989de4cbec"
urlread10 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17590&lang=indonesian&device_id=b271bb989de4cbec"
urlread11 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17163&lang=indonesian&device_id=b271bb989de4cbec"
urlread12 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=7925&lang=indonesian&device_id=b271bb989de4cbec"
urlread13 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=8416&lang=indonesian&device_id=b271bb989de4cbec"
urlread14 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17589&lang=indonesian&device_id=b271bb989de4cbec"
urlread15 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17643&lang=indonesian&device_id=b271bb989de4cbec"
urlread16 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17644&lang=indonesian&device_id=b271bb989de4cbec"
urlread17 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17645&lang=indonesian&device_id=b271bb989de4cbec"
urlread18 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17647&lang=indonesian&device_id=b271bb989de4cbec"
urlread19 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17648&lang=indonesian&device_id=b271bb989de4cbec"
urlread20 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17646&lang=indonesian&device_id=b271bb989de4cbec"
urlread21 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17640&lang=indonesian&device_id=b271bb989de4cbec"
urlread22 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=13608&lang=indonesian&device_id=b271bb989de4cbec"
urlread23 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17166&lang=indonesian&device_id=b271bb989de4cbec"
urlread24 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17272&lang=indonesian&device_id=b271bb989de4cbec"
urlread25 = "https://ugg.idkota.com/Content/Content/read?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17069&lang=indonesian&device_id=b271bb989de4cbec"
urlshare = "https://ugg.idkota.com/Content/Content/share?member_token=NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA%3D%3D&content_id=17603&lang=indonesian&device_id=b271bb989de4cbec"
urlconvert = "https://ugg.idkota.com/User/User/convert"

UA = {
  "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; M53 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.116 Mobile Safari/537.36"
}

data = {
  "cfduid": "d93a1e758b0c4bf7958e8b2384e2584321571589902", "PHPSESSID": "mr2sd9na6tpt8n120lj3q6ki58"
}

file = {
  "member_token": "NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA==", "device_id": "b271bb989de4cbec"
}
convert = {
"member_token": "NjIwODgyMTU0NzkxOTMtLXx8LS0yNWQzZTVlNTVjNjhiYjMzMzdlYjJiYjZkNjcyNDc0NA==", "lang": "indonesian", "device_id": "b271bb989de4cbec"
}

c = requests.Session()

def login():
    r = c.post(url, cookies=data, headers=UA, data=file)
    person_dict = json.loads(r.content)
    print ("\033[92mIIIIIIIIIIIIIIIIIIIIIIIIIIIII PROFIL IIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
    print ("\033[95mUser Name :",(person_dict["user"]["member_real_name"]))
    print ("Koin Emas :",(person_dict["user"]["member_gold"]))
    print ("Penghasilan :",(person_dict["user"]["member_income"]))

def login2():
    r = c.post(url, cookies=data, headers=UA, data=file)
    person_dict = json.loads(r.content)
    print ("\033[91mIIIIIIIIIIIIIIIIIIIIIIIIIIIII PROFIL IIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
    print ("\033[93mUser Name :",(person_dict["user"]["member_real_name"]))
    print ("Koin Emas :",(person_dict["user"]["member_gold"]))
    print ("Penghasilan :",(person_dict["user"]["member_income"]))

def read1():
    r = c.get(urlread1, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("\033[93m[✓].SUCCESS :",(person_dict["msg"]))

def read2():
    r = c.get(urlread2, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read3():
    r = c.get(urlread3, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))
    
def read4():
    r = c.get(urlread4, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read5():
    r = c.get(urlread5, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read6():
    r = c.get(urlread6, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read7():
    r = c.get(urlread7, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read8():
    r = c.get(urlread8, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read9():
    r = c.get(urlread9, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read10():
    r = c.get(urlread10, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))
    
def read11():
    r = c.get(urlread11, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read12():
    r = c.get(urlread12, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read13():
    r = c.get(urlread13, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read14():
    r = c.get(urlread14, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read15():
    r = c.get(urlread15, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read16():
    r = c.get(urlread16, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read17():
    r = c.get(urlread17, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read18():
    r = c.get(urlread18, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read19():
    r = c.get(urlread19, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read20():
    r = c.get(urlread20, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read21():
    r = c.get(urlread21, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read22():
    r = c.get(urlread22, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read23():
    r = c.get(urlread23, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))
    
def read24():
    r = c.get(urlread24, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def read25():
    r = c.get(urlread25, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("[✓].SUCCESS :",(person_dict["msg"]))

def share1():
    r = c.get(urlshare, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("\033[92m1.SUCCESS :",(person_dict["msg"]))

def share2():
    r = c.get(urlshare, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("2.SUCCESS :",(person_dict["msg"]))

def share3():
    r = c.get(urlshare, cookies=data, headers=UA)
    person_dict = json.loads(r.content)
    print ("3.SUCCESS :",(person_dict["msg"]))

def tukar():
    r = c.post(urlconvert, cookies=data, headers=UA, data=convert)
    person_dict = json.loads(r.content)
    print (">>>\033[91mTUKARKAN HASIL KEMARIN<<<")
    print ("\033[94m[√].\033[93mSUCCESS :",(person_dict["msg"]))
    
def koin():
    r = c.post(url, cookies=data, headers=UA, data=file)
    person_dict = json.loads(r.content)
    print ("[√]")
    print ("\033[93m>>\033[95mTOTAL KOIN EMAS DI DAPAT HARI INI :",(person_dict["user"]["member_gold"]))

def log1():
    print ("\033[91m>>>>>LOGIN BERHASIL BROOOOWWWWWW.........")

def log2():
    print ("\033[94mIIIIIIIIIIIIIIIIIIIIIIIIIIIIII BACA IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")

def log3():
    print ("\033[95mIIIIIIIIIIIIIIIIIIIIIIIIIIIIII SHARE IIIIIIIIIIIIIIIIIIIIIIIIIIIIII")

def log4():
    print ("\033[94mIIIIIIIIIIIIIIIIIIIIIIIIIIIIII CONVERT IIIIIIIIIIIIIIIIIIIIIIIIIIII")

def log5():
    print ("\033[95m>>>>>SUDAH SELESAI BOSSSSSSKUUUHHH...........")


os.system('clear')

def bot():
       log1()
       sleep(15)
       login()
       sleep(15)
       log4()
       sleep(15)
       tukar()
       sleep(30)
       log2()
       sleep(15)
       read1()
       sleep(40)
       read2()
       sleep(40)
       read3()
       sleep(40)
       read4()
       sleep(40)
       read5()
       sleep(40)
       read6()
       sleep(40)
       read7()
       sleep(40)
       read8()
       sleep(40)
       read9()
       sleep(40)
       read10()
       sleep(40)
       read11()
       sleep(40)
       read12()
       sleep(40)
       read13()
       sleep(40)
       read14()
       sleep(40)
       read15()
       sleep(40)
       read16()
       sleep(40)
       read17()
       sleep(40)
       read18()
       sleep(40)
       read19()
       sleep(40)
       read20()
       sleep(40)
       read21()
       sleep(40)
       read22()
       sleep(40)
       read23()
       sleep(40)
       read24()
       sleep(40)
       read25()
       sleep(40)
       log3()
       sleep(15)
       share1()
       sleep(40)
       share2()
       sleep(40)
       share3()
       sleep(40)
       koin()
       sleep(15)
       login2()
       sleep(15)
       log5()
       sleep(15)

bot()