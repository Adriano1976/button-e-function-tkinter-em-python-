from tkinter import *
class Janela(object):	
	def __init__(self,toplevel):		
	    self.frame = Frame(toplevel)
	    self.frame.pack()

	    self.botao1 = Button(self.frame)
	    self.botao1['text'] = 'Olá Mundo'
	    self.botao1['bg'] = 'green'
	    self.botao1['font'] = ('Verdana','12','italic','bold')
	    self.botao1['height'] = 4	    
	    self.botao1.pack(side=BOTTOM)

	    self.botao2 = Button(self.frame)
	    self.botao2['text'] = 'Boa Noite Pessoal'
	    self.botao2['bg'] = 'red'
	    self.botao2['font'] = ('Time','16')
	    self.botao2['fg'] = 'Yellow'
	    self.botao2['height'] = 4
	    self.botao2['width'] = 18
	    self.botao2.pack()

	    self.botao3 = Button(self.frame)
	    self.botao3['text'] = 'Validar Mensagem'	    
	    self.botao3['font'] = ('Verdana','12','italic','bold')
	    self.botao3['bg'] = 'DimGray'
	    self.botao3['fg'] = 'DarkSlateBlue'
	    self.botao3['height'] = 3
	    self.botao3.pack()
	    
root = Tk()
Janela(root)
root.mainloop()
		
