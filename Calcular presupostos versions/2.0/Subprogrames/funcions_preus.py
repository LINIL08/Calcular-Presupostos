import math


def postes(meters):
    postes = meters / 3 + 1
    percent = postes + (postes / 100) * 3
    postes_final = math.ceil(max(2, percent))
    return postes_final


def poste_print(poste, preu, cost):
    print(f"Postes: {poste}                 Preu final: {preu}€            "
          f"Preu de cost total: {cost}€")


def tornapuntes(meters, cantonada):
    tornapuntes = meters / 25 * 2
    percent = tornapuntes + (tornapuntes / 100) * 3
    if meters <= 3:
        tornapuntes_finals = 1
    else:
        tornapuntes_finals = math.ceil(max(2, percent))
    return (tornapuntes_finals + cantonada * 2)


def torna_print(torna, preu, cost):
    print(f"Tornapuntes: {torna}              Preu final: {preu}€            "
          f"Preu de cost total: {cost}€")


def suport(tornapuntes):
    pal_tensor = tornapuntes / 4 + 1
    suport = (tornapuntes / 2 + 1) + 3 * pal_tensor
    percent = suport + (suport / 100) * 3
    suports = math.ceil(percent)
    return suports


def suport_print(suports, preu, cost):
    print(f"Suports: {suports}                  Preu final: {preu}€            "
          f"Preu de cost final: {cost}€")


def cargol(tornapuntes_finals):
    cargol = math.ceil(tornapuntes_finals)
    return cargol


def cargol_print(cargol, preu, cost):
    print(f"Cargols: {cargol}                  Preu final: {preu}€            "
          f"Preu de cost final: {cost}€")


def tap(postes_final):
    tap = math.ceil(postes_final)
    return tap


def tap_print(tap, preu, cost):
    print(f"Taps: {tap}                     Preu final: {preu}€          "
          f"Preu de cotst final: {cost}€")


def tela(meters):
    try:
        tela = int(math.ceil(meters))
    except:
        tela = meters
    return tela


def tela_print(tela, preu, cost):
    print(f"Tela: {tela}                     Preu final: {preu}€           "
          f"Preu de cost final: {cost}€")


def fil(dos, meters):
    if dos is False:
        filferro = meters * 3
    else:
        filferro = meters * 4
    percent = filferro + (filferro / 100) * 3
    return math.ceil(percent)


def fil_print(fil, preu, cost):
    print(f"Filferro: {fil}                 Preu final: {preu}€           "
          f"Preu de cost final: {cost}€")


def tensor(dos, meters):
    if dos is False:
        tensors = meters / 25 * 3
    else:
        tensors = meters / 25 * 4
    percent = tensors + (tensors / 100) * 3
    return math.ceil(max(2, percent))


def tensor_print(tensor, preu, cost):
    print(f"Tensors: {tensor}                  Preu final: {preu}€            "
          f"Preu de cost final: {cost}€")


def grapes(postes):
    grapes = postes * 10
    return round(grapes)


def grapa_print(grapa, preu, cost):
    print(f"Grapes: {grapa}                   Preu final: {preu}€           "
          f"Preu de cost final: {cost}€")


def ancoratge(poste):
    return math.ceil(poste * 3)


def anco_print(anco, preu, cost):
    print(f"Material ancoratge: {anco}       Preu final: {preu}€           "
          f"Preu de cost final: {cost}€")


def hores_print(hora, preu, cost):
    print(f"Hores: {hora}                       Preu final: {preu}€           "
          f"Preu de cost final: {cost}€")


def total_preu(poste, torna, suport, cargol, tap, fil, tensor, grapa, anco, hora):
    total = round(poste + torna + suport + cargol + tap + fil + tensor + grapa + anco + hora, 2)
    return total


def preu_print(total):
    print(f"Total: {total}€", end="                       ")


def total_cost(poste, torna, suport, cargol, tap, fil, tensor, grapa, anco, hora):
    total = round(poste + torna + suport + cargol + tap + fil + tensor + grapa + anco + hora, 2)
    return total


def cost_print(total):
    print(f"Total cost: {total}€")


def total_benefici(preu, cost):
    benefici = round(preu - cost, 2)
    return benefici


def benefici_print(benefici, hora):
    print(f"Benefici total: {benefici}€                       Benefici per hora: {round(benefici/hora, 2)}€")


def preu_material(poste, torna, suport, cargol, tap, tela, fil, tensor, grapa):
    return poste + torna + suport + cargol + tap + tela + fil + tensor + grapa


def calcular_k(hora, preu, descompte, counter):
    if counter == 1:
        return descompte
    else:
        benefici_necessari = 15 * hora
        descompte = benefici_necessari * 100 / preu
        return descompte


def descompte_print(descomtpe):
    print(f"Descompte: {round(100 - descomtpe)}%")
