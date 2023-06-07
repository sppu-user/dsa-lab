class record
    def_init_(self):
        self.name = none
        self.number = none
        
    def get_name(self):
    return self.name
    
    def get_number(self):
    return self.number
    
    def set_name(self,name):
    self.name = name
    
    def set_number(self,number):
    self.number = number
    
    def str(self):
    record = "Name: "+str(self.get_name())+"\t"+"\tNumber: "+str(self.get_number())
    return record