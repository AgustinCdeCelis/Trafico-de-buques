import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_2016= pd.read_csv(r'C:\Users\LENOVO\Desktop\programacion\buques\data\buques-pasajeros-2016.csv',encoding='latin-1')

df_2016



df_2017 = pd.read_csv(r'data\buques-pasajeros-2017.csv',encoding='latin-1')

df_2017
df_2018 = pd.read_csv(r'data\buques-pasajeros-2018.csv',encoding='latin-1')
df_2018
df_2019= pd.read_csv(r'data\buques-pasajeros-2019.csv',encoding='latin-1') 
df_2019
df_2020=pd.read_csv(r'data\buques-pasajeros-2020.csv',encoding='latin-1')

df_2020
df_2021=pd.read_csv(r'data\buques-pasajeros-2021.csv',encoding='latin-1')
df_2021
df = pd.concat([df_2016,df_2017,df_2018,df_2019,df_2020,df_2021])

df
df.isnull().sum()
df[df.duplicated()]
df.drop_duplicates(keep=False, inplace=True)

df
df.describe().apply(lambda s: s.apply('{0:.3f}'.format))
df['buque'].nunique()
df['imo'].nunique()
df['buque'].value_counts().loc[lambda x: x>100]
df['puerto'].value_counts()
df['sentido'].value_counts()
df['servicio'].value_counts()
df['anio'].value_counts()
df['cantidad_dias'] = df['fecha'].rank(method='dense').astype(int)

df
carga=df[df['servicio']=='Carga']

index=df['servicio'].value_counts().index

values=df['servicio'].value_counts().values
palette=['darkblue','lightblue']

fig, ax= plt.subplots(nrows=1, ncols=2, figsize=(8,4))


sns.countplot(ax=ax[0],x=df['servicio'],palette=palette,linewidth=2.5, edgecolor=".2")
ax[0].set_title('Tipo de servicio',size=12,weight='bold',pad=20)
ax[0].spines[['right', 'top', 'left','bottom']].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False,labelsize=12)


for i in ax[0].containers:
    ax[0].bar_label(i,fontsize=12);
    
    
    
plt.pie(values, labels = index, autopct='%.0f%%' ,colors=['darkblue','lightblue'],wedgeprops={"edgecolor":"0",'linewidth': 2.5,
                    'antialiased': True},startangle=90,textprops={'fontsize': 12})
ax[1].set_title('Porcentaje de tipo de servicio',size=12,weight='bold',pad=20);
plt.rcParams['figure.figsize']= 8,4

palette=['darkred','red','darkorange','goldenrod','khaki','yellow']
plt.rcParams['axes.spines.left'] = True
#plt.rcParams['axes.spines.right'] = False
#plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.bottom'] = True
plt.title("Tipo de servicio por año",size=12,weight='bold',pad=20)
sns.countplot(data=df,x='servicio',hue='anio',linewidth=1.5, edgecolor=".2",palette=palette)
plt.xlabel(None)
plt.ylabel(None)

plt.show()
df['puerto'].value_counts()
df['fecha']= pd.to_datetime(df['fecha']).dt.date

df['mes'] = pd.to_datetime(df['fecha']).dt.month

df['año'] = pd.to_datetime(df['fecha']).dt.year

df['dia_semana'] = pd.to_datetime(df['fecha']).dt.weekday

df['semana_año'] = pd.to_datetime(df['fecha']).dt.isocalendar().week

df['dia'] = pd.to_datetime(df['fecha']).dt.day

df['dayofyear'] =pd.to_datetime(df['fecha']).dt.dayofyear
df
colonia = df[df['puerto']=='COLONIA EXPRESS BAIRES']
rou_colonia = df[df['puerto']=='ROU - COLONIA']
buquebus = df[ df['puerto']=='BUQUEBUS']
puerto_bsas = df[df['puerto']=='PUERTO BUENOS AIRES']
rou_montevideo = df[df['puerto']== 'ROU - MONTEVIDEO']
terminal = df[df['puerto']== 'TERMINAL CRUCEROS PTO. BS. AS.']

str_list = ['2016','2017','2018','2019','2020','2021']

fig, ax= plt.subplots(nrows=2, ncols=3, figsize=(10,5))

plt.suptitle('Cantidad de pasajeros por año desde enero de 2016 a octubre de 2021',size=12,weight='bold')

#PUERTO COLONIA EXPRESS BAIRES

