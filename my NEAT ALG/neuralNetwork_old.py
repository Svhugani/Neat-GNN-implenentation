import random

class NeuralNetwork:
    "this is neuralNetwork class - a part (organisms) in NEAT algorithm"
    
    list_Of_Innovations=[]
    node_Labels=['sensor','output','hidden']
    
    
    def __init__(self, id_Number, inputs, outputs ):
        
        self.n_inputs=len(inputs)
        self.n_outputs=len(outputs)
        self.id_Number=id_Number
        
        node_Ids=list(range(self.n_inputs+self.n_outputs))
        node_States=NeuralNetwork.node_Labels[0:1]*self.n_inputs + NeuralNetwork.node_Labels[1:2]*self.n_outputs
        
        self.node_Genes=dict(zip(node_Ids, node_States))
        self.connect_Genes=[]
    
    def make_connection(self, in_Number, out_Number, weight):        

        if [in_Number, out_Number] not in NeuralNetwork.list_Of_Innovations:
            NeuralNetwork.list_Of_Innovations.append([in_Number, out_Number])
            self.connect_Genes.append([in_Number,out_Number,weight,True, len(NeuralNetwork.list_Of_Innovations)-1])
        else:
            self.connect_Genes.append([in_Number,out_Number,weight,True, NeuralNetwork.list_Of_Innovations.index([in_Number, out_Number])])
        
    def add_node(self, name):
    
    def add_random_connections(self, num):
        
        for ind in range(num):
            i=random.randint(0,self.n_inputs)
            j=random.randint(self.n_inputs,self.n_inputs + self.n_outputs)
            self.make_connection(i,j,random.random())
                 
    
    def mutate(self,p_weight, p_add, p_connect, list_Of_Innovations):
        #mutate: add node
        if random.random()<p_add:
            r = random.randint(0,len(self.connect_Genes)-1)
            if self.connect_Genes[r][3]==True:
                self.node_Genes[len(self.node_Genes)]='hidden'
                self.connect_Genes[r][3]=False
                self.make_connection(self.connect_Genes[r][0],len(self.node_Genes),1, True, innov_Number+1)
                self.make_connection(len(self.node_Genes),self.connect_Genes[r][1],self.connect_Genes[r][2], True ,innov_Number+2)
            else:
                if random.random() > 0.75:
                    self.connect_Genes[r][3]=True
                    
        #mutate add connection
        if random.random()<p_connect:
                node_1=random.randint(0,len(self.node_Genes))
        
        
        #mutate weights
        for i in range(len(self.connect_Genes)):
            r=random.random()
            if r < p_weight/2:
                self.connect_Genes[i][2] = r
            elif r < p_weight:
                self.connect_Genes[i][2] = min(1,2*random.random()*self.connect_Genes[i][2])
    
        