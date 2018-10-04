'''
Created on 02-Oct-2018

@author: shubham
'''
class weighted_quick_union(object):
    def __init__(self,filepath):
        self.file=open(filepath,"r+")
        array_length=int(self.file.readline().strip("\n"))
        self.data=[i for i in range(array_length)]
        self.size=[1 for i in range(array_length)]
        self.initialise()
        print self.data
        
    def initialise(self):
        for i in self.file:
            a=int(i.strip("\n").split(" ")[0])
            b=int(i.strip("\n").split(" ")[1])
            self.union(a,b) 
            
    def union(self,a,b):
        if self.connected(a,b):
            pass
        else:
           a1=self.root(a)
           b1=self.root(b)
           if self.size[a1]<self.size[b1]:
               self.data[a1]=b1
               self.size[b1]+=self.size[a1]
           else:   
               
               self.data[b1]=a1
               self.size[a1]+=self.size[b1]
               
          
    def connected(self,a,b):
        
        a1=self.root(a)
        b1=self.root(b)
        if a1==b1:
            return True
        else:
            return False
        
    def root(self,a):
        while a!=self.data[a]:
            a=self.data[a]
        return a     
    
    
if __name__=="__main__":
        filepath="/home/shubham/Desktop/data.txt"
        t1=weighted_quick_union(filepath)