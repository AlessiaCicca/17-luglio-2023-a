import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        colore = self._view.ddcolor.value
        if colore is None:
            self._view.create_alert("Selezionare un colore")
            return
        anno = self._view.ddyear.value
        if anno is None:
            self._view.create_alert("Selezionare un Anno")
            return

        grafo = self._model.creaGrafo(int(anno),colore)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        prodotti, lista=self._model.analisi()
        for (p1,p2,peso) in lista:
            self._view.txt_result.controls.append(ft.Text(f"Arco da {p1} a {p2}, peso= {peso}"))
        self._view.txt_result.controls.append(ft.Text("I nodi ripetuti sono"))
        for prodotto in prodotti:
            self._view.txt_result.controls.append(ft.Text(f"{prodotto}"))

        self._view.update_page()

    def fillDD(self):
            ann = "201"
            for i in range(5, 9):
                anno = ann + str(i)
                self._view.ddyear.options.append(ft.dropdown.Option(
                    text=anno))
            colori = self._model.getColori
            for colore in colori:
                self._view.ddcolor.options.append(ft.dropdown.Option(
                    text=colore))
