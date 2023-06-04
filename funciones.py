from tabulate import tabulate

def listarCursos(cursos):
  print(f"Cursos ({len(cursos)}):")

  print(tabulate(cursos, headers = ["#", "Código", "Nombre", "Créditos"], tablefmt = "grid", showindex = range(1, len(cursos) + 1)))

  print("")

def pedirDatosRegistro():
  codigo    = input("Ingrese el código: ")
  nombre    = input("Ingrese el nombre: ")
  creditos  = int(input("Ingrese los créditos: ")) 

  return (codigo, nombre, creditos)

def pedirDatosActualizacion(cursos):
  listarCursos(cursos)

  codigo = input("Ingrese el código del curso a editar: ")

  codigoExiste = False
  for curso in cursos:
    if curso[0] == int(codigo):
      codigoExiste = True
      break

  if not codigoExiste:
    return None
  
  nombre    = input("Ingrese el nombre: ")
  creditos  = int(input("Ingrese los créditos: ")) 

  return (codigo, nombre, creditos)
  
def pedirDatosEliminacion(cursos):
  listarCursos(cursos)

  codigo = input("Ingrese el código del curso a eliminar: ")

  codigoExiste = False
  for curso in cursos:
    if curso[0] == int(codigo):
      codigoExiste = True
      break

  return codigo if codigoExiste else ""