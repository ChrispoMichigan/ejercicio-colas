import queue
import random
class Cliente:
    def __init__(self,
                 id: int,
                 tiempo_llegada: float,
                 tiempo_fin_atencion = 0,
                ):
        self.id = id
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_fin_atencion = tiempo_fin_atencion

    def iniciarAtencion(tiempo: float):
        pass
    
    def finalizarAtencion(tiempo: float):
        pass

    def calcularTiempoEspera() -> float:
         pass
    
    def calcularTiempoAtencion() -> float:
         pass
class Estadisticas:
    def __init__(self, 
                 clientes_atendidos = [],
                 tiempo_espera_max = 0,
                 sum_time_wait = 0,
                 time_open_cashier = 0
                ):
        self.clientes_atendidos = clientes_atendidos
        self.tiempo_espera_max = tiempo_espera_max
        self.sum_time_wait = sum_time_wait
        self.time_open_cashier_4 = time_open_cashier

    def agregarClienteAtendido(self, cliente: Cliente):
        self.clientes_atendidos.append(cliente)

    def actualizar_tiempo_espera_maximo(self):
        #print(self.obtener_clientes_atendidos())
        tiempos_de_espera = [round(cliente.tiempo_fin_atencion - cliente.tiempo_llegada, 1) for cliente in self.clientes_atendidos]
        self.tiempo_espera_max = max(tiempos_de_espera)

    def agregar_tiempo_cuarta_caja(self, tiempo: float):
        self.time_open_cashier_4 = round(tiempo, 1)

    def obtener_clientes_atendidos(self) -> int: 
        return len(self.clientes_atendidos)
    
    def obtener_tiempo_espera_maximo(self) -> float:
        return self.tiempo_espera_max

    def obtener_tiempo_cuarta_caja(self) -> float:
        return self.time_open_cashier_4
        
    def calcular_tiempo_espera_promedio(self) -> float:
        tiempos_de_espera = [round(cliente.tiempo_fin_atencion - cliente.tiempo_llegada, 1) for cliente in self.clientes_atendidos]
        return round(sum(tiempos_de_espera) / self.obtener_clientes_atendidos(), 2)
class GenerardorLlegadas:
    def __init__(self,
                 tiempo_medio: float,
                 proxima_llegada = 0,
                 contador_clientes = 0
                ):
        self.tiempo_medio = tiempo_medio
        self.proxima_llegada = proxima_llegada
        self.contador_clientes = contador_clientes
        
    def generarProximaLlegada(self) -> float:
        '''
        random.expovariate(1.0): Genera números aleatorios con distribución exponencial. El parámetro 1.0 significa que la media es 1 minuto.
        '''
        tiempo_de_espera = round(random.expovariate(1 / self.tiempo_medio), 1)
        #print(tiempo_de_espera)
        return tiempo_de_espera
    
    def esTiempoDeLlegada(self, tiempo_actual: float) -> bool:
         pass
    
    def crearCliente(self, id: int, tiempo_llegada: float) -> Cliente:
        cliente = Cliente(id, tiempo_llegada)
        return cliente
    
    def programarSiguienteLlegada(tiempo_actual: float):
        pass

class FilaClientes:
    def __init__(self,
                 len_max: int,
                 len_sum: float,
                 mediciones: int,
                 contador_id = 0,
                 cola = queue.SimpleQueue()
                ):
        self.cola = cola
        self.len_max = len_max
        self.len_sum = len_sum
        self.mediciones = mediciones
        self.contador_id = contador_id
    
    def agregarCliente(self, cliente: Cliente):
        self.cola.put(cliente)
    
    def sacarCliente(self) -> Cliente:
        return self.cola.get()
    
    def estaVacia() -> bool:
        pass

    def lenFila(self) -> int:
        return self.cola.qsize()
    
    def calcularLongitudPromedio() -> float:
         pass
    
    def len_max(self) -> int:
         return self.len_max
    
    def actualizarEstadisticas():
         pass
    
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

    def estaLibre(self) -> bool:
        '''
        True: Esta libre
        False: Esta ocuapada
        '''
        return not self.ocupada
    
    def tieneCliente(self) -> bool:
        '''
        True: Tiene
        False: No tiene
        '''
        return self.cliente_actual is not None

    
    def atenderCliente(self, cliente: Cliente, tiempo_actual: float):
        self.cliente_actual = cliente
        self.tiempo_activacion = tiempo_actual
        self.ocupada = True
        tiempo_de_atencion = self.generar_tiempo_atencion()
        #print(tiempo_de_atencion)
        self.tiempo_fin_atencion = round(tiempo_actual + tiempo_de_atencion, 1)
        cliente.tiempo_fin_atencion = self.tiempo_fin_atencion
        self.tiempo_total_activa = self.tiempo_total_activa + tiempo_de_atencion

    def finalizar_atencion(self) -> Cliente:
        cliente_atendido = self.cliente_actual
        self.cliente_actual = None
        self.ocupada = False
        return cliente_atendido

    
    def generar_tiempo_atencion(self) -> float:
        '''
        random.uniform retorna un float del rango indicado
        '''
        return round(random.uniform(self.tiempo_min, self.tiempo_max), 1)

    def activar(self):
        self.is_activa = True

    def desactivar(self):
        self.is_activa = False

    def estaActiva(self) -> bool:
        return self.is_activa
    
    def calcular_tiempo_activa() -> float:
        pass
