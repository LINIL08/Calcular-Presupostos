import os


def nom():
    resposta = "11"

    while resposta != "1" and resposta != "2" \
        and resposta != "3" and resposta != "4"\
        and resposta != "5" and resposta != "6"\
        and resposta != "7" and resposta != "8"\
            and resposta != "9" and resposta != "10":

        os.system("cls")
        resposta = input("Mida i color de la tanca: \n"
                         "1 = 100V\n"
                         "2 = 100G\n"
                         "3 = 120V\n"
                         "4 = 120G\n"
                         "5 = 150V\n"
                         "6 = 150G\n"
                         "7 = 180V\n"
                         "8 = 180G\n"
                         "9 = 200V\n"
                         "10 = 200G\n")

        if resposta == "1":
            return "11"
        elif resposta == "2":
            return "10"
        elif resposta == "3":
            return "9"
        elif resposta == "4":
            return "8"
        elif resposta == "5":
            return "7"
        elif resposta == "6":
            return "6"
        elif resposta == "7":
            return "5"
        elif resposta == "8":
            return "4"
        elif resposta == "9":
            return "3"
        elif resposta == "10":
            return "2"
        else:
            input("La seva resposta no es correcta")
