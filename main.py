import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

#criar janela
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("600x750")

dic_conversoes_disponiveis = conversoes_disponiveis()

#criar elementos
titulo = customtkinter.CTkLabel(janela, text='Conversor de Moedas', font=("", 20))
texto_valor = customtkinter.CTkLabel(janela, text="Digite o valor a ser convertido")
campo_valor = customtkinter.CTkEntry(janela, placeholder_text="Ex: 10")
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destidno = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destidno)

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()),
                                                 command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])

def converter_moeda():
    try:
        valor = float(campo_valor.get())
        moeda_origem = campo_moeda_origem.get()
        moeda_destino = campo_moeda_destino.get()
        if moeda_origem and moeda_destino and valor > 0:
            cotacao = float(pegar_cotacao_moeda(moeda_origem, moeda_destino))  # Conversão para float
            valor_convertido = valor * cotacao
            texto_cotacao_moeda.configure(
                text=f"1 {moeda_origem} = {cotacao:.2f} {moeda_destino}\n"
                     f"{valor} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}"
            )
        else:
            texto_cotacao_moeda.configure(text="Por favor, preencha todos os campos corretamente.")
    except ValueError:
        texto_cotacao_moeda.configure(text="Digite um valor numérico válido.")
    except Exception as e:
        texto_cotacao_moeda.configure(text=f"Erro inesperado: {e}")


botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

moedas_disponiveis = nomes_moedas()
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()

#colocar elementos na tela
titulo.pack(padx=10, pady=10)
texto_valor.pack(padx=10, pady=10)
campo_valor.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)


#rodar janela

janela.mainloop()