from libs.JsonFileFactory import JsonFileFactory
from models.Product import Mousse

mousses=[]
mousses.append(Mousse("CB1","Romance Blossom",480000,0,"","D:/FinalProject/images/romance_blossom.png"))
mousses.append(Mousse("CB2","Royal Nut Harmony",480000,0,"","D:/FinalProject/images/royal_nut.png"))
mousses.append(Mousse("CB3","Berry Symphony",480000,0,"","D:/FinalProject/images/berry_symphony.png"))
mousses.append(Mousse("CB4","Pandora Delight",480000,0,"","D:/FinalProject/images/pandora_delight.png"))
mousses.append(Mousse("CB5","Amber Kiss",480000,0,"","D:/FinalProject/images/amber_kiss.png"))
mousses.append(Mousse("CB6","Imperial Oolong",480000,0,"","D:/FinalProject/images/imperial_oolong.png"))
print("List of cookies:")
for m in mousses:
    print(m)
filename="mousses.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
jff.write_data(mousses,path)