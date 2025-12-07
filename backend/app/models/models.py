from typing import  List, Optional
from datetime import datetime
from sqlmodel import ARRAY,JSON, Column, Field, SQLModel, String, Integer, create_engine


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

class ResponseProcesses(SQLModel, table=True):
    __tablename__ = "response_processes"


    id: int = Field(sa_column_kwargs={"name": "id_serial"}, primary_key=True)
    eli: str
    analysis: str


class Consultation(SQLModel, table=True):
    __tablename__ = "consultations"

    id: int = Field(primary_key=True)
    publisher: str
    project_name: str
    description: str
    status: str # "finished"|"in_progress"
    submission_date: datetime
    start_date: datetime
    end_date: datetime

    consultation_id: str # RPW/34467/2025

    project_pos: Optional[int]
    poll_amount: Optional[int]


class Comment(SQLModel, table=True):
    __tablename__ = "comments"

    id: int = Field(primary_key=True)
    consultation_id: str
    question: str
    comment_text: str
    author: str
    poll_number: str

class ProcessDetails(SQLModel, table=True):
    __tablename__ = "process_details"

    id: int = Field(sa_column_kwargs={"name": "id_serial"}, primary_key=True)
    term: Optional[int]
    number: Optional[str]
    title: Optional[str]
    description: Optional[str]
    u_e: Optional[str]
    document_date: Optional[datetime]
    change_date: Optional[datetime]
    web_generated_date: Optional[datetime]
    process_start_date: Optional[datetime]
    document_type: Optional[str]
    document_type_enum: Optional[str]
    comments: Optional[str]
    prints_considered_jointly: List[str] = Field(default=None, sa_column=Column(ARRAY(String())))
    title_final: Optional[str]
    closure_date: Optional[datetime]
    address: Optional[str]
    display_address: Optional[str]
    e_li: Optional[str]
    passed: Optional[bool]
    shorten_procedure: Optional[bool]
    urgency_status: Optional[str]
    urgency_withdraw_date: Optional[datetime]
    rcl_num: Optional[str]
    rcl_link: Optional[str]
    legislative_committee: Optional[bool]
    principle_of_subsidiarity: Optional[bool]
    links: Optional[List[dict]] = Field(default=None, sa_column=Column(JSON))
    stages: Optional[List[dict]] = Field(default=None, sa_column=Column(JSON))
    other_documents: Optional[List[dict]] = Field(default=None, sa_column=Column(JSON))
