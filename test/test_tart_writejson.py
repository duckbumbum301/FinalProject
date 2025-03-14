from libs.JsonFileFactory import JsonFileFactory
from models.Product import Tart

tarts=[]
tarts.append(Tart("CB7","Crimson Melody",55000,0,"","D:/FinalProject/images/crimson_melody.png"))
tarts.append(Tart("CB8","Banana Cloud",60000,0,"","D:/FinalProject/images/banana_cloud.png"))
tarts.append(Tart("CB9","Very Merry",60000,0,"","D:/FinalProject/images/very_merry.png"))
tarts.append(Tart("CB10","Cheese Crust",65000,0,"","D:/FinalProject/images/cheese_crust.png"))
tarts.append(Tart("CB11","Pink Velvet",120000,0,"","D:/FinalProject/images/pink_velvet.png"))
tarts.append(Tart("CB12","Sunny Kernel",110000,0,"","D:/FinalProject/images/sunny_kernel.png"))

print("List of tarts:")
for t in tarts:
    print(t)
filename="tarts.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
jff.write_data(tarts,path)