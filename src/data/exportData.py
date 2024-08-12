import json
from tkinter import messagebox
import pandas as pd
import customtkinter


from pathlib import Path
from datetime import (datetime, 
                      timedelta)

from src.data.shareables import ShareHereby
from src.LOG.LOG_manager import KingLog


class Archives:
    PATH = Path(r'filesGenerated')
    PATH.mkdir(exist_ok=True, parents=True)
    
    NotRelocatedFromEmployee:list[tuple[Path, Path]] = list()
    RelocatedFromEmployee:list[tuple[Path, Path]] = list()
    
    @staticmethod
    def __validatorToExport():
        if (len(Archives.RelocatedFromEmployee)==0) and (len(Archives.NotRelocatedFromEmployee)==0):
            return False
        
        
    @staticmethod
    def __prepareSuffix():
        return datetime.now().strftime('%d%m%Y-%H%M%S')


    @staticmethod
    def exportToXLSX():
        if not (len(Archives.RelocatedFromEmployee)==0) and (len(Archives.NotRelocatedFromEmployee)==0):
            data = {
                "RelocatedFromEmployee": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.RelocatedFromEmployee],
                "NotRelocatedFromEmployee": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.NotRelocatedFromEmployee],
            }
            
            filename = Archives.PATH / f'XLSX {Archives.__prepareSuffix()}.xlsx'
            with pd.ExcelWriter(filename) as writer:
                for sheet_name, rows in data.items():
                    df = pd.DataFrame(rows[1:], columns=rows[0])
                df.to_excel(writer, sheet_name=sheet_name, index=False)
            KingLog(f'XLSX exportado: {filename}', 'INFO')
        else:
            messagebox.showerror('Erro ao Exportar - XLSX', f'Impossível exportar dados sem realizar uma das as tarefas de\n{", ".join(ShareHereby.KEYS)}')
            KingLog(f'XLSX - Impossível exportar dados sem realizar uma das as tarefas de\n{", ".join(ShareHereby.KEYS)}', 'WARNING')
            

    @staticmethod
    def exportToJSON():
        if not (len(Archives.RelocatedFromEmployee)==0) and (len(Archives.NotRelocatedFromEmployee)==0):
            data = {
                "RelocatedFromEmployee": [{"File": str(file), "Destination": str(destination)} for file, destination in Archives.RelocatedFromEmployee],
                "NotRelocatedFromEmployee": [{"File": str(file), "Destination": str(destination)} for file, destination in Archives.NotRelocatedFromEmployee],
            }
            
            filename = Archives.PATH / f'JSON {Archives.__prepareSuffix()}.json'
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            KingLog(f'JSON exportado: {filename}', 'INFO')
        else:
            messagebox.showerror('Erro ao Exportar - JSON', f'Impossível exportar dados sem realizar uma das as tarefas de\n{", ".join(ShareHereby.KEYS)}')
            KingLog(f'JSON - Impossível exportar dados sem realizar uma das as tarefas de\n{", ".join(ShareHereby.KEYS)}', 'WARNING')
            
            

        
        
    def InvokeStreamlit(self):
        app = StreamlitServerRun()
        
        KingLog('Streamlit Server construído.')
        
        
class StreamlitServerRun():
    ...
    
    

# class ExportWindow(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Exportação")
#         self.geometry("300x180")
        
#         self.xlsx_var = tk.BooleanVar()
#         self.json_var = tk.BooleanVar()
#         self.streamlit_var = tk.BooleanVar()
        
#         xlsx_cB = tk.Checkbutton(self, text="Exportar para XLSX", variable=self.xlsx_var).pack(anchor="w", padx=20, pady=5)
#         json_cB = tk.Checkbutton(self, text="Exportar para JSON", variable=self.json_var).pack(anchor="w", padx=20, pady=5)
#         streanlit_cB = tk.Checkbutton(self, text="Invocar Streamlit", variable=self.streamlit_var).pack(anchor="w", padx=20, pady=5)
        
#         button_exec = tk.Button(self, text="Exportar", command=self.export).pack(pady=20)

#     def export(self):
#         # Atualiza as variáveis antes de usar
#         self.update_idletasks()
        
#         print("JSON:", self.json_var.get())
#         print("XLSX:", self.xlsx_var.get())
#         print("Streamlit:", self.streamlit_var.get())
        
#         if self.json_var.get():
#             print("Exportando JSON")
#             # Archives.exportToJSON()
#         if self.xlsx_var.get():
#             print("Exportando XLSX")
#             # Archives.exportToXLSX()
#         if self.streamlit_var.get():
#             print("Invocando Streamlit")
#             # Archives.InvokeStreamlit()

class ExportWindow:
    
    def __init__(self, master) -> None:
        self.masterForUsage = master
        
        self.validatorToXLSX = customtkinter.BooleanVar(value=False)
        self.validatorToJSON = customtkinter.BooleanVar(value=False)
        self.validatorToStreamlit = customtkinter.BooleanVar(value=False)
        
        self.run()
        
        
    def run(self):
        self.buildTopLevel()
        self.buildCheckBoxXLSX()
        self.buildCheckBoxJSON()
        self.buildCheckBoxStreamlit()
        self.buildExecutionButton()
        
        self.PACK_ALL()
        
        
    def PACK_ALL(self):
        self.buttonCBXLSX.pack(padx=(5, 0), pady=(30, 0))
        self.buttonCBJSON.pack(padx=(5, 0), pady=(10, 0))
        self.buttonCBDStreamlit.pack(padx=(5, 0), pady=(10, 0))
        self.execButton.pack(side="bottom", fill="x", padx=0, pady=0)

    
    def buildTopLevel(self):
        self.top = customtkinter.CTkToplevel(self.masterForUsage)
        self.top.grab_set()
        
        self.top.title("DIF - Preparações")
        self.top.geometry("+%d+%d" % (self.masterForUsage.winfo_screenwidth() // 2 - 100, self.masterForUsage.winfo_screenheight() // 2 - 50))
        self.top.resizable(False, False)
        self.top.pack_propagate(False)

        
    def buildCheckBoxXLSX(self):
        self.buttonCBXLSX = customtkinter.CTkCheckBox(self.top, 
                                                        text='Exportar para XLSX', 
                                                        variable=self.validatorToXLSX)
        
    def buildCheckBoxJSON(self):
        self.buttonCBJSON = customtkinter.CTkCheckBox(self.top, 
                                                        text='Exportar para JSON', 
                                                        variable=self.validatorToJSON)
        
    def buildCheckBoxStreamlit(self):
        self.buttonCBDStreamlit = customtkinter.CTkCheckBox(self.top, 
                                                        text='Exportar para StreamLit', 
                                                        variable=self.validatorToStreamlit)
        
    def buildExecutionButton(self):
        self.execButton = customtkinter.CTkButton(self.top, 
                                                  text="Exportar", 
                                                  command=self.export)

    def export(self):
        print("JSON:", self.validatorToJSON.get())
        print("XLSX:", self.validatorToXLSX.get())
        print("Streamlit:", self.validatorToStreamlit.get())
        
        if self.validatorToJSON.get():
            Archives.exportToJSON()
        if self.validatorToXLSX.get():
            Archives.exportToXLSX()
        if self.validatorToStreamlit.get():
            Archives.InvokeStreamlit()
        
        
        