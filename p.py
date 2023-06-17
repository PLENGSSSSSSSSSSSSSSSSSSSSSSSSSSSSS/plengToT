import customtkinter
import customtkinter
app = customtkinter.CTk()
app.title('กริกริ๊วววววววววววววววว')
app.geometry('500x500')

# ข้อความแสดงผล
label = customtkinter.CTkLabel(app, text="Plengja", font=('Aria', 40))
label.pack(pady=(20, 0))

#ข้อความแสดงคำตอบ
answer_text = customtkinter.StringVar()
answer_label = customtkinter.CTkLabel(app, textvariable=answer_text, font=('Aria', 40))
answer_label.pack(pady=(20, 0))

# กล่องรับค่า Inputs
entry = customtkinter.CTkEntry(app, placeholder_text="ใส่ Input ของคุณตรงนี้")
entry.pack(pady=(15, 0))

#ปุ่มกด บลาๆ
def button_event():
    user_input = entry.get()
    answer = eval(user_input)
    answer_text.set(answer)
    print(user_input, answer)
 

 
button = customtkinter.CTkButton(app, text="กดฉันเลย", command = button_event)
button.pack(pady=(20, 0))

app.mainloop()
