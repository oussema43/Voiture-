from PyQt6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon
from init import *

app = QApplication([])
windows = loadUi("gui.ui")


selected_row = -1  # Global variable to store the selected row

def quit_click():
    """ Save voitures and exit the application """
    sauvegarder_voitures(voitures)
    QMessageBox.information(windows, "Info", "Données sauvegardées. Fermeture.")
    exit()

def ajout_click():
    """ Add a new car """
    if windows.marq.text() == "":
        QMessageBox.critical(windows, "Error", "Marque is empty")
        return
    if windows.mod.text() == "":
        QMessageBox.critical(windows, "Error", "Modèle is empty")
        return
    if windows.anne.text() == "":
        QMessageBox.critical(windows, "Error", "Année is empty")
        return
    if not windows.anne.text().isdigit():
        QMessageBox.critical(windows, "Error", "Année is not a number")
        return

    marque = windows.marq.text()
    modele = windows.mod.text()
    annee = int(windows.anne.text())
    ajouter_voiture(marque, modele, annee)
    QMessageBox.information(windows, "Success", "Voiture ajoutée avec succès")
    windows.marq.setText("")
    windows.mod.setText("")
    windows.anne.setText("")
    tout_click()

def tout_click():
    """ Show all cars in the table """
    windows.tab.setRowCount(0)  # Clear the table first
    i = 0
    for voiture in voitures.values():
        print(f"voiture: {voiture}")  # Debug print to check the structure of 'voiture'
        windows.tab.setRowCount(i+1)  # Ensure i is an integer here
        windows.tab.setItem(i, 0, QTableWidgetItem(str(voiture['marque'])))
        windows.tab.setItem(i, 1, QTableWidgetItem(str(voiture['modele'])))
        windows.tab.setItem(i, 2, QTableWidgetItem(str(voiture['annee'])))
        windows.tab.setItem(i, 3, QTableWidgetItem("Oui" if voiture["disponible"] else "Non"))
        i += 1

    

def aff_click():
    """ Show only available cars """
    windows.tab.setRowCount(0)  # Clear the table first
    i = 0
    for voiture in voitures.values():
        if voiture["disponible"]:
            windows.tab.setRowCount(i + 1)
            windows.tab.setItem(i, 0, QTableWidgetItem(voiture['marque']))
            windows.tab.setItem(i, 1, QTableWidgetItem(voiture['modele']))
            windows.tab.setItem(i, 2, QTableWidgetItem(str(voiture['annee'])))
            windows.tab.setItem(i, 3, QTableWidgetItem("Oui"))
            i += 1
    return


def store_selected_row(row, _):
    """ Store the selected row when a cell is clicked """
    global selected_row
    selected_row = row

def get_selected_row_data():
    """ Get data from the selected row """
    if selected_row == -1:
        QMessageBox.critical(windows, "Error", "Aucune ligne sélectionnée")
        return None

    row_data = []
    for col in range(windows.tab.columnCount()):
        item = windows.tab.item(selected_row, col)
        if item:
            row_data.append(item.text())
    return row_data

def supp_click():
    """ Remove the selected car """
    row_data = get_selected_row_data()
    if not row_data:
        return

    for id, voiture in voitures.items():
        if (voiture["marque"] == row_data[0] and 
            voiture["modele"] == row_data[1] and 
            str(voiture["annee"]) == row_data[2]):
            supprimer_voiture(voitures, id)
            QMessageBox.information(windows, "Success", "Voiture supprimée avec succès")
            tout_click()
            return

def louer_click():
    """ Rent the selected car """
    row_data = get_selected_row_data()
    if not row_data:
        return

    for id, voiture in voitures.items():
        if (voiture["marque"] == row_data[0] and 
            voiture["modele"] == row_data[1] and 
            str(voiture["annee"]) == row_data[2]):
            louer_voiture(voitures, id)
            QMessageBox.information(windows, "Success", "Voiture louée avec succès")
            tout_click()
            return

def retourner_click():
    """ Return the selected car """
    row_data = get_selected_row_data()
    if not row_data:
        return

    for id, voiture in voitures.items():
        if (voiture["marque"] == row_data[0] and 
            voiture["modele"] == row_data[1] and 
            str(voiture["annee"]) == row_data[2]):
            retourner_voiture(voitures, id)
            QMessageBox.information(windows, "Success", "Voiture retournée avec succès")
            tout_click()
            return

def main():
    """ Main function to show the GUI and connect signals """
    windows.setWindowTitle("Voiture")
    windows.setWindowIcon(QIcon("car.ico"))
    windows.show()
    windows.tout.clicked.connect(tout_click)
    windows.aff.clicked.connect(aff_click)
    windows.louer.clicked.connect(louer_click)
    windows.retourner.clicked.connect(retourner_click)
    windows.supp.clicked.connect(supp_click)
    windows.quit.clicked.connect(quit_click)
    windows.ajout.clicked.connect(ajout_click)
    windows.tab.cellClicked.connect(store_selected_row)
    app.exec()
