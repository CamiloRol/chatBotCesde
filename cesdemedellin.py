from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy.orm import sessionmaker, relationship;

# Datos de conexión
server = '401-02'
database = 'cesdemedellin'
username = 'cesde_crud_9'
password = 'cesde_crud'
driver = 'ODBC Driver 17 for SQL Server'

# Crear conexión
engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}')
Base = declarative_base()

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()
class SedeMedellin(Base):
    __tablename__ = 'sedeMedellin'
    id_sede = Column(Integer, primary_key=True)
    direccion = Column(String(100))
    horarios = Column(DateTime)

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    id_sede = Column(Integer, ForeignKey('sedeMedellin.id_sede'))
    correo_electronico = Column(String(100))
    nombre_usuario = Column(String(75))
    telefono = Column(Integer)
    sede = relationship("SedeMedellin")

class Preguntas(Base):
    __tablename__ = 'preguntas'
    id_pregunta = Column(Integer, primary_key=True, autoincrement=True)
    tipo_pregunta = Column(String(75))
    total_preguntas = Column(String(300))
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    usuario = relationship("Usuarios")

class Respuestas(Base):
    __tablename__ = 'respuestas'
    id_respuesta = Column(Integer, primary_key=True, autoincrement=True)
    id_pregunta = Column(Integer, ForeignKey('preguntas.id_pregunta'))
    total_respuestas = Column(String(300))
    pregunta = relationship("Preguntas")

class PreguntasUsuarios(Base):
    __tablename__ = 'preguntas_usuarios'
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), primary_key=True)
    id_pregunta = Column(Integer, ForeignKey('preguntas.id_pregunta'), primary_key=True)

class PreguntasRespuestas(Base):
    __tablename__ = 'preguntas_respuestas'
    id_pregunta = Column(Integer, ForeignKey('preguntas.id_pregunta'), primary_key=True)
    id_respuesta = Column(Integer, ForeignKey('respuestas.id_respuesta'), primary_key=True)

# Crear las tablas
Base.metadata.create_all(engine)
# Crear una nueva sede
def create_sede(id_sede, direccion, horarios):
    nueva_sede = SedeMedellin(id_sede=id_sede, direccion=direccion, horarios=horarios)
    session.add(nueva_sede)
    session.commit()

# Crear un nuevo usuario
def create_usuario(correo_electronico, nombre_usuario, telefono, id_sede):
    nuevo_usuario = Usuarios(correo_electronico=correo_electronico, nombre_usuario=nombre_usuario, telefono=telefono, id_sede=id_sede)
    session.add(nuevo_usuario)
    session.commit()

# Crear una nueva pregunta
def create_pregunta(tipo_pregunta, total_preguntas, id_usuario):
    nueva_pregunta = Preguntas(tipo_pregunta=tipo_pregunta, total_preguntas=total_preguntas, id_usuario=id_usuario)
    session.add(nueva_pregunta)
    session.commit()

# Crear una nueva respuesta
def create_respuesta(id_pregunta, total_respuestas):
    nueva_respuesta = Respuestas(id_pregunta=id_pregunta, total_respuestas=total_respuestas)
    session.add(nueva_respuesta)
    session.commit()

# Leer usuarios
def get_usuarios():
    return session.query(Usuarios).all()

# Actualizar un usuario
def update_usuario(id_usuario, correo_electronico=None, nombre_usuario=None, telefono=None):
    usuario = session.query(Usuarios).get(id_usuario)
    if correo_electronico:
        usuario.correo_electronico = correo_electronico
    if nombre_usuario:
        usuario.nombre_usuario = nombre_usuario
    if telefono:
        usuario.telefono = telefono
    session.commit()

# Eliminar un usuario
def delete_usuario(id_usuario):
    usuario = session.query(Usuarios).get(id_usuario)
    session.delete(usuario)
    session.commit()
