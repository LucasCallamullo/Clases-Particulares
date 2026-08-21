


from comida import *

class Category:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name




    
    


def buscar_cinco_con_mas_proteinas(v_comidas):
    # Ordenamos la lista en orden descendente por cantidad de proteínas
    comidas_ordenadas = sorted(v_comidas, key=lambda c: c.proteins, reverse=True)
    
    # Tomamos las primeras 5
    top_cinco = comidas_ordenadas[:5]
    
    return top_cinco


def validar_categoria(v_categories, category_name):

     
    
    category = None
    for i in v_categories:
        if i.name == category_name:
            category = i
            break
        
    if category is None:
        category = Category(category_name)
        v_categories.append(category)
        
    return category


def main():
    
    fd = "foods.csv"
    m = open(fd, "r")
    
    v_comidas = []
    
    v_categories = []
    
    cont = 0
    for linea in m:
        cont += 1
        if cont > 1:
            # indices            0                1            2            3
            #  lista_str = [ "Alaskan salmon", "25.4","0","6.7","170","Fish","Animal","Omnivorous" ]
            lista_str = linea.split(",")
            
            name = lista_str[0].replace('"', '')
            proteins = float(lista_str[1].replace('"', ''))
            carbohydrates = float(lista_str[2].replace('"', ''))
            
            category_name = lista_str[5].replace('"', '')
            
            category = validar_categoria(v_categories, category_name)
            
            
            
            comida = Comida(name, proteins, carbohydrates, category)
            v_comidas.append(comida)
            
            
    # indices        0   1   2
    # v_comidas = [ C1, C2, C3 ]
    #for i in v_comidas:
        # i --> vale como cada elemento de la lista
        # i = C1, C2, C3
    #    print(i)
            
    #for i in range(len(v_comidas)):        # range(3)
        # 0, 1, 2
    #    print(i)
        
        
    z = buscar_cinco_con_mas_proteinas(v_comidas)
    for comida in z:
        print(comida)
    
        
    print("Categorias totales:", len(v_categories))
    

if __name__ == "__main__": 
    main()
