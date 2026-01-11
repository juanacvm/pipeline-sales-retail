from sqlalchemy import Column 
from sqlalchemy.types import Integer, Boolean, Float, NVARCHAR, DateTime
from sqlalchemy.orm import declarative_base 

Base = declarative_base()

#Crea la tabla ventas
class Sales(Base):
    __tablename__ = 'sales'

    transaction_id = Column(NVARCHAR(40), primary_key=True, autoincrement=False)
    customer_id = Column(NVARCHAR(100))
    category = Column(NVARCHAR(100))
    item = Column(NVARCHAR(100))
    price_per_unit = Column(Float)
    quantity = Column(Float)
    total_spent = Column(Float)
    payment_method = Column(NVARCHAR(100))
    location = Column(NVARCHAR(100))
    transaction_date = Column(DateTime)
    discount_applied = Column(Boolean)