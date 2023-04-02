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

        header_widget = BoxLayout(orientation="horizontal")
        self.header_label = Label(text="Výpocet renty AČR")
        header_widget.add_widget(self.header_label)
        self.add_widget(header_widget)

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

        button_widget = BoxLayout(orientation="horizontal")
        self.count_button = Button(text="Spočítat")
        button_widget.add_widget(self.count_button)
        self.add_widget(button_widget)

        result_widget = BoxLayout(orientation="horizontal")
        self.result_label = Label(text="Vaše měsíční renta je: ")
        result_widget.add_widget(self.result_label)
        self.add_widget(result_widget)

        info_widget = BoxLayout(orientation="horizontal")
        self.info_label = Label(text="")
        info_widget.add_widget(self.info_label)
        self.add_widget(info_widget)

        footer_widget = BoxLayout(orientation="horizontal")
        self.footer_label = Label(text="Copyright © 2023 Karel Minarcik")
        footer_widget.add_widget(self.footer_label)
        self.add_widget(footer_widget)

    def get_month_salary(self, *args):
        rank = df["Hodnost"].values.tolist()
        rank = [el.replace('\xa0', '') for el in rank]
        for one_rank in rank:
            if one_rank == self.combobox.text:
                return df.iloc[(rank.index(one_rank)), 1]

    def get_percentages(self, *args):
        age = df_2["Roky"].values.tolist()
        for one_age in age:
            if one_age == self.combobox2.text:
                return df_2.iloc[(age.index(one_age)), 1]

    def bonus_amount(self, *args):
        bonus = self.bonus_input.text
        try:
            bonus = float(bonus.replace(",", ".")) * 0.01
            return bonus
        except ValueError:
            self.info_widget.text= "Zadejte prosím číslo. Desetinné místo oddělte tečkou."
            return 0


class RentaApp(App):
    def build(self):
        return RentaLayout()


RentaApp().run()
