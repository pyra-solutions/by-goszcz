-- Table: public.status_dokumentu

-- DROP TABLE IF EXISTS public.status_dokumentu;

CREATE TABLE IF NOT EXISTS public.status_dokumentu
(
    id integer NOT NULL DEFAULT nextval('status_dokumentu_id_seq'::regclass),
    status character varying(128) COLLATE pg_catalog."default",
    CONSTRAINT status_dokumentu_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.status_dokumentu
    OWNER to db_admin;
