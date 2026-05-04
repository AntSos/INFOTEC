# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Es una EDF FIFO.
class Queue:
    def __init__(self): # Constructor de la clase.
        self.lista = [] # Atributo de la clase, lista vacia.
        
    def enqueue(self, data):
        self.lista.append(data)

    def dequeue(self): # Regresar el primer elemento.
        return self.lista.pop(0)      
        
    def is_emty(self):
        bool_response = False
        
        if not self.lista:
            bool_response = True
        
        return bool_response
    
    def screen_print(self):
        string_out = ""
        
        for e in self.lista:
            string_out += str(e) + ", "
        
        print(string_out)
    
    # @Override
    def __str__(self): # or __rpr__
        #string_out = ""
        
        #for e in self.lista:
            #string_out += str(e) + ", "
        
        return str(self.lista)
        
        
if __name__ == "__main__":
    # Test the clas atributes and methods.
    cola = Queue()
    print(cola.is_emty())
    cola.enqueue(11)
    cola.enqueue(22)
    cola.enqueue(33)
    cola.enqueue(44)
    cola.enqueue(55)
    
    Queue.enqueue(cola, 99)

    #cola.screen_print()
    #print(cola.is_emty())

    #while not cola.is_emty():
        #print(cola.dequeue())
        #cola.screen_print()
        #print(cola.is_emty())
    print(cola)
    
    

    
    
    