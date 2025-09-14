from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import settings

# Motor de conexión asincrónica
engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

# Sesiones
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependencia para usar en los endpoints
async def get_db():
    async with async_session() as session:
        yield session
