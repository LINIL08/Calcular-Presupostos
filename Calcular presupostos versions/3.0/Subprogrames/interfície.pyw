from tkinter import *
from tkinter import messagebox

# ---------------------------------Configuració finestra--------------------------------------------------
arrel = Tk()
arrel.iconbitmap("suinco.ico")
arrel.title("Càlcul presupostos Suinco")
frame = Frame(arrel, width="900", height="600")
frame.pack(fill="both", expand=True)
separador_dalt = Label(frame)
separador_dalt.config(font=("Arial", 1))
separador_dalt.grid(row=0, column=4, pady=0)
separador_baix = Label(frame)
separador_baix.config(font=("Arial", 1))
separador_baix.grid(row=12, column=4, pady=0)


# ---------------------------------Obtenir Mida----------------------------------------------------

varOpcio = IntVar()

Label(frame, text="Selecciona el color i mida de la tanca:").grid(row=1, column=0, padx=15)
centV = Radiobutton(frame, text="100V", variable=varOpcio, value="11")
centV.grid(row=2, column=0)
centG = Radiobutton(frame, text="100G", variable=varOpcio, value="10")
centG.grid(row=3, column=0)
vintV = Radiobutton(frame, text="120V", variable=varOpcio, value="9")
vintV.grid(row=4, column=0)
vintG = Radiobutton(frame, text="120G", variable=varOpcio, value="8")
vintV.grid(row=5, column=0)
cincV = Radiobutton(frame, text="150V", variable=varOpcio, value="7")
cincV.grid(row=6, column=0)
cincG = Radiobutton(frame, text="150G", variable=varOpcio, value="6")
cincG.grid(row=7, column=0)
vuitV = Radiobutton(frame, text="180V", variable=varOpcio, value="5")
vuitV.grid(row=8, column=0)
vuitG = Radiobutton(frame, text="180G", variable=varOpcio, value="4")
vuitG.grid(row=9, column=0)
dosV = Radiobutton(frame, text="200V", variable=varOpcio, value="3")
dosV.grid(row=10, column=0)
dosG = Radiobutton(frame, text="200G", variable=varOpcio, value="2")
dosG.grid(row=11, column=0)


# -------------------------------Obtenir Metres--------------------------------------------------
metres = StringVar()
Label(frame, text="Metres de tanca:").grid(row=1, column=1, sticky="e")
m = Entry(frame, textvariable=metres)
m.grid(row=1, column=2, padx=10)

# -------------------------------Obtenir hores--------------------------------------------------
hores = StringVar()
Label(frame, text="Hores de feina:").grid(row=2, column=1, sticky="e")
h = Entry(frame, textvariable=hores)
h.grid(row=2, column=2)


# -------------------------------Obtenir cantonades----------------------------------------------
cantonades = StringVar()
Label(frame, text="Nombre de cantonades:").grid(row=3, column=1, sticky="e")
ca = Entry(frame, textvariable=cantonades)
ca.grid(row=3, column=2)

# -----------------------------Funcions--------------------------------------------------


