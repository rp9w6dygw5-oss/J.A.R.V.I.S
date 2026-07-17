from brain import Brain

jarvis = Brain()

print("J.A.R.V.I.S ONLINE")

while True:
    comando = input("Tu: ")

    if comando.lower() == "esci":
        print("Jarvis: A presto.")
        break

    risposta = jarvis.think(comando)
    print("Jarvis:", risposta)
from command import esegui_comando

print("Jarvis avviato. Sistema online.")

while True:
    comando = input("Tu: ")

    risposta = esegui_comando(comando)

    print("Jarvis:", risposta)
