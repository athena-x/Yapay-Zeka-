import pyttsx3
import os
import time
import socket
import sys
import re
import requests
banner = """

Yapay Zeka Protokolüne Hoşgeldin

"""
print(banner)
os.system('cls')
engine = pyttsx3.init()
engine.say(' Yeni tooluma hosgeldin')
engine.runAndWait()
engine.say('What was your name ?')
engine.runAndWait()
b = input('Adın ney morukk ? :')
engine.say('Memnun oldum bende Athenanın kölesi'+b)
engine.runAndWait()
engine.say('Ee ne yapmak istersin ? sana secenekler sundum')
engine.runAndWait()
a = input("""

{1}Sql açıklı site ara
{2}Athena'yı sik
{3}Acık ara
{4}Admin Paneli Bul [Bakımda]
{5}Xss Açığı Ara
{6}Blogspot Zaafiyeti
{7}ÇIK GİT
{8}Reverse Ip LookUp""")
if a == "1":
    engine.say('Siktirr tamam lan tamam')
    engine.runAndWait()
    if sys.platform == 'win32':
        engine.say('Seni  gidi  aptal  kos  linuxa')
        engine.runAndWait()
        exit()
if a == "2":
    engine.say('I am so lovely with my owner you dumb !')
    engine.runAndWait()
if a == "3":
    engine.say('Hedef site at yaslı')
    engine.runAndWait()
    c = input('Hedef site yaşlı')
    engine.say('Bu arada linuxa git')
    engine.runAndWait()
    os.system('nikto -h'+c)
if a == "4":
    engine.say('Site at')
    engine.runAndWait()
    d = input('Site linki :')
    r = requests.get(d+"/admin")
    print(r.url["Doğru Link Olabilir !"])
if a == "5":
    engine.say('Site')
    engine.runAndWait()
    e = input('Site adresi :')
    r = requests.get(e+"<h1>hacked by athena</h1>")
    if "hacked by athena" in r.text:
        print(r.url ["Xss Açığı Bulundu"])
if a == "6":
    engine.say('Bana liste at ')
    engine.runAndWait()
    f = input('Blogspot olan site listesi at varmı elinde liste ?')
    if f == "hayır":
        engine.say('Git bul banane amına koyim')
        engine.runAndWait()
        os.system('exit')
if a == "7":
    engine.say('Siktir git')
    engine.runAndWait()
    os.system("exit")
if a == "8":
    engine.say('Site link')
    engine.runAndWait()
    g = input('hedef link example.com')
    r = requests.get("https://api.hackertarget.com/reverseiplookup/?q="+g)
    print(r.text)
