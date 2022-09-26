"""
Nombre de los integrantes 

SMIS083121 - Luna Acosta, Kevin Aleander 
SMIS912820 - Zuniga Villatoro, Saul Emmanuel 
SMIS030921 - Cruz Ventura, Ulises Arquimides 
"""
# Importamos la libreria tkinder 
from calendar import Calendar
from email import message
from tkinter import Place, Tk, Button, messagebox, Label, Entry
from tkinter.ttk import Combobox
# Funcion para los mensajes 
def Opciones():
    messagebox.showinfo(title="Opciones", message="Si paga con tarjeta se le hara un descuento del 20%")
    messagebox.showinfo(title="Opciones", message="Si paga con efectivo se le hara un descuento del 10%")
    messagebox.showinfo(title="Opciones", message="Si paga con efectivo y el valor de la compra es menor a $20 no se le hara descuento")
    
# Creamo nuestra interfaz 
Interfaz = Tk ()
Interfaz.title("CAJERO PRINCIPAL") # Añadimos titulo
Interfaz.geometry("300x200") # Añadimos expansion 
Interfaz.config(bg= "skyblue") # Para cambiar el color de la ventana

# Label Precio, Cantidad y Opciones de pago
Precio = Label(Interfaz, text="Precio: $ ", bg= "skyblue")
Precio.place(x=30,y=20,width=100,height=30)

Cantidad = Label(Interfaz, text="Cantidad:  ", bg= "skyblue")
Cantidad.place(x=30,y=60,width=100,height=30)

OpcionesPago = Label(Interfaz, text="Opciones de pago :  ", bg= "skyblue")
OpcionesPago.place(x=30, y= 90, width=120,height=30)

# Caja de texto para Precio y Cantidad 

Precio = Entry(Interfaz)
Precio.place(x=140,y=20,width=100,height=25)

Cantidad = Entry(Interfaz)
Cantidad.place(x=140,y=60,width=100,height=25)


# Boton para opciones  
opc = Button(Interfaz, text="Opciones", bg= "spring green", command=Opciones)
opc.place(x=140, y= 130, width=100,height=30)



# Combobox para tipo de pago , Efectivo , Credito , Debito 
Opciones_Pago = Combobox(Interfaz, state="readonly")
Opciones_Pago ['values']=("Efectivo","Con Tarjeta")
Opciones_Pago.place(x=140, y= 90, width=100,height=30)


# Funcion para la compra 

def Comprar():
    if (Precio.get() != "" and Cantidad.get() != ""  and Opciones_Pago.get() != "" ):
        precio = float(Precio.get())
        cantidad = int(Cantidad.get())
        opciones_pago = Opciones_Pago.get()
        if (opciones_pago == "Con Tarjeta"):
            total = precio * cantidad
            descuento = total * 0.20
            total_pagar = total - descuento
            messagebox.showinfo("Cajero", f"El Precio es de $ {precio} Cantidad: {cantidad} Total {total} Forma de pago {opciones_pago} Descuendo : $ {round(descuento,2)} Total A pagar: $ {round(total_pagar,2)}")  
        
        elif (opciones_pago == "Efectivo"): 

            
            if(cantidad >= 20): 
              total = precio * cantidad
              descuento = total * 0.10
              total_pagar = total - descuento
              messagebox.showinfo("Cajero", f"El Precio es de $ {precio} Cantidad: {cantidad} Total {total} Forma de pago {opciones_pago} Descuendo : $ {round(descuento,2)} Total A pagar: $ {round(total_pagar,2)}") 

            else: 
                (cantidad <20 )
                total = precio * cantidad
                total_pagar = total 
                messagebox.showinfo("Cajero", f"El Precio es de $ {precio} Cantidad: {cantidad} Total {total} Forma de pago {opciones_pago} Total A pagar: $ {round(total_pagar,2)}") 

    else:
        messagebox.showerror("Cajero", "Debe de ingresar valores ")

# boton para pargar 
Cancelar = Button(Interfaz, text="Pagar", bg= "cyan", command=Comprar)
Cancelar.place(x=30, y= 130, width=100,height=30)



Interfaz.mainloop() 

