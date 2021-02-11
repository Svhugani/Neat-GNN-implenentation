import random

class NeuralNetwork:
    "this is neuralNetwork class - a part (organisms) in NEAT algorithm"
    
    list_Of_Innovations=[]
    node_Labels=['sensor','output','hidden']
    
    
    def __init__(self, id_Number, inputs, outputs ):
        
        self.inputs=inputs
        self.n_inputs = len(inputs)
        self.n_outputs = len(outputs)
        self.id_Number = id_Number
        self.node_Genes =NeuralNetwork.node_Labels[1:2]*self.n_outputs + NeuralNetwork.node_Labels[0:1]*self.n_inputs
        self.connect_Genes = []
        
        
    def randomizer():
        return 0.1*random.random()    
    
    
    def propagate(self):
        
    
    
    
    def print_self(self):
        
        print("this is neural net with ID: ", self.id_Number)
        print("nodes in net: ", len(self.node_Genes))
        print("connections in net: ", len(self.connect_Genes))
        print()
        
        
    
    def make_connection(self, in_Number, out_Number, weight):        

        if [in_Number, out_Number] not in NeuralNetwork.list_Of_Innovations:
            self.connect_Genes.append([in_Number,out_Number,weight,True, len(NeuralNetwork.list_Of_Innovations)])
            NeuralNetwork.list_Of_Innovations.append([in_Number, out_Number])            
        else:
            self.connect_Genes.append([in_Number,out_Number,weight,True, NeuralNetwork.list_Of_Innovations.index([in_Number, out_Number])])
        
    def add_node(self, name):
        self.node_Genes.append(name)
    
    def add_random_connections(self, num):
        
        for ind in range(num):
            i=random.randint(0,self.n_inputs)
            j=random.randint(self.n_inputs,self.n_inputs + self.n_outputs)
            self.make_connection(i,j,NeuralNetwork.randomizer())
                 
    
    def mutate(self,p_weight, p_add, p_connect, p_resurrect):
        
        "mutate: add node"
        
        if (random.random() < p_add and len(self.connect_Genes) > 0) :
            r = random.randint(0,len(self.connect_Genes)-1)
            if self.connect_Genes[r][3]==True:
                self.add_node(NeuralNetwork.node_Labels[2])
                self.connect_Genes[r][3]=False
                self.make_connection(self.connect_Genes[r][0],len(self.node_Genes)-1,1)
                self.make_connection(len(self.node_Genes)-1,self.connect_Genes[r][1],self.connect_Genes[r][2])
            else:
                if random.random() < p_resurrect:
                    self.connect_Genes[r][3]=True
                    
        "mutate: add connection, no loops between output and hidden!"
        
        if random.random()<p_connect:
            node_1=random.randint(self.n_outputs,len(self.node_Genes)-1)
            node_2=random.randint(0,len(self.node_Genes)-1)
            if not (self.node_Genes[node_1]==NeuralNetwork.node_Labels[0] and self.node_Genes[node_2]==NeuralNetwork.node_Labels[0]):
                self.make_connection(node_1, node_2, NeuralNetwork.randomizer())
                
        
        "mutate: modify weights"
        
        for i in range(len(self.connect_Genes)):
            r=random.random()
            if r < p_weight/2:
                self.connect_Genes[i][2] = 10*NeuralNetwork.randomizer()
            elif r < p_weight:
                self.connect_Genes[i][2] = min(1,2*random.random()*self.connect_Genes[i][2])
    
        