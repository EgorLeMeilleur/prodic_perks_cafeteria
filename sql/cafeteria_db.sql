--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: benefit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.benefit (
    id integer NOT NULL,
    name character varying NOT NULL,
    price money NOT NULL,
    city character varying NOT NULL
);


ALTER TABLE public.benefit OWNER TO postgres;

--
-- Name: benefit_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.benefit ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.benefit_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: benefits_of_employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.benefits_of_employee (
    bought_or_wished boolean NOT NULL,
    id_employee integer NOT NULL,
    id_benefit integer NOT NULL
);


ALTER TABLE public.benefits_of_employee OWNER TO postgres;

--
-- Name: COLUMN benefits_of_employee.bought_or_wished; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.benefits_of_employee.bought_or_wished IS 'true - bought, false - wished';


--
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    id integer NOT NULL,
    name character varying NOT NULL,
    login character varying NOT NULL,
    password character varying NOT NULL,
    "position" character varying NOT NULL,
    experience integer NOT NULL,
    balance money NOT NULL,
    city character varying NOT NULL
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- Name: employee_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.employee ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.employee_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: benefit; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: benefits_of_employee; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Name: benefit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.benefit_id_seq', 1, false);


--
-- Name: employee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.employee_id_seq', 1, false);


--
-- Name: benefit benefit_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.benefit
    ADD CONSTRAINT benefit_pk PRIMARY KEY (id);


--
-- Name: employee employee_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pk PRIMARY KEY (id);


--
-- Name: benefits_of_employee benefits_of_employee_benefit_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.benefits_of_employee
    ADD CONSTRAINT benefits_of_employee_benefit_id_fk FOREIGN KEY (id_benefit) REFERENCES public.benefit(id);


--
-- Name: benefits_of_employee benefits_of_employee_employee_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.benefits_of_employee
    ADD CONSTRAINT benefits_of_employee_employee_id_fk FOREIGN KEY (id_employee) REFERENCES public.employee(id);


--
-- PostgreSQL database dump complete
--

