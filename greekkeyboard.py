# Created 1.8.22
# Finished . .

import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")

greek_alphabet = [('α', 'A'),
                  ('β', 'B'),
                  ('γ', 'Γ'),
                  ('δ', 'Δ'),
                  ('ϵ', 'E'),
                  ('ζ', 'Z'),
                  ('η', 'H'),
                  ('θ', 'Θ'),
                  ('ι', 'I'),
                  ('κ', 'K'),
                  ('λ', 'Λ'),
                  ('μ', 'M'),
                  ('ν', 'N'),
                  ('ξ', 'Ξ'),
                  ('o', 'O'),
                  ('π', 'Π'),
                  ('ρ', 'P'),
                  ('σ', 'Σ'),
                  ('τ', 'T'),
                  ('υ', 'ϒ'),
                  ('ϕ', 'Φ'),
                  ('χ', 'X'),
                  ('ψ', 'Ψ'),
                  ('ω', 'Ω')]


def buttonfunc(y):
    print(f"{y.cget('text')}")


class GreekKeyboard(ctk.CTkFrame):

    def __init__(self, root, entry=None):
        super().__init__(root)
        super().configure(corner_radius=10,
                          width=600)
        self.entry = entry
        self.root = root
        self.control_button = ctk.CTkButton(self,
                                            width=550,
                                            height=30,
                                            command=self.keyboard_control_func,
                                            text="▼  G R E E K  K E Y B O A R D  ▼",
                                            font=("Roboto", 20),
                                            corner_radius=5)
        self.control_button.grid(row=5,
                                 column=0,
                                 columnspan=6,
                                 pady=(5, 5),
                                 padx=5)
        self.configure()

    def keyboard_control_func(self):
        if self.control_button.cget('text') == "▼  G R E E K  K E Y B O A R D  ▼":
            self.control_button.configure(text="▲  G R E E K  K E Y B O A R D  ▲",
                                          width=500)
            for r in range(4):
                for c in range(6):
                    x = ctk.CTkButton(self, text="Blank")
                    x.grid(row=r,
                           column=c,
                           padx=5,
                           pady=4,
                           sticky='nsew')

            caps_button = ctk.CTkButton(self,
                                        text="A/a",
                                        width=40,
                                        height=30,
                                        command=self.case_change)
            caps_button.grid(row=3,
                             column=6,
                             padx=5)

            for n, i in enumerate(self.grid_slaves()[1:-1]):
                i.configure(text=f'{greek_alphabet[-n - 1][0]}',
                            width=75,
                            height=30,
                            font=('Roboto', 14),
                            command=lambda s=i: self.keyboard_button_func(s))
        elif self.control_button.cget('text') == "▲  G R E E K  K E Y B O A R D  ▲":
            self.control_button.configure(text="▼  G R E E K  K E Y B O A R D  ▼",
                                          width=560)
            for b in self.winfo_children()[1:]:
                b.destroy()

    def case_change(self):
        if self.grid_slaves()[1].cget('text').islower():
            for n, b in enumerate(self.grid_slaves()[1:-1]):
                b.configure(text=f'{greek_alphabet[-n - 1][1]}')
        elif self.grid_slaves()[1].cget('text').isupper():
            for n, b in enumerate(self.grid_slaves()[1:-1]):
                b.configure(text=f'{greek_alphabet[-n - 1][0]}')

    def keyboard_button_func(self, btn, entry):
        entry.insert('end', btn.cget('text'))


if __name__ == '__main__':
    wibbly = ctk.CTk()
    test = GreekKeyboard(wibbly)

    test.pack()
    wibbly.mainloop()
