import math
postes = True
preu_postes = 16.35
tornapuntes = True
preu_tornapuntes = 13.05
tensors = True
preu_tensors = 1.42
suports = True
preu_suport = 2.78
filferro = True
preu_filferro = 0.16
grapes = True
preu_grapes = 0.11
preu_cargols = 0.34
preu_tap = 0.65
preu_tela = 6.96
preu_ancoratge = 0.6
canvi_preu = True

while True:
    meters = int(input("Insereixi els metres de tanca:"))

    print("\nTanca 1'50m verda\n")
# Postes
    postes = meters / 3 + 2
    postes_final = math.ceil(max(2, postes))
    preu_postes_final = round(preu_postes * postes_final)
    print("Postes: {}                   ".format(postes_final),
          "Preu final: {}".format(preu_postes_final))

# Tornapuntes
    tornapuntes = meters / 25 * 2 + (3 * tornapuntes / 100)
    if meters <= 3:
        tornapuntes_finals = 1
    else:
        tornapuntes_finals = math.ceil(max(2, tornapuntes))
    preu_tornapuntes_final = round(preu_tornapuntes * tornapuntes_finals)
    print("Tornapuntes: {}              ".format(tornapuntes_finals),
          "Preu final: {}" .format(preu_tornapuntes_final))

# Tensors
    tensors = meters / 25 * 3 + (3 * tensors / 100)
    tensors_finals = math.ceil(max(2, tensors))
    preu_tensors_final = round(preu_tensors * tensors_finals)
    print("Tensors: {}                  " .format(tensors_finals),
          "Preu final: {}" .format(preu_tensors_final))

# Pal tensor
    pal_tensor = tornapuntes/4 + 1

# Suport
    suports = math.ceil((tornapuntes_finals/2 + 1) + 3 * pal_tensor + (3 * suports / 100))
    preu_suport_final = round(preu_suport * suports, 1)
    print("Suports: {}                  " .format(suports),
          "Preu final: {}" .format(preu_suport_final))

# Cargol
    cargols_finals = math.ceil(tornapuntes_finals)
    preu_cargols_final = round(preu_cargols * cargols_finals, 1)
    print("Cargols: {}                  ".format(cargols_finals),
          "Preu final: {}" .format(preu_cargols_final))

# Tap
    taps_finals = math.ceil(postes_final)
    preu_tap_finals = round(preu_tap * taps_finals)
    print("Taps: {}                     ".format(taps_finals),
          "Preu final: {}" .format(preu_tap_finals))

# Tela
    tela_final = math.ceil(meters)
    preu_tela_final = round(preu_tela * tela_final)
    print("Tela: {}                     " .format(meters),
          "Preu final: {}" .format(preu_tela_final))

# Filferro
    filferro = meters * 3 + (3 * filferro / 100)
    filferro_final = math.ceil(filferro)
    preu_filferro_final = round(preu_filferro * filferro_final)
    print("Filferro: {}                 ".format(filferro_final),
          "Preu final: {}" .format(preu_filferro_final))

# Grapes
    grapes = postes_final * 10 + (3 * grapes / 100)
    grapes_final = round(grapes)
    preu_grapes_final = round(preu_grapes * grapes_final)
    print("Grapes: {}                   ".format(grapes_final),
          "Preu final: {}" .format(preu_grapes_final))

# Ancoratge
    ancoratge_final = math.ceil(postes_final * 3)
    preu_ancoratge_final = round(preu_ancoratge * ancoratge_final, 1)
    print("Material ancoratge: {}       ".format(ancoratge_final),
          "Preu final: {}\n" .format(preu_ancoratge_final))

    preu_total = round(preu_postes_final + preu_ancoratge_final + preu_grapes_final + preu_filferro_final
                       + preu_tornapuntes_final + preu_suport_final + preu_cargols_final
                       + preu_tap_finals + preu_tela_final)

    print("Preu total: {}€".format(preu_total))

    input("\n")

    print("Preu per unitat:\n")
    print("Postes:      {}" .format(preu_postes))
    print("Tornapuntes: {}" .format(preu_tornapuntes))
    print("Tensors:     {}".format(preu_tensors))
    print("Suports:     {}".format(preu_suport))
    print("Cargols:     {}".format(preu_cargols))
    print("Taps:        {}".format(preu_tap))
    print("Tela:        {}".format(preu_tela))
    print("Grapes:      {}".format(preu_grapes))
    print("Ancoratge:   {}\n".format(preu_ancoratge))

    while canvi_preu != 10:
        canvi_preu = int(input("""Vols canviar algun preu?
                    1 = Postes
                    2 = Tornapuntes
                    3 = Tensors
                    4 = Suport
                    5 = Cargols
                    6 = Taps
                    7 = Tela
                    8 = Grapes
                    9 = Material Ancoratge
                    10 = Cap\n"""))
        if canvi_preu == 1:
            postes_nou_preu = float(input("Insereixi el nou preu per als postes:\n"))
            preu_postes = postes_nou_preu
            input("Preu inserit")

        elif canvi_preu == 2:
            tornapuntes_nou_preu = float(input("Insereixi el nou preu per als tornapuntes:\n"))
            preu_tornapuntes = tornapuntes_nou_preu
            input("Preu inserit")

        elif canvi_preu == 3:
            tensors_nou_preu = float(input("Insereixi el nou preu per als tensors:\n"))
            preu_tensors = tensors_nou_preu
            input("Preu inserit")

        elif canvi_preu == 4:
            suport_nou_preu = float(input("Insereixi el nou preu per als suports:\n"))
            preu_suport = suport_nou_preu
            input("Preu inserit")

        elif canvi_preu == 5:
            cargols_nou_preu = float(input("Insereixi el nou preu per als cargols:\n"))
            preu_cargols = cargols_nou_preu
            input("Preu inserit")

        elif canvi_preu == 6:
            taps_nou_preu = float(input("Insereixi el nou preu per als taps:\n"))
            preu_tap = taps_nou_preu
            input("Preu inserit")

        elif canvi_preu == 7:
            tela_nou_preu = float(input("Insereixi el nou preu per a la tela:\n"))
            preu_tela = tela_nou_preu
            input("Preu inserit")

        elif canvi_preu == 8:
            grapes_nou_preu = float(input("Insereixi el nou preu per les grapes:\n"))
            preu_grapes = grapes_nou_preu
            input("Preu inserit")

        elif canvi_preu == 9:
            ancoratge_nou_preu = float(input("Insereixi el nou preu per l'ancorate:\n"))
            preu_ancoratge = ancoratge_nou_preu
            input("Preu inserit")

        elif canvi_preu == 10:
            print("No es canviarà cap preu més\n")

        else:
            print("Nobre erroni\n")

    canvi_preu = True

    print("Preu per unitat:\n")
    print("Postes:      {}" .format(preu_postes))
    print("Tornapuntes: {}" .format(preu_tornapuntes))
    print("Tensors:     {}".format(preu_tensors))
    print("Suports:     {}".format(preu_suport))
    print("Cargols:     {}".format(preu_cargols))
    print("Taps:        {}".format(preu_tap))
    print("Tela:        {}".format(preu_tela))
    print("Grapes:      {}".format(preu_grapes))
    print("Ancoratge:   {}\n".format(preu_ancoratge))
