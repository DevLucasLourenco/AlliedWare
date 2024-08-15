import os
import json
import pandas as pd
import customtkinter

from tkinter import messagebox
from pathlib import Path
from datetime import datetime

from src.data.shareables import ShareHereby
from src.LOG.LOG_manager import KingLog


class Archives:
    PATH = Path(r'filesGenerated')
    PATH.mkdir(exist_ok=True, parents=True)
    
    NotRelocatedFromEmployee:list[tuple[Path, Path]] = list()
    RelocatedFromEmployee:list[tuple[Path, Path]] = list()
    
    RelocatedCC:list[tuple[Path, Path]] = list()
    NotRelocatedCC:list[tuple[Path, Path]] = list()
    
    RelocatedCP:list[tuple[Path, Path]] = list()
    NotRelocatedCP:list[tuple[Path, Path]] = list()
    
    RelocatedHE:list[tuple[Path, Path]] = list()
    NotRelocatedHE:list[tuple[Path, Path]] = list()
    
    
    
    LISTAGE_OF_ALL_DATA_ABOUT_RELOCATING = [RelocatedFromEmployee, RelocatedFromEmployee, RelocatedCC, NotRelocatedCC, RelocatedCP, NotRelocatedCP, RelocatedHE, NotRelocatedHE]
    
    
    @staticmethod
    def __emptinessOfLists():
        res = any(len(item) != 0 for majorItem in Archives.LISTAGE_OF_ALL_DATA_ABOUT_RELOCATING for item in majorItem)
        return res
        
        
    @staticmethod
    def __prepareSuffix():
        return datetime.now().strftime('%d%m%Y-%H%M%S')


    @staticmethod
    def generateDictToExport():
        data = {
                "RelocatedFromEmployee": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.RelocatedFromEmployee],
                "NotRelocatedFromEmployee": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.NotRelocatedFromEmployee],
                "RelocatedCC": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.RelocatedCC],
                "NotRelocatedCC": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.NotRelocatedCC],
                "RelocatedCP": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.RelocatedCP],
                "NotRelocatedCP": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.NotRelocatedCP],
                "RelocatedHE": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.RelocatedHE],
                "NotRelocatedHE": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.NotRelocatedHE],
            }

        return data
        

    @staticmethod
    def exportToXLSX():
        
        if Archives.__emptinessOfLists():
            data = Archives.generateDictToExport()
            
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
         
        if Archives.__emptinessOfLists():
            data = Archives.generateDictToExport()
            
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
        validator = False
        if self.validatorToXLSX.get():
            Archives.exportToXLSX()
            validator = True
        if self.validatorToJSON.get():
            Archives.exportToJSON()
            validator = True
        if self.validatorToStreamlit.get():
            Archives.InvokeStreamlit()
            
        self.top.destroy()
        
        if validator:
            if self.validatorToJSON.get() or self.validatorToXLSX.get():
                os.startfile(Archives.PATH)
            
