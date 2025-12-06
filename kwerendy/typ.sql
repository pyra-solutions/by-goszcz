-- Table: public.typ_dokumentu

-- DROP TABLE IF EXISTS public.typ_dokumentu;

CREATE TABLE IF NOT EXISTS public.typ_dokumentu
(
    id integer NOT NULL DEFAULT nextval('typ_dokumentu_id_seq'::regclass),
    status character varying(128) COLLATE pg_catalog."default",
    CONSTRAINT typ_dokumentu_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.typ_dokumentu
    OWNER to db_admin;
