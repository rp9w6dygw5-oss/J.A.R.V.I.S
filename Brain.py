from memory import Memory

class Brain:
    def __init__(self):
        self.memory = Memory()

    def think(self, message):
        text = message.lower()

        if "ciao" in text:
            return "Ciao! Sono Jarvis."

        if "come ti chiami" in text:
            return "Mi chiamo Jarvis."

        if "ricorda" in text:
            dato = text.replace("ricorda", "").strip()
            self.memory.remember("nota", dato)
            return "Va bene, lo ricorderò."

        if "cosa ricordi" in text:
            nota = self.memory.recall("nota")
            if nota:
                return f"Ricordo questo: {nota}"
            return "Per ora non ricordo nulla."

        return "Sto ancora imparando."
