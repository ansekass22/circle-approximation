from tkinter import *
import math

#############################################################
# (C) Antti Kasslin
# 2022
#############################################################
# Tässä moduulissa sijaitevat kaikki toiminnot, jotka
# ympyraApproksimaatio.py vaatii (pistejoukon määritteleminen,
# pinta-ala, ympärysmitan pituus, ym.)
#############################################################
def ympyraApprox(R, dR):
    #alustetaan ympyräapproksimaation kehää tutkivat x- ja y-muuttujat
    x = R
    y = 0
    #alustetaan ympyräapproksimaation muodostavien pisteiden taulukko, aloituspiste valmiiksi
    pointsX,pointsY = [x],[y]
    #otetaan approksimaatipolkukin talteen
    pathX,pathY = [x],[y]
    #erikoistapaus: 1. askel aina y + 1
    y += 1
    pathX.append(x)
    pathY.append(y)
    if abs(R - ((x**2 + y**2)**0.5)) < dR: #lähellä oikeaa sädettä olevat pisteet lisätään approksimaatioon
        pointsX.append(x)
        pointsY.append(y)
    while x > y:
        if abs((R - (((y+1)**2 + x**2)**0.5))) < abs((R - (((y)**2 + (x-1)**2)**0.5))): # seur. askel määräytyy sen mukaan, miten lähellä se pysyy varsinaista sädettä
            y += 1
            pathX.append(x)
            pathY.append(y)
        else:
            x -= 1
            pathX.append(x)
            pathY.append(y)
        if abs(R - ((x**2 + y**2)**0.5)) < dR: #lähellä oikeaa sädettä olevat pisteet lisätään approksimaatioon
            pointsX.append(x)
            pointsY.append(y)
    
    #´´Täytetään´´ approksimaation  1. neljännes x=y -linjaan nähden symmetrisillä pisteillä
    #(tähän mennessä saadut pisteet muodostavat vain kahdeksasosan).
    
    N = len(pointsX) #voisi olla pointsY myös;samanpituisiahan nämä vektorit
    uusiX = 0
    uusiY = 0
    i = 1 #iteraatiomuuttuja
    while i <= N:
        uusiX = pointsY[N-i]
        uusiY = pointsX[N-i]
        pointsX.append(uusiX)
        pointsY.append(uusiY)
        i += 1
    return pointsX,pointsY,pathX,pathY

#´´Täydennetään´´ ympyrän neljänneksen approksimaatio koko ympyrän vastaavaksi.
def taydennaApprox(pointsX,pointsY):     
    #Sitten ympyräapproksimaation 2. neljänneksen pisteet
    #(symmetrisiä y-akselin suhteen 1. neljänneksen kanssa).
    N = len(pointsX)
    _2_4_pointsX = []
    _2_4_pointsY = []
    i = 2
    while i < N:
        uusiX = -1*pointsX[N-i]
        uusiY = pointsY[N-i]
        _2_4_pointsX.append(uusiX)
        _2_4_pointsY.append(uusiY)
        i += 1
  
    #Sitten ympyräapproksimaation 3. neljänneksen pisteet
    #(pisteillä negatiiviset arvot 1. neljänneksen suhteen).
    
    _3_4_pointsX = []
    _3_4_pointsY = []
    i = 0
    while i < N:
        uusiX = -1*pointsX[i]
        uusiY = -1*pointsY[i]
        _3_4_pointsX.append(uusiX)
        _3_4_pointsY.append(uusiY)
        i += 1
    #Sitten ympyräapproksimaation 4. neljänneksen pisteet
    #(pisteillä negatiiviset arvot 2. neljänneksen suhteen).
    
    _4_4_pointsX = []
    _4_4_pointsY = []
    N = len(_2_4_pointsX)
    i = 0
    while i < N:
        uusiX = -1*_2_4_pointsX[i]
        uusiY = -1*_2_4_pointsY[i]
        _4_4_pointsX.append(uusiX)
        _4_4_pointsY.append(uusiY)
        i += 1
    #Lopuksi yhdistetään pisteet yhteen taulukkoon niin, että pisteet 
    #kulkevat vastapäivään täyden kierroksen alkaen pisteestä (r,0).
    
    pointsX.extend(_2_4_pointsX)
    pointsX.extend(_3_4_pointsX)
    pointsX.extend(_4_4_pointsX)
    pointsY.extend(_2_4_pointsY)
    pointsY.extend(_3_4_pointsY)
    pointsY.extend(_4_4_pointsY)

    pointsX.append(pointsX[0])
    pointsY.append(pointsY[0])

    #Palautetaan valmis pistetaulukko
    return pointsX,pointsY

# shoeLace-funktio laskee pistejoukon ympäröimän 
# alueen pinta-alan "kengännauha"teorian avulla

def shoeLace(pointsX,pointsY):
    pintaAla = 0 #pinta-alamuuttujan alustus
    L = len(pointsX) 
    i = 0
    while i < (L-1):
        pintaAla += (pointsX[i]*pointsY[i+1] - pointsX[i+1]*pointsY[i])
        i += 1
    pintaAla += (pointsX[L-1]*pointsY[0] - pointsX[0]*pointsY[L-1])
    return 0.5*pintaAla

def piirinPituus(pointsX,pointsY):
    pituus = 0 #pituusmuuttujan alustus
    L = len(pointsX)
    i = 0
    while i < (L-1):
        pituus += ((pointsX[i]-pointsX[i+1])**2 + (pointsY[i]-pointsY[i+1])**2)**0.5
        i += 1
    #pituus += ((pointsX[L-1]-pointsX[0])**2 + (pointsY[L-1]-pointsY[0])**2)**0.5 tämä rivi käytössä vain silloin, kun pistejoukko on sulkeutuva
    return pituus