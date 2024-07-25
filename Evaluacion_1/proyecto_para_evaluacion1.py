import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, TextField
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import numpy as np

def main(page: Page) -> None:
    page.title = 'Evaluacion numero 1'
    page.window_width = 720
    page.window_height = 800
    
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        #Principal
        page.views.append(
            View(
                #defino la ruta
                route = ' /',
                controls =[
                    #barra superior
                    AppBar(title=Text(''), bgcolor='pink'),
                    Text(value='Principal', size=30), 
                    ElevatedButton(text='Ir al traductor', on_click=lambda _: page.go(' /traductor')),
                    ElevatedButton(text='Ir a Gauss-Seidel', on_click=lambda _: page.go(' /seidel'))
                ],
                vertical_alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
            
        )
        
        #decimal a binario
        def decimal_a_binario(decimal):
            if decimal ==0:
                return "0"
            binario = ""
            while decimal>0:
                resto = decimal%2
                binario = str(resto) + binario
                decimal//=2
            return binario
        
        
        def convertir_a_binario(e):
            try:
                num_decimal = float(tb1.value)
                num_binario = decimal_a_binario(int(num_decimal))
                t.value = f"El equivalente binario de {num_decimal} es: {num_binario}"
            except ValueError:
                t.value = "Ingrese un numero"   
            page.update()
            
        #decimal a octal
            
        def decimal_a_octal(decimal):
            if decimal ==0:
                return "0"
            octal = ""
            while decimal>0:
                resto = decimal%8
                octal = str(resto)+octal
                decimal//=8
            return octal
        
        def convertir_a_octal(e):
            try:
                num_decimal= float(tb1.value)
                num_octal = decimal_a_octal(int(num_decimal))
                t.value = f"El equivalente octal de {num_decimal} es: {num_octal}"
            except ValueError:
                t.value = "Ingrese un numero"
            page.update()
            
        #deicmal a hexadecimal
            
        def decimal_a_hexadecimal(decimal):
            tabla = {
                0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
                }
            hexadecimal = ""
            while decimal>0:
                resto = decimal%16
                hexadecimal = tabla[resto] + hexadecimal
                decimal//=16
            return hexadecimal
            
        def convertir_a_hexadecimal(e):
            try:
                num_decimal= float(tb1.value)
                num_hexadecimal = decimal_a_hexadecimal(int(num_decimal))
                t.value = f"El equivalente hexadecimal de {num_decimal} es: {num_hexadecimal}"
            except ValueError:
                t.value = "Ingrese un numero"
            page.update()
            
        def decimal_a_ternario(decimal):
            if decimal == 0:
                return "0"
            ternario = ""
            while decimal > 0:
                resto = decimal % 3
                ternario = str(resto) + ternario
                decimal //= 3
            return ternario
            
        
        def convertir_a_ternario(e):
            try:
                num_decimal = float(tb1.value)
                num_ternario = decimal_a_ternario(int(num_decimal))
                t.value = f"El equivalente ternario de {num_decimal} es: {num_ternario}"
            except ValueError:
                t.value = "Ingrese un numero"
            page.update()
            
        def decimal_a_cuaternario(decimal):
            if decimal == 0:
                return "0"
            cuaternario = ""
            while decimal > 0:
                resto = decimal % 4
                cuaternario = str(resto) + cuaternario
                decimal //= 4
            return cuaternario
            
        
        def convertir_a_cuaternario(e):
            try:
                num_decimal = float(tb1.value)
                num_cuaternario = decimal_a_cuaternario(int(num_decimal))
                t.value = f"El equivalente cuaternario de {num_decimal} es: {num_cuaternario}"
            except ValueError:
                t.value = "Ingrese un numero"
            page.update()
            
        
        t = ft.Text()
        tb1 = ft.TextField(label="Numero decimal")
        btn_binario = ft.ElevatedButton(text="Convertir a binario", on_click=convertir_a_binario)             
        btn_octal = ft.ElevatedButton(text="Convertir a octal", on_click=convertir_a_octal)
        btn_hexadecimal = ft.ElevatedButton(text="Convertir a hexadecimal", on_click=convertir_a_hexadecimal)    
        btn_ternario = ft.ElevatedButton(text="Convertir a ternario", on_click=convertir_a_ternario)
        btn_cuaternario = ft.ElevatedButton(text="Convertir a cuaternario", on_click=convertir_a_cuaternario)
        
        #Interfaz de Traductor
        if page.route == ' /traductor':
            
            page.views.append(
                View(
                    route = ' /traductor',
                    controls =[
                        AppBar(title=Text('Traductor'), bgcolor='pink'),
                        Text(value='Traductor', size=30),
                        tb1,
                        t,
                        btn_binario,
                        btn_octal,
                        btn_hexadecimal,
                        btn_ternario,
                        btn_cuaternario,
                        #ElevatedButton(text='Convertir a binario', on_click=lambda _: convert_to_binary(decimal_input, binary_output)),
                        #ElevatedButton(text='Regresar a principal', on_click=lambda _: page.go(' /'))
                        ],
                    vertical_alignment = MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                    )
            
        )
        page.update()
        

        #matriz
        def generate_matriz(n):
            return np.random.randint(low=0, high=100, size=(n,n))
        
        def gauss_seidel(A, b, x0, tol=1e-5, max_iter=15):
            n = len(A)
            x = x0.copy()
            for _ in range(max_iter):
                x_new = x0.copy()
                for i in range(n):
                    s1 = np.dot(A[i, :i], x[:i])
                    s2 = np.dot(A[i, i + 1:], x[i + 1:])
                    x_new[i] = (b[i] - s1 - s2) / A[i, i]
                if np.allclose(x, x_new, rtol=tol):
                    break
                x = x_new
            return x
        
        #Interfaz de seidel, solo frontend   
        if page.route == ' /seidel':
            n = ft.TextField(label="Tamaño de la matriz")
            matriz_text = ft.Text(value="", size=30)
            b = ft.Text(value="", size=30)
                                  
            def on_generate_click(_):
                size = int(n.value)
                matriz = generate_matriz(size)
                matriz_str = "\n".join(" ".join(str(cell) for cell in row) for row in matriz)
                matriz_text.value = matriz_str
                matriz_text.update()
                
            generate_button = ft.ElevatedButton(text = 'Generar matriz',on_click=on_generate_click)
            result_text = ft.Text(value="", size=30)
            
            solve_button = ft.ElevatedButton(text='Resolver')
            
            def on_solve_click(_):
                matriz_str = matriz_text.value.split("\n")
                matriz = np.array([list(map(int, row.split())) for row in matriz_str])
                b = np.random.randint(low=0, high=100, size=len(matriz))
                x0 = np.zeros_like(b)
                
                x = gauss_seidel(matriz, b, x0)
                
                result_text.value = "Vector b: [" + " ".join(str(bi) for bi in b)+"]" + "\nSolución: [" + " ".join(str(xi) for xi in x)+"]"
                result_text.update()
                
                
            solve_button.on_click = on_solve_click
                
            page.update()
            
            page.views.append(
            View(
                route = ' /seidel',
                controls =[
                    AppBar(title=Text('Gauss Seidel'), bgcolor='pink'),
                    Text(value='Gauss Seidel', size=30),
                    n,
                    generate_button,
                    matriz_text,
                    solve_button,
                    b,
                    result_text,
                    #ElevatedButton(text='Regresar a principal', on_click=lambda _: page.go(' /'))
                ],
                vertical_alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
            
        )
            
        page.update()
       
    #manejo el boton de retroceso 
    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)
        
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
if __name__ == '__main__':
    ft.app(target=main)
