-- Table: public.wnioskodawca

-- DROP TABLE IF EXISTS public.wnioskodawca;

CREATE TABLE IF NOT EXISTS public.wnioskodawca
(
    id integer NOT NULL DEFAULT nextval('wnioskodawca_id_seq'::regclass),
    status character varying(128) COLLATE pg_catalog."default",
    CONSTRAINT wnioskodawca_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.wnioskodawca
    OWNER to db_admin;
