from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.app import App
from kivy.uix.textinput import TextInput
import pandas as pd

df = pd.read_excel("salary.xlsx")
df_2 = pd.read_excel("Rokyvsprocenta.xlsx")


class RentaLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(RentaLayout, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.header_label = Label(text="Výpocet renty AČR")
        self.add_widget(self.header_label)

        rank_widget = BoxLayout(orientation="horizontal")
        self.rank_label = Label(text="Vaše hodnost")
        self.combobox = Spinner(text="Vojín", values=("Vojín", "Svobodník", "Destátník", "Četař", "Rotný", "Rotmistr", "Nadrotmistr", "Praporčík", "Nadpraporčík", "Štábní praporčík", "Poručík", "Nadporučík", "Kapitán", "Major", "Podplukovník", "Plukovník", "Brigádní generál", "Generálmajor", "Generálporučík", "Armádní generál"))
        rank_widget.add_widget(self.rank_label)
        rank_widget.add_widget(self.combobox)
        self.add_widget(rank_widget)

        service_widget = BoxLayout(orientation="horizontal")
        self.service_label = Label(text="Delka služby")
        self.combobox2 = Spinner(text="15", values=("16", "17", "18", "19", "20"))
        service_widget.add_widget(self.service_label)
        service_widget.add_widget(self.combobox2)
        self.add_widget(service_widget)

        bonus_widget = BoxLayout(orientation="horizontal")
        self.bonus_label = Label(text="Vykonnostní příplatek")
        self.bonus_input = TextInput(text="0")
        bonus_widget.add_widget(self.bonus_label)
        bonus_widget.add_widget(self.bonus_input)
        self.add_widget(bonus_widget)

        self.count_button = Button(text="Spočítat", on_press=self.count)
        self.add_widget(self.count_button)

        self.result_label = Label(text="Vaše měsíční renta je: ")
        self.add_widget(self.result_label)

        self.info_label = Label(text="")
        self.add_widget(self.info_label)

        self.footer_label = Label(text="Copyright © 2023 Karel Minarcik")
        self.add_widget(self.footer_label)

    def count(self, *args):
        self.rank = df["Hodnost"].values.tolist()
        self.rank = [el.replace('\xa0', '') for el in self.rank]
        for one_rank in self.rank:
            if one_rank == self.combobox.text:
                salary = df.iloc[(self.rank.index(one_rank)), 1]
                print(salary)
        self.age = df_2["Roky"].values.tolist()
        for one_age in self.age:
            if one_age == int(self.combobox2.text):
                percentage = df_2.iloc[(self.age.index(one_age)), 1]
                print(percentage)
        self.bonus = self.bonus_input.text
        try:
            self.bonus = float(self.bonus.replace(",", ".")) * 0.01
            print(self.bonus)
        except ValueError:
            self.info_label.text = "Zadejte prosím číslo. Desetinné místo oddělte tečkou. Ve vysledku nejsou zahrnuta procenta výkonnostního příplatku."
            self.bonus = 0
        self.result_label.text = f"Vaše měsíční renta je {(round((salary + (salary * self.bonus)) * percentage))} Kč."


class RentaApp(App):
    def build(self):
        return RentaLayout()


RentaApp().run()
