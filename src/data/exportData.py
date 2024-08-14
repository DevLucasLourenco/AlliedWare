import json
import os
from tkinter import messagebox
import pandas as pd
import customtkinter


from pathlib import Path
from datetime import (datetime, 
                      timedelta)

from src.GUI.topLevels.dynamicalWindow import DynamicalWindowApproach
from src.data.shareables import ShareHereby
from src.LOG.LOG_manager import KingLog


class Archives:
    PATH = Path(r'filesGenerated')
    PATH.mkdir(exist_ok=True, parents=True)
    
    NotRelocatedFromEmployee:list[tuple[Path, Path]] = list()
    RelocatedFromEmployee:list[tuple[Path, Path]] = list()
    
    
    @staticmethod
    def __emptinessOfLists():
        if (len(Archives.RelocatedFromEmployee)==0) and (len(Archives.NotRelocatedFromEmployee)==0):
            return False
        
        
    @staticmethod
    def __prepareSuffix():
        return datetime.now().strftime('%d%m%Y-%H%M%S')


    @staticmethod
    def exportToXLSX():
        if not Archives.__emptinessOfLists():
            data = {
                "RelocatedFromEmployee": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.RelocatedFromEmployee],
                "NotRelocatedFromEmployee": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.NotRelocatedFromEmployee],
                # fazer assim pra todos "CC": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.algumacoisaaqui],
            } # criar um loop desse dict aq de cima como uma função q vai retornar exatamente isto
            
            filename = Archives.PATH / f'XLSX_{Archives.__prepareSuffix()}.xlsx'
            with pd.ExcelWriter(filename) as writer:
                for sheet_name, rows in data.items():
                    df = pd.DataFrame(rows[1:], columns=rows[0])
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            KingLog(f'XLSX exportado: {filename}', 'INFO')
        else:
            messagebox.showerror('Erro ao Exportar - XLSX', f'Impossível exportar dados sem realizar uma das as tarefas de\n{", ".join(ShareHereby.KEYS)}')
            KingLog(f'XLSX - Impossível exportar dados sem realizar uma das as tarefas de {", ".join(ShareHereby.KEYS)}', 'WARNING')
            

    @staticmethod
    def exportToJSON():
        if not Archives.__emptinessOfLists():
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
            KingLog(f'JSON - Impossível exportar dados sem realizar uma das as tarefas de {", ".join(ShareHereby.KEYS)}', 'WARNING')
            
            
    def InvokeStreamlit(self):
        app = StreamlitServerRun()
        
        KingLog('Streamlit Server construído.')
        
        
class StreamlitServerRun():
    ...
    

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
        
        self.top.title("Export Window")
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
        print("XLSX:", self.validatorToXLSX.get())
        print("JSON:", self.validatorToJSON.get())
        print("Streamlit:", self.validatorToStreamlit.get())
        
        if self.validatorToXLSX.get():
            Archives.exportToXLSX()
        if self.validatorToJSON.get():
            Archives.exportToJSON()
        if self.validatorToStreamlit.get():
            Archives.InvokeStreamlit()
            
        self.top.destroy()
        
        if self.validatorToJSON or self.validatorToXLSX:
            os.startfile(Archives.PATH)
            
        print("Realocado:", Archives.RelocatedFromEmployee, "Não realocado:", Archives.NotRelocatedFromEmployee, sep='\n')
            
            
        
        
# class SelectOptionsToExportWindow():
#     def __init__(self, masterForUsage) -> None:
#         self.masterForUsage = masterForUsage
        
#     def instanceDynamicalWindow(self):
#         options={
#             "DIF":,
#             "CC":print,
            
#         }
        
#         app = DynamicalWindowApproach(self.masterForUsage)
#         app.giveOptions()