import pandas as pd
import tkinter as tk
import customtkinter

from openpyxl import Workbook
from tkinter import messagebox


class Archives:
    NotRelocatedFromEmployee: list = list()
    RelocatedFromEmployee:dict
    
    def receiveInfo(self, infos:dict):
        ...
        
    def prepareToEachExportMethod(self):
        ... # aqui será para realizar um meio de, a partir das informações recebidas, alocar o uso automático pra LOG, XLSx e JSON

    def exportToXLSX():
        ...
    
        
    def exportToJSON(self):
        ...
        
    def InvokeStreamlit(self):
        app = StreamlitServerRun()
        ...
        
        
class StreamlitServerRun():
    ...
    
    
class ExportWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exportação")
        self.geometry("300x180")
        
        # Inicializar a instância da classe Archives
        self.archives = Archives()
        
        # Criação de checkboxes para as opções
        self.xlsx_var = tk.BooleanVar()
        self.json_var = tk.BooleanVar()
        self.streamlit_var = tk.BooleanVar()
        
        tk.Checkbutton(self, text="Exportar para XLSX", variable=self.xlsx_var).pack(anchor="w", padx=20, pady=5)
        tk.Checkbutton(self, text="Exportar para JSON", variable=self.json_var).pack(anchor="w", padx=20, pady=5)
        tk.Checkbutton(self, text="Invocar Streamlit", variable=self.streamlit_var).pack(anchor="w", padx=20, pady=5)
        
        export_button = tk.Button(self, text="Exportar", command=self.export)
        export_button.pack(pady=20)
        
    def export(self):
        if self.json_var.get():
            self.archives.expowrtToJSON()
        if self.xlsx_var.get():
            self.archives.exportToXLSX()
        if self.streamlit_var.get():
            self.archives.InvokeStreamlit()
        