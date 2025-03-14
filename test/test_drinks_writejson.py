from libs.JsonFileFactory import JsonFileFactory
from models.Product import Cookies

drinks=[]
drinks.append(Cookies("CB25","Tira-Miss-U",55000,0,"","D:/FinalProject/images/tira_miss_u.png"))
drinks.append(Cookies("CB26","Matcha S'more",70000,0,"","D:/FinalProject/images/matcha_smore.png"))
drinks.append(Cookies("CB27","Choco S'more",65000,0,"","D:/FinalProject/images/choco_smore.png"))
drinks.append(Cookies("CB28","Lush Pear",60000,0,"","D:/FinalProject/images/lush_pear.png"))
drinks.append(Cookies("CB29","Bergamot Brew",60000,0,"","D:/FinalProject/images/bergamot_brew.png"))
print("List of drinks:")
for d in drinks:
    print(d)
filename="drinks.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
jff.write_data(drinks,path)