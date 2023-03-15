import PySimpleGUI as sg


layout = [
    [sg.Text('Hello World')], [sg.Button('Ok')]
    ]

window = sg.Window('Caca', layout)





while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Button':
        window['Text'].update('Caca')


window.close()        