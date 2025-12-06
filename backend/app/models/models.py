from typing import  List, Optional
from datetime import datetime
from sqlmodel import ARRAY, Column, Field, SQLModel, String


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
    promulgation: Optional[datetime]
    announcement_date: Optional[datetime]
    text_pdf: Optional[bool]
    text_html: Optional[bool]
    change_date: Optional[datetime]
    eli: Optional[str] = Field(sa_column=Column("eli", String, unique=True))
    act_type: Optional[str]
    status: Optional[str]

    # additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

class ProcessHeader(SQLModel, table=True):
    __tablename__ = "process_header"


    id: int = Field(sa_column_kwargs={"name": "id_serial"}, primary_key=True)
    u_e: Optional[str]
    e_li: Optional[str]
    term: Optional[int]
    number: Optional[str]
    title: Optional[str]
    title_final: Optional[str]
    description: Optional[str]
    ue: Optional[str]
    document_date: Optional[datetime]
    process_start_date: Optional[datetime]
    change_date: Optional[datetime]
    document_type: Optional[str]
    document_type_enum: Optional[str]
    comments: Optional[str]
    web_generated_date: Optional[datetime]
    closure_date: Optional[datetime]
    address: Optional[str]
    display_address: Optional[str]
    eli: Optional[str]
    passed: Optional[bool]
    links: List[str] = Field(default=None, sa_column=Column(ARRAY(String())))
    shorten_procedure: Optional[bool]
    urgency_status: Optional[str]
    urgency_withdraw_date: Optional[datetime]

class SubscriberList(SQLModel, table=True):
    __tablename__ = "subscriber_list"


    id: int = Field(sa_column_kwargs={"name": "id_serial"}, primary_key=True)
    email: str
    categories: List[str] = Field(default=None, sa_column=Column(ARRAY(String())))
    active: bool

class Response(SQLModel, table=True):
    __tablename__ = "response"

    id: int = Field(primary_key=True)
    eli: str
    title: str
    pos: int
    pdf_url: str
    analysis: str


