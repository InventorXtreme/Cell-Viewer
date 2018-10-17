import tkinter
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox


#cell definitions


def mitochondria():
    #p, a
    messagebox.showinfo("Mitochondrion", "The Mitochondrion is the powerhouse of the cell.")

def cell_wall():
    #p
    messagebox.showinfo("Cell Wall", "The cell wall is found on the border of plant cells and helps defend them and give them shape.")
def cell_mem():
    #p, a
    messagebox.showinfo("Cell Membrane", "A semipermeable barrier surrounding a cell.")
def cyto():
    #p, a
    messagebox.showinfo("Cytoplasm", "Gel in a cell, it holds organelles.")
def nucle():
    #p, A
    messagebox.showinfo("Nucleus", "Holds DNA, acts as brain of cell.")
def vacole():
    #p, a
    messagebox.showinfo("Vacule", "The vacule stores minerals and water.")
def nuceo():
    #p, a
    messagebox.showinfo("Nucleolus", "Makes ribosomes")
def nemem():
    #p, a
    messagebox.showinfo("Nuclear Membrane", "Keeps DNA in and other stuff out.")
def cloroplast():
    #p
    messagebox.showinfo("Cloroplast", "Preforms photosynthesis")
def ribosome():
    #p, a
    messagebox.showinfo("Ribosomes", "Makes proteins.")
def cen():
    #para p, a
    messagebox.showinfo("Centrioles", "Aid in cell division. Found in all animal cells and some plant cells.")
def ly():
    #a
    messagebox.showinfo("Lysosomes", "Holds enzymes used for digestion.")
def gol():
    #a, p
    messagebox.showinfo("Golgi Body", "Packages and processes molecules.")
def en():
    #p, a
    messagebox.showinfo("Endoplasmic Reticulum", "Conected to the nucleus.\nThe rough ER acts as a factory and packagin"
                                                 "g "
                                                 "plant for protiens it, unlike the smooth ER, has ribosomes on it.\nTh"
                                                 "e "
                                                 "smooth ER is important in the creation of lipids.")
root = tk.Tk()

root.title("Whirlwind Cell Viewer")

cellpic = PhotoImage(file="cellim.gif")


cellimg = Frame(root)
cellimg.pack()

menubar=Menu(root)
cellviewer = Menu(menubar, tearoff=0)
acell = Menu(cellviewer, tearoff=0)
pcell = Menu(cellviewer, tearoff=0)
about = Menu(menubar, tearoff=0)

acell.add_command(label="Mitochondria", command=mitochondria)
acell.add_command(label="Cell Membrane", command=cell_mem)
acell.add_command(label="Cytoplasm", command=cyto)
acell.add_command(label="Nucleus", command=nucle)
acell.add_command(label="Nucleolus", command=nuceo)
acell.add_command(label="Lysosomes", command=ly)
acell.add_command(label="Endoplasmic Reticulum", command=en)
acell.add_command(label="Golgi Body", command=gol)
acell.add_command(label="Centrioles", command=cen)
acell.add_command(label="Nuclear Membrane", command=nemem)
acell.add_command(label="Ribosome", command=ribosome)
acell.add_command(label="Vacuole", command=vacole)


pcell.add_command(label="Cytoplasm", command=cyto)
pcell.add_command(label="Mitochondria", command=mitochondria)
pcell.add_command(label="Cell Wall", command=cell_wall)
pcell.add_command(label="Cell Membrane", command=cell_mem)
pcell.add_command(label="Cloroplast", command=cloroplast)
pcell.add_command(label="Nucleus", command=nucle)
pcell.add_command(label="Nucleolus", command=nuceo)
pcell.add_command(label="Ribosome", command=ribosome)
pcell.add_command(label="Golgi Body", command=gol)
pcell.add_command(label="Vacuole", command=vacole)
pcell.add_command(label="Endoplasmic Reticulum", command=en)
pcell.add_command(label="Nuclear Membrane", command=nemem)
pcell.add_command(label="Centrioles", command=cen)


menubar.add_cascade(label="Cell Viewer", menu=cellviewer)
cellviewer.add_cascade(label="Animal Cell", menu=acell)
cellviewer.add_cascade(label="Plant Cell", menu=pcell)
t=ttk.Button(root,text="help")
#t.pack()

def ima():
    messagebox.showinfo("Image credits", "Icon: https://healthmatters.io/media/public/healthmatters/biomarker_category_images/cell.png\nMain Image: https://qph.fs.quoracdn.net/main-qimg-067bc9c9ce364aa1fd3f0f9308ac39a3")
def aboutc():
    messagebox.showinfo("About","Whirlwind Cell Viewer V 1.2.2\n\n \nAlex Moening\nWhirlwind")
menubar.add_cascade(label="About", menu=about)
about.add_command(label="About",command=aboutc)
about.add_command(label="Images", command=ima)

tst = Label(cellimg, image=cellpic)
tst.image = cellpic
tst.pack()
s=ttk.Style()
try:
    themeu = "vista"
    s.theme_use(themeu)
except:
    print("Whrilwind Recovery System\n"
          "We have fixed a ttk theme error"
          "Error: Theme "+ themeu +" not found")
    
root.resizable(0,0)
#root.overrideredirect(1) # will remove the top badge of window
root.config(menu=menubar)
root.iconbitmap(r'cellicon.ico')
root.mainloop()
