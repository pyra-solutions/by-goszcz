from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class Main(SQLModel, table=True):
    __tablename__ = "main"
    
    id: int = Field(sa_column_kwargs={"name": "id_serial"}, primary_key=True)
    status_dokumentu_id: int = Field(foreign_key="status.id")
    typ_dokumentu_id: int
    wnioskodawca_id: int
    tytul: str
    data_dokumentu: datetime
    file_path: str
    api_address: Optional[str] = None



class StatusDokumentu(SQLModel, table=True):
    __tablename__ = "status_dokumentu"
    
    id: int = Field(sa_column_kwargs={"name": "id_serial"}, primary_key=True)
    status: str = Field(max_length=128)


class TypDokumentu(SQLModel, table=True):
    __tablename__ = "typ_dokumentu"
    
    id: int = Field(sa_column_kwargs={"name": "id_serial"}, primary_key=True)
    status: str = Field(max_length=128)



class Wnioskodawca(SQLModel, table=True):
    __tablename__ = "wnioskodawca"
    
    id: int = Field(sa_column_kwargs={"name": "id_serial"}, primary_key=True)
    status: str = Field(max_length=128)




