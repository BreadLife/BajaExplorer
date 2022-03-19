from PyQt5.QtWidgets import QMessageBox
from gui_stylesheet import windowStyleSheetString


def liveClockingProcede_dialog():
    Text = "AVERTISSEMENT: \n" \
           "Assurez-vous que la EVT n'est PAS installé sur le véhicule lorsque le " \
           "mode de live clocking est activé."
    InformativeText = "Le mode live clocking permet de faire tourner la trompette en " \
                      "temps réel. La trompette VA casser si le EVT est installé sur la " \
                      "transmission. Procédez à vos propres risques."

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setStyleSheet(windowStyleSheetString)

    msg.setText(Text)
    msg.setInformativeText(InformativeText)
    msg.setWindowTitle("Avertissement")

    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Abort)

    return msg.exec_()