import customtkinter

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)


    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip_window = tw = customtkinter.CTkToplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        
        frame = customtkinter.CTkFrame(tw, corner_radius=8, fg_color="#333333")
        frame.pack(padx=1, pady=1)

        label = customtkinter.CTkLabel(frame, text=self.text, justify='left', font=("Rebolo", 12))
        label.pack(padx=10, pady=5)


    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
        self.tooltip_window = None


    def update_text(self, new_text):
        self.text = new_text