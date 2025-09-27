import csv 

def read_graph_from_csv(file_path):
    graph = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Falls es eine Kopfzeile gibt

        for row in reader:
            if len(row) < 2:
                continue  # Ungültige Zeile überspringen

            src, dest = row[0].strip(), row[1].strip()

            if src not in graph:
                graph[src] = []
            graph[src].append(dest)

            # Optional: Für ungerichteten Graph, auch rückwärts hinzufügen
            # if dest not in graph:
            #     graph[dest] = []
            # graph[dest].append(src)

    return graph

file_path = 'gaph.csv'
struktur = read_graph_from_csv(file_path)

# Beispielausgabe

#for node, neighbors in graph.items():
#    print(f"{node} -> {neighbors}")

# Einfache Produktstruktur
"""
struktur = {
    "A": ["B", "C", "E", "F"],
    "B": ["D", "E"],
    "C": ["F", "D"],
    "D": [],
    "E": [],
    "F": []
}
"""
# Funktion zur Berechnung der Stückliste (einfache rekursive Zählung)
def stueckliste(produkt):
    teile = {}

    def zaehle(knoten):
        for teil in struktur.get(knoten, []):
            if teil in struktur and struktur[teil]:  # hat Unterteile
                zaehle(teil)
            else:
                if teil in teile:
                    teile[teil] += 1
                else:
                    teile[teil] = 1

    if produkt in struktur:
        zaehle(produkt)
        print(f"{produkt} enthält:")
        for teil, anzahl in teile.items():
            print(f" - {anzahl}x {teil}")
    else:
        print("(Fehler) Teil nicht gefunden.")

# Funktion zur Suche, wo ein Teil verwendet wird
def verwendung(gesucht):
    verwendet_von = []

    def enthaelt(knoten, ziel):
        if ziel in struktur.get(knoten, []):
            return True
        for unter in struktur.get(knoten, []):
            if enthaelt(unter, ziel):
                return True
        return False

    for produkt in struktur:
        if enthaelt(produkt, gesucht):
            verwendet_von.append(produkt)

    if verwendet_von:
        print(f"{gesucht} wird verwendet von: {', '.join(verwendet_von)}")
    else:
        print("(Fehler) Teil nicht gefunden oder nicht verwendet.")

# Menü
while True:
    print("\n1 – Stückliste anzeigen")
    print("2 – Einzelteil prüfen")
    print("0 – Programm beenden")
    wahl = input("> Auswahl: ")

    if wahl == "0":
        break
    elif wahl == "1":
        name = input("Produkt eingeben: ")
        stueckliste(name)
    elif wahl == "2":
        name = input("Einzelteil eingeben: ")
        verwendung(name)
    else:
        print("(Fehler) Ungültige Auswahl – bitte 0, 1 oder 2 eingeben.")