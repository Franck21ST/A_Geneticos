from django.shortcuts import render
import math,matplotlib.pyplot as plt,random

# Create your views here.
def home(request):
    return render(request,'index.html',{"v":''})

def boton(request):
    global w,porcent
    if request.method == 'GET':
        w = str(request.GET.get('peso')).split(",")
        w = [int(w[0]),int(w[1])]
        porcent = float(request.GET.get('mutacion'))
        llenado()
    activar={
        "v":"si"
    }
    return render(request,'index.html',activar)

def siguiente(request):
    if request.method == 'GET':
        iteracion()
    f=""
    if final=="Terminado":
        f="Terminado"
    activa={
        "v":"si",
        "f":f
    }
    return render(request,'index.html',activa)

#Metodos
i=0
t=[0,1]
w=[]
def Vector():
    v=0
    v=[random.randrange(1,50),random.randrange(1,50)]
    return v

def Distancia(a,b):
    d=0
    d=math.sqrt((math.pow(b[0]-a[0],2)+math.pow(b[1]-a[1],2)))
    return d

def graficacion(y):
    plt.plot(y[0],y[1],marker = 'o',c='b')

LV=[]
def llenado():
    global final
    final=""
    LV.clear()
    plt.cla()
    for c in range(1000):
        s=Vector()
        arr=[s,Distancia(s,w)]
        LV.append(arr)
    organi(LV)
    mostrar(LV)

def mostrar(l):
    plt.switch_backend('agg')
    plt.title("Vectores")
    plt.plot([0,w[0]],[0,w[1]],c = 'r')
    for x in l:
        graficacion(x[0])
    organi(LV)
    plt.savefig("./static/Grafica.jpg")
    plt.cla()

def organi(l):
    for z in range(len(l)):
        for y in range(0,len(l)-1):
            if float(l[y][1]) > float(l[y+1][1]):
                l[y],l[y+1]=l[y+1],l[y]

porcent=0
def mutacion(porcent):
    for z in range(round((porcent*1000))):
        LV[random.randrange(0,999)][0][random.randrange(0,1)]=Vector()[0]

LH=[]
def cruce1(l):
    for i in range(random.randrange(1,1000)):
        LH.clear()
        a=random.randrange(0,1000)
        b=random.randrange(0,1000)
        A=[l[a][0][0],l[b][0][1]]
        B=[l[b][0][0],l[a][0][1]]
        LH.append([A,Distancia(A,w)])
        LH.append([B,Distancia(B,w)])
        organi(LH)
        if LV[a][1]>LV[b][1]:
            if LH[0][1]<LV[a][1]:
                LV[a]=LH[0]
        if LV[b][1]>LV[a][1]:
            if LH[0][1]<LV[b][1]:
                LV[b]=LH[0]
    mutacion(porcent)

def cruce2(l):
    for i in range(random.randrange(1,1000)):
        LH.clear()
        a=random.randrange(0,1000)
        b=random.randrange(0,1000)
        A=[l[b][0][0],l[a][0][1]]
        B=[l[a][0][0],l[b][0][1]]
        LH.append([A,Distancia(A,w)])
        LH.append([B,Distancia(B,w)])
        organi(LH)
        if LV[a][1]>LV[b][1]:
            if LH[0][1]<LV[a][1]:
                LV[a]=LH[0]
        if LV[b][1]>LV[a][1]:
            if LH[0][1]<LV[b][1]:
                LV[b]=LH[0]
    mutacion(porcent)

final=""
def iteracion():
    global i,final
    if LV[0]==LV[999] and LV[0][0]==w:
        final="Terminado"
    if t[i]==0:
        cruce1(LV)
        mostrar(LV)
    elif t[i]==1:
        cruce2(LV)
        mostrar(LV)
    if i==0:
        i=1
    else:
        i=0
