# Begun: 12.20.2022
# Named Lipara on 1.7.2023
# Renamed Kozuchi on 1.12.2023
# Finished: Probably never?

# Main execution file for the program

import customtkinter as ctk
from addvariable import AddVariableWizard

font_string = "Roboto"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class MainWindow(ctk.CTk):

    def __init__(self):
        # Set up window
        super().__init__()
        self.title("Lipara")
        self.resizable(False, True)
        # Set up frame
        main_frame = ctk.CTkFrame(self,
                                  width=300,
                                  height=400,
                                  corner_radius=10)
        main_frame.pack(pady=25, padx=25)
        label = ctk.CTkLabel(main_frame, text="Welcome to Lipara!", font=(font_string, 18))
        label.pack(pady=10)
        # Separator Frames

        sessionframe = ctk.CTkFrame(main_frame, fg_color='transparent')
        eqnframe = ctk.CTkFrame(main_frame, fg_color='transparent')
        varframe = ctk.CTkFrame(main_frame, fg_color='transparent')

        # Add New Session/Import Session Button Here
        new_session = ctk.CTkButton(master=sessionframe,
                                    text="New Session",
                                    font=(font_string, 24),
                                    width=275,
                                    height=50,
                                    corner_radius=10,
                                    command=self.new_session_func)
        import_session = ctk.CTkButton(sessionframe,
                                       width=137,
                                       height=8,
                                       text="Import Session",
                                       font=(font_string, 13),
                                       corner_radius=5)

        add_variable = ctk.CTkButton(varframe,
                                     width=250,
                                     height=30,
                                     text="Add Variable",
                                     font=(font_string, 13),
                                     corner_radius=10,
                                     command=self.add_variable_func)

        edit_variable = ctk.CTkButton(varframe,
                                      width=100,
                                      height=15,
                                      text="Edit Variable",
                                      font=(font_string, 13),
                                      corner_radius=5)

        add_equation = ctk.CTkButton(eqnframe,
                                     width=250,
                                     height=30,
                                     text="Add Equation",
                                     font=(font_string, 13),
                                     corner_radius=10)

        edit_equation = ctk.CTkButton(eqnframe,
                                      width=100,
                                      height=15,
                                      text="Edit Equation",
                                      font=(font_string, 13),
                                      corner_radius=5)
        settings = ctk.CTkButton(main_frame,
                                 width=100,
                                 height=15,
                                 text="Settings",
                                 font=(font_string, 13),
                                 corner_radius=5)
        sessionframe.pack(padx=10, pady=5)
        varframe.pack(padx=10, pady=5)
        eqnframe.pack(padx=10, pady=5)

        new_session.pack(padx=10, pady=2)
        import_session.pack(padx=10, pady=10)
        add_variable.pack(padx=10, pady=2)
        edit_variable.pack(padx=10, pady=10)
        add_equation.pack(padx=10, pady=2)
        edit_equation.pack(padx=10, pady=10)
        settings.pack(padx=10, pady=15)

    def new_session_func(self):
        print(self.winfo_geometry()[7:])

    def import_session_fun(self):
        pass

    def add_variable_func(self):
        wizard = AddVariableWizard()


if __name__ == '__main__':
    MainWindow().mainloop()
