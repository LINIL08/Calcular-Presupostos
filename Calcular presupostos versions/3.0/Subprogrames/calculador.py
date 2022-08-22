from Subprogrames import preus_excel, cost_excel
import math


class C:
    resposta = 0
    dos = False
    metres = 0
    hores = 0
    cantonades = 0

    # Preu
    preu = preus_excel.Preu
    preu.num = resposta

    descompte = 100
    counter = 0

    while True:
        if resposta != 0:
            while counter != 2:
                # Postes
                postes = metres / 3 + 1
                percent = postes + (postes / 100) * 3
                postes_final = math.ceil(max(2, percent))
                preu_poste = preus_excel.Preu.PreuPostes.value
                cost_poste = cost_excel.Cost.PreuPostes.value
                poste_preu = round(preu_poste * postes_final, 2)
                poste_preu = round(poste_preu * descompte / 100, 2)
                poste_cost = round(cost_poste * postes_final, 2)

                # Tornapuntes
                tornapuntes = metres / 25 * 2
                percent = tornapuntes + (tornapuntes / 100) * 3
                if metres <= 3:
                    tornapuntes_finals = 1
                else:
                    tornapuntes_finals = math.ceil(max(2, percent))
                tornapuntes = tornapuntes_finals + cantonades * 2
                preu_torna = preus_excel.Preu.PreuTorna.value
                cost_torna = cost_excel.Cost.PreuTorna.value
                tornapuntes_preu = round(preu_torna * tornapuntes, 2)
                tornapuntes_preu = round(tornapuntes_preu * descompte / 100, 2)
                torapuntes_cost = round(cost_torna * tornapuntes, 2)

                # Suport
                preu_suport = preus_excel.Preu.PreuSuport.value
                cost_suport = cost_excel.Cost.PreuSuport.value
                pal_tensor = tornapuntes / 4 + 1
                suport = (tornapuntes / 2 + 1) + 3 * pal_tensor
                percent = suport + (suport / 100) * 3
                suport = math.ceil(percent)
                suport_preu = round(preu_suport * suport, 2)
                suport_preu = round(suport_preu * descompte / 100, 2)
                suport_cost = round(cost_suport * suport, 2)

                # Cargol
                preu_cargol = preus_excel.Preu.PreuCargol.value
                cost_cargol = cost_excel.Cost.PreuCargol.value
                cargol = math.ceil(tornapuntes)
                cargol_preu = round(preu_cargol * cargol, 2)
                cargol_preu = round(cargol_preu * descompte / 100, 2)
                cargol_cost = round(cost_cargol * cargol, 2)

                # Tap
                preu_tap = preus_excel.Preu.PreuTap.value
                cost_tap = cost_excel.Cost.PreuTap.value
                tap = math.ceil(postes_final)
                tap_preu = round(preu_tap * tap, 2)
                tap_preu = round(tap_preu * descompte / 100, 2)
                tap_cost = round(cost_tap * tap, 2)

                # Tela
                preu_tela = preus_excel.Preu.PreuTela.value
                cost_tela = cost_excel.Cost.PreuTela.value
                tela = int(math.ceil(metres))
                tela_preu = round(preu_tela * tela, 2)
                tela_preu = round(tela_preu * descompte / 100, 2)
                tela_cost = round(cost_tela * tela, 2)

                # Fil
                preu_fil = preus_excel.Preu.PreuFil.value
                cost_fil = cost_excel.Cost.PreuFil.value
                if dos is False:
                    filferro = metres * 3
                else:
                    filferro = metres * 4
                percent = filferro + (filferro / 100) * 3
                fil = math.ceil(percent)
                fil_preu = round(preu_fil * fil, 2)
                fil_preu = round(fil_preu * descompte / 100, 2)
                fil_cost = round(cost_fil * fil, 2)

                # Tensors
                preu_tensor = preus_excel.Preu.PreuTensor.value
                cost_tensor = cost_excel.Cost.PreuTensor.value
                if dos is False:
                    tensors = metres / 25 * 3
                else:
                    tensors = metres / 25 * 4
                percent = tensors + (tensors / 100) * 3
                tensors = math.ceil(max(2, percent))
                tensor_preu = round(preu_tensor * tensors, 2)
                tensor_preu = round(tensor_preu * descompte / 100, 2)
                tensor_cost = round(cost_tensor * tensors, 2)

                # Grapa
                preu_grapa = preus_excel.Preu.PreuGrapa.value
                cost_grapa = cost_excel.Cost.PreuGrapa.value
                grapes = postes * 10
                grapa = round(grapes)
                grapes_preu = round(preu_grapa * grapa, 2)
                grapes_preu = round(grapes_preu * descompte / 100)
                grapes_cost = round(cost_grapa * grapa, 2)

                # Ancoratge
                preu_anco = preus_excel.Preu.PreuAnco.value
                cost_anco = cost_excel.Cost.PreuAnco.value
                anco = math.ceil(postes_final * 3)
                anco_preu = round(preu_anco * anco, 2)
                anco_cost = round(cost_anco * anco, 2)

                # Hores
                preu_hora = preus_excel.Preu.PreuHora.value
                cost_hora = cost_excel.Cost.PreuHora.value
                hores_preu = round(hores * preu_hora, 2)
                hores_cost = round(hores * cost_hora, 2)

                # Total
                preu = round(postes_final + tornapuntes + suport + cargol + tap + fil + tensors + grapa + anco + hores, 2)
                cost = round(postes_final + tornapuntes + suport + cargol + tap + fil + tensors + grapa + anco + hores, 2)

                # Benfici
                benefici = round(preu - cost, 2)

                # Percentatge
                if counter == 0:
                    preu_material = postes_final + tornapuntes + suport + cargol + tap + tela + fil + tensors + grapa
                    benefici_necessari = 15 * hores
                    descompte = benefici_necessari * 100 / preu
                    descompte = max(descompte, 60)
                counter += 1
            resposta = 0