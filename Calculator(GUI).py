import tkinter as tk

window = tk.Tk()

lbl_risult = tk.Label(
    window,
    text='0',
    width=30,
    height=4,
    bg='pink',
    font='Helvetica 18 bold',
    )
lbl_risult.grid(row=0,column=0,columnspan=4)


def is_number_decimal(current): #mesal-> 123+45.6
    for char in current[::-1]:  # nokte-> current[::-1]
        if char == '.':
            return True
        if char in ['*','/','+','-','%']:
            return False
        
    return False


def insert_risult_in_label(btn_text):
    
    current = lbl_risult['text']

    if current == '0' and btn_text == 'F°':
        pass
    elif btn_text == 'F°':
        lbl_risult['text'] = str(float(current) * 1.8 + 32)
    elif current in ['','0'] and btn_text in ['*','/','+','%']:
        pass
    elif current == '0' and btn_text == '.':
        lbl_risult['text'] = current + btn_text
    elif btn_text == '=' and current[-1] in ['*','/','+','-','%','0']:
        pass
    elif btn_text == '=':
        lbl_risult['text'] = str(eval(current))
    elif btn_text == 'cc' and current == '0':
        lbl_risult['text'] = '0'
    elif btn_text == 'cc' and current == '':
        lbl_risult['text'] = '0'
    elif btn_text == 'cc' and current != 0:
        lbl_risult['text'] = current[:-1]
    elif btn_text == 'C' and current == '0':
        lbl_risult['text'] = '0'
    elif btn_text == 'C':
        lbl_risult['text'] = '0'
    elif current == '0':
        lbl_risult['text'] = btn_text
    elif btn_text in ['*','/','+','-','%'] and current[-1] in ['*','/','+','-','%']:
        lbl_risult['text'] = current[:-1] + btn_text
    elif btn_text == '.':
        if is_number_decimal(current):
            pass
        else:
            lbl_risult['text'] += btn_text
    else:
        lbl_risult['text'] = (current + btn_text)


button_infos = [ # item haye button_infos bayad dakhele yek list[] bashad ta betavan rooye aan harekat kard.
    {'text':'cc' , 'command':lambda:insert_risult_in_label('cc')},
    {'text':'F°' , 'command':lambda:insert_risult_in_label('F°')},
    {'text':'%' , 'command':lambda:insert_risult_in_label('%')},
    {'text':'/' , 'command':lambda:insert_risult_in_label('/')},
    {'text':'7' , 'command':lambda:insert_risult_in_label('7')},
    {'text':'8' , 'command':lambda:insert_risult_in_label('8')},
    {'text':'9' , 'command':lambda:insert_risult_in_label('9')},
    {'text':'+' , 'command':lambda:insert_risult_in_label('+')},
    {'text':'4' , 'command':lambda:insert_risult_in_label('4')},
    {'text':'5' , 'command':lambda:insert_risult_in_label('5')},
    {'text':'6' , 'command':lambda:insert_risult_in_label('6')},
    {'text':'-' , 'command':lambda:insert_risult_in_label('-')},
    {'text':'1' , 'command':lambda:insert_risult_in_label('1')},
    {'text':'2' , 'command':lambda:insert_risult_in_label('2')},
    {'text':'3' , 'command':lambda:insert_risult_in_label('3')},
    {'text':'*' , 'command':lambda:insert_risult_in_label('*')},
    {'text':'C' , 'command':lambda:insert_risult_in_label('C')},
    {'text':'0' , 'command':lambda:insert_risult_in_label('0')},
    {'text':'.' , 'command':lambda:insert_risult_in_label('.')},
    {'text':'=' , 'command':lambda:insert_risult_in_label('=')},
] 

button_data = []

for button_info in button_infos:
    btn = tk.Button(window,text=button_info['text'],command=button_info['command'],height=2,font='Helvetica 18 bold',bg='silver')
    button_data.append(btn)


for i , data in enumerate(button_data):
    data.grid(row= (i // 4)+1 , column= i % 4 , sticky='nsew')


window.title('< CALCULATOR >')

window.mainloop()