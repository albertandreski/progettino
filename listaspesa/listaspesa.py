lista_della_spesa = []
def aggiungi():
    lista_della_spesa.append(valore)

def visualizza():
    for i in range(len(lista_della_spesa)):
    print(f"{i+1}. {lista_della_spesa[i]}")

def rimuovi():
    lista_della_spesa.pop(valore)

while True:
    print("premi 0 per uscire,\npremi 1 per aggiungerre un elemento,\npremi 2 per
visualizzare la lista,\n premi 3 per eliminare un elemento,\n premi 4 per contare
gli elementi della lista,\n premi 5 per eliminare un elemento")
    x=int(input(""))
    if x == 0:
        break
    elif x == 1:
        aggiungi()
    elif x == 2:
        visualizza()
    elif x == 3:
        rimuovi()
    elif x == 4:
        conta()
    elif x == 5:
        svuota_lista()