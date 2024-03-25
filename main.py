import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class OurCustomKeyboard(tk.Frame):
    # Custom keyboard for input
    def __init__(self, master, entry):
        super().__init__(master)
        self.entry = entry
        self.create_keyboard()

    def create_keyboard(self):
        # Create buttons for the custom keyboard with improved styling
        buttons = [
            "1", "2", "3", "-", "4", "5", "6", "<-", "7", "8", "9", "Clear", "0", ".", "Enter"
        ]
        row_count = 0
        col_count = 0

        for button_text in buttons:
            # Create and place each button in a grid
            button = ttk.Button(self, text=button_text, width=6, style="TButton", command=lambda b=button_text: self.on_keyboard_button_click(b))
            button.grid(row=row_count, column=col_count, padx=10, pady=10, sticky="nsew")  # Increased padx and pady
            col_count += 1

            if col_count > 3:
                col_count = 0
                row_count += 1

    def on_keyboard_button_click(self, button_text):
        # Handle button clicks
        if button_text == "<-":
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text[:-1])
        elif button_text == "Clear":
            self.entry.delete(0, tk.END)
        elif button_text == "Enter":
            # Implement the action you want when the Enter button is pressed (currently, it's a placeholder)
            pass
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text + button_text)

class WebScraper(tk.Tk):
    # Main application window
    def __init__(self):
        super().__init__()
        self.title("Multiple Page App")
        self.geometry("400x500")
        self.resizable(False, False)  # Disable resizing
        self.pages = {}
        self.create_main_page()
        self.create_info_page()
        self.create_search_page()
        
    def create_main_page(self):
        # Create the main page with a blue background
        main_page = tk.Frame(self, bg="lightblue")
        main_page.pack_propagate(False)
        main_page.pack(fill=tk.BOTH, expand=True)
        
        label = tk.Label(main_page, text="Hello Hacker🧑‍💻", font=("Arial", 28), bg="lightblue")
        label.pack(pady=20)
        
        button_style = {
            "font": ("Arial", 18),  # Larger font size
            "relief": tk.RAISED,
            "bg": "lightgray",
        }
        #buttons on the main page: "Start", "Info" and "Quit" 
        start_button = ttk.Button(main_page, text="Start", command=self.show_search_page, style="TButton")
        start_button.pack(pady=20, padx=20, ipadx=20, ipady=15)
        
        info_button = ttk.Button(main_page, text="Info", command=self.show_info_page, style="TButton")
        info_button.pack(pady=20, padx=20, ipadx=20, ipady=15)
        
        quit_button = ttk.Button(main_page, text="Quit", command=self.confirm_quit, style="TButton")
        quit_button.pack(pady=20, padx=20, ipadx=20, ipady=15)
        
        self.pages["main"] = main_page
    
    def create_info_page(self):
        # Create the info page with a green background
        info_page = tk.Frame(self, bg="lightgreen")
        info_page.pack_propagate(False)
        
        label = tk.Label(info_page, text="Info Page", font=("Arial", 28), bg="lightgreen")
        label.pack(pady=20)
        
        info_text = "This tool is made for web scraping."
        info_label = tk.Label(info_page, text=info_text, font=("Arial", 18), bg="lightgreen")
        info_label.pack(pady=20)
        
        back_button = ttk.Button(info_page, text="Back", command=self.show_main_page, style="TButton")
        back_button.pack(pady=20, padx=20, ipadx=20, ipady=15)
        
        self.pages["info"] = info_page

    def create_search_page(self):
        # Create the search page with a yellow background
        search_page = tk.Frame(self, bg="lightyellow")
        search_page.pack_propagate(False)
        
        label = tk.Label(search_page, text="Search Page", font=("Arial", 28), bg="lightyellow")
        label.pack(pady=20)
        
        input_entry = tk.Entry(search_page, font=("Arial", 18), width=20)
        input_entry.pack(pady=10)

        keyboard_frame = OurCustomKeyboard(search_page, input_entry)
        keyboard_frame.pack(pady=10)
        
        back_button = ttk.Button(search_page, text="Back", command=self.show_main_page, style="TButton")
        back_button.pack(pady=20, padx=20, ipadx=20, ipady=15)
        
        self.pages["search"] = search_page

    def show_page(self, page_name):
        # Show the selected page and hide others
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack(fill=tk.BOTH, expand=True)
        
    def show_main_page(self):
        self.show_page("main")
        
    def show_info_page(self):
        self.show_page("info")
        
    def show_search_page(self):
        self.show_page("search")
        
    def confirm_quit(self):
        result = messagebox.askquestion("Confirm Quit", "Are you sure you want to quit?))))")
        if result == "yes":
            self.destroy()
    
if __name__ == "__main__":
    app = WebScraper()
    app.mainloop()
