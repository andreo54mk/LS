import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

#df = pd.read_csv("https://docs.google.com/spreadsheets/d/1goYJbYjskPjgQGL5KASWZLax-ahpjqPxtEXn1ixScpw/export?gid=0&format=csv", skiprows=1)
#print (df)

#df2 = pd.read_csv("https://docs.google.com/spreadsheets/d/1Gb_IWPHKDkxDpc4Pd43fwzsfmFjFGZWf-XaojgyppeE/export?gid=0&format=csv",skiprows=1)
#print (df2)

df3 = pd.read_csv("СТАДІО.csv")


df3.index = ['X', 'Y', 'Остап', 'Єгор', 'Корабел','Kelt','Монокулюс','АліМон','Володимир Vovas','Calcioaway87','Паспарту','Валентин','MD','Andreo54MK','Квітка Ночі','Eugene','NO' ]
df3.index.name = 'Стадіон'
#print(df3)


NEW = df3.T.iloc[6:]
X = NEW['X'].str.replace(',','.').astype(float)
Y = NEW['Y'].str.replace(',','.').astype(float)  
NEW['geometry'] = list(zip(X,Y))
NEW['geometry'] = NEW['geometry'].apply(Point)
NEW = gpd.GeoDataFrame(NEW)

#print (df3)
print (NEW)


print(NEW[NEW.Остап=='1'])

Part = NEW.columns[2:-2]
for name in Part:
    Os = NEW[['geometry',name]]
    Os = Os[Os[name]=='1'].reset_index().rename(columns={"index":'Назва'})
    if len(Os)<1 :
        continue
    print(Os)
    Os.to_file(f'{name}.json',driver = 'GeoJSON')
    
    



