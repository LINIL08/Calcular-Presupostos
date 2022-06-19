from Subprogrames import preus_excel, funcions_preus, cost_excel, ObtenirNom, Comprovador
import os


def central():

    resposta = ObtenirNom.nom()
    dos = Comprovador.comprovar(resposta)

    # Preu
    preu = preus_excel.Preu
    preu.num = resposta

    # Obtenir metres
    metres = float(input("Metres de tanca: "))
    hores = int(input("Quantes hores necessitarà aquesta obra? "))
    os.system("")
    print("\033[4m", end="")

    descompte = 100
    counter = 0

    for i in range(2):
        # Postes
        preu_poste = preus_excel.Preu.PreuPostes.value
        cost_poste = cost_excel.Cost.PreuPostes.value
        poste = funcions_preus.postes(metres)
        poste_preu = round(preu_poste * poste, 2)
        poste_preu = round(poste_preu * descompte / 100, 2)
        poste_cost = round(cost_poste * poste, 2)

        # Tornapuntes
        preu_torna = preus_excel.Preu.PreuTorna.value
        cost_torna = cost_excel.Cost.PreuTorna.value
        tornapuntes = funcions_preus.tornapuntes(metres)
        tornapuntes_preu = round(preu_torna * tornapuntes, 2)
        tornapuntes_preu = round(tornapuntes_preu * descompte / 100, 2)
        torapuntes_cost = round(cost_torna * tornapuntes, 2)

        # Suport
        preu_suport = preus_excel.Preu.PreuSuport.value
        cost_suport = cost_excel.Cost.PreuSuport.value
        suport = funcions_preus.suport(tornapuntes)
        suport_preu = round(preu_suport * suport, 2)
        suport_preu = round(suport_preu * descompte / 100, 2)
        suport_cost = round(cost_suport * suport, 2)

        # Cargol
        preu_cargol = preus_excel.Preu.PreuCargol.value
        cost_cargol = cost_excel.Cost.PreuCargol.value
        cargol = funcions_preus.cargol(tornapuntes)
        cargol_preu = round(preu_cargol * cargol, 2)
        cargol_preu = round(cargol_preu * descompte / 100, 2)
        cargol_cost = round(cost_cargol * cargol, 2)

        # Tap
        preu_tap = preus_excel.Preu.PreuTap.value
        cost_tap = cost_excel.Cost.PreuTap.value
        tap = funcions_preus.tap(poste)
        tap_preu = round(preu_tap * tap, 2)
        tap_preu = round(tap_preu * descompte / 100, 2)
        tap_cost = round(cost_tap * tap, 2)

        # Tela
        preu_tela = preus_excel.Preu.PreuTela.value
        cost_tela = cost_excel.Cost.PreuTela.value
        tela = funcions_preus.tela(metres)
        tela_preu = round(preu_tela * tela, 2)
        tela_preu = round(tela_preu * descompte / 100, 2)
        tela_cost = round(cost_tela * tela, 2)

        # Fil
        preu_fil = preus_excel.Preu.PreuFil.value
        cost_fil = cost_excel.Cost.PreuFil.value
        fil = funcions_preus.fil(dos, metres)
        fil_preu = round(preu_fil * fil, 2)
        fil_preu = round(fil_preu * descompte / 100, 2)
        fil_cost = round(cost_fil * fil, 2)

        # Tensors
        preu_tensor = preus_excel.Preu.PreuTensor.value
        cost_tensor = cost_excel.Cost.PreuTensor.value
        tensor = funcions_preus.tensor(dos, metres)
        tensor_preu = round(preu_tensor * tensor, 2)
        tensor_preu = round(tensor_preu * descompte / 100, 2)
        tensor_cost = round(cost_tensor * tensor, 2)

        # Grapa
        preu_grapa = preus_excel.Preu.PreuGrapa.value
        cost_grapa = cost_excel.Cost.PreuGrapa.value
        grapa = funcions_preus.grapes(poste)
        grapes_preu = round(preu_grapa * grapa, 2)
        grapes_preu = round(grapes_preu * descompte / 100)
        grapes_cost = round(cost_grapa * grapa, 2)

        # Ancoratge
        preu_anco = preus_excel.Preu.PreuAnco.value
        cost_anco = cost_excel.Cost.PreuAnco.value
        anco = funcions_preus.ancoratge(poste)
        anco_preu = round(preu_anco * anco, 2)
        anco_cost = round(cost_anco * anco, 2)

        # Hores
        preu_hora = preus_excel.Preu.PreuHora.value
        cost_hora = cost_excel.Cost.PreuHora.value
        hores_preu = round(hores * preu_hora, 2)
        hores_cost = round(hores * cost_hora, 2)

        # Total
        preu = funcions_preus.total_preu(poste_preu, tornapuntes_preu, suport_preu, cargol_preu, tap_preu, fil_preu,
                                         tensor_preu, grapes_preu, anco_preu, hores_preu)
        cost = funcions_preus.total_cost(poste_cost, torapuntes_cost, suport_cost, cargol_cost, tap_cost, fil_cost,
                                         tensor_cost, grapes_cost, anco_cost, hores_cost)

        # Benfici
        benefici = funcions_preus.total_benefici(preu, cost)

        # Percentatge
        preu_material = funcions_preus.preu_material(poste_preu, tornapuntes_preu, suport_preu, cargol_preu, tap_preu,
                                                     fil_preu, tensor_preu, tensor_preu, grapes_preu)
        descompte = funcions_preus.calcular_k(hores, preu_material, descompte, counter)
        descompte = max(descompte, 60)
        counter += 1

    # Imprimir
    funcions_preus.poste_print(poste, poste_preu, poste_cost)
    funcions_preus.torna_print(tornapuntes, tornapuntes_preu, torapuntes_cost)
    funcions_preus.suport_print(suport, suport_preu, suport_cost)
    funcions_preus.cargol_print(suport, cargol_preu, cargol_cost)
    funcions_preus.tap_print(tap, tap_preu, tap_cost)
    funcions_preus.tela_print(tela, tela_preu, tela_cost)
    funcions_preus.fil_print(fil, fil_preu, fil_cost)
    funcions_preus.tensor_print(tensor, tensor_preu, tensor_cost)
    funcions_preus.grapa_print(grapa, grapes_preu, grapes_cost)
    funcions_preus.anco_print(anco, anco_preu, anco_cost)
    funcions_preus.hores_print(hores, hores_preu, hores_cost)
    funcions_preus.preu_print(preu)
    funcions_preus.cost_print(cost)
    funcions_preus.benefici_print(15 * hores, hores)
    funcions_preus.descompte_print(descompte)

    print("\033[0m")
