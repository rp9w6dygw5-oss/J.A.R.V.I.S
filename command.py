def esegui_comando(comando):
    comando = comando.lower()

    if comando == "ciao":
        return "Ciao, sono Jarvis."

    elif comando == "stato":
        return "Tutti i sistemi sono online."

    elif comando == "memoria":
        return "Memoria pronta."

    else:
        return "Comando non riconosciuto."
