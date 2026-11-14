"""
Programa: Árbol Binario de Búsqueda con interfaz gráfica (tkinter)
Clases: Nodo, Arbol y VentanaArbol
Ejecutar con:  python arbol_gui.py
"""

import tkinter as tk
from tkinter import ttk


# ======================================================
#  CLASE NODO
# ======================================================
class Nodo:
    """Un nodo guarda un dato y apunta a su hijo izquierdo y derecho."""

    def __init__(self, dato):
        self.dato = dato
        self.izq = None   # hijo izquierdo (valores menores)
        self.der = None   # hijo derecho (valores mayores)


# ======================================================
#  CLASE ARBOL (árbol binario de búsqueda)
# ======================================================
class Arbol:
    """Menores a la izquierda, mayores a la derecha."""

    def __init__(self):
        self.raiz = None

    def esta_vacio(self):
        return self.raiz is None

    # ---------- Insertar ----------
    def insertar(self, dato):
        """Devuelve True si se insertó, False si ya existía."""
        if self.buscar(dato):
            return False
        self.raiz = self._insertar(self.raiz, dato)
        return True

    def _insertar(self, nodo, dato):
        if nodo is None:
            return Nodo(dato)
        if dato < nodo.dato:
            nodo.izq = self._insertar(nodo.izq, dato)
        else:
            nodo.der = self._insertar(nodo.der, dato)
        return nodo

    # ---------- Buscar ----------
    def buscar(self, dato):
        nodo = self.raiz
        while nodo is not None:
            if dato == nodo.dato:
                return True
            nodo = nodo.izq if dato < nodo.dato else nodo.der
        return False

    # ---------- Eliminar (3 casos) ----------
    def eliminar(self, dato):
        """Devuelve True si se eliminó, False si no existía."""
        if not self.buscar(dato):
            return False
        self.raiz = self._eliminar(self.raiz, dato)
        return True

    def _eliminar(self, nodo, dato):
        if nodo is None:
            return None
        if dato < nodo.dato:
            nodo.izq = self._eliminar(nodo.izq, dato)
        elif dato > nodo.dato:
            nodo.der = self._eliminar(nodo.der, dato)
        else:
            if nodo.izq is None and nodo.der is None:   # caso 1: hoja
                return None
            if nodo.izq is None:                        # caso 2: un hijo
                return nodo.der
            if nodo.der is None:
                return nodo.izq
            sucesor = self._minimo(nodo.der)            # caso 3: dos hijos
            nodo.dato = sucesor.dato
            nodo.der = self._eliminar(nodo.der, sucesor.dato)
        return nodo

    # ---------- Mínimo y máximo ----------
    def _minimo(self, nodo):
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo

    def minimo(self):
        return None if self.esta_vacio() else self._minimo(self.raiz).dato

    def maximo(self):
        if self.esta_vacio():
            return None
        nodo = self.raiz
        while nodo.der is not None:
            nodo = nodo.der
        return nodo.dato

    # ---------- Recorridos ----------
    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, res):      # Raíz, Izq, Der
        if nodo:
            res.append(nodo.dato)
            self._preorden(nodo.izq, res)
            self._preorden(nodo.der, res)

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, res):       # Izq, Raíz, Der
        if nodo:
            self._inorden(nodo.izq, res)
            res.append(nodo.dato)
            self._inorden(nodo.der, res)

    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, res):     # Izq, Der, Raíz
        if nodo:
            self._postorden(nodo.izq, res)
            self._postorden(nodo.der, res)
            res.append(nodo.dato)

    def por_niveles(self):
        resultado = []
        if self.raiz is None:
            return resultado
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.dato)
            if nodo.izq:
                cola.append(nodo.izq)
            if nodo.der:
                cola.append(nodo.der)
        return resultado

    # ---------- Información ----------
    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self._altura(nodo.izq), self._altura(nodo.der))

    def contar_nodos(self):
        return len(self.preorden())

    def contar_hojas(self):
        return self._hojas(self.raiz)

    def _hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.izq is None and nodo.der is None:
            return 1
        return self._hojas(nodo.izq) + self._hojas(nodo.der)


