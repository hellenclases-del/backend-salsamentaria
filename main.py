from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Base, Cliente
from database import engine, get_db
from schemas import ClienteCreate, ClienteOut

app = FastAPI(title="API Salsamentaria - NyN")

# Crear tablas automáticamente en la BD
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Listar clientes
@app.get("/clientes", response_model=list[ClienteOut])
async def listar_clientes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Cliente))
    clientes = result.scalars().all()
    return clientes


# Crear cliente
@app.post("/clientes", response_model=ClienteOut)
async def crear_cliente(cliente: ClienteCreate, db: AsyncSession = Depends(get_db)):
    nuevo_cliente = Cliente(**cliente.dict())
    db.add(nuevo_cliente)
    await db.commit()
    await db.refresh(nuevo_cliente)
    return nuevo_cliente

# Actualizar cliente
@app.put("/clientes/{id_cliente}", response_model=ClienteOut)
async def actualizar_cliente(id_cliente: int, cliente: ClienteCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Cliente).where(Cliente.id_cliente == id_cliente))
    cliente_db = result.scalar_one_or_none()
    if not cliente_db:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    for key, value in cliente.dict().items():
        setattr(cliente_db, key, value)

    await db.commit()
    await db.refresh(cliente_db)
    return cliente_db

# Eliminar cliente
@app.delete("/clientes/{id_cliente}")
async def eliminar_cliente(id_cliente: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Cliente).where(Cliente.id_cliente == id_cliente))
    cliente_db = result.scalar_one_or_none()
    if not cliente_db:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    await db.delete(cliente_db)
    await db.commit()
    return {"detail": f"Cliente {id_cliente} eliminado correctamente"}