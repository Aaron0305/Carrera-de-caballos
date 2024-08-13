class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def hash_function(self, date):
        day, month, year = map(int, date.split('/'))  # Suponiendo que la fecha es ingresada como 'día/mes/año'
        hash_key = ((day / month) / 2 ** 0.5) % self.size
        return int(hash_key)

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        found = False
        for index, element in enumerate(self.hash_table[hash_key]):
            if len(element) == 2 and element[0] == key:
                self.hash_table[hash_key][index] = (key, value)
                found = True
                break
        if not found:
            self.hash_table[hash_key].append((key, value))

    def get(self, key):
        hash_key = self.hash_function(key)
        for element in self.hash_table[hash_key]:
            if element[0] == key:
                return element[1]
        return None

    def display(self):
        print("Tabla Hash:")
        for index, items in enumerate(self.hash_table):
            print(f"Índice {index}: {items}")

# Función para el menú
def menu():
    print("\n----- Menú -----")
    print("1. Insertar datos")
    print("2. Mostrar tabla hash")
    print("3. Buscar valor por clave")
    print("4. Ingresar fecha de nacimiento")
    print("5. Salir")

# Creación de la tabla hash con tamaño proporcionado por el usuario
size = int(input("Ingrese el tamaño de la tabla hash: "))
hash_table = HashTable(size)

while True:
    menu()
    choice = input("Ingrese su elección: ")

    if choice == '1':
        key = int(input("Ingrese la clave: "))
        value = input("Ingrese el valor: ")
        hash_table.insert(key, value)
        print("Datos insertados exitosamente.")
    elif choice == '2':
        hash_table.display()
    elif choice == '3':
        search_key = int(input("Ingrese la clave para buscar su valor correspondiente: "))
        result = hash_table.get(search_key)
        if result is not None:
            print(f"El valor asociado a la clave {search_key} es: {result}")
        else:
            print(f"No se encontró ningún valor para la clave {search_key}")
    elif choice == '4':
        birth_date = input("Ingrese su fecha de nacimiento (día/mes/año): ")
        hash_key = hash_table.hash_function(birth_date)
        print(f"La clave hash para la fecha {birth_date} es: {hash_key}")
    elif choice == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")