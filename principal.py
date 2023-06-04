from BD.conexion import DAO
import funciones

def pintarMenuPrincipal():
  continuar = True
  while continuar:
    opcionCorrecta = False
    if not opcionCorrecta:
      print("================ MENÚ PRINCIPAL ================")
      print("1·- Listar cursos")
      print("2·- Agregar curso")
      print("3·- Actualizar cursos")
      print("4·- Eliminar curso")
      print("5·- Salir")
      print("================================================")

      opcion = int(input("Seleccione una opción: "))
      print("")

      if opcion < 1 or opcion > 5:
        print("Opción incorrecta, ingrese de nuevo\n")
      elif opcion == 5:
        continuar = False
        print("¡Gracias por usar el sistema!")
        break
      else:
        opcionCorrecta = True
        ejecutarOpcion(opcion) 

def ejecutarOpcion(opcion):
  dao = DAO()

  # 1·- Listar cursos
  if opcion == 1:
    cursos = dao.listarCursos()
    if len(cursos) > 0:
      funciones.listarCursos(cursos)
    else:
      print("No se encontraron cursos")

  # 2·- Agregar curso
  elif opcion == 2:
    curso = funciones.pedirDatosRegistro()
    try:
      dao.agregarCurso(curso)
    except:
      print("¡Ha ocurrido un error!")

  # 3·- Actualizar cursos
  elif opcion == 3:
    try:
      cursos = dao.listarCursos()
      if len(cursos) > 0:
        curso = funciones.pedirDatosActualizacion(cursos)
        if not curso == None:
          dao.actualizarCurso(curso)
        else:
          print("No se encontró ningún curso\n")
      else:
        print("No se encontraron cursos")
    except:
      print("¡Ha ocurrido un error!")

  # 4·- Eliminar curso
  elif opcion == 4:
    try:
      cursos = dao.listarCursos()
      if len(cursos) > 0:
        codigoCurso = funciones.pedirDatosEliminacion(cursos)
        if not codigoCurso == "":
          dao.eliminarCurso(codigoCurso)
        else:
          print("No se encontró ningún curso\n")
      else:
        print("No se encontraron cursos")
    except:
      print("¡Ha ocurrido un error!")

  # 5·- Opción Incorrecta
  else:
    print("¡Opción Incorrecta!")


pintarMenuPrincipal()