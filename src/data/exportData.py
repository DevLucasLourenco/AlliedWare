import os
import json
import time
import webbrowser
import pandas as pd
import customtkinter

from pathlib import Path
from threading import Timer
from datetime import datetime
from tkinter import messagebox

from src.data.shareables import ShareHereby
from src.LOG.LOG_manager import LOGGER


class Archives:
    PATH = Path(r'filesGenerated')
    PATH.mkdir(exist_ok=True, parents=True)
    
    RelocatedFromEmployee:list[tuple[Path, Path]] = list()
    NotRelocatedFromEmployee:list[tuple[Path, Path]] = list()
    
    RelocatedFromEmployeeFired:list[tuple[Path, Path]] = list()
    NotRelocatedFromEmployeeFired:list[tuple[Path, Path]] = list()
    
    RelocatedCC:list[tuple[Path, Path]] = list()
    NotRelocatedCC:list[tuple[Path, Path]] = list()
    
    RelocatedCP:list[tuple[Path, Path]] = list()
    NotRelocatedCP:list[tuple[Path, Path]] = list()
    
    RelocatedHE:list[tuple[Path, Path]] = list()
    NotRelocatedHE:list[tuple[Path, Path]] = list()
    
    
    LISTAGE_OF_ALL_DATA_ABOUT_RELOCATING = [RelocatedFromEmployee, NotRelocatedFromEmployee, 
                                            RelocatedFromEmployeeFired, NotRelocatedFromEmployeeFired, 
                                            RelocatedCC, NotRelocatedCC, 
                                            RelocatedCP, NotRelocatedCP, 
                                            RelocatedHE, NotRelocatedHE,
                                            ]
    
    
    @staticmethod
    def _emptinessOfLists():
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
                
                "RelocatedFromEmployeeFired":[("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.RelocatedFromEmployeeFired],
                "NotRelocatedFromEmployeeFired":[("File", "Destination")] + [(str(file), str(destination)) for file, destination in Archives.NotRelocatedFromEmployeeFired],
                
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
        
        if Archives._emptinessOfLists():
            data = Archives.generateDictToExport()
            
            filename = Archives.PATH / f'XLSX_{Archives.__prepareSuffix()}.xlsx'
            with pd.ExcelWriter(filename) as writer:
                for sheet_name, rows in data.items():
                    df = pd.DataFrame(rows[1:], columns=rows[0])
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                    
            LOGGER(f'XLSX exportado: {filename}', 'INFO')
            
        else:
            messagebox.showerror('Erro ao Exportar - XLSX', f'Impossível exportar dados sem realizar uma das as tarefas de\n{", ".join(ShareHereby.KEYS)}')
            LOGGER(f'XLSX - Impossível exportar dados sem realizar uma das as tarefas de {", ".join(ShareHereby.KEYS)}', 'WARNING')
            

    @staticmethod
    def exportToJSON():
        
         
        if Archives._emptinessOfLists():
            data = Archives.generateDictToExport()
            
            filename = Archives.PATH / f'JSON {Archives.__prepareSuffix()}.json'
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            LOGGER(f'JSON exportado: {filename}', 'INFO')
            
        else:
            messagebox.showerror('Erro ao Exportar - JSON', f'Impossível exportar dados sem realizar uma das as tarefas de\n{", ".join(ShareHereby.KEYS)}')
            LOGGER(f'JSON - Impossível exportar dados sem realizar uma das as tarefas de {", ".join(ShareHereby.KEYS)}', 'WARNING')
            
        
        

class ExportWindow:
    
    def __init__(self, master) -> None:
        self.masterForUsage = master
        
        self.validatorToXLSX = customtkinter.BooleanVar(value=False)
        self.validatorToJSON = customtkinter.BooleanVar(value=False)
        
        self.run()
        
        
    def run(self):
        self.buildTopLevel()
        
        self.buildButtonOpenDir()
        self.buildCheckBoxXLSX()
        self.buildCheckBoxJSON()
        self.buildExecutionButton()
        
        self.PACK_ALL()
        
        
    def PACK_ALL(self):
        self.buttonToDir.pack(padx=(5, 0), pady=(10, 0))
        self.buttonCBXLSX.pack(padx=(5, 0), pady=(20, 0))
        self.buttonCBJSON.pack(padx=(7, 0), pady=(10, 0))
        self.execButton.pack(side="bottom", fill="x", padx=0, pady=(5, 0))

    
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
        
    def buildExecutionButton(self):
        self.execButton = customtkinter.CTkButton(self.top, 
                                                  text="Exportar", 
                                                  command=self.export)

    def buildButtonOpenDir(self):
        self.buttonToDir = customtkinter.CTkButton(self.top,
                                                   text='Abrir Diretório',
                                                   command=self._openDir)
    
    
    def _openDir(self):
        os.startfile(r'filesGenerated')
        
    
    def export(self):
        if self.validatorToXLSX.get():
            Archives.exportToXLSX()
        if self.validatorToJSON.get():
            Archives.exportToJSON()
            
        self.top.destroy()
    
        if Archives._emptinessOfLists():
            if self.validatorToJSON.get() or self.validatorToXLSX.get():
                os.startfile(Archives.PATH)
                
