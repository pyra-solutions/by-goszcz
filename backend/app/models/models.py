from typing import Optional
from datetime import date
from sqlmodel import Field, SQLModel


class ActInfo(SQLModel, table=True):
    __tablename__ = "act_info"
    
    id: int = Field(sa_column_kwargs={"name": "id_serial"}, primary_key=True)
    address: Optional[str]
    publisher: Optional[str]
    year: Optional[int]
    volume: Optional[int]
    pos: Optional[int]
    title: Optional[str]
    display_address: Optional[str]
    promulgation: Optional[date]
    announcement_date: Optional[date]
    text_pdf: Optional[bool]
    text_html: Optional[bool]
    change_date: Optional[date]
    eli: Optional[str]
    type_: Optional[str]
    status: Optional[str]

    # additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)
