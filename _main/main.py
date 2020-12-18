######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS

# -*- coding: utf-8 -*-

# Arquivo local:
from gui_main import Gui_main

# Arquivo de sistema:
import sys

# Arquivo da biblioteca de interface gráfica:
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Gui_main()

    win.show()
    sys.exit(app.exec_())