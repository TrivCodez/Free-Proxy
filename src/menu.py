import requests
import os
import time
import sys

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mAll")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mUSA")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mRussia")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mUkraine")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mIndia")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mItaly")
print("  # \033[1;34m[ 07 ] >> \033[1;36;40mCanada")
print("  # \033[1;34m[ 08 ] >> \033[1;36;40mFrance")
print("  # \033[1;34m[ 09 ] >> \033[1;36;40mThailand")
print("  # \033[1;34m[ 10 ] >> \033[1;36;40mPoland")
print("  # \033[1;34m[ 11 ] >> \033[1;36;40mNetherlands")
print("  # \033[1;34m[ 12 ] >> \033[1;36;40mMexico")
print("  # \033[1;34m[ 13 ] >> \033[1;36;40mKazakhstan")
print("  # \033[1;34m[ 14 ] >> \033[1;36;40mIran")
print("  # \033[1;34m[ 15 ] >> \033[1;36;40mEgypt")
print("  # \033[1;34m[ 16 ] >> \033[1;36;40mHong Kong")
print("  # \033[1;34m[ 17 ] >> \033[1;36;40mGermany")
print("  # \033[1;34m[ 18 ] >> \033[1;36;40mVietman")
print("  # \033[1;34m[ 19 ] >> \033[1;36;40mHungary")
print("  # \033[1;34m[ 20 ] >> \033[1;36;40mBrazilia")
print("  # \033[1;34m[ 21 ] >> \033[1;36;40mJapan")
print("  # \033[1;34m[ 22 ] >> \033[1;36;40mKambodia")
print("  # \033[1;34m[ 23 ] >> \033[1;36;40mChina")
print("  # \033[1;34m[ 24 ] >> \033[1;36;40mChile")
print('')
print("  # \033[1;34m[ 25 ] >> \033[1;36;40mSSL PROXY")
print("  # \033[1;34m[ 26 ] >> \033[1;36;40mSOCKS4 PROXY")
print("  # \033[1;34m[ 27 ] >> \033[1;36;40mSOCKS5 PROXY")
print("  # \033[1;34m[ 28 ] >> \033[1;36;40mUPDATE UTILITY")
print("  # \033[1;34m[ 29 ] >> \033[1;36;40mEXIT UTILITY")

op=int(raw_input("Options: "))

if(op==1):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==2):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==3):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==4):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==5):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==6):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==7):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==8):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==9):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==10):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==11):
  proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==12):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==13):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==14):
  proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==15):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==16):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==17):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==18):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==19):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==20):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==21):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==22):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==23):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==24):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==25):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==26):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==27):
 proxyDomain = ""
 system = requests.get(proxyDomain).text
 print(system)
elif(op==28):
 print("Updating tool. Please wait a moment")
 os.system("cd src")
 os.system("bash ProxyUpdater.sh")
elif(op==29):
 print("\033[1;31;40mQuiting Utility...")
 time.sleep(0.8)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1.5)
 sys.exit()
