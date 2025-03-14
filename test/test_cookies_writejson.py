from libs.JsonFileFactory import JsonFileFactory
from models.Product import Cookies

cookies=[]
cookies.append(Cookies("CB19","Classic Choco Chip",35000,0,"","D:/FinalProject/images/classic_choco_chip.png"))
cookies.append(Cookies("CB20","Dark Mix",40000,0,"","D:/FinalProject/images/dark_mix.png"))
cookies.append(Cookies("CB21","Cookies&Cream",45000,0,"","D:/FinalProject/images/cookies_cream.png"))
cookies.append(Cookies("CB22","Creamy Matcha",45000,0,"","D:/FinalProject/images/creamy_matcha.png"))
cookies.append(Cookies("CB23","Twisted Love",45000,0,"","D:/FinalProject/images/twisted_love.png"))
cookies.append(Cookies("CB24","Oreo Chocolate",45000,0,"","D:/FinalProject/images/oreo_chocolate.png"))
print("List of cookies:")
for c in cookies:
    print(c)
filename="cookies.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
jff.write_data(cookies,path)