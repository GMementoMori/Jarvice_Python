import pyowm
from colorama import init
import random
import time
import pyautogui
from gtts import gTTS
from playsound import playsound
from colorama import Fore, Back, Style
def all():
  
 def jarvice_weather():

   owm = pyowm.OWM('ebf37974297c176754ec62e0ac3fce61')

   print(Back.GREEN + "Прогноз погоды запущщен...")

   place = input(Back.GREEN + "Take your city: ")

   observation = owm.weather_at_place(place)
   w = observation.get_weather()
   s = w.get_status()
   temp = w.get_temperature('celsius')['temp']
   flo = int(temp)
   print('Температура в раёне: ' + str(flo))


   if s == "Clouds":
     s_place = "В " + place + " довольно облачно"
     s_wolk = "Возможен дождь, лучше берите зонтик!"
     s_tem = 'Температура в раёне ' + str(flo) + "градуса по цельсию"

     speak_weather = s_place + s_wolk + s_tem
     tts = gTTS(speak_weather, lang='ru')
     tts.save('file.mp3')
     playsound('/root/Python/Jarvice/file.mp3')

   elif s == "Clear":
     s_place = "В " + place + " чистое небо"
     s_wolk = "Спокойной выходите на улицу"
     s_tem = 'Температура в раёне ' + str(flo) + "градуса по цельсию"

     speak_weather = s_place + s_wolk + s_tem
     tts = gTTS(speak_weather, lang='ru')
     tts.save('file.mp3')
     playsound('/root/Python/Jarvice/file.mp3')

   elif s == "Rain":
     s_place = "В " + place + " будет дождь"
     s_wolk = "Гулять не стоит"
     s_tem = 'Температура в раёне ' + str(flo) + "градуса по цельсию"

     speak_weather = s_place + s_wolk + s_tem
     tts = gTTS(speak_weather, lang='ru')
     tts.save('file.mp3')
     playsound('/root/Python/Jarvice/file.mp3')

 def jarvice_ask():

   print(Fore.GREEN + "Советник запущщен...")

   input(Fore.BLUE + name + " ваш вопрос: ")
 
   var0 = "  Да!"
   var1 = "  Нет!"
   var2 = "  Возможно"
   var3 = "  И не думай!"
   var4 = "  Очень вероятно"

   num = random.randrange(6)  # значение от 0 до 10

   if num == 0:
     speak_0_choise = name + var0
     tts = gTTS(speak_0_choise, lang='ru')
     tts.save('file.mp3')
     playsound('/root/Python/Jarvice/file.mp3')

     print(Fore.GREEN + name + " " + var0)

   if num == 1:
     speak_1_choise = name + var1
     tts = gTTS(speak_1_choise, lang='ru')
     tts.save('file.mp3')
     playsound('/root/Python/Jarvice/file.mp3')

     print(Fore.GREEN + name + " " + var1)

   if num == 2:
     speak_2_choise = name + var2
     tts = gTTS(speak_2_choise, lang='ru')
     tts.save('file.mp3')
     playsound('/root/Python/Jarvice/file.mp3')

     print(Fore.GREEN + name + " " + var2)

   if num == 3:
     speak_3_choise = name + var3
     tts = gTTS(speak_3_choise, lang='ru')
     tts.save('file.mp3')
     playsound('/root/Python/Jarvice/file.mp3')

     print(Fore.GREEN + name + " " + var3)

   if num == 4:
      speak_4_choise = name + var4
      tts = gTTS(speak_4_choise, lang='ru')
      tts.save('file.mp3')
      playsound('/root/Python/Jarvice/file.mp3')

      print(Fore.GREEN + name + " " + var4)

   if num == 5:

     speak_5_choise = name + " к сожалению не одного правильного варианта нет"
     tts = gTTS(speak_5_choise, lang='ru')
     tts.save('file.mp3')
     playsound('/root/Python/Jarvice/file.mp3')

     print(Fore.RED + name + " к сожалению не одного правильного варианта нет...")


 def jarvice_search() :

   print(Back.GREEN + "Креативный поисковик запущен...")
   print(Fore.RED + "Вводите запросы только латиницей!")
   print("1.Url")
   print("2.Youtube")

   searcher = input()
   if searcher == "1" :
     url = input(Fore.YELLOW + "Введите ваш запрос(На английском!): ")
 
     pyautogui.moveTo(830, 767, duration=2)
     time.sleep(1)
     pyautogui.click()
     time.sleep(2)
     pyautogui.tripleClick(553, 110, duration=3)
     pyautogui.press("del")
     pyautogui.typewrite(url)
     pyautogui.press("enter")

     speak_1_search = "Все готового " + name + " можете работатать!"
     tts = gTTS(speak_1_search, lang='ru')
     tts.save('file.mp3')
     playsound('/root/Python/Jarvice/file.mp3')

   if searcher == "2" :

     search = input(Fore.GREEN + "Введите ваш запрос(На английском!): ")
     pyautogui.moveTo(830, 767, duration=2)
     time.sleep(1)
     pyautogui.click()
     time.sleep(2)
     pyautogui.tripleClick(553, 111, duration=3)
     pyautogui.press("del")
     pyautogui.typewrite("https://youtube.com")
     pyautogui.press("enter")
     time.sleep(2)
     pyautogui.click(640, 200, duration=4)
     pyautogui.typewrite(search)
     pyautogui.press("enter")
     pyautogui.click(380, 380 , duration=4)
  
     speak_2_search = "Все готового " + name + " можете работать!"
     tts = gTTS(speak_2_search, lang='ru')
     tts.save('file.mp3')
     playsound('/root/Python/Jarvice/file.mp3')

 def talk_request() :
   talk_r = input()
   tts = gTTS(talk_r, lang='ru')
   tts.save('file.mp3')
   playsound('/root/Python/Jarvice/file.mp3')

 def oxxxy() :
   playsound('/root/Python/Jarvice/oxxxy.mp3')


 speak_1 = name + " выбирайте действие: "
 tts = gTTS(speak_1, lang='ru')
 tts.save('file.mp3')
 playsound('/root/Python/Jarvice/file.mp3')

 print(Fore.GREEN + name + " выбирайте действие: ")
 print(Fore.BLUE + "1.Погода")
 print(Fore.BLUE + "2.Советник") 
 print(Fore.BLUE + "3.Поиск для вас") 
 print(Fore.BLUE + "4.Нужно сказать") 
 print(Fore.BLUE + "5.Oxxxymiron") 

 
 task = input()

 if task == "1":
   v_pogoda = "Выбран прогноз погоды! Напишите название города латиницей!"
   tts = gTTS(v_pogoda, lang='ru')
   tts.save('file.mp3')
   playsound('/root/Python/Jarvice/file.mp3')
   jarvice_weather()
   all()

 elif task == "2":
   v_choise = "Выбран модуль советник!"
   tts = gTTS(v_choise, lang='ru')
   tts.save('file.mp3')
   playsound('/root/Python/Jarvice/file.mp3')
     
   jarvice_ask()
   all()

 elif task == "3":
   v_search = "Выбран модуль интерактивного поиска!"
   tts = gTTS(v_search, lang='ru')
   tts.save('file.mp3')
   playsound('/root/Python/Jarvice/file.mp3')
    
   jarvice_search()
   all()

 elif task == "4":
   v_voise = "Что вы хотите услышать?"
   tts = gTTS(v_voise, lang='ru')
   tts.save('file.mp3')
   playsound('/root/Python/Jarvice/file.mp3')
     
   talk_request()
   all()

 elif task == "5":
   v_oxxxy = "Включаю вам Oxxxymirona!"
   tts = gTTS(v_oxxxy, lang='ru')
   tts.save('file.mp3')
   playsound('/root/Python/Jarvice/file.mp3')
    
   oxxxy()
   all()

init(autoreset=True)
J_Run = "Jarvice running..."

print(Fore.GREEN + "{0:*^60}".format(J_Run))

print(Fore.BLUE + "Введите ваше имя: ")

name = input(Fore.GREEN)

all()