class Rodent:
#self refers to Rodent
    def _init_(self, tag_id):
        self.tag_id=tag_id
        #refering to self above makes accessible to other functions
        self.weights=[]
        
    def plot(self):
        return self.tag_id[0]
        
    def add_weight(self, weight):
        self.weights.append(weight)
        