# ======================================================
#  VENTANA (interfaz gráfica)
# ======================================================
class VentanaArbol:
    RADIO = 20

    def __init__(self, raiz_tk):
        self.arbol = Arbol()
        self.resaltado = None      # valor que se pinta de otro color
        self.color_resaltado = "#f6c945"

        self.root = raiz_tk
        self.root.title("Árbol Binario de Búsqueda")
        self.root.geometry("1100x620")
        self.root.minsize(900, 520)

        self._crear_controles()
        self._crear_zona_dibujo()
        self._crear_panel_respuestas()
        self.actualizar()

    # ---------- Construcción de la ventana ----------
    def _crear_controles(self):
        barra = ttk.Frame(self.root, padding=8)
        barra.pack(side="top", fill="x")

        ttk.Label(barra, text="Número:").pack(side="left")
        self.entrada = ttk.Entry(barra, width=8)
        self.entrada.pack(side="left", padx=6)
        self.entrada.bind("<Return>", lambda e: self.insertar())
        self.entrada.focus()

        ttk.Button(barra, text="Insertar", command=self.insertar).pack(side="left", padx=3)
        ttk.Button(barra, text="Buscar", command=self.buscar).pack(side="left", padx=3)
        ttk.Button(barra, text="Eliminar", command=self.eliminar).pack(side="left", padx=3)
        ttk.Button(barra, text="Ejemplo", command=self.cargar_ejemplo).pack(side="left", padx=(18, 3))
        ttk.Button(barra, text="Limpiar", command=self.limpiar).pack(side="left", padx=3)

        self.mensaje = ttk.Label(barra, text="Escribe un número e inserta.", foreground="#444")
        self.mensaje.pack(side="left", padx=18)

    def _crear_zona_dibujo(self):
        marco = ttk.LabelFrame(self.root, text=" Árbol ", padding=4)
        marco.pack(side="left", fill="both", expand=True, padx=(8, 4), pady=(0, 8))
        self.canvas = tk.Canvas(marco, bg="white", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self.dibujar())

    def _crear_panel_respuestas(self):
        marco = ttk.LabelFrame(self.root, text=" Respuestas del árbol ", padding=10)
        marco.pack(side="right", fill="y", padx=(4, 8), pady=(0, 8))
        marco.configure(width=340)

        self.etiquetas = {}
        campos = [
            ("Preorden", "(Raíz, Izq, Der)"),
            ("Inorden", "(Izq, Raíz, Der)"),
            ("Postorden", "(Izq, Der, Raíz)"),
            ("Por niveles", "(fila por fila)"),
            ("Altura", ""),
            ("Nodos", ""),
            ("Hojas", ""),
            ("Mínimo", ""),
            ("Máximo", ""),
        ]
        for nombre, ayuda in campos:
            fila = ttk.Frame(marco)
            fila.pack(fill="x", pady=3)
            titulo = nombre + (" " + ayuda if ayuda else "")
            ttk.Label(fila, text=titulo, font=("Segoe UI", 9, "bold")).pack(anchor="w")
            valor = ttk.Label(fila, text="-", wraplength=310, justify="left",
                              font=("Consolas", 11))
            valor.pack(anchor="w")
            self.etiquetas[nombre] = valor

    # ---------- Leer el número escrito ----------
    def _leer(self):
        texto = self.entrada.get().strip()
        try:
            numero = int(texto)
        except ValueError:
            self._decir("Escribe un número entero válido.", "#b00020")
            return None
        return numero

    def _decir(self, texto, color="#1b5e20"):
        self.mensaje.config(text=texto, foreground=color)

    # ---------- Acciones de los botones ----------
    def insertar(self):
        n = self._leer()
        if n is None:
            return
        self.resaltado = None
        if self.arbol.insertar(n):
            self.resaltado = n
            self._decir(f"Se insertó el {n}.")
        else:
            self._decir(f"El {n} ya está en el árbol.", "#b00020")
        self._despues_de_accion()

    def buscar(self):
        n = self._leer()
        if n is None:
            return
        if self.arbol.buscar(n):
            self.resaltado = n
            self._decir(f"El {n} SÍ está en el árbol.")
        else:
            self.resaltado = None
            self._decir(f"El {n} NO está en el árbol.", "#b00020")
        self.actualizar()
        self.entrada.focus()

    def eliminar(self):
        n = self._leer()
        if n is None:
            return
        self.resaltado = None
        if self.arbol.eliminar(n):
            self._decir(f"Se eliminó el {n}.")
        else:
            self._decir(f"El {n} no existe, no se pudo eliminar.", "#b00020")
        self._despues_de_accion()

    def cargar_ejemplo(self):
        self.arbol = Arbol()
        for n in [50, 30, 70, 20, 40, 60, 80, 35]:
            self.arbol.insertar(n)
        self.resaltado = None
        self._decir("Ejemplo cargado: 50, 30, 70, 20, 40, 60, 80, 35")
        self.actualizar()

    def limpiar(self):
        self.arbol = Arbol()
        self.resaltado = None
        self._decir("Árbol vacío.", "#444")
        self.actualizar()

    def _despues_de_accion(self):
        self.entrada.delete(0, "end")
        self.entrada.focus()
        self.actualizar()

    # ---------- Actualizar pantalla ----------
    def actualizar(self):
        self.dibujar()
        a = self.arbol
        if a.esta_vacio():
            for etiqueta in self.etiquetas.values():
                etiqueta.config(text="-")
            return
        unir = lambda lista: "  ".join(str(x) for x in lista)
        self.etiquetas["Preorden"].config(text=unir(a.preorden()))
        self.etiquetas["Inorden"].config(text=unir(a.inorden()))
        self.etiquetas["Postorden"].config(text=unir(a.postorden()))
        self.etiquetas["Por niveles"].config(text=unir(a.por_niveles()))
        self.etiquetas["Altura"].config(text=str(a.altura()))
        self.etiquetas["Nodos"].config(text=str(a.contar_nodos()))
        self.etiquetas["Hojas"].config(text=str(a.contar_hojas()))
        self.etiquetas["Mínimo"].config(text=str(a.minimo()))
        self.etiquetas["Máximo"].config(text=str(a.maximo()))

    # ---------- Dibujo del árbol ----------
    def _posiciones(self):
        """Calcula (x, y) de cada nodo: x por orden inorden, y por nivel."""
        posiciones = {}
        contador = [0]
        profundidad_max = [0]

        def recorrer(nodo, nivel):
            if nodo is None:
                return
            recorrer(nodo.izq, nivel + 1)
            posiciones[nodo] = (contador[0], nivel)
            contador[0] += 1
            profundidad_max[0] = max(profundidad_max[0], nivel)
            recorrer(nodo.der, nivel + 1)

        recorrer(self.arbol.raiz, 0)
        return posiciones, contador[0], profundidad_max[0]

    def dibujar(self):
        c = self.canvas
        c.delete("all")
        ancho, alto = c.winfo_width(), c.winfo_height()
        if self.arbol.esta_vacio():
            c.create_text(ancho / 2, alto / 2, text="El árbol está vacío",
                          fill="#888", font=("Segoe UI", 16))
            return

        posiciones, total, prof = self._posiciones()
        margen = 40
        paso_x = (ancho - 2 * margen) / max(total - 1, 1)
        paso_x = min(paso_x, 70)
        paso_y = (alto - 2 * margen) / max(prof, 1)
        paso_y = min(paso_y, 90)
        inicio_x = (ancho - paso_x * (total - 1)) / 2

        def coord(nodo):
            col, nivel = posiciones[nodo]
            return inicio_x + col * paso_x, margen + nivel * paso_y

        # primero las líneas, luego los círculos
        for nodo in posiciones:
            x, y = coord(nodo)
            for hijo in (nodo.izq, nodo.der):
                if hijo:
                    hx, hy = coord(hijo)
                    c.create_line(x, y, hx, hy, fill="#555", width=2)

        for nodo in posiciones:
            x, y = coord(nodo)
            es_raiz = nodo is self.arbol.raiz
            if nodo.dato == self.resaltado:
                color = self.color_resaltado
            elif es_raiz:
                color = "#90caf9"
            else:
                color = "#e0e0e0"
            c.create_oval(x - self.RADIO, y - self.RADIO, x + self.RADIO, y + self.RADIO,
                          fill=color, outline="#333", width=2)
            c.create_text(x, y, text=str(nodo.dato), font=("Segoe UI", 11, "bold"))


# ======================================================
#  PROGRAMA PRINCIPAL
# ======================================================
if __name__ == "__main__":
    ventana = tk.Tk()
    VentanaArbol(ventana)
    ventana.mainloop()