def preus():

    from Subprogrames import calculador as calculator
    i = calculator.C
    i.metres = int(metres.get())
    i.hores = int(hores.get())
    i.cantonades = int(cantonades.get())

    # ------------------------------------Poste-----------------------------------------
    Label(frame, text=f"Postes: {i.postes_final}").grid(row=8, column=1, sticky="e")
    Label(frame, text=f"Preu final: {i.poste_preu}€").grid(row=8, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.poste_cost}€").grid(row=8, column=3, sticky="e", padx=10)

    # ------------------------------------Torna-------------------------------------------
    Label(frame, text=f"Tornapuntes: {i.tornapuntes}").grid(row=9, column=1, sticky="e")
    Label(frame, text=f"Preu final: {i.tornapuntes_preu}€").grid(row=9, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.torapuntes_cost}").grid(row=9, column=3, sticky="e", padx=10)

    # ----------------------------------Suport------------------------------------------
    Label(frame, text=f"Suport: {i.suport}").grid(row=10, column=1, sticky="e")
    Label(frame, text=f"Preu final: {i.suport_preu}€").grid(row=10, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.suport_cost}€").grid(row=10, column=3, sticky="e", padx=10)

    # ----------------------------------Cargol----------------------------------------------
    Label(frame, text=f"Cargols: {i.cargol}").grid(row=11, column=1, sticky="e")
    Label(frame, text=f"Preu final: {i.cargol_preu}€").grid(row=11, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.cargol_cost}€").grid(row=11, column=3, sticky="e", padx=10)

    # -----------------------------------Tap-----------------------------------------------
    Label(frame, text=f"Taps: {i.tap}").grid(row=12, column=1, sticky="e")
    Label(frame, text=f"Preu final: {i.tap_preu}€").grid(row=12, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.tap_cost}€").grid(row=12, column=3, sticky="e", padx=10)

    # ---------------------------------Tela----------------------------------------------
    Label(frame, text=f"Tela: {i.tela}").grid(row=13, column=1, sticky="e")
    Label(frame, text=f"Preu final: {i.tela_preu}€").grid(row=13, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.tela_cost}€").grid(row=13, column=3, sticky="e", padx=10)

    # --------------------------------Fil-------------------------------------------------
    Label(frame, text=f"Fil: {i.fil}").grid(row=14, column=1, sticky="e")
    Label(frame, text=f"Preu fnal: {i.fil_preu}€").grid(row=14, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.fil_cost}€").grid(row=14, column=3, sticky="e", padx=10)

    # ---------------------------------Tensor---------------------------------------------
    Label(frame, text=f"Tensors: {i.tensors}").grid(row=15, column=1, sticky="e")
    Label(frame, text=f"Preu final: {i.tensor_preu}€").grid(row=15, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.tensor_cost}€").grid(row=15, column=3, sticky="e", padx=10)

    # ----------------------------------Grapa--------------------------------------------
    Label(frame, text=f"Grapes: {i.grapa}").grid(row=16, column=1, sticky="e")
    Label(frame, text=f"Preu final: {i.grapes_preu}€").grid(row=16, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.grapes_cost}€").grid(row=16, column=3, sticky="e", padx=10)

    # ---------------------------------Anco-----------------------------------------------
    Label(frame, text=f"Acoratge: {i.anco}").grid(row=17, column=1, sticky="e")
    Label(frame, text=f"Preu final: {i.anco_preu}€").grid(row=17, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.anco_cost}€").grid(row=17, column=3, sticky="e", padx=10)

    # ----------------------------------Hora----------------------------------------------
    Label(frame, text=f"Hores: {i.hores}").grid(row=18, column=1, sticky="e")
    Label(frame, text=f"Preu final: {i.hores_preu}€").grid(row=18, column=2, sticky="e")
    Label(frame, text=f"Preu cost final: {i.hores_cost}€").grid(row=18, column=3, sticky="e", padx=10)

    # ----------------------------------Total---------------------------------------------
    Label(frame, text=f"Benefici: {i.benefici_necessari}€").grid(row=19, column=1, sticky="e", padx=10)
    Label(frame, text=f"Preu total: {i.preu}€").grid(row=19, column=2, sticky="e")
    Label(frame, text=f"Preu cost total: {i.cost}€").grid(row=19, column=3, sticky="e", padx=10)

    # -----------------------------------Separadors-----------------------------------------------
    separador_sobre = Label(frame)
    separador_sobre.config(font=("Arial", 1))
    separador_sobre.grid(row=8, column=4, pady=0)
    separador_sota = Label(frame)
    separador_sota.config(font=("Arial", 1))
    separador_sota.grid(row=20, column=4, pady=0)


def central():
    if varOpcio.get() != 0 and len(metres.get()) > 0 and len(hores.get()) > 0 and len(cantonades.get()) > 0:
        try:
            float(metres.get())
            float(hores.get())
            float(cantonades.get())
            desactivar()
            preus()
        except:
            error()
    else:
        error()


def desactivar():
    centV.config(state="disabled")
    centG.config(state="disabled")
    vintV.config(state="disabled")
    vintG.config(state="disabled")
    cincV.config(state="disabled")
    cincG.config(state="disabled")
    vuitV.config(state="disabled")
    vuitG.config(state="disabled")
    dosV.config(state="disabled")
    dosG.config(state="disabled")
    m.config(state="disabled")
    h.config(state="disabled")
    ca.config(state="disabled")


def error():
    messagebox.showerror("Error en les dades", "Hi ha algun camp sense emplenar, o mal emplenat, siusplau emplena'l "
                                               "correctament")


# -------------------------------------------Botó---------------------------------------------------------

Button(frame, text="Calcular", command=central).grid(row=6, column=1)

arrel.mainloop()
