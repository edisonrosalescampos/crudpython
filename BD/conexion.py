import mysql.connector

class DAO:
  def __init__(self):
    try:
      self.conexion = mysql.connector.connect(
        host      = "localhost",
        port      = 3306,
        user      = "root",
        password  = "",
        database  = "crudpython"
      )
      self.cursor = self.conexion.cursor()
    except mysql.connector.Error as e:
      print("Error al conectarse SGBD", e)

  def listarCursos(self):
    if self.conexion.is_connected():
      try:
        self.cursor.execute("SELECT * FROM `cursos` ORDER BY `codigo` ASC")
        result = self.cursor.fetchall()
        return result
      except mysql.connector.Error as e:
        print("Error al relizar consulta:", e)

  def agregarCurso(self, curso):
    if self.conexion.is_connected():
      try:
        self.cursor.execute("INSERT INTO `cursos` (`codigo`, `nombre`, `creditos`) VALUES (%s, %s, %s)", curso)
        self.conexion.commit()
        self.conexion.close()
        print("¡Curso registrado exitosamente!\n")
      except mysql.connector.Error as e:
        print("Error al relizar consulta:", e)

  def actualizarCurso(self, curso):
    if self.conexion.is_connected():
      try:
        self.cursor.execute(f"UPDATE `cursos` SET `nombre` = '{curso[1]}', `creditos` = '{curso[2]}' WHERE `codigo` = '{curso[0]}'")
        self.conexion.commit()
        self.conexion.close()
        print("¡Curso actualizado exitosamente!\n")
      except mysql.connector.Error as e:
        print("Error al relizar consulta:", e)

  def eliminarCurso(self, codigoCurso):
    if self.conexion.is_connected():
      try:
        self.cursor.execute(f"DELETE FROM `cursos` WHERE `codigo` = '{codigoCurso}'")
        self.conexion.commit()
        self.conexion.close()
        print("¡Curso eliminado exitosamente!\n")
      except mysql.connector.Error as e:
        print("Error al relizar consulta:", e)
