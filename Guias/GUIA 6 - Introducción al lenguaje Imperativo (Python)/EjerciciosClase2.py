#1ERA FORMA
def sumaTotal(l:list[int])->int:
    s:int = 0
    for i in range(0,len(l)):
        s += l[i]
    return s

print(sumaTotal([1,2,3]))

#2ERA FORMA
def sumaTotal2(s:list[int])->int: 
      total:int = 0
      indice = 0
      longitud = len(s)
      while (indice < longitud):
            valorActual = s[indice]
            total += valorActual
            indice += 1 
      return total       
x = sumaTotal2([1,2,3])
print(x)

#--------------------------------------------------------------------

# 1ERA FORMA 
def pertenece(s:list[int],e:int)->bool:
    verifica:bool = e in s
    return verifica 
print(pertenece([1,2,3],4))

#2DA FORMA
def pertenece2(s:list[int],e:int)->bool:
    for i in range(len(s)):
        if e == s[i] : 
          return True   
    return False
print(pertenece2([1,2,3],4))   

#3ERA FORMA
def pertenece3(s:list[int],e:int)->bool:
    i:int = 0
    while e <= len(s):
          if i == e: 
             return True
          i+= 1
    return False
print(pertenece3([1,2,3],7)) 
    
#4TA FORMA
def pertenece4(s:list[int],e:int)->bool:
    return s.count(e) > 0 

#5TA FORMA (TIPO GENERICO ?)
def pertenece4(s:list[str],e:str)->bool:
    return s.count(e) > 0 

print(pertenece4(["a","b","c"],"b"))




#--------------------------------------------------------------------

#def fortalezaContra(s:str)->str:








































