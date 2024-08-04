import matplotlib.pyplot as plt 
import networkx as nx 
from PIL import Image

G = nx.Graph() 
G.add_node(1,pos=(7,100)) 
G.add_node(2,pos=(8,60)) 
G.add_node(3,pos=(9,35)) 
G.add_node(3,pos=(9,20)) 
G.add_node(4,pos=(2,-12)) 
G.add_node(5,pos=(7,-14)) 
G.add_node(6,pos=(14,-21)) 
G.add_node(7,pos=(18,-21))  
G.add_node(8,pos=(24,-20)) 
G.add_node(9,pos=(19,-41)) 
G.add_node(10,pos=(15,-41)) 
G.add_node(11,pos=(9,-38)) 
G.add_node(12,pos=(27,-40))  
G.add_node(13,pos=(3.75,-60)) 
G.add_node(14,pos=(8,-80))
G.add_node(15,pos=(12,-100))

G.add_edge(1,2,weight=49.6)
G.add_edge(2,3,weight=32.0) 
G.add_edge(3,4,weight=159)  
G.add_edge(3,5,weight=87.1) 
G.add_edge(3,7,weight=66)  
G.add_edge(4,5,weight=70.7)
G.add_edge(4,13,weight=15.7) 
G.add_edge(5,6,weight=30.5)  
G.add_edge(5,7,weight=28.6) 
G.add_edge(5,11,weight=14)   
G.add_edge(5,13,weight=62)
G.add_edge(6,7,weight=2.2)
G.add_edge(6,10,weight=2.3) 
G.add_edge(7,8,weight=56.1)  
G.add_edge(7,9,weight=0.88) 
G.add_edge(8,9,weight=44.7)  
G.add_edge(8,12,weight=18.5) 
G.add_edge(9,10,weight=0.850) 
G.add_edge(9,15,weight=98.4) 
G.add_edge(10,11,weight=32.3)  
G.add_edge(10,14,weight=24.2)
G.add_edge(11,13,weight=56.3) 
G.add_edge(11,14,weight=69.4) 
G.add_edge(12,9,weight=36.5) 
G.add_edge(12,15,weight=113)  
G.add_edge(13,14,weight=70.3) 
G.add_edge(14,15,weight=24.2 )  

pos = nx.get_node_attributes(G,'pos') 
labels = nx.get_edge_attributes(G,'weight') 

nx.draw_networkx_edge_labels(G,pos,edge_labels=labels) 
nx.draw(G,pos,with_labels=True,font_color='red',node_color='pink',node_size=350) 



again ='y' 
while again =='y':    

    print ('='*58) 
    print ('TRAVEL PROGRAM') 
    print ('='*58)  
    print("(1) Map Display")
    print("(2) Choose 2-5 Place for choose the best way for travel ")
    print("(3) Ticket office ") 
    print ('='*58)  
    cchoice = input('Choose your choice : ') 
    
    if cchoice == '1': 
        img = Image.open('Nakhon-si.jpg')
        img.show()
        
    if cchoice == '2': 
            stp = (input('How many places are you going to travel ? : '))            
            if stp =="2":                
                f1 = int(input('First spot :  '))
                f2 = int(input('Second spot :  '))                
                print('The shortest path is : ',
                nx.shortest_path(G, source=f1, target= f2, weight='weight' ))
                print('Sum of distance is : ',
                nx.shortest_path_length(G, source=f1, target=f2, weight='weight'),"KM")
                plt.show()
                
                
            if stp =="3":
                                                                     
                    s1 = int(input('First spot : '))
                    s2 = int(input('Second spot : '))
                    s3 = int(input('Third spot : '))

                    list=[s1,s2,s3]
                    nlist=sorted(list)

                    print('The shortest path is : ',
                    nx.shortest_path(G, source=nlist[0] , target=nlist[2], weight='weight'))            
                    print('Sum of distance is : ',
                    nx.shortest_path_length(G, source=nlist[0], target=nlist[2], weight='weight'),"KM")
                    plt.show()        
                
            if stp =="4":                                
                    x1 = int(input('First spot : '))
                    x2 = int(input('Second spot : '))
                    x3 = int(input('Third spot : '))
                    x3 = int(input('Fourth spot : '))

                    list=[x1,x2,x3]
                    nlist=sorted(list)

                    print('The shortest path is : ',
                    nx.shortest_path(G, source=nlist[0], target=nlist[2], weight='weight'))            
                    print('Sum of distance is : ',
                    nx.shortest_path_length(G, source=nlist[0], target=nlist[2], weight='weight'),"KM")
                    plt.show()
                
            if stp =="5":           
                    y1 = int(input('First spot : '))
                    y2 = int(input('Second spot : '))
                    y3 = int(input('Third spot : '))
                    y3 = int(input('Fourth spot : '))
                    y3 = int(input('Fifth spot : '))

                    list=[y1,y2,y3]
                    nlist=sorted(list)

                    print('The shortest path is : ',
                    nx.shortest_path(G, source=nlist[0], target=nlist[2], weight='weight'))            
                    print('Sum of distance is : ',
                    nx.shortest_path_length(G, source=nlist[0], target=nlist[2], weight='weight'),'KM')
                    plt.show()
    
    
    if cchoice =='3': 
        def nks():  
            display_menu() 

            age = int(input("Welcome to the nakhon si thammarat . What is your age ?   : "))
       
            children_ticket = 100

            adult_ticket = 150

            senior_ticket = 130

            if age <= 12: 
                        print ('='*58) 
                        print("The children's ticket costs : ", children_ticket,'baht')
                        print ('='*58) 
                        
            if age >= 65: 
                        print ('='*35) 
                        print("The senior ticket costs : ", senior_ticket,'baht')
                        print ('='*40)  

            if (age >= 13) and (age <= 64): 
                        print ('='*40) 
                        print("The adult ticket costs : ", adult_ticket,'baht')
                        print ('='*40)  

            ttps = input("Are you tourist ? so, We have a tourist cost if you are type 'yes':  ")
   

            toursitprice = 50

            if ttps.lower() == "yes": 

                if age >= 65: 
                    print ('='*40) 
                    print("The Senior ticket costs : ", senior_ticket + toursitprice,'baht') 
                    print ('='*35)  

                elif age > 12: 
                    print ('='*40) 
                    print("The Adult costs", adult_ticket + toursitprice,'baht') 
                    print ('='*40)  

                else: 
                    print ('='*40) 
                    print("The Children's ticket costs : ", children_ticket + toursitprice,'baht') 
                    print ('='*40)  

            else: 
                print ('-'*40) 
                print(" Then you will get the normal cost . . .  ")
                print ('-'*40)   

        def display_menu():
            inflie = open('Menu.txt','r')
            s = inflie.read()
            print(s)
            inflie.close()
        nks()
     
    print ('='*40) 
    again = str(input('Press Y to Try again Press N for exit : ')) 
    if  again != 'n':
        again ='y' 
    else: 
        pass
    
    print ('='*15) 
    print('Thank You <3') 
    print ('='*15)  
 
