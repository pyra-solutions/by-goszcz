from typing import Optional
from sqlmodel import Field, SQLModel


# ============================================================
# dziennik
# ============================================================

class DziennikBase(SQLModel):
    status: Optional[str] = None


class Dziennik(DziennikBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class DziennikCreate(DziennikBase):
    pass


class DziennikRead(DziennikBase):
    id: int


class DziennikUpdate(SQLModel):
    status: Optional[str] = None


# ============================================================
# status_dokumentu
# ============================================================

class StatusDokumentuBase(SQLModel):
    status: Optional[str] = None


class StatusDokumentu(StatusDokumentuBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class StatusDokumentuCreate(StatusDokumentuBase):
    pass


class StatusDokumentuRead(StatusDokumentuBase):
    id: int


class StatusDokumentuUpdate(SQLModel):
    status: Optional[str] = None


# ============================================================
# typ_dokumentu
# ============================================================

class TypDokumentuBase(SQLModel):
    status: Optional[str] = None


class TypDokumentu(TypDokumentuBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TypDokumentuCreate(TypDokumentuBase):
    pass


class TypDokumentuRead(TypDokumentuBase):
    id: int


class TypDokumentuUpdate(SQLModel):
    status: Optional[str] = None


# ============================================================
# wnioskodawca
# ============================================================

class WnioskodawcaBase(SQLModel):
    status: Optional[str] = None


class Wnioskodawca(WnioskodawcaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class WnioskodawcaCreate(WnioskodawcaBase):
    pass


class WnioskodawcaRead(WnioskodawcaBase):
    id: int


class WnioskodawcaUpdate(SQLModel):
    status: Optional[str] = None


# ============================================================
# main
# ============================================================

class MainBase(SQLModel):
    status_dokumentu_id: Optional[int] = Field(default=None, foreign_key="status_dokumentu.id")
    typ_dokumentu_id: Optional[int] = Field(default=None, foreign_key="typ_dokumentu.id")
    wnioskodawca_id: Optional[int] = Field(default=None, foreign_key="wnioskodawca.id")
    tytul: Optional[str] = None
    data_dokumentu: Optional[str] = None   # or date if using Python date type
    file_path: Optional[str] = None
    api_address: Optional[str] = None


class Main(MainBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class MainCreate(MainBase):
    pass


class MainRead(MainBase):
    id: int


class MainUpdate(SQLModel):
    status_dokumentu_id: Optional[int] = None
    typ_dokumentu_id: Optional[int] = None
    wnioskodawca_id: Optional[int] = None
    tytul: Optional[str] = None
    data_dokumentu: Optional[str] = None
    file_path: Optional[str] = None
    api_address: Optional[str] = None

