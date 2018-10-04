'''
Created on 02-Oct-2018

@author: shubham
'''
class quickfind(object):
    
    def __init__(self,filepath):
        self.file=open(filepath,"r+")
        array_length=int(self.file.readline().strip("\n"))
        self.data=[i for i in range(array_length)]
        self.initialise()
        print self.data
        
    def initialise(self):
        for i in self.file:
            a=int(i.strip("\n").split(" ")[0])
            b=int(i.strip("\n").split(" ")[1])
            self.union(a,b) 
            
    def union(self,a,b):
        a1=self.data[a]
        b1=self.data[b]
        if self.connected(a,b):
            pass
        else:
            for i in range(len(self.data)):
                if self.data[i]==b1:
                    self.data[i]=a1
                    
                else:
                    continue
                
    def connected(self,a,b):
        if self.data[a]==self.data[b]:
            return True
        else:
            return False
        
if __name__=="__main__":
    filepath="/home/shubham/Desktop/data.txt"
    t1=quickfind(filepath)
    
            
