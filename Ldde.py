from No import No


class Ldde:
    def __init__(self):
        self.prim=self.ult=None
        self.quant=0
        
    def show(self):
        aux = self.prim
        while aux!=None:
            print(aux.info,end=' ')
            aux = aux.prox
        print('\n')
    
    def show_inverso(self):
        aux = self.ult
        while aux!=None:
            print(aux.info,end=' ')
            aux = aux.ant
        print('/n')
            
    def inserir_inicio(self,valor):
        if self.quant==0:
            self.ult=self.prim=No(None,valor,None)
        else:
            self.prim.ant = self.prim = No(None,valor,self.prim)
        self.quant+=1
    
    def inserir_fim(self,valor):
        if self.quant==0:
            self.ult=self.prim=No(None,valor,None)
        else:
            self.ult.prox = self.ult = No(self.ult,valor,None)
        self.quant+=1
    
    def remover_inicio(self):
        if self.quant==1:
            self.ult = self.prim = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant-=1
            
    def remover_fim(self):
        if self.quant==1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ult.prox=None
        self.quant-=1
        
    def remover(self,valor):
        aux=self.prim
        if self.prim.info == valor:
            self.remover_inicio()
        elif self.ult.info == valor:
            self.remover_fim()
        else:
            while aux.info!=valor:
                aux = aux.prox
            aux.ant.prox = aux.prox
            aux.prox.ant = aux.ant
            self.quant-=1
            
    def inserirAposDet(self,valor1,valor2):
        if self.quant==0:
            print('A lista está vazia!')
        else:
            aux = self.prim
            while aux!=None and aux.info!=valor2:
                aux = aux.prox
            if aux==None:
                print('Valor',valor2,'não está na lista!')
            else:
                if aux==self.ult:
                    self.ult.prox = self.ult = No(self.ult,valor1,None)
                else:
                    aux.prox.ant = aux.prox = No(aux,valor1,aux.prox) 
            self.quant+=1
            