tabStyleSheetStringV1 = "QTabWidget::pane { " \
                      "    border-top: 2px solid #C2C7CB;" \
                      "    position: absolute;" \
                      "    top: -0.5em;" \
                      "}" \
                      "QTabWidget::tab-bar {" \
                      "    alignment: center;" \
                      "}" \
 \
                      "QTabBar::tab {" \
                      "    background: rgb(0, 0, 0)" \
                      "    color: rgb(0, 0, 0)" \
                      "    border: 2px solid #C4C4C3;" \
                      "    border-bottom-color: #C2C7CB; " \
                      "    border-top-left-radius: 4px; " \
                      "    border-top-right-radius: 4px;" \
                      "    min-width: 8ex;" \
                      "    padding: 2px;" \
                      "}" \
 \
                      "QTabBar::tab:selected, QTabBar::tab:hover {" \
                      "    background: rgb(44, 46, 47)" \
                      "}" \
 \
                      "QTabBar::tab:selected {" \
                      "    border-color: #9B9B9B;" \
                      "    border-bottom-color: #C2C7CB; " \
                      "}"

tabStyleSheetStringV2 = "QTabWidget::pane {" \
                        "    background: white;" \
                        "}" \
 \
                        "QTabWidget::tab-bar:top {" \
                        "    top: 1px;" \
                        "}" \
 \
                        "QTabWidget::tab-bar:bottom {" \
                        "    bottom: 1px;" \
                        "}" \
 \
                        "QTabWidget::tab-bar:left {" \
                        "    right: 1px;" \
                        "}" \
 \
                        "QTabWidget::tab-bar:right {" \
                        "    left: 1px;" \
                        "}" \
 \
                        "QTabBar::tab {" \
                        "    border: 1px solid black;" \
                        "}" \
 \
                        "QTabBar::tab:selected {" \
                        "    background: #adb5bd;" \
                        "}" \
 \
                        "QTabBar::tab:!selected {" \
                        "    background: transparent;" \
                        "}" \
 \
                        "QTabBar::tab:!selected:hover {" \
                        "    background: #343a40;" \
                        "}" \
 \
                        "QTabBar::tab:top:!selected {" \
                        "    margin-top: 3px;" \
                        "}" \
 \
                        "QTabBar::tab:bottom:!selected {" \
                        "    margin-bottom: 3px;" \
                        "}" \
 \
                        "QTabBar::tab:top, QTabBar::tab:bottom {" \
                        "    min-width: 8ex;" \
                        "    margin-right: -1px;" \
                        "    padding: 5px 10px 5px 10px;" \
                        "}" \
 \
                        "QTabBar::tab:top:selected {" \
                        "    border-bottom-color: none;" \
                        "}" \
 \
                        "QTabBar::tab:bottom:selected {" \
                        "    border-top-color: none;" \
                        "}" \
 \
                        "QTabBar::tab:top:last, QTabBar::tab:bottom:last," \
                        "QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {" \
                        "    margin-right: 0;" \
                        "}" \
 \
                        "QTabBar::tab:left:!selected {" \
                        "    margin-right: 3px;" \
                        "}" \
 \
                        "QTabBar::tab:right:!selected {" \
                        "    margin-left: 3px;" \
                        "}" \
 \
                        "QTabBar::tab:left, QTabBar::tab:right {" \
                        "    min-height: 8ex;" \
                        "    margin-bottom: -1px;" \
                        "    padding: 10px 5px 10px 5px;" \
                        "}" \
 \
                        "QTabBar::tab:left:selected {" \
                        "    border-left-color: none;" \
                        "}" \
 \
                        "QTabBar::tab:right:selected {" \
                        "    border-right-color: none;" \
                        "}" \
 \
                        "QTabBar::tab:left:last, QTabBar::tab:right:last," \
                        "QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {" \
                        "    margin-bottom: 0;" \
                        "}"

tabStyleSheetString = "QTabWidget::pane {" \
                        "    background-color: rgb(58,63,66);" \
                        "    top: -0.7em;" \
                        "}" \
 \
                        "QTabWidget::tab-bar {" \
                        "   width: 999999px;" \
                        "}" \
 \
                        "QTabBar::tab {" \
                        "    border: 0px solid black;" \
                        "}" \
 \
                        "QTabBar::tab:selected {" \
                        "    background: #adb5bd;" \
                        "    font-size: 16pt;" \
                        "    height: 40px;" \
                        "}" \
 \
                        "QTabBar::tab:!selected {" \
                        "    background: transparent;" \
                        "    font-size: 14pt;" \
                        "    height: 35px;" \
                        "}" \
 \
                        "QTabBar::tab:!selected:hover {" \
                        "    background: #343a40;" \
                        "    font-size: 16pt;" \
                        "}" \
 \
                        "QTabBar::tab:top:!selected {" \
                        "    margin-top: 3px;" \
                        "}" \
 \
                        "QTabBar::tab:bottom:!selected {" \
                        "    margin-bottom: 3px;" \
                        "}" \
 \
                        "QTabBar::tab:top, QTabBar::tab:bottom {" \
                        "    min-width: 8ex;" \
                        "    margin-right: -1px;" \
                        "    padding: 5px 10px 5px 10px;" \
                        "}" \
 \
                        "QTabBar::tab:top:selected {" \
                        "    border-bottom-color: none;" \
                        "}" \
 \
                        "QTabBar::tab:bottom:selected {" \
                        "    border-top-color: none;" \
                        "}" \
 \
                        "QTabBar::tab:top:last, QTabBar::tab:bottom:last," \
                        "QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {" \
                        "    margin-right: 0;" \
                        "}" \
 \
                        "QTabBar::tab:left:!selected {" \
                        "    margin-right: 3px;" \
                        "}" \
 \
                        "QTabBar::tab:right:!selected {" \
                        "    margin-left: 3px;" \
                        "}" \
 \
                        "QTabBar::tab:left, QTabBar::tab:right {" \
                        "    min-height: 8ex;" \
                        "    margin-bottom: -1px;" \
                        "    padding: 10px 5px 10px 5px;" \
                        "}" \
 \
                        "QTabBar::tab:left:selected {" \
                        "    border-left-color: none;" \
                        "}" \
 \
                        "QTabBar::tab:right:selected {" \
                        "    border-right-color: none;" \
                        "}" \
 \
                        "QTabBar::tab:left:last, QTabBar::tab:right:last," \
                        "QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {" \
                        "    margin-bottom: 0;" \
                        "}"

pushButtonStyleSheetString = "QPushButton{" \
                             "color: rgba(255,255,255,255); " \
                             "border-style: solid; " \
                             "border-radius: 4px; " \
                             "border-width: 1px; " \
                             "border-color: rgba(255,255,255,255);" \
                             "}" \
                             "QPushButton::hover{" \
                             "color: rgba(56,56,56,255);" \
                             "background-color: rgba(255,255,255,255);" \
                             "}"
pushButtonSelectedStyleSheetString = "QPushButton{" \
                             "color: rgba(56,56,56,255); " \
                             "background-color: rgba(200,200,200,255);" \
                             "border-style: solid; " \
                             "border-radius: 4px; " \
                             "border-width: 1px; " \
                             "border-color: rgba(255,255,255,255);" \
                             "}" \
                             "QPushButton::hover{" \
                             "color: rgba(56,56,56,255);" \
                             "background-color: rgba(255,255,255,255);" \
                             "}"

windowStyleSheetString = "background-color: rgb(58,63,66);" \
                         "color: rgb(255, 255, 255);"
