def ObrirPreus(nom):
    try:
        arxiu = open(nom, "r").read().splitlines()
        return arxiu
    except:
        return 0
