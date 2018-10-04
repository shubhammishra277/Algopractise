'''
Created on 02-Oct-2018

@author: shubham
'''
class quickunion(object):
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
        if self.connected(a,b):
            pass
        else:
           a1=self.root(a)
           b1=self.root(b)
           self.data[b1]=a1
          
    def connected(self,a,b):
        
        a1=self.root(a)
        b1=self.root(b)
        if a1==b1:
            return True
        else:
            return False
        
    def root(self,a):
        #print "self.data[a]",a
        while a!=self.data[a]:
         #   print "a",a
            a=self.data[a]
        return a        
        
if __name__=="__main__":
        filepath="/home/shubham/Desktop/data.txt"
        t1=quickunion(filepath)
        