from openpyxl import load_workbook


class Preu:
    num = "11"
    excel = load_workbook("Preus.xlsx")
    full = excel["Preus"]
    PreuPostes = full[f"B{num}"]
    PreuTorna = full[f"C{num}"]
    PreuSuport = full[f"D{num}"]
    PreuCargol = full[f"E{num}"]
    PreuTap = full[f"F{num}"]
    PreuTela = full[f"G{num}"]
    PreuFil = full[f"H{num}"]
    PreuTensor = full[f"I{num}"]
    PreuGrapa = full[f"J{num}"]
    PreuAnco = full[f"K{num}"]
    PreuHora = full[f"L2"]
