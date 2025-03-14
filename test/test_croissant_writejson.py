from libs.JsonFileFactory import JsonFileFactory
from models.Product import Croissant

croissants=[]
croissants.append(Croissant("CB13","Honey Glaze",65000,0,"","D:/FinalProject/images/honey_glaze.png"))
croissants.append(Croissant("CB14","Strawberry Breeze",60000,0,"","D:/FinalProject/images/strawberry_breeze.png"))
croissants.append(Croissant("CB15","Classic",50000,0,"","D:/FinalProject/images/classic.png"))
croissants.append(Croissant("CB16","Blush Crust",100000,0,"","D:/FinalProject/images/blush_crust.png"))
croissants.append(Croissant("CB17","Tiramisiu Cake",100000,0,"","D:/FinalProject/images/tiramisu_cake.png"))
croissants.append(Croissant("CB18","Earl-Grey & Almond",100000,0,"","D:/FinalProject/images/earl_grey_almond.png.png"))


print("List of croissants:")
for cr in croissants:
    print(cr)
filename="croissants.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
jff.write_data(croissants,path)