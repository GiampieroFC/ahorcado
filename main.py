# -*- coding: utf-8 -*-

import tkinter as tk
from scrap import random_word, rae_word, definiciones
import window

palabra = random_word
your_letters = ""

turns = 2 + len(palabra)


def el_juego(random_word):
    global ventana, your_letters, turns

    ventana.escribir(f'\n{"="*35}\n\nPalabra de {len(palabra)} letras:\n\n')

    a = set(random_word)

    for i in random_word:

        if i in your_letters:
            print(i, end="")
            ventana.escribir(i)
        else:
            print("_", end="")
            ventana.escribir('_ ')

    print("\n OPORTUNIDADES: ", turns)
    ventana.escribir('\n\n(Tienes ' + str(turns) + ' oportunidad(es)')

    ventana.escribir("\n\n>>Ingresa una letra\n")

    print(your_letters)
    ventana.escribir('Ya has ingresado: '+your_letters+'\n')

    b = set(your_letters)
    if a.issubset(b):
        print(f"\n\tGANASTE!! La palabra era '{random_word}'")
        ventana.escribir(f"\nGANASTE!! La palabra era: '{random_word}'")
        ventana.escribir(f"\n\n {rae_word.upper()}:")
        for definicion in definiciones:
            ventana.escribir(f"\n\t {definicion}")
    elif turns == 0:
        print(f"\n\tJá, perditeeee!! La palabra era {random_word}")
        ventana.escribir(
            f"\nJa, perdisteeee!! La palabra era: '{random_word}'")
        ventana.escribir(f"\n\n {rae_word.upper()}:")
        ventana.frameDer.update_idletasks()
        for definicion in definiciones:
            ventana.escribir(f"\n\t {definicion}")

    if turns == 9:
        ventana.canva.create_text(150, 230, text='''
           
                                
                                  
                                  
                                 
                                  
                            
                                  
                                
                           
     
                           
                              
                                
                                
======================
======================''', fill="white", font=('Helvetica 15'))

    if turns == 8:
        ventana.canva.create_text(150, 230, text='''
           
     ||                      
     ||                       
     ||                        
     ||                          
     ||                              
     ||                          
     ||                           
     ||                           
     ||                               
     ||                           
     ||                           
     ||                         
     ||                           
     ||                           
======================
======================''', fill="white", font=('Helvetica 15'))

    if turns == 7:
        ventana.canva.create_text(150, 230, text='''
     /===============        
     ||////                          
     ||///                           
     ||//                            
     ||/                            
     ||                              
     ||                            
     ||                               
     ||                              
     ||                           
     ||                           
     ||                           
     ||                  
     ||                           
     ||                           
======================
======================''', fill="white", font=('Helvetica 15'))

    if turns == 6:
        ventana.canva.create_text(150, 230, text='''
     /===============        
     ||////                      |       
     ||///                       |        
     ||//                        |         
     ||/                         
     ||                              
     ||                         
     ||                                   
     ||                            
     ||                            
     ||                           
     ||                           
     ||                        
     ||                           
     ||                           
======================
======================''', fill="white", font=('Helvetica 15'))

    if turns == 5:
        ventana.canva.create_text(150, 230, text='''
     /===============        
     ||////                      | 
     ||///                       | 
     ||//                        | 
     ||/                       (O o) 
     ||                         -U 
     ||                   
     ||                                
     ||                             
     ||                             
     ||                           
     ||                           
     ||                       
     ||                           
     ||                           
======================
======================''', fill="white", font=('Helvetica 15'))

    if turns == 4:
        ventana.canva.create_text(150, 230, text='''
     /===============        
     ||////                      | 
     ||///                       | 
     ||//                        | 
     ||/                       (O o) 
     ||                         -U 
     ||                         // 
     ||                         \\ 
     ||                        
     ||                               
     ||                           
     ||                           
     ||                      
     ||                           
     ||                           
======================
======================''', fill="white", font=('Helvetica 15'))

    if turns == 3:
        ventana.canva.create_text(150, 230, text='''
     /===============        
     ||////                      | 
     ||///                       | 
     ||//                        | 
     ||/                       (O o) 
     ||                         -U 
     ||                     ----// 
     ||                         \\ 
     ||                               
     ||                             
     ||                           
     ||                           
     ||                  
     ||                           
     ||                           
======================
======================''', fill="white", font=('Helvetica 15'))

    if turns == 2:
        ventana.canva.create_text(150, 230, text='''
     /===============        
     ||////                      | 
     ||///                       | 
     ||//                        | 
     ||/                       (O o) 
     ||                         -U 
     ||                     ----//----  
     ||                         \\ 
     ||                            
     ||                         
     ||                           
     ||                           
     ||                        
     ||                           
     ||                           
======================
======================''', fill="white", font=('Helvetica 15'))

    if turns == 1:
        ventana.canva.create_text(150, 230, text='''
     /===============        
     ||////                      | 
     ||///                       | 
     ||//                        | 
     ||/                       (O o) 
     ||                         -U 
     ||                     ----//---- 
     ||                         \\ 
     ||                        / 
     ||                       / 
     ||                           
     ||                           
     ||                    
     ||                           
     ||                           
======================
======================''', fill="white", font=('Helvetica 15'))

    if turns <= 0:
        ventana.entrada.config(state=tk.DISABLED)
        ventana.canva.create_text(150, 230, text='''
     /===============        
     ||////                      | 
     ||///                       | 
     ||//                        | 
     ||/                       (O o) 
     ||                         -U 
     ||                     ----//---- 
     ||                         \\ 
     ||                        / \ 
     ||                       /  \ 
     ||                           
     ||                           
     ||   Perdiste         
     ||                           
     ||                           
======================
======================''', fill="white", font=('Helvetica 15'))


def insertar(event=None):
    global ventana, your_letters, palabra, turns
    if turns > 0:
        letter = ventana.entrada.get()

        if len(letter) > 1 or letter.isnumeric():
            print("\n¡¡¡INGRESA SOLO UNA LETRA!!!")
            ventana.escribir("\n\n¡¡¡INGRESA SOLO UNA LETRA!!!\n\n")

        if letter not in palabra:
            turns -= 1
        your_letters += letter[0]

        el_juego(palabra)
        ventana.entrada.delete(0, tk.END)
    else:
        ventana.escribir('\n\t\tYA PERDISTE')


ventana = window.Ventana(
    'El ahorcado', 'C:/Users/gferm/OneDrive/Escritorio/Programation/ahorcado/khangman_94222.ico')

ventana.ventana.bind('<Return>', insertar)

ventana.button.config(command=lambda: insertar())

el_juego(palabra)

ventana.mostrar()
