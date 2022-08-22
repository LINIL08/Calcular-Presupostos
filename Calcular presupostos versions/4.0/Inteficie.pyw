from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from openpyxl import load_workbook

# Totes les funcions van en aquest tram:


def central():
    try:
        m = int(metres.get())
        t = int(trams.get())
        g = int(graons.get())
        h = int(hores.get())
        if len(llista.get()) != 4:
            error_dades()
        else:
            desactivar()

        a = True
    except:
        error_dades()
        a = False
    """
    if a:
        try:
            resultat(m, t, g, h)
        except:
            error_calcul()"""
    resultat(m, t, g, h)


def desactivar():
    metre.config(state="disabled")
    tram.config(state="disabled")
    grao.config(state="disabled")
    hora.config(state="disabled")
    llista.config(state="disabled")


def error_dades():
    messagebox.showerror("Error", "Hi ha algun error en les dades, arregli'l per continuar")


def error_calcul():
    messagebox.showerror("Error", "Error en fer el cálcul")


def resultat(metres, trams, graons, hores):
# -----------------------------------------------Obtenir Quantitat------------------------------------------------
    k_torna = 2
    k_suport = 4
    k_tensor = 3
    k_cargol = 2
    postes = metres / 3 + 2
    torna = k_torna * trams
    suports = k_suport * trams
    cargols = k_cargol * trams
    taps = metres / 3 + 2
    tela = metres
    fil = metres * 3
    tensors = k_tensor * trams
    grapes = 10 * postes
    anco = 3 * postes
# -----------------------------------------------Convertir tipus---------------------------------------------------
    if llista.get() == "200G":
        tipus = "2"
    elif llista.get() == "200V":
        tipus = "3"
    elif llista.get() == "180G":
        tipus = "4"
    elif llista.get() == "180V":
        tipus = "5"
    elif llista.get() == "150G":
        tipus = "6"
    elif llista.get() == "150V":
        tipus = "7"
    elif llista.get() == "120G":
        tipus = "8"
    elif llista.get() == "120V":
        tipus = "9"
    elif llista.get() == "100G":
        tipus = "10"
    elif llista.get() == "100V":
        tipus = "11"


# ------------------------------------Obtenir P. Venta-------------------------------------------------------------
    excel = load_workbook("Preus.xlsx")
    full1 = excel["Preus"]
    full = excel["Cost"]
    num = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    preu = []
    cost = []

    for i in num:
        preu.append(full1[i + tipus].value)
    preu.append(full1["L2"])

    for i in num:
        cost.append(full[i + tipus].value)
    cost.append(full["L2"])

# ----------------------------------------------Aplicació de dte---------------------------------------------------
    materials = [postes, torna, suports, cargols, taps, fil, tensors, graons, anco, hores]

    p1p = 0
    for i in range(9):
        p1p += preu[i] * materials[i]

    p1c = 0
    for i in range(9):
        p1c += cost[i] * materials[i]

    dte = (15 * hores * 100) / (p1p - p1c)
    dte1 = 100 - dte

    p2p = 0
    for i in range(11):
        p2p += preu[i] * materials[i]

    p2c = 0
    for i in range(11):
        p2c += cost[i] * materials[i]

    pt = p1p / 100 * dte1 + preu[9] * anco + preu[10] * hores
    dte = round(dte)