class Simulador():

    def __init__(self, 
                 tiempo_simulacion : float,
                 estadisticas = Estadisticas(),
                 # Probando valores
                 #cajas = [Caja(1, 2, 3), Caja(2, 2, 5), Caja(3, 2, 5), Caja(4, 2, 4.5, is_activa=False)],
                 # Valores del ejercicio
                 cajas = [Caja(1, 1.5, 2.5), Caja(2, 2, 5), Caja(3, 2, 4), Caja(4, 2, 4.5, is_activa=False)],
                 tiempo_actual = 0,
                 fila_clientes = None,
                 ):
        self.tiempo_simulacion = tiempo_simulacion * 60 # Convertir a minutos
        self.tiempo_actual = tiempo_actual
        self.fila_clientes = fila_clientes
        self.cajas = cajas
        self.estadisticas = estadisticas
    
    def ejecutarSimulacion(self):
        fila_de_clientes = FilaClientes(30, 0, 0) # Máximo 30 clientes en fila
        generador = GenerardorLlegadas(1) # Tiempo medio de 1 minuto
        id_clientes = 0
        proxima_llegada = generador.generarProximaLlegada()

        while self.tiempo_actual < self.tiempo_simulacion:
                #print(fila_de_clientes.lenFila())

                self.gestionarCuartaCaja(fila_de_clientes.lenFila())

                self.procesarAtenciones()

                if self.tiempo_actual > proxima_llegada and fila_de_clientes.lenFila() < fila_de_clientes.len_max:
                        '''
                        Agrega un cliente nuevo
                        '''
                        id_clientes += 1
                        fila_de_clientes.agregarCliente(generador.crearCliente(id_clientes, self.tiempo_actual))

                        '''
                        Tiempo de nuevo cliente
                        '''
                        proxima_llegada = round(self.tiempo_actual + generador.generarProximaLlegada(), 1)
                        #print(proxima_llegada)
                '''
                Asignar caja a cliente
                '''
                if fila_de_clientes.lenFila() > 0:
                    caja_a_usar = self.obtenerCajaLibre()
                    if caja_a_usar is not None:
                        cliente_a_atender = fila_de_clientes.sacarCliente()
                        caja_a_usar.atenderCliente(cliente_a_atender, self.tiempo_actual)
                        self.estadisticas.agregarClienteAtendido(cliente_a_atender)
        
                # Aumentar el tiempo en 0.1 minutos
                self.tiempo_actual = round(self.tiempo_actual + 0.1, 1)

        self.estadisticas.actualizar_tiempo_espera_maximo()
        self.estadisticas.agregar_tiempo_cuarta_caja(self.cajas[3].tiempo_total_activa)
        self.estadisticas.actualizar_tiempo_espera_maximo()
        self.mostrar_resultados()

    def procesarLlegadas():
        pass
    
    def procesarAtenciones(self):
        cajas_atendiento = [caja for caja in self.cajas if caja.tieneCliente()]
        for caja in cajas_atendiento:
            if self.tiempo_actual > caja.tiempo_fin_atencion:
                caja.finalizar_atencion()


    def gestionarCuartaCaja(self, lenFila: int):
        if lenFila > 20:
            self.cajas[3].activar()
            #print('Cuarta caja activa')
            return
        self.cajas[3].desactivar()
            
    
    def obtenerCajaLibre(self) -> Caja:
        cajas_disponibles = [caja for caja in self.cajas if caja.estaActiva() and caja.estaLibre()]
        cantidad_disponibles = len(cajas_disponibles)
        #print(f'Cantidad de cajas disponibles: {cantidad_disponibles}')
        if cantidad_disponibles > 0:
            caja_a_usar = cajas_disponibles[random.randint(0, cantidad_disponibles - 1)]
            return caja_a_usar
        return None
    
    def mostrar_resultados(self):
        print('-' * 60)
        print(f'Simulación de {self.tiempo_simulacion} minutos')
        print('Unidades de tiempo en minutos')
        print('Clientes atendidos durante la simulación:\t', end="")
        print(self.estadisticas.obtener_clientes_atendidos())
        print('Tiempo de 4ta Caja:\t\t\t\t', end="")
        print(self.estadisticas.obtener_tiempo_cuarta_caja())
        print('Tiempo de espera promedio:\t\t\t', end="")
        print(self.estadisticas.calcular_tiempo_espera_promedio())
        print('Tiempo de espera máximo:\t\t\t', end="")
        print(self.estadisticas.obtener_tiempo_espera_maximo())
        print('-' * 60)

def main():
    simulacion = Simulador(7) # 7 horas
    simulacion.ejecutarSimulacion()

main()