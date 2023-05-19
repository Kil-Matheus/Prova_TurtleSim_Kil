class Fila():
    
    def __init__(self):
        self.coordenadas = [(0.0, 0.5), (0.5, 0.0), (0.0, 0.5), (0.5, 0.0), (0.0, 1.0), (1.0, 0.0)]
        self.coordenadas_invertida = [(1.0, 0.0), (0.0, -1.0), (0.5, 0.0), (0.0, -0.5), (0.5, 0.0), (0.0, -0.5)]
        
    def n_itens(self):
        return len(self.coordenadas)
    
    def enfileirar(self, x):
        return self.coordenadas.append(x)
    
    def chamar_item(self):
        if self.coordenadas == 0:
            return print('A Fila está Vazia')
        else:
            resposta_1 = float(self.coordenadas[0][0])
            resposta_2 = float(self.coordenadas[0][1])
            self.coordenadas.pop(0)
            return resposta_1, resposta_2
        
    def ver(self):
        return print(self.coordenadas)
    
    def invertida(self):
        return len(self.coordenadas_invertida)
    
    def ver_invertida(self):
        return print(self.coordenadas_invertida)
    
    def chamar_invertida(self):
        if self.coordenadas == 0:
            return print('A Fila está Vazia')
        else:
            resposta_1 = float(self.coordenadas_invertida[0][0])
            resposta_2 = float(self.coordenadas_invertida[0][1])
            self.coordenadas_invertida.pop(0)
            return resposta_1, resposta_2