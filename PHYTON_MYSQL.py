
# Importar la biblioteca tkinter
import tkinter as tk

# Importar módulos restantes de tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Clientes import *

from Conexion import *

class FormularioCliente:
    #VARIABLES GLOBALE
    #esta variable es globar su valor se incializa cuando recien esta inresa aqui
    # texBoxId = Entry(groupBox)
    global base
    base =None

    global texBoxId
    texBoxId =None

    global texBoxNombres
    texBoxNombres =None

    global texBoxApellidos
    texBoxApellidos =None

    global combo
    combo =None

    global groupBox
    groupBox =None

    global tree
    tree =None


   
def formulario():
        #aqui ponemos un nuevo valor a las varibles globales las cuales no solo basta con llmarlas si no decirle cuales voy a utlizar
        global texBoxId
        global texBoxNombres
        global texBoxApellidos
        global combo
        global base
        global groupBox
        global tree


        try:
            # Crear ventana principal
            base = Tk()
            base.geometry("900x300")  # Establecer tamaño de la ventana
            base.title("Formulario Python")

            groupBox = LabelFrame(base,text="Datos del personal", padx=8,pady=8) # 8 px de espacio horizontal, 8 px de espacio vertical
            groupBox. grid(row=0,column=0,padx=10,pady=10)
            # esta es la prte del texto se deol txtlabel
            
            LabelId=Label(groupBox,text="ID:",width=16,font=("arial",12)).grid(row=0,column=0)
            # esta es la  deol text label ccua<dro a rellenar
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=0, column=1)


            LabelNombres=Label(groupBox,text="Nombres:",width=16,font=("arial",12)).grid(row=1,column=0)
            texBoxNombres = Entry(groupBox)
            texBoxNombres.grid(row=1, column=1)

            LabelApellidos=Label(groupBox,text="Apellidos:",width=16,font=("arial",12)).grid(row=2,column=0)
            texBoxApellidos = Entry(groupBox)
            texBoxApellidos.grid(row=2, column=1)

            LabelSexo=Label(groupBox,text="Sexo:",width=16,font=("arial",12)).grid(row=3,column=0)
            seleccionsexo = tk.StringVar() # ESTE CORCETE ME PERMITE ALMACENAR CON DEFECTO N TEXTO YA QUE AHOR EST VCIO PERO O PDEO RELLENAR
            combo = ttk.Combobox(groupBox,values=["MASCULIN0", "FEMENINO" ] ,textvariable=seleccionsexo )
            combo.grid(row=3, column=1)
            # LE DECIMOS QUE POR DEFECTO ESTEON SEXO FEMNINO
            seleccionsexo.set("FEMENINO")

            Button(groupBox,text="Guardar",width=18,command=guardarRegistros).grid(row=4,column=0)
            Button(groupBox,text="Modificar",width=18, command=modificarRegistros).grid(row=4,column=1)
            Button(groupBox,text="Eliminar",width=18,command= eliminarRegistros).grid(row=4,column=2)

            #este espacio es para crear una nueva tabla tomar en cuenta

            groupBox = LabelFrame(base,text="Lista del Personal", padx=5,pady=5)
            groupBox.grid(row=0, column=1,padx=5,pady=5)

            #creamos un treeview
            #primero configuramos las columnas
            tree = ttk.Treeview(groupBox,columns=("id","Nombres","Apellidos","Sexo"), show=  'headings', height=5)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Id")

            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Nombres")

            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Apellidos")

            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Sexo")
            #Agregar los datos a la tabla
            #Mostrar la tabla

            for row in Clientes.mostrarClientes():
                 tree.insert("","end",values=row)

            #ejecutar la funcion de hacer click y mostrara el resultado
            tree.bind("<<TreeviewSelect>>",seleccionarRegistro)


            #el  tree.pack() sirve par imprmir los nombres que tomaran las columnas 
            tree.pack()

            # Iniciar el bucle principal
            base.mainloop()
        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))
def guardarRegistros():
        global texBoxNombres, texBoxApellidos,combo,groupBox
        try:
            #verificar si widgets(botones) estan inicializados
            if texBoxNombres is None or texBoxApellidos is None or combo is None:
                print("los widgets no estan inicializados")
                return
            nombres= texBoxNombres.get()
            apellidos= texBoxApellidos.get()
            sexo= combo.get()

            Clientes.ingresarClientes(nombres,apellidos,sexo)
            messagebox.showinfo("Información", "Los datos fueron guardadaos")

            #aqui llamamos y reutlizamos
            actualizarTreeView()

            #limpiamos los campos

            texBoxNombres.delete(0,END)
            texBoxApellidos.delete(0,END)

        except ValueError as error:
            print("Error al ingresar los datos{}".format(error))
        
def actualizarTreeView():
     global tree

     try:
          # borrar todos los elementos acltuales del treView
          tree.delete(*tree.get_children())
          #Obtener los nuevos datos que deseamos mostrar
          datos =Clientes.mostrarClientes() 
          #Insertar los nueo datos del treeView
          for row in Clientes.mostrarClientes():
            tree.insert("","end",values=row)
     except ValueError as error:
          print("Error al actualizar tabla{}".format(error))


def seleccionarRegistro(event):
    try:
        itemselecionado =tree.focus()

        if itemselecionado:
          #obtener el id del elementoselecionado
          values = tree.item(itemselecionado)['values']

          #establecer los valores en los widgets Entry
          texBoxId.delete(0,END)
          texBoxId.insert(0,values[0])

          texBoxNombres.delete(0,END)
          texBoxNombres.insert(0,values[1])

          texBoxApellidos.delete(0,END)
          texBoxApellidos.insert(0,values[2])

          combo.set(values[3])
          
    except ValueError as error:
        print("Error al selcionar egristro {}".format(error))

 
def modificarRegistros():
        global texBoxId,texBoxNombres, texBoxApellidos,combo,groupBox
        try:
            #verificar si widgets(botones) estan inicializados
            if texBoxNombres is None or texBoxApellidos is None or combo is None:
                print("los widgets no estan inicializados")
                return
            idUsuario = texBoxId.get()
            nombres= texBoxNombres.get()
            apellidos= texBoxApellidos.get()
            sexo= combo.get()

            Clientes.modificarClientes(idUsuario,nombres,apellidos,sexo)
            messagebox.showinfo("Información", "Los datos fueron ctualizados")

            #aqui llamamos y reutlizamos
            actualizarTreeView()

            #limpiamos los campos
            texBoxId.delete(0,END)

            texBoxNombres.delete(0,END)
            texBoxApellidos.delete(0,END)

        except ValueError as error:
            print("Error al modificar los datos{}".format(error))  

def eliminarRegistros():
        global texBoxId, texBoxNombres, texBoxApellidos
        try:
            #verificar si widgets(botones) estan inicializados
            if texBoxNombres is None or texBoxApellidos is None or combo is None:
                print("los widgets no estan inicializados")
                return
            idUsuario = texBoxId.get()
            

            Clientes.eliminarClientes(idUsuario)
            messagebox.showinfo("Información", "Los datos fueron eliminados")

            #aqui llamamos y reutlizamos
            actualizarTreeView()

            #limpiamos los campos
            texBoxId.delete(0,END)

            texBoxNombres.delete(0,END)
            texBoxApellidos.delete(0,END)

        except ValueError as error:
            print("Error al modificar los datos{}".format(error))  

                 
# Llamar al método estático para mostrar el formulario
formulario()
  