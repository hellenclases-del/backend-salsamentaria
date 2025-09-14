from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20))
    correo = Column(String(100))
    direccion = Column(String(150),nullable=False)
    fecha_registro = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


# Crear todas las tablas en la base de datos con las otras entidades