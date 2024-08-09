import customtkinter


class DynamicalWindowApproach:
    def __init__(self, master):
        self.master = master

    def giveOptions(self, options_dict):
        
        self.top = customtkinter.CTkToplevel(self.master)
        self.top.grab_set()  
                
        self.top.title("Escolha uma opção")

        
        for i, obj_dict in enumerate(options_dict.items()):
            button_text, function = obj_dict
            
            button = customtkinter.CTkButton(self.top, text=button_text, command=function)
            button.grid(row=0, column=i, padx=(15,15), pady=(15,15))

        
        self.top.geometry("+%d+%d" % (self.master.winfo_screenwidth() // 2 - 100, self.master.winfo_screenheight() // 2 - 50))
