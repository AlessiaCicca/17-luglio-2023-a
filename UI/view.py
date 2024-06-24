import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self.ddyear = None
        self.ddcolor = None
        self.txtN = None

        self.btn_graph = None
        self.btn_volume = None
        self.btn_path = None

        self.txt_result = None
        self.txtOut2 = None
        self.txtOut3 = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("ESAME 17/07/23 A", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddyear = ft.Dropdown(label="Anno")
        self.ddcolor= ft.Dropdown(label="Colore")
        self.ddprodotto = ft.Dropdown(label="Prodotto")
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)

        row1 = ft.Row([self.ddyear],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        row2 = ft.Row([self.ddcolor,self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        row3 = ft.Row([self.ddprodotto],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        self._controller.fillDD()

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=0, spacing=5, padding=5, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