sns.scatterplot(data=colonia, x='cantidad_dias',y='pax',ax=ax[0,0])
ax[0,0].set_title('Puerto: Colonia-Express Baires',size=8,weight='bold',pad=20)
#ax[0].spines[['right', 'top', 'left','bottom']].set_visible(False)
ax[0,0].set_ylabel(None)
ax[0,0].set_xlabel(None)
ax[0,0].set_xticks([0,365,730,1095,1460,1825])
ax[0,0].set_xticklabels(str_list)
ax[0,0].set_yticks([0,500,1000,2000])
#ax[0].tick_params(labelleft=False, left=False,labelsize=12)

#PUERTO ROU-COLONIA
sns.scatterplot(data=rou_colonia, x='cantidad_dias',y='pax',ax=ax[0,1],color='purple')

ax[0,1].set_title('Puerto: Rou-Colonia',size=8,weight='bold',pad=20)
#ax[0].spines[['right', 'top', 'left','bottom']].set_visible(False)
ax[0,1].set_ylabel(None)
ax[0,1].set_xlabel(None)
ax[0,1].set_xticks([0,365,730,1095,1460,1825])
ax[0,1].set_xticklabels(str_list)
ax[0,1].set_yticks([0,500,1000,2000])
#ax[0].tick_params(labelleft=False, left=False,labelsize=12)



#PUERTO BUQUEBUS
sns.scatterplot(data=buquebus, x='cantidad_dias',y='pax',ax=ax[0,2],color='darkred')
ax[0,2].set_title('Puerto: Buquebus',size=8,weight='bold',pad=20)
#ax[0].spines[['right', 'top', 'left','bottom']].set_visible(False)
ax[0,2].set_ylabel(None)
ax[0,2].set_xlabel(None)
ax[0,2].set_xticks([0,365,730,1095,1460,1825])
ax[0,2].set_xticklabels(str_list)
ax[0,2].set_yticks([0,500,1000,2000])
#ax[0].tick_params(labelleft=False, left=False,labelsize=12)




#PUERTO BUENOS AIRES
sns.scatterplot(data=puerto_bsas, x='cantidad_dias',y='pax',ax=ax[1,0],color='darkblue')
ax[1,0].set_title('Puerto: Buenos Aires',size=8,weight='bold',pad=20)
#ax[0].spines[['right', 'top', 'left','bottom']].set_visible(False)
ax[1,0].set_ylabel(None)
ax[1,0].set_xlabel(None)
ax[1,0].set_xticks([0,365,730,1095,1460,1825])
ax[1,0].set_xticklabels(str_list)
#ax[0].tick_params(labelleft=False, left=False,labelsize=12)



#PUERTO ROU-MONTEVIDEO
sns.scatterplot(data=rou_montevideo, x='cantidad_dias',y='pax',ax=ax[1,1],color='darkgreen')
ax[1,1].set_title('Puerto: Rou-Montevideo',size=8,weight='bold',pad=20)
#ax[0].spines[['right', 'top', 'left','bottom']].set_visible(False)
ax[1,1].set_ylabel(None)
ax[1,1].set_xlabel(None)
ax[1,1].set_xticks([0,365,730,1095,1460,1825])
ax[1,1].set_yticks([0,500,1000,2000])
ax[1,1].set_xticklabels(str_list)
#ax[0].tick_params(labelleft=False, left=False,labelsize=12)




#PUERTO ROU-MONTEVIDEO
sns.scatterplot(data=terminal, x='cantidad_dias',y='pax',ax=ax[1,2],color='red')

ax[1,2].set_title('Puerto: Rou-Montevideo',size=8,weight='bold')
#ax[0].spines[['right', 'top', 'left','bottom']].set_visible(False)
ax[1,2].set_ylabel(None)
ax[1,2].set_xlabel(None)
ax[1,2].set_xticks([0,365,730,1095,1460,1825])
ax[1,2].set_xticklabels(str_list)
ax[1,2].set_yticks([0,2000,4000])
#ax[0].tick_params(labelleft=False, left=False,labelsize=12)
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

fig.tight_layout()

terminal['mes'].value_counts()
terminal['servicio'].value_counts()
mes_codigo= {1:'enero',2:'febrero',3:'marzo',4:'abril',5:'mayo',6:'junio',
             7:'julio',8:'agosto',9:'septiembre',10:'octubre',11:'noviembre',12:'diciembre'}

df['mes'] = df['mes'].map(mes_codigo)
plt.title("Variación mensual por año de cantidad de viajes",size=12,weight='bold',pad=20)
sns.countplot(data=df,x='anio',hue='mes',linewidth=0.5, edgecolor=".2")
plt.legend(bbox_to_anchor=(1.1, 1.05))
plt.xlabel(None)
plt.ylabel('Cantidad de viajes')

plt.show()