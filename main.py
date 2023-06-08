import tkinter

window = tkinter.Tk()
window.minsize(300,300)
window.title("BMI Calculator")

weight = 0
height = 0


label = tkinter.Label(text="Enter your Weight (kg)", font=("Arial",10,"bold"))
label.pack()

def clickButton():
    weight_input = weight_entry.get()
    height_input = height_entry.get()

    if not weight_input.isdigit() or not height_input.isdigit():
        result_label.config(text="Adam gibi bir şey gir!")
    else:
        result = int(weight_input) / (int(height_input) / 100) ** 2
        if result < 18.5:
            result_label.config(text="Zayıfsınız: {}".format(result))
        elif result >= 18.5 and result < 25:
            result_label.config(text="Kilonuz normal: {}".format(result))
        elif result >= 25 and result < 30:
            result_label.config(text="Falza kilolusunuz: {}".format(result))
        elif result >= 30:
            result_label.config(text="Obezitesiniz: {}".format(result))


weight_entry = tkinter.Entry()
weight_entry.pack()

label2 = tkinter.Label(text="Enter your Height (cm)", font=("Arial",10,"bold"))
label2.pack()

height_entry = tkinter.Entry()
height_entry.pack()

calculate_button = tkinter.Button(text="Calculate", command=clickButton)
calculate_button.pack()


result_label = tkinter.Label(text="result is: ")
result_label.pack()


window.mainloop()