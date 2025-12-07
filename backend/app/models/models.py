from typing import  List, Optional
from datetime import datetime
from sqlmodel import ARRAY,JSON, Column, Field, SQLModel, String, Integer, create_engine
from pydantic import BaseModel

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

# Pydantic models for nested structures (nie są tabelami w bazie)
class Link(BaseModel):
    href: str
    rel: str

class Voting(BaseModel):
    abstain: Optional[int] = None
    date: Optional[datetime] = None
    description: Optional[str] = None
    kind: Optional[str] = None
    links: Optional[List[Link]] = None
    majorityType: Optional[str] = None
    majorityVotes: Optional[int] = None
    no: Optional[int] = None
    notParticipating: Optional[int] = None
    present: Optional[int] = None
    sitting: Optional[int] = None
    sittingDay: Optional[int] = None
    term: Optional[int] = None
    title: Optional[str] = None
    totalVoted: Optional[int] = None
    votingNumber: Optional[int] = None
    yes: Optional[int] = None

class StageChild(BaseModel):
    date: Optional[datetime] = None
    stageName: Optional[str] = None
    committeeCode: Optional[str] = None
    stageType: Optional[str] = None
    type: Optional[str] = None
    voting: Optional[Voting] = None

class Stage(BaseModel):
    date: Optional[datetime] = None
    stageName: Optional[str] = None
    printNumber: Optional[str] = None
    stageType: Optional[str] = None
    decision: Optional[str] = None
    sittingNum: Optional[int] = None
    children: Optional[List[StageChild]] = None

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

class LegislationAct(SQLModel, table=True):
    __tablename__ = "legislation_acts"

    id: int = Field(sa_column_kwargs={"name": "id_serial"}, primary_key=True)
    title: str
    applicant: Optional[str]
    number: Optional[str]
    date_created: Optional[datetime]
    date_modified: Optional[datetime]
    link: str = Field(unique=True)
    status: Optional[str]
    category_id: int
