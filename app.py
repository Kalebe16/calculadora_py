import PySimpleGUI as sg

tema = "Reddit"
fonte = "Helvitica 36 italic"
sb_num = (4, 1) # size dos botoes numericos
cor_botao = "Grey"



def criar_janela():
    sg.theme(tema)

    menu_def = [
        ["Opções", ["Ajuda", "Sobre", "Sair"]],
        
    ]

    layout = [
        [sg.Menu(menu_def, font="Helvitica 14 italic")],
        [sg.Input("", disabled=True, size=(19, 1), key="-INPUT-")],
        [sg.Button("c", size=sb_num, button_color=cor_botao), sg.Button("<", size=sb_num, button_color=cor_botao), sg.Button("/", size=sb_num, button_color=cor_botao), sg.Button("%", size=sb_num, button_color=cor_botao)],
        [sg.Button("7", size=sb_num), sg.Button("8", size=sb_num), sg.Button("9", size=sb_num), sg.Button("*", size=sb_num, button_color=cor_botao)],
        [sg.Button("4", size=sb_num), sg.Button("5", size=sb_num), sg.Button("6", size=sb_num), sg.Button("-", size=sb_num, button_color=cor_botao)],
        [sg.Button("1", size=sb_num), sg.Button("2", size=sb_num), sg.Button("3", size=sb_num), sg.Button("+", size=sb_num, button_color=cor_botao)],
        [sg.Button("**", size=sb_num, button_color=cor_botao), sg.Button("0", size=sb_num), sg.Button(".", size=sb_num, button_color=cor_botao), sg.Button("=", size=sb_num, button_color=cor_botao)]
    ]

    return sg.Window("CALCULADORA", layout=layout, finalize=True, font=fonte, text_justification=True, element_justification='center',  return_keyboard_events=True, icon="img\icone_calcs.ico")


def atualizar_input():
    
    if event == "<" or event == "BackSpace:8":
        # removendo o ultimo caractere da string:
        minha_string = values["-INPUT-"]
        string_final= minha_string[:-1]
        janela["-INPUT-"].update(string_final)
    elif event == "7":
        values["-INPUT-"] = str(values["-INPUT-"]) + "7"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "8":
        values["-INPUT-"] = str(values["-INPUT-"]) + "8"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "9":
        values["-INPUT-"] = str(values["-INPUT-"]) + "9"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "c" or event == "Delete:46":
        janela["-INPUT-"].update("")
    elif event == "4":
        values["-INPUT-"] = str(values["-INPUT-"]) + "4"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "5":
        values["-INPUT-"] = str(values["-INPUT-"]) + "5"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "6":
        values["-INPUT-"] = str(values["-INPUT-"]) + "6"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "/":
        if values["-INPUT-"] == "":
            pass
        else:
            values["-INPUT-"] = str(values["-INPUT-"]) + "/"
            janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "1":
        values["-INPUT-"] = str(values["-INPUT-"]) + "1"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "2":
        values["-INPUT-"] = str(values["-INPUT-"]) + "2"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "3":
        values["-INPUT-"] = str(values["-INPUT-"]) + "3"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "*":
        values["-INPUT-"] = str(values["-INPUT-"]) + "*"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "0":
        values["-INPUT-"] = str(values["-INPUT-"]) + "0"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "+":
        values["-INPUT-"] = str(values["-INPUT-"]) + "+"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "-":
        values["-INPUT-"] = str(values["-INPUT-"]) + "-"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "%":
        values["-INPUT-"] = str(values["-INPUT-"]) + "%"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "**" or event == "x":
        values["-INPUT-"] = str(values["-INPUT-"]) + "**"
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "." or event == ",":
        values["-INPUT-"] = str(values["-INPUT-"]) + "."
        janela["-INPUT-"].update(values["-INPUT-"])
    elif event == "=" or event == "p" or event == "P":
        expressao_matematica = values["-INPUT-"]
        resultado = eval(expressao_matematica)
        janela["-INPUT-"].update(resultado)


def atualizar_menu():

    if event == "Ajuda":
        sg.popup("ATALHOS", "Sair    =    'Esc'\nEnter  =    'P'\n   **     =    'x'\n   c      =    'del'\n   <      =    'Backspace'", font="Helvitica 27 bold italic", icon="img\icone_ajuda.ico")
    elif event == "Sobre":
        sg.popup("CRÉDITOS", "Desenvolvido por Kalebe Chimanski de Almeida.", font="Helvitica 16 bold italic", icon="img\icone_sobre.ico")
    


janela = criar_janela()

flag = True

while flag:
    window, event, values = sg.read_all_windows(timeout=1)

    atualizar_menu()
    
    try:
        atualizar_input()
    except ZeroDivisionError:
        sg.popup('ERRO', 'NÃO É POSSIVEL DIVIDIR POR ZERO.', font="Helvitica 18 italic", icon="img\icone_erro.ico")
        janela["-INPUT-"].update("")
    except SyntaxError:
        sg.popup("ERRO", "ESSA EXPRESSÃO MATEMÁTICA NÃO EXISTE.", font="Helvitica 18 italic", icon="img\icone_erro.ico")
        janela["-INPUT-"].update("")


    if window == janela and event == sg.WIN_CLOSED or event == "Escape:27" or event == "Sair":
        flag = False
    





             