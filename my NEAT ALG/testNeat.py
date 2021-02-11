import NeuralNetwork as NE



def initialize_population(n):
    Organizms = []
    inputs = [0,1,1,0,1,0,0,1]
    outputs = [1,2]
    for i in range(n):
        Organizms.append(NE.NeuralNetwork(i, inputs, outputs ))
    return Organizms


def evolution(n,m):
    Organizms = initialize_population(n)
    p_weight = 0.03
    p_add = 0.1
    p_connect = 0.2
    p_resurrect = 0.1
    for i in range(m):
        for el in Organizms:
            el.mutate(p_weight, p_add, p_connect, p_resurrect)
            
        
        if i % 1000 == 0:
            print()
            print()
            print("this is evolution number: ",i, "--------------------------")
            print()
        
            for el in Organizms:
                el.print_self()
                
                
                
evolution(100,3000)