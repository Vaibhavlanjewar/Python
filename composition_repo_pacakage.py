class repo:
    def __in__(self):
        self.paclages={}
    def add_package(self,package):
        self.packages[package.name]=package
    def total_size(self): 
       result=0
       for package in self.package.values():
           result ++package.size
       print(result)    
    

r=repo()
r.add_package()
r.total_size()