"""
Visualización gráfica de una PILA (estructura LIFO: Last In, First Out).

Operaciones:
  - Push (apilar): agrega un elemento en el tope.
  - Pop (desapilar): quita el elemento del tope.
  - Peek (ver tope): consulta el elemento del tope sin quitarlo.
  - Limpiar: vacía la pila.

Requisitos: Python 3 con Tkinter (viene incluido en la mayoría de instalaciones).
"""

import random
import tkinter as tk
from tkinter import ttk


# ----------------------------------------------------------------------
# Estructura de datos
# ----------------------------------------------------------------------
class Pila:
    """Pila con capacidad máxima, implementada sobre una lista."""

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self._items = []

    def push(self, valor):
        if self.esta_llena():
            raise OverflowError("Desbordamiento (stack overflow): la pila está llena")
        self._items.append(valor)

    def pop(self):
        if self.esta_vacia():
            raise IndexError("Subdesbordamiento (stack underflow): la pila está vacía")
        return self._items.pop()

    def peek(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía, no hay tope")
        return self._items[-1]

    def esta_vacia(self):
        return len(self._items) == 0

    def esta_llena(self):
        return len(self._items) >= self.capacidad

    def tamano(self):
        return len(self._items)

    def limpiar(self):
        self._items.clear()


# ----------------------------------------------------------------------
# Interfaz gráfica
# ----------------------------------------------------------------------
class AplicacionPila(tk.Tk):
    CAPACIDAD = 8

    # Geometría del dibujo
    ANCHO, ALTO = 400, 580
    X0, X1 = 110, 290          # paredes del contenedor
    BASE = 540                 # y del fondo del contenedor
    CELDA = 58                 # alto de cada "casilla"
    BLOQUE_H = 52              # alto del bloque dentro de la casilla
    Y_ENTRADA = 20             # altura desde donde cae un bloque nuevo
    PASO = 14                  # píxeles por fotograma de animación
    RETARDO = 16               # ms entre fotogramas

    COLORES = ["#4C9AFF", "#36B37E", "#FFAB00", "#FF5630",
               "#6554C0", "#00B8D9", "#F06292", "#8D6E63"]

    def __init__(self):
        super().__init__()
        self.title("Pila (Stack) – Visualización gráfica")
        self.resizable(False, False)
        self.configure(bg="#F4F5F7")

        self.pila = Pila(self.CAPACIDAD)
        self.bloques = []          # lista paralela a la pila: (rect_id, texto_id, color)
        self.animando = False
        self.contador_color = 0

        self._crear_widgets()
        self._dibujar_contenedor()
        self._actualizar_estado()
        self._log("Pila creada (capacidad %d)." % self.CAPACIDAD, "info")

    # ---------------------------- Widgets ----------------------------
    def _crear_widgets(self):
        marco = tk.Frame(self, bg="#F4F5F7")
        marco.pack(padx=12, pady=12)

        # Lienzo
        self.lienzo = tk.Canvas(marco, width=self.ANCHO, height=self.ALTO,
                                bg="white", highlightthickness=1,
                                highlightbackground="#C1C7D0")
        self.lienzo.grid(row=0, column=0, rowspan=2, padx=(0, 12))

        # Panel de control
        panel = tk.Frame(marco, bg="#F4F5F7")
        panel.grid(row=0, column=1, sticky="n")

        tk.Label(panel, text="PILA (LIFO)", font=("Helvetica", 16, "bold"),
                 bg="#F4F5F7", fg="#172B4D").pack(anchor="w")
        tk.Label(panel, text="El último en entrar es el primero en salir.",
                 font=("Helvetica", 9), bg="#F4F5F7", fg="#5E6C84").pack(anchor="w", pady=(0, 10))

        tk.Label(panel, text="Valor a apilar:", bg="#F4F5F7").pack(anchor="w")
        self.entrada = ttk.Entry(panel, width=18, font=("Helvetica", 12))
        self.entrada.pack(anchor="w", pady=(0, 4))
        self.entrada.bind("<Return>", lambda e: self.apilar())
        self.entrada.focus()
        tk.Label(panel, text="(vacío = número aleatorio)", font=("Helvetica", 8),
                 bg="#F4F5F7", fg="#97A0AF").pack(anchor="w", pady=(0, 8))

        self.botones = []
        for texto, comando in [("⬇  Push (apilar)", self.apilar),
                               ("⬆  Pop (desapilar)", self.desapilar),
                               ("👁  Peek (ver tope)", self.ver_tope),
                               ("🗑  Limpiar pila", self.limpiar)]:
            b = ttk.Button(panel, text=texto, command=comando, width=22)
            b.pack(anchor="w", pady=2)
            self.botones.append(b)

        # Estado
        self.lbl_estado = tk.Label(panel, text="", justify="left", anchor="w",
                                   font=("Courier", 10), bg="#DFE1E6", fg="#172B4D",
                                   padx=8, pady=6)
        self.lbl_estado.pack(fill="x", pady=(12, 8))

        # Registro de operaciones
        tk.Label(panel, text="Registro de operaciones:", bg="#F4F5F7").pack(anchor="w")
        cont_log = tk.Frame(panel)
        cont_log.pack(fill="both")
        self.log = tk.Text(cont_log, width=34, height=14, state="disabled",
                           font=("Courier", 9), wrap="word", bg="white",
                           relief="flat", highlightthickness=1,
                           highlightbackground="#C1C7D0")
        barra = ttk.Scrollbar(cont_log, command=self.log.yview)
        self.log.configure(yscrollcommand=barra.set)
        self.log.pack(side="left", fill="both")
        barra.pack(side="right", fill="y")
        self.log.tag_config("push", foreground="#00875A")
        self.log.tag_config("pop", foreground="#DE350B")
        self.log.tag_config("peek", foreground="#0052CC")
        self.log.tag_config("error", foreground="#BF2600", font=("Courier", 9, "bold"))
        self.log.tag_config("info", foreground="#5E6C84")

    # ---------------------------- Dibujo ----------------------------
    def _y_bloque(self, indice):
        """Coordenadas (y0, y1) del bloque en la posición `indice` (0 = fondo)."""
        y1 = self.BASE - indice * self.CELDA - (self.CELDA - self.BLOQUE_H) // 2
        return y1 - self.BLOQUE_H, y1

    def _dibujar_contenedor(self):
        c = self.lienzo
        tope_cont = self.BASE - self.CAPACIDAD * self.CELDA
        # Casillas guía (índices)
        for i in range(self.CAPACIDAD):
            y = self.BASE - (i + 1) * self.CELDA
            c.create_line(self.X0, y, self.X1, y, fill="#EBECF0", dash=(3, 3))
            c.create_text(self.X0 - 14, y + self.CELDA / 2, text=str(i),
                          fill="#97A0AF", font=("Helvetica", 9))
        # Paredes en forma de "U"
        c.create_line(self.X0, tope_cont - 10, self.X0, self.BASE,
                      self.X1, self.BASE, self.X1, tope_cont - 10,
                      width=5, fill="#42526E", joinstyle="round", capstyle="round")
        c.create_text((self.X0 + self.X1) / 2, self.BASE + 20,
                      text="FONDO", fill="#42526E", font=("Helvetica", 9, "bold"))
        # Mensaje de pila vacía y flecha TOPE (se redibujan dinámicamente)
        self.id_vacia = c.create_text((self.X0 + self.X1) / 2, self.BASE - self.CELDA / 2,
                                      text="(pila vacía)", fill="#A5ADBA",
                                      font=("Helvetica", 12, "italic"))
        self.id_tope = None

    def _dibujar_tope(self):
        """Dibuja/mueve la flecha 'TOPE' junto al último bloque."""
        c = self.lienzo
        if self.id_tope:
            for i in self.id_tope:
                c.delete(i)
            self.id_tope = None
        if self.pila.esta_vacia():
            return
        y0, y1 = self._y_bloque(self.pila.tamano() - 1)
        ym = (y0 + y1) / 2
        flecha = c.create_line(self.X1 + 50, ym, self.X1 + 8, ym, arrow="last",
                               width=3, fill="#DE350B")
        texto = c.create_text(self.X1 + 52, ym, text="TOPE", anchor="w",
                              fill="#DE350B", font=("Helvetica", 11, "bold"))
        self.id_tope = (flecha, texto)

    def _crear_bloque(self, valor, y0):
        color = self.COLORES[self.contador_color % len(self.COLORES)]
        self.contador_color += 1
        rect = self.lienzo.create_rectangle(self.X0 + 6, y0, self.X1 - 6, y0 + self.BLOQUE_H,
                                            fill=color, outline="#172B4D", width=2)
        texto = self.lienzo.create_text((self.X0 + self.X1) / 2, y0 + self.BLOQUE_H / 2,
                                        text=str(valor), fill="white",
                                        font=("Helvetica", 16, "bold"))
        return rect, texto, color

    # --------------------------- Utilidades ---------------------------
    def _log(self, mensaje, etiqueta="info"):
        self.log.configure(state="normal")
        self.log.insert("end", mensaje + "\n", etiqueta)
        self.log.see("end")
        self.log.configure(state="disabled")

    def _actualizar_estado(self):
        p = self.pila
        tope = repr(p._items[-1]) if not p.esta_vacia() else "—"
        self.lbl_estado.config(text=(
            f"Tamaño   : {p.tamano()} / {p.capacidad}\n"
            f"Tope     : {tope}\n"
            f"¿Vacía?  : {'Sí' if p.esta_vacia() else 'No'}\n"
            f"¿Llena?  : {'Sí' if p.esta_llena() else 'No'}"))
        self.lienzo.itemconfigure(self.id_vacia,
                                  state="normal" if p.esta_vacia() else "hidden")

    def _bloquear(self, bloquear):
        self.animando = bloquear
        for b in self.botones:
            b.state(["disabled"] if bloquear else ["!disabled"])

    def _parpadear_error(self):
        """Pequeña sacudida del contenedor para indicar un error."""
        self.lienzo.configure(highlightbackground="#DE350B", highlightthickness=3)
        self.after(350, lambda: self.lienzo.configure(highlightbackground="#C1C7D0",
                                                      highlightthickness=1))

    # --------------------------- Operaciones ---------------------------
    def apilar(self):
        if self.animando:
            return
        valor = self.entrada.get().strip()
        if not valor:
            valor = str(random.randint(1, 99))
        if len(valor) > 8:
            valor = valor[:8]
        try:
            self.pila.push(valor)
        except OverflowError as e:
            self._log("push(%s) → ERROR: %s" % (valor, e), "error")
            self._parpadear_error()
            return

        self.entrada.delete(0, "end")
        indice = self.pila.tamano() - 1
        destino_y0, _ = self._y_bloque(indice)
        rect, texto, color = self._crear_bloque(valor, self.Y_ENTRADA)
        self.bloques.append((rect, texto, color))
        self._log("push(%s)  → tamaño = %d" % (valor, self.pila.tamano()), "push")

        self._bloquear(True)
        self._animar_caida(rect, texto, destino_y0, self.Y_ENTRADA)

    def _animar_caida(self, rect, texto, destino_y0, y_actual):
        y_nueva = min(y_actual + self.PASO, destino_y0)
        dy = y_nueva - y_actual
        self.lienzo.move(rect, 0, dy)
        self.lienzo.move(texto, 0, dy)
        if y_nueva < destino_y0:
            self.after(self.RETARDO, self._animar_caida, rect, texto, destino_y0, y_nueva)
        else:
            self._dibujar_tope()
            self._actualizar_estado()
            self._bloquear(False)

    def desapilar(self):
        if self.animando:
            return
        try:
            valor = self.pila.pop()
        except IndexError as e:
            self._log("pop() → ERROR: %s" % e, "error")
            self._parpadear_error()
            return

        rect, texto, _ = self.bloques.pop()
        self._log("pop()  → devuelve %s, tamaño = %d" % (valor, self.pila.tamano()), "pop")
        # Se quita la flecha del tope mientras sale el bloque
        if self.id_tope:
            for i in self.id_tope:
                self.lienzo.delete(i)
            self.id_tope = None

        self._bloquear(True)
        y0 = self.lienzo.coords(rect)[1]
        self._animar_salida(rect, texto, y0)

    def _animar_salida(self, rect, texto, y_actual):
        y_nueva = max(y_actual - self.PASO, self.Y_ENTRADA - self.BLOQUE_H)
        dy = y_nueva - y_actual
        self.lienzo.move(rect, 0, dy)
        self.lienzo.move(texto, 0, dy)
        if y_nueva > self.Y_ENTRADA - self.BLOQUE_H:
            self.after(self.RETARDO, self._animar_salida, rect, texto, y_nueva)
        else:
            self.lienzo.delete(rect)
            self.lienzo.delete(texto)
            self._dibujar_tope()
            self._actualizar_estado()
            self._bloquear(False)

    def ver_tope(self):
        if self.animando:
            return
        try:
            valor = self.pila.peek()
        except IndexError as e:
            self._log("peek() → ERROR: %s" % e, "error")
            self._parpadear_error()
            return
        self._log("peek() → el tope es %s (no se elimina)" % valor, "peek")
        rect = self.bloques[-1][0]
        self._bloquear(True)
        self._resaltar(rect, 6)

    def _resaltar(self, rect, veces):
        """Parpadeo del borde del bloque del tope."""
        if veces == 0:
            self.lienzo.itemconfigure(rect, outline="#172B4D", width=2)
            self._bloquear(False)
            return
        if veces % 2 == 0:
            self.lienzo.itemconfigure(rect, outline="#FFD700", width=5)
        else:
            self.lienzo.itemconfigure(rect, outline="#172B4D", width=2)
        self.after(180, self._resaltar, rect, veces - 1)

    def limpiar(self):
        if self.animando:
            return
        self.pila.limpiar()
        for rect, texto, _ in self.bloques:
            self.lienzo.delete(rect)
            self.lienzo.delete(texto)
        self.bloques.clear()
        self._dibujar_tope()
        self._actualizar_estado()
        self._log("limpiar() → pila vacía.", "info")


if __name__ == "__main__":
    AplicacionPila().mainloop()