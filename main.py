from tkinter import messagebox
from src.GUI.GUI import GUIMain
from datetime import datetime

if __name__ == "__main__":
    
    if datetime.today() <= datetime(2024, 12, 30):
        app = GUIMain()
        app.master.mainloop()
    else:
        messagebox.showinfo('Atenção', 'Atualização necessária.\nContate o desenvolvedor')


# pyinstaller AlliedWare.spec

