-- Table: public.main

-- DROP TABLE IF EXISTS public.main;

CREATE TABLE IF NOT EXISTS public.main
(
    id integer NOT NULL DEFAULT nextval('main_id_seq'::regclass),
    status_dokumentu_id integer,
    typ_dokumentu_id integer,
    wnioskodawca_id integer,
    tytul text COLLATE pg_catalog."default",
    data_dokumentu date,
    file_path text COLLATE pg_catalog."default",
    api_address text COLLATE pg_catalog."default",
    CONSTRAINT main_pkey PRIMARY KEY (id),
    CONSTRAINT fk_status FOREIGN KEY (status_dokumentu_id)
        REFERENCES public.status_dokumentu (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_typ FOREIGN KEY (typ_dokumentu_id)
        REFERENCES public.typ_dokumentu (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_wnioskodawca FOREIGN KEY (wnioskodawca_id)
        REFERENCES public.wnioskodawca (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.main
    OWNER to db_admin;
