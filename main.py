from src.GUI.GUI import GUIMain

if __name__ == "__main__":
    app = GUIMain()
    app.master.mainloop()

# pyinstaller --onefile  --windowed main.py