# ---------------------------------Taula Preus---------------------------------------------------------------------
    total = []
    for i in range(11):
        total.append(round(preu[i] * materials[i] / 100 * dte, 2))
    ben = round((pt-p2c)/ 100 * dte, 2)
    pvp = round(p2p, 2)
    pt = round(pt, 2)
    employee_list = [('Quantitat:', 'Article:', 'P.Cost:', 'P.Venta:', 'Total:'),
                     (round(postes), '      Postes', cost[0], preu[0], total[0]),
                     (round(torna), '      Tornapuntes', cost[1], preu[1], total[1]),
                     (round(suports), '      Suports', cost[2], preu[2], total[2]),
                     (round(cargols), '      Cargols', cost[3], preu[3], total[3]),
                     (round(taps), '      Taps', cost[4], preu[4], total[4]),
                     (round(tela), '      Tela', cost[5], preu[5], total[5]),
                     (round(fil), '      Filferro', cost[6], preu[6], total[6]),
                     (round(tensors), '      Tensors', cost[7], preu[7], total[7]),
                     (round(grapes), '      Grapes', cost[8], preu[8], total[8]),
                     (round(anco), '      Ancoratge', cost[9], preu[9], total[9]),
                     (round(hores), '      Hores', cost[10], preu[10], total[10]),
                     ("", f"Dte: {dte}%", f"Ben: {ben}€", f"P.V.P: {pvp}€", f"P. Final: {pt}€")]

    total_rows = len(employee_list)
    total_columns = len(employee_list[0])

    for i in range(total_rows):
        for j in range(total_columns):
            print(i)
            if i == 0:
                entry = Entry(frame2, width=14, bg='light grey', fg='Black',
                              font=('Arial', 11, 'bold'))
            else:
                entry = Entry(frame2, width=14, fg='black',
                              font=('Arial', 11, ''), justify="right")
                if j == 1 and i != 12:
                    entry.config(justify='left')

            entry.grid(row=i, column=j)
            entry.insert(END, employee_list[i][j])


arrel = Tk()
arrel.iconbitmap("Suinco.ico")
arrel.title("Càlcul presupostos Suinco")
frame = Frame(arrel, width="500", height="200")
frame.grid(row=0, column=0)
frame2 = Frame(arrel, width="1", height="1")
frame2.config(bg="white")
frame2.grid(row=1, column=0)
separador_dalt = Label(frame)
separador_dalt.config(font=("Arial", 1))
separador_dalt.grid(row=0, column=4, pady=0)
separador_baix = Label(frame)
separador_baix.config(font=("Arial", 1))
separador_baix.grid(row=12, column=4, pady=0)

# -----------------------------------------------------------------------------------------------------
metres = StringVar()
Label(frame, text="Metres de tanca:", font=("Arial", 11)).grid(row=1, column=0, sticky="e", padx=5)
metre = Entry(frame, textvariable=metres, font=("Arial", 11))
metre.grid(row=1, column=1, pady=20)

# -----------------------------------------------------------------------------------------------------
trams = StringVar()
Label(frame, text="Nombre de trams:", font=("Arial", 11)).grid(row=2, column=0, sticky="e", padx=5)
tram = Entry(frame, textvariable=trams, font=("Arial", 11))
tram.grid(row=2, column=1)

# -----------------------------------------------------------------------------------------------------
graons = StringVar()
Label(frame, text="Graons:", font=("Arial", 11)).grid(row=3, column=0, sticky="e", padx=5)
grao = Entry(frame, textvariable=graons, font=("Arial", 11))
grao.grid(row=3, column=1, pady=20)

# -----------------------------------------------------------------------------------------------------
Label(frame, text="Tipus de tanca:", font=("Arial", 11)).grid(row=1, column=2, padx=10, sticky="e")
llista = ttk.Combobox(values=["200V", "200G", "180V", "180G", "150V", "150G", "120V", "120G", "100V", "100G"],
                      state="readonly", font=("Arial", 11))
llista.place(x=425, y=30)
Label(frame, text="").grid(row=1, column=3, padx=70)

# -----------------------------------------------------------------------------------------------------
hores = StringVar()
Label(frame, text="Hores:", font=("Arial", 11)).grid(row=2, column=2, sticky="e", padx=10)
hora = Entry(frame, textvariable=hores, font=("Arial", 11))
hora.grid(row=2, column=3, padx=20)

# -----------------------------------------------------------------------------------------------------
Button(frame, text="Calcular", command=central, bg="light grey", font=("Arial", 11)).grid(row=3, column=3)

arrel.mainloop()
