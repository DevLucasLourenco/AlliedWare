from src.GUI.GUI import GUIMain

if __name__ == "__main__":
    app = GUIMain()
    app.master.mainloop()


# pyinstaller --windowed --add-data "src/GUI/images:src/GUI/images" --add-data "tutorial/data*:tutorial/data" --onefile main.py --name AlliedWare


