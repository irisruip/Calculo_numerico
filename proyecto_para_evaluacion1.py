import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, TextField
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment


def main(page: Page) -> None:
    page.title = 'Evaluacion numero 1'
    page.window_width = 720
    page.window_height = 500
    
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        
        #Principal
        page.views.append(
            View(
                #defino la ruta
                route = ' /',
                controls =[
                    #barra superior
                    AppBar(title=Text(''), bgcolor='purple'),
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
            
        
        t = ft.Text()
        tb1 = ft.TextField(label="Numero decimal")
        btn_binario = ft.ElevatedButton(text="Convertir a binario", on_click=convertir_a_binario)             
        btn_octal = ft.ElevatedButton(text="Convertir a octal", on_click=convertir_a_octal)
        btn_hexadecimal = ft.ElevatedButton(text="Convertir a hexadecimal", on_click=convertir_a_hexadecimal)    
        
        
        #Interfaz de Traductor
        if page.route == ' /traductor':
            
            page.views.append(
                View(
                    route = ' /traductor',
                    controls =[
                        #AppBar(title=Text('Traductor'), bgcolor='blue'),
                        Text(value='Traductor', size=30),
                        tb1,
                        t,
                        btn_binario,
                        btn_octal,
                        btn_hexadecimal,
                        #ElevatedButton(text='Convertir a binario', on_click=lambda _: convert_to_binary(decimal_input, binary_output)),
                        ElevatedButton(text='Regresar a principal', on_click=lambda _: page.go(' /'))
                        ],
                    vertical_alignment = MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                    )
            
        )
        page.update()
        
        
        #Interfaz de seidel, solo frontend   
        if page.route == ' /seidel':
            page.views.append(
            View(
                route = ' /seidel',
                controls =[
                    #AppBar(title=Text('Gauss Seidel'), bgcolor='blue'),
                    Text(value='Gauss Seidel', size=30),
                    ElevatedButton(text='Regresar a principal', on_click=lambda _: page.go(' /'))
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
