from automaton import Automaton
import xml.etree.ElementTree as ET
def printAutomatons():
    print("****** Automatons ******",end="\n\n")
    for s in automatons:
        print("id: " + s.id,"| nome: " + s.nome,end="")
        print(" | x: " + s.x,"| y: " + s.y,"| label: " + s.label, end="\n")
        print("****** Transicoes ****** ")
        for t in s.transition:
            print("from: "+ s.id,"to:",t[0],"lendo:",t[1])
        print(s.visitado,end="\n\n")

def printarCidades():
    print("****** Cidades disponiveis ******")
    for s in automatons:
        print("* " + s.nome)
    print("")


tree = ET.parse('jflap.jff')
root = tree.getroot()
automatons = []

for states in root.iter('state'):
    automatons.append(Automaton(states.get("id"),states.get("name"),states.find("x").text,states.find("y").text,states.find("label").text))

# print("\n\nTransitions")
for t in root.iter('transition'):
    for a in automatons:
        if(a.id == t.find("from").text):
            a.transition.append([t.find("to").text,t.find("read").text])
            break
# printAutomatons(automatons)