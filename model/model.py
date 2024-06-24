import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.getColori=DAO.getColori()
        self.getAllProdotti=DAO.getProdotti()
        self.grafo=nx.Graph()
        self._idMap={}
        for v in self.getAllProdotti:
            self._idMap[v.Product_number] = v

    def creaGrafo(self, anno,colore):
        self.nodi = DAO.getNodi(colore)
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges(anno,colore)

        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self, anno,colore):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni(colore,anno)
        for connessione in allEdges:
            nodo1 = self._idMap[connessione.v1]
            nodo2 = self._idMap[connessione.v2]
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes and nodo1!=nodo2:
                if self.grafo.has_edge(nodo1, nodo2) == False:
                    self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)

    def analisi(self):
        lista=[]
        prodotti=[]
        risultato=set()
        for arco in self.grafo.edges:
            lista.append((arco[0],arco[1],self.grafo[arco[0]][arco[1]]["weight"]))
        listaOrdinata=sorted(lista, key=lambda x:x[2],reverse=True)
        print(listaOrdinata)
        listaOrdinata=listaOrdinata[:3]
        for (p1,p2,peso) in listaOrdinata:
            if p1 in prodotti:
                risultato.add(p1)
            else:
                prodotti.append(p1)
            if p2 in prodotti:
                risultato.add(p2)
            else:
                prodotti.append(p2)
        return risultato,listaOrdinata
