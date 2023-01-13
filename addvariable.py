# Started 1.7.2022
# Finished ???

import customtkinter as ctk

from greekkeyboard import GreekKeyboard
from variable import Variable

font_string = "Roboto"
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


class AddVariableWizard(ctk.CTkToplevel):
    """Make sure to change this back to TopLevel"""

    def __init__(self):
        super().__init__()
        self.variable = Variable
        self.title("Add Variable")
        self.resizable(False, True)
        self.tab_view = ctk.CTkTabview(self,
                                       width=550,
                                       height=550,
                                       corner_radius=15,
                                       command=self.check_page
                                       )
        self.tab_view._segmented_button.configure(font=(font_string, 12))
        self.tab_view.pack(pady=25,
                           padx=25)

        tab_names = ['Symbol', 'Subscript', 'Notation', 'Constant', 'Value', 'Units', 'Overview']
        for i in tab_names:
            self.tab_view.add(i)

        self.tab_view.segmented_button._buttons_dict["Value"].configure(state="disabled")

        """Pages"""

        # Symbol Page
        symbol_page = self.tab_view.tab("Symbol")

        self._symbol_heading_frame = ctk.CTkFrame(symbol_page)

        self._symbol_label = ctk.CTkLabel(self._symbol_heading_frame,
                                          text="Enter the symbol of the variable",
                                          font=(font_string, 28))

        self._symbol_entry = ctk.CTkEntry(symbol_page,
                                          height=72,
                                          width=72,
                                          font=(font_string, 56))

        self._symbol_button = ctk.CTkButton(symbol_page,
                                            text='Submit',
                                            font=(font_string, 24),
                                            command=self.update_symbol)

        self._symbol_heading_frame.pack(padx=25,
                                        pady=25)
        self._symbol_label.pack(padx=20)

        self._symbol_entry.pack(pady=35)

        self._symbol_button.pack(side='bottom',
                                 fill='x',
                                 pady=10)

        # Subscript Page
        subscript_page = self.tab_view.tab("Subscript")

        self._subscript_heading_frame = ctk.CTkFrame(subscript_page)

        self._subscript_heading = ctk.CTkLabel(self._subscript_heading_frame,
                                          text="Enter the subscript of the variable",
                                          font=(font_string, 28))

        self._subscript_entry = ctk.CTkEntry(subscript_page,
                                          height=72,
                                          width=72,
                                          font=(font_string, 56))

        self._subscript_button = ctk.CTkButton(subscript_page,
                                            text='Submit',
                                            font=(font_string, 24),
                                            command=self.update_symbol)

        self._subscript_heading_frame.pack(padx=25,
                                        pady=25)
        self._subscript_heading.pack(padx=20)

        self._subscript_entry.pack(pady=35)

        self._subscript_button.pack(side='bottom',
                                 fill='x',
                                 pady=10)
        # Notation Page
        notation_page = self.tab_view.tab("Notation")

        # Constant Page
        constant_page = self.tab_view.tab("Constant")
        constant_heading = ctk.CTkLabel(constant_page,
                                        text="Is the variable a constant?",
                                        font=(font_string, 36))
        y_button = ctk.CTkButton(constant_page,
                                 width=145,
                                 height=50,
                                 text='Yes',
                                 font=(font_string, 22),
                                 command=self.y_button_func)
        n_button = ctk.CTkButton(constant_page,
                                 width=145,
                                 height=50,
                                 text='No',
                                 font=(font_string, 22),
                                 command=self.n_button_func)
        constant_heading.pack(pady=75)
        y_button.place(x=20, y=250)
        n_button.place(x=355, y=250)

        # Value Page
        value_page = self.tab_view.tab("Value")

        value_heading_frame = ctk.CTkFrame(value_page,
                                           corner_radius=10,
                                           width=550)

        value_heading = ctk.CTkLabel(value_heading_frame,
                                     text="Input the value of the constant below",
                                     font=(font_string, 28))
        value_subheading = ctk.CTkLabel(value_heading_frame,
                                        text="(Assume SI Units)",
                                        font=(font_string, 18))
        entry_frame = ctk.CTkFrame(value_page,
                                   fg_color='transparent'
                                   )
        coefficient_entry = ctk.CTkEntry(entry_frame,
                                         width=225,
                                         height=36,
                                         font=(font_string, 36))
        base = ctk.CTkLabel(entry_frame,
                            text="x 10",
                            font=(font_string, 36))

        power_entry = ctk.CTkEntry(entry_frame,
                                   width=35,
                                   height=35)

        back_button = ctk.CTkButton(value_page,
                                    text="Back")

        value_heading_frame.grid(row=0,
                                 column=0,
                                 sticky=['e', 'w'],
                                 pady=(60, 0))
        value_heading.pack(padx=25,
                           pady=(10, 5))
        value_subheading.pack(pady=(0, 5))

        entry_frame.grid(row=2,
                         column=0,
                         pady=(45, 165))
        coefficient_entry.grid(row=1,
                               column=0,
                               rowspan=3,
                               sticky='ew',
                               padx=(0, 15))
        base.grid(row=1,
                  column=1,
                  rowspan=3,
                  sticky='ew', )
        power_entry.grid(row=0,
                         column=2,
                         sticky='new',
                         pady=0)

        back_button.grid(row=3,
                         column=0,
                         pady=(0, 15),
                         sticky='sew',
                         columnspan=2)

        # Units Page
        units_page = self.tab_view.tab("Units")

        # Overview Page
        overview_page = self.tab_view.tab("Overview")

        self.greek_keyboard = GreekKeyboard(self, self.bind_entries(self.tab_view.tab(self.tab_view.get())))
        self.greek_keyboard.pack(pady=(0, 10),
                                 side='bottom')

    """Functions"""

    # Symbol
    def update_symbol(self):
        self.variable.symbol = self._symbol_entry.get().strip()
        self._symbol_button.configure(text='Update')
        self.tab_view.set("Subscript")

    # Subscript
    def update_subscript(self):
        self.variable.subscript = self._subscript_entry.get().strip()
        self._subscript_button.configure(text="Update")
        self.tab_view.set("Notation")
    # Notation

    # Constant
    def y_button_func(self):
        self.variable.constant = True
        self.tab_view._segmented_button._buttons_dict["Value"].configure(state="enabled")
        self.tab_view.set("Value")

    def n_button_func(self):
        self.variable.constant = False
        self.tab_view._segmented_button._buttons_dict["Value"].configure(state="disabled")
        self.tab_view.set("Units")

    # Value
    def create_value_page(self):
        pass

    def back_button_func(self):
        pass

    # Units

    # Custom Units

    # Overview

    # Misc

    def check_page(self):
        self.bind_entries(self.tab_view.tab(self.tab_view.get()))
        if self.tab_view.get() in ['Symbol', 'Subscript', 'Value']:
            self.greek_keyboard.pack(pady=(0, 10))
        else:
            if len(self.pack_slaves()) > 1:
                self.greek_keyboard.pack_forget()
            else:
                pass

    def bind_entries(self, container):
        tab_children = container.winfo_children()
        for child in tab_children:
            if isinstance(child, ctk.CTkEntry):
                child.bind('<FocusIn>',
                           command=lambda event, o=child: self.change_entry(o))
            if isinstance(child, ctk.CTkFrame):
                self.bind_entries(child)
            else:
                pass
        return tab_children

    def change_entry(self, entry):
        self.greek_keyboard.entry = entry


if __name__ == '__main__':
    AddVariableWizard().mainloop()
