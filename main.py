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
