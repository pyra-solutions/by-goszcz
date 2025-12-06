-- Table: public.dziennik

-- DROP TABLE IF EXISTS public.dziennik;

CREATE TABLE IF NOT EXISTS public.dziennik
(
    id integer NOT NULL DEFAULT nextval('dziennik_id_seq'::regclass),
    status character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT dziennik_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.dziennik
    OWNER to db_admin;
