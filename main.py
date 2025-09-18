import queue

class Estadisticas:
    def __init__(self, 
                 clientes_atendidos = 0,
                 tiempo_espera_max = 0,
                 sum_time_wait = 0,
                 time_open_cashier = 0
                ):
        self.clientes_atendidos = clientes_atendidos
        self.tiempo_espera_max = tiempo_espera_max
        self.sum_time_wait = sum_time_wait
        self.time_open_cashier = time_open_cashier

class GenerardoLlegadas:
    def __init__(self,
                 tiempo_medio: float,
                 proxima_llegada: float,
                 contador_clientes: int
                ):
        self.tiempo_medio = tiempo_medio
        self.proxima_llegada = proxima_llegada
        self.contador_clientes = contador_clientes


class Cliente:
    def __init__(self,
                 id: int,
                 tiempo_llegada: float,
                 tiempo_inicio_atencion: float,
                 tiempo_fin_atencion: float,
                ):
        self.id = id
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_inicio_atencion = tiempo_inicio_atencion
        self.tiempo_fin_atencion = tiempo_fin_atencion

class FilaClientes:
    def __init__(self,
                 cola: queue,
                 len_max: int,
                 len_sum: float,
                 mediciones: int
                ):
        self.cola = cola
        self.len_max = len_max
        self.len_sum = len_sum
        self.mediciones = mediciones

class Caja:
    def __init__(self,
                 numero: int,
                 tiempo_min: float,
                 tiempo_max: float,
                 ocupada = False,
                 cliente_actual = None,
                 tiempo_fin_atencion = 0,
                 is_activa = True,
                 tiempo_activacion = 0,
                 tiempo_total_activa = 0
                ):
        self.numero = numero
        self.tiempo_min = tiempo_min
        self.tiempo_max = tiempo_max
        self.ocupada = ocupada
        self.cliente_actual = cliente_actual
        self.tiempo_fin_atencion = tiempo_fin_atencion
        self.is_activa = is_activa
        self.tiempo_activacion = tiempo_activacion
        self.tiempo_total_activa = tiempo_total_activa

class Simulador():

    def __init__(self, 
                 tiempo_simulacion : float,
                 estadisticas = Estadisticas(),
                 cajas = [Caja(1, 1.5, 2.5), Caja(2, 2, 5), Caja(3, 2, 4), Caja(4, 2, 4.5, is_activa=False)],
                 tiempo_actual = 0,
                 fila_clientes = None,
                 ):
        self.tiempo_simulacion = tiempo_simulacion * 60  + 0.5 # Convertir a minutos
        self.tiempo_actual = tiempo_actual
        self.fila_clientes = fila_clientes
        self.cajas = cajas
        self.estadisticas = estadisticas
    
    def iniciarSimulacion(self):
        fila_de_clientes = Cliente(queue.SimpleQueue(), )
        
        while self.tiempo_actual < self.tiempo_simulacion:
                # print(self.tiempo_actual)
                if self.tiempo_actual % 1 == 0 and self.tiempo_actual > 0:
                        print(self.tiempo_actual)
                
                self.tiempo_actual += 0.5



def main():
    simulacion = Simulador(7) # 7 horas
    simulacion.iniciarSimulacion()

main()