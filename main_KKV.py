from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


# Функция для запроса и выведения стоимости криптовалюты
def kripto_price():
    kripto_code = kripto_combobox.get().lower()
    val_code = val_combobox.get().lower()

    if val_code and kripto_code:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={kripto_code}&vs_currencies={val_code}')
            response.raise_for_status()
            dict_kv = response.json()
            if val_code in dict_kv[kripto_code]:
                price_k = dict_kv[kripto_code][val_code]
                kripto = kriptoval[kripto_code.upper()]
                val = valuti[val_code.upper()]
                finish_label.config(text=f"За 1 {kripto}: {price_k:.2f} {val}")
            else:
                mb.showerror("Ошибка", f"Валюта {val_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")


# Получаем полное название криптовалюты из словаря и обновляем метку
def new_k_label(event):
    code = kripto_combobox.get()
    name = kriptoval[code]
    k_label.config(text=name)
    finish_label.config(text="")


# Получаем полное название валюты из словаря и обновляем метку
def new_v_label(event):
    code = val_combobox.get()
    name = valuti[code]
    v_label.config(text=name)
    finish_label.config(text="")


# Словарь кодов криптовалют, символов (если есть) и их полных названий
kriptoval = {
    "BITCOIN": "₿ Биткоин",
    "ETHEREUM": "Ξ Эфириум",
    "TETHER": "₮ USDT",
    "BINANCECOIN": "BNB",
    "SOLANA": "SOL",
    "USD-COIN": "USDC",
    "RIPPLE": f"✕ XRP",
    "DOGECOIN": "Ɖ DOGE",
    "CARDANO": "₳ ADA",
    "TRON": "TRX",
    "AVALANCHE-2": "AVAX"
}

# Словарь кодов валют, символов (если есть) и их полных названий
valuti = {
    "USD": "$ Доллар США",
    "EUR": "€ Евро",
    "JPY": "¥ Японская йена",
    "GBP": "£ Британский фунт",
    "AUD": "AU$ Австралийский доллар",
    "CAD": "C$ Канадский доллар",
    "CHF": "SFr Швейцарский франк",
    "CNY": "¥ Китайский юань",
    "RUB": "₽ Российский рубль",
}

# Создание графического интерфейса
window = Tk()
window.title("Курс криптовалют")
window.geometry("300x300+400+250")

style = ttk.Style()
style.configure("TLabelframe", padding=10)
style.configure("TLabelframe.Label", foreground="DarkGreen", font=("Time New Roman", 14))

group_1 = ttk.LabelFrame(window, text="Криптовалюта:")
group_1.pack(fill="both", expand=True)

kripto_combobox = ttk.Combobox(group_1, values=list(kriptoval.keys()))
kripto_combobox.grid(row=0, column=0, columnspan=1, sticky="ew")
kripto_combobox.bind("<<ComboboxSelected>>", new_k_label)

k_label = ttk.Label(group_1)
k_label.grid(row=1, column=0, columnspan=1, sticky="ew")

group_2 = ttk.LabelFrame(window, text="Валюта:")
group_2.pack(fill="both", expand=True)

val_combobox = ttk.Combobox(group_2, values=list(valuti.keys()))
val_combobox.grid(row=0, column=0, columnspan=1, sticky="ew")
val_combobox.bind("<<ComboboxSelected>>", new_v_label)

v_label = ttk.Label(group_2)
v_label.grid(row=1, column=0, columnspan=1, sticky="ew")

group_3 = ttk.LabelFrame(window, text="Курс:")
group_3.pack(fill="both", expand=True)

finish_label = ttk.Label(group_3)
finish_label.grid(row=1, column=0, columnspan=1, sticky="ew")

Button(text="Получить курс", command=kripto_price).pack(padx=10, pady=10)

window.mainloop()
