toc.dat                                                                                             0000600 0004000 0002000 00000061543 14621577323 0014462 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP       5                |            SMAN3    16.2    16.2 S    I           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         J           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false         K           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false         L           1262    41804    SMAN3    DATABASE     ~   CREATE DATABASE "SMAN3" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
    DROP DATABASE "SMAN3";
                postgres    false         �            1259    41809    admin    TABLE     �   CREATE TABLE public.admin (
    id_admin integer NOT NULL,
    nama_admin character varying(100) NOT NULL,
    username character varying(50) NOT NULL,
    password character varying(50) NOT NULL
);
    DROP TABLE public.admin;
       public         heap    postgres    false         �            1259    41808    admin_id_admin_seq    SEQUENCE     �   CREATE SEQUENCE public.admin_id_admin_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.admin_id_admin_seq;
       public          postgres    false    216         M           0    0    admin_id_admin_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.admin_id_admin_seq OWNED BY public.admin.id_admin;
          public          postgres    false    215         �            1259    41892    alamat    TABLE       CREATE TABLE public.alamat (
    id_alamat integer NOT NULL,
    provinsi character varying(30) NOT NULL,
    kabupatenkota character varying(30) NOT NULL,
    kecamatan character varying(30) NOT NULL,
    jalan character varying(60) NOT NULL,
    detail character varying(60)
);
    DROP TABLE public.alamat;
       public         heap    postgres    false         �            1259    41891    alamat_id_alamat_seq    SEQUENCE     �   CREATE SEQUENCE public.alamat_id_alamat_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.alamat_id_alamat_seq;
       public          postgres    false    228         N           0    0    alamat_id_alamat_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.alamat_id_alamat_seq OWNED BY public.alamat.id_alamat;
          public          postgres    false    227         �            1259    41853    guru    TABLE     _  CREATE TABLE public.guru (
    id_guru integer NOT NULL,
    nama_guru character varying(100) NOT NULL,
    no_telp character varying(13) NOT NULL,
    jenis_kelamin character varying(15) NOT NULL,
    id_pelajaran integer,
    id_alamat integer,
    id_admin integer,
    status boolean,
    deskripsi text,
    nip character varying(18) NOT NULL
);
    DROP TABLE public.guru;
       public         heap    postgres    false         �            1259    41852    guru_id_guru_seq    SEQUENCE     �   CREATE SEQUENCE public.guru_id_guru_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.guru_id_guru_seq;
       public          postgres    false    220         O           0    0    guru_id_guru_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.guru_id_guru_seq OWNED BY public.guru.id_guru;
          public          postgres    false    219         �            1259    41871    jadwal_pelajaran    TABLE        CREATE TABLE public.jadwal_pelajaran (
    id_jadwal integer NOT NULL,
    hari character varying(50) NOT NULL,
    awal_pelajaran time without time zone NOT NULL,
    akhir_pelajaran time without time zone NOT NULL,
    id_guru integer,
    id_pelajaran integer,
    id_kelas integer
);
 $   DROP TABLE public.jadwal_pelajaran;
       public         heap    postgres    false         �            1259    41870    jadwal_pelajaran_id_jadwal_seq    SEQUENCE     �   CREATE SEQUENCE public.jadwal_pelajaran_id_jadwal_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.jadwal_pelajaran_id_jadwal_seq;
       public          postgres    false    222         P           0    0    jadwal_pelajaran_id_jadwal_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.jadwal_pelajaran_id_jadwal_seq OWNED BY public.jadwal_pelajaran.id_jadwal;
          public          postgres    false    221         �            1259    42323    jenis_tugas    TABLE     s   CREATE TABLE public.jenis_tugas (
    id_tugas integer NOT NULL,
    jenis_tugas character varying(60) NOT NULL
);
    DROP TABLE public.jenis_tugas;
       public         heap    postgres    false         �            1259    42322    jenis_tugas_id_tugas_seq    SEQUENCE     �   CREATE SEQUENCE public.jenis_tugas_id_tugas_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.jenis_tugas_id_tugas_seq;
       public          postgres    false    230         Q           0    0    jenis_tugas_id_tugas_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.jenis_tugas_id_tugas_seq OWNED BY public.jenis_tugas.id_tugas;
          public          postgres    false    229         �            1259    41878    kelas    TABLE     g   CREATE TABLE public.kelas (
    id_kelas integer NOT NULL,
    kelas character varying(30) NOT NULL
);
    DROP TABLE public.kelas;
       public         heap    postgres    false         �            1259    41877    kelas_id_kelas_seq    SEQUENCE     �   CREATE SEQUENCE public.kelas_id_kelas_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.kelas_id_kelas_seq;
       public          postgres    false    224         R           0    0    kelas_id_kelas_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.kelas_id_kelas_seq OWNED BY public.kelas.id_kelas;
          public          postgres    false    223         �            1259    42353    mata_pelajaran    TABLE     �   CREATE TABLE public.mata_pelajaran (
    id_pelajaran integer NOT NULL,
    kode_pelajaran character varying(5) NOT NULL,
    nama_pelajaran character varying(50) NOT NULL,
    semester integer NOT NULL
);
 "   DROP TABLE public.mata_pelajaran;
       public         heap    postgres    false         �            1259    42352    mata_pelajaran_id_pelajaran_seq    SEQUENCE     �   CREATE SEQUENCE public.mata_pelajaran_id_pelajaran_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.mata_pelajaran_id_pelajaran_seq;
       public          postgres    false    232         S           0    0    mata_pelajaran_id_pelajaran_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.mata_pelajaran_id_pelajaran_seq OWNED BY public.mata_pelajaran.id_pelajaran;
          public          postgres    false    231         �            1259    41885    nilai_siswa    TABLE     �   CREATE TABLE public.nilai_siswa (
    id_nilai_siswa integer NOT NULL,
    nilai_tugas integer NOT NULL,
    id_guru integer,
    id_siswa integer,
    id_tugas integer
);
    DROP TABLE public.nilai_siswa;
       public         heap    postgres    false         �            1259    41884    nilai_siswa_id_nilai_siswa_seq    SEQUENCE     �   CREATE SEQUENCE public.nilai_siswa_id_nilai_siswa_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.nilai_siswa_id_nilai_siswa_seq;
       public          postgres    false    226         T           0    0    nilai_siswa_id_nilai_siswa_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.nilai_siswa_id_nilai_siswa_seq OWNED BY public.nilai_siswa.id_nilai_siswa;
          public          postgres    false    225         �            1259    41837    siswa    TABLE     �  CREATE TABLE public.siswa (
    id_siswa integer NOT NULL,
    nisn character varying(10) NOT NULL,
    nama_siswa character varying(100) NOT NULL,
    no_telp character varying(13) NOT NULL,
    tahun_angkatan integer NOT NULL,
    tgl_lahir date NOT NULL,
    tempat_lahir character varying(50) NOT NULL,
    jenis_kelamin character varying(15) NOT NULL,
    id_alamat integer,
    id_kelas integer,
    id_admin integer,
    status boolean NOT NULL,
    deskripsi text
);
    DROP TABLE public.siswa;
       public         heap    postgres    false         �            1259    41836    siswa_id_siswa_seq    SEQUENCE     �   CREATE SEQUENCE public.siswa_id_siswa_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.siswa_id_siswa_seq;
       public          postgres    false    218         U           0    0    siswa_id_siswa_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.siswa_id_siswa_seq OWNED BY public.siswa.id_siswa;
          public          postgres    false    217         x           2604    41812    admin id_admin    DEFAULT     p   ALTER TABLE ONLY public.admin ALTER COLUMN id_admin SET DEFAULT nextval('public.admin_id_admin_seq'::regclass);
 =   ALTER TABLE public.admin ALTER COLUMN id_admin DROP DEFAULT;
       public          postgres    false    215    216    216         ~           2604    41895    alamat id_alamat    DEFAULT     t   ALTER TABLE ONLY public.alamat ALTER COLUMN id_alamat SET DEFAULT nextval('public.alamat_id_alamat_seq'::regclass);
 ?   ALTER TABLE public.alamat ALTER COLUMN id_alamat DROP DEFAULT;
       public          postgres    false    227    228    228         z           2604    41856    guru id_guru    DEFAULT     l   ALTER TABLE ONLY public.guru ALTER COLUMN id_guru SET DEFAULT nextval('public.guru_id_guru_seq'::regclass);
 ;   ALTER TABLE public.guru ALTER COLUMN id_guru DROP DEFAULT;
       public          postgres    false    219    220    220         {           2604    41874    jadwal_pelajaran id_jadwal    DEFAULT     �   ALTER TABLE ONLY public.jadwal_pelajaran ALTER COLUMN id_jadwal SET DEFAULT nextval('public.jadwal_pelajaran_id_jadwal_seq'::regclass);
 I   ALTER TABLE public.jadwal_pelajaran ALTER COLUMN id_jadwal DROP DEFAULT;
       public          postgres    false    222    221    222                    2604    42326    jenis_tugas id_tugas    DEFAULT     |   ALTER TABLE ONLY public.jenis_tugas ALTER COLUMN id_tugas SET DEFAULT nextval('public.jenis_tugas_id_tugas_seq'::regclass);
 C   ALTER TABLE public.jenis_tugas ALTER COLUMN id_tugas DROP DEFAULT;
       public          postgres    false    230    229    230         |           2604    41881    kelas id_kelas    DEFAULT     p   ALTER TABLE ONLY public.kelas ALTER COLUMN id_kelas SET DEFAULT nextval('public.kelas_id_kelas_seq'::regclass);
 =   ALTER TABLE public.kelas ALTER COLUMN id_kelas DROP DEFAULT;
       public          postgres    false    224    223    224         �           2604    42356    mata_pelajaran id_pelajaran    DEFAULT     �   ALTER TABLE ONLY public.mata_pelajaran ALTER COLUMN id_pelajaran SET DEFAULT nextval('public.mata_pelajaran_id_pelajaran_seq'::regclass);
 J   ALTER TABLE public.mata_pelajaran ALTER COLUMN id_pelajaran DROP DEFAULT;
       public          postgres    false    232    231    232         }           2604    41888    nilai_siswa id_nilai_siswa    DEFAULT     �   ALTER TABLE ONLY public.nilai_siswa ALTER COLUMN id_nilai_siswa SET DEFAULT nextval('public.nilai_siswa_id_nilai_siswa_seq'::regclass);
 I   ALTER TABLE public.nilai_siswa ALTER COLUMN id_nilai_siswa DROP DEFAULT;
       public          postgres    false    226    225    226         y           2604    41840    siswa id_siswa    DEFAULT     p   ALTER TABLE ONLY public.siswa ALTER COLUMN id_siswa SET DEFAULT nextval('public.siswa_id_siswa_seq'::regclass);
 =   ALTER TABLE public.siswa ALTER COLUMN id_siswa DROP DEFAULT;
       public          postgres    false    217    218    218         6          0    41809    admin 
   TABLE DATA           I   COPY public.admin (id_admin, nama_admin, username, password) FROM stdin;
    public          postgres    false    216       4918.dat B          0    41892    alamat 
   TABLE DATA           ^   COPY public.alamat (id_alamat, provinsi, kabupatenkota, kecamatan, jalan, detail) FROM stdin;
    public          postgres    false    228       4930.dat :          0    41853    guru 
   TABLE DATA           �   COPY public.guru (id_guru, nama_guru, no_telp, jenis_kelamin, id_pelajaran, id_alamat, id_admin, status, deskripsi, nip) FROM stdin;
    public          postgres    false    220       4922.dat <          0    41871    jadwal_pelajaran 
   TABLE DATA           }   COPY public.jadwal_pelajaran (id_jadwal, hari, awal_pelajaran, akhir_pelajaran, id_guru, id_pelajaran, id_kelas) FROM stdin;
    public          postgres    false    222       4924.dat D          0    42323    jenis_tugas 
   TABLE DATA           <   COPY public.jenis_tugas (id_tugas, jenis_tugas) FROM stdin;
    public          postgres    false    230       4932.dat >          0    41878    kelas 
   TABLE DATA           0   COPY public.kelas (id_kelas, kelas) FROM stdin;
    public          postgres    false    224       4926.dat F          0    42353    mata_pelajaran 
   TABLE DATA           `   COPY public.mata_pelajaran (id_pelajaran, kode_pelajaran, nama_pelajaran, semester) FROM stdin;
    public          postgres    false    232       4934.dat @          0    41885    nilai_siswa 
   TABLE DATA           _   COPY public.nilai_siswa (id_nilai_siswa, nilai_tugas, id_guru, id_siswa, id_tugas) FROM stdin;
    public          postgres    false    226       4928.dat 8          0    41837    siswa 
   TABLE DATA           �   COPY public.siswa (id_siswa, nisn, nama_siswa, no_telp, tahun_angkatan, tgl_lahir, tempat_lahir, jenis_kelamin, id_alamat, id_kelas, id_admin, status, deskripsi) FROM stdin;
    public          postgres    false    218       4920.dat V           0    0    admin_id_admin_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.admin_id_admin_seq', 3, true);
          public          postgres    false    215         W           0    0    alamat_id_alamat_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.alamat_id_alamat_seq', 6, true);
          public          postgres    false    227         X           0    0    guru_id_guru_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.guru_id_guru_seq', 3, true);
          public          postgres    false    219         Y           0    0    jadwal_pelajaran_id_jadwal_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.jadwal_pelajaran_id_jadwal_seq', 3, true);
          public          postgres    false    221         Z           0    0    jenis_tugas_id_tugas_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.jenis_tugas_id_tugas_seq', 3, true);
          public          postgres    false    229         [           0    0    kelas_id_kelas_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.kelas_id_kelas_seq', 4, true);
          public          postgres    false    223         \           0    0    mata_pelajaran_id_pelajaran_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.mata_pelajaran_id_pelajaran_seq', 3, true);
          public          postgres    false    231         ]           0    0    nilai_siswa_id_nilai_siswa_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.nilai_siswa_id_nilai_siswa_seq', 3, true);
          public          postgres    false    225         ^           0    0    siswa_id_siswa_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.siswa_id_siswa_seq', 3, true);
          public          postgres    false    217         �           2606    41814    admin admin_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (id_admin);
 :   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_pkey;
       public            postgres    false    216         �           2606    41897    alamat alamat_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.alamat
    ADD CONSTRAINT alamat_pkey PRIMARY KEY (id_alamat);
 <   ALTER TABLE ONLY public.alamat DROP CONSTRAINT alamat_pkey;
       public            postgres    false    228         �           2606    41858    guru guru_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.guru
    ADD CONSTRAINT guru_pkey PRIMARY KEY (id_guru);
 8   ALTER TABLE ONLY public.guru DROP CONSTRAINT guru_pkey;
       public            postgres    false    220         �           2606    41876 &   jadwal_pelajaran jadwal_pelajaran_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.jadwal_pelajaran
    ADD CONSTRAINT jadwal_pelajaran_pkey PRIMARY KEY (id_jadwal);
 P   ALTER TABLE ONLY public.jadwal_pelajaran DROP CONSTRAINT jadwal_pelajaran_pkey;
       public            postgres    false    222         �           2606    42330 '   jenis_tugas jenis_tugas_jenis_tugas_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.jenis_tugas
    ADD CONSTRAINT jenis_tugas_jenis_tugas_key UNIQUE (jenis_tugas);
 Q   ALTER TABLE ONLY public.jenis_tugas DROP CONSTRAINT jenis_tugas_jenis_tugas_key;
       public            postgres    false    230         �           2606    42328    jenis_tugas jenis_tugas_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.jenis_tugas
    ADD CONSTRAINT jenis_tugas_pkey PRIMARY KEY (id_tugas);
 F   ALTER TABLE ONLY public.jenis_tugas DROP CONSTRAINT jenis_tugas_pkey;
       public            postgres    false    230         �           2606    41883    kelas kelas_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.kelas
    ADD CONSTRAINT kelas_pkey PRIMARY KEY (id_kelas);
 :   ALTER TABLE ONLY public.kelas DROP CONSTRAINT kelas_pkey;
       public            postgres    false    224         �           2606    42360 0   mata_pelajaran mata_pelajaran_kode_pelajaran_key 
   CONSTRAINT     u   ALTER TABLE ONLY public.mata_pelajaran
    ADD CONSTRAINT mata_pelajaran_kode_pelajaran_key UNIQUE (kode_pelajaran);
 Z   ALTER TABLE ONLY public.mata_pelajaran DROP CONSTRAINT mata_pelajaran_kode_pelajaran_key;
       public            postgres    false    232         �           2606    42358 "   mata_pelajaran mata_pelajaran_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.mata_pelajaran
    ADD CONSTRAINT mata_pelajaran_pkey PRIMARY KEY (id_pelajaran);
 L   ALTER TABLE ONLY public.mata_pelajaran DROP CONSTRAINT mata_pelajaran_pkey;
       public            postgres    false    232         �           2606    41890    nilai_siswa nilai_siswa_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.nilai_siswa
    ADD CONSTRAINT nilai_siswa_pkey PRIMARY KEY (id_nilai_siswa);
 F   ALTER TABLE ONLY public.nilai_siswa DROP CONSTRAINT nilai_siswa_pkey;
       public            postgres    false    226         �           2606    42372    siswa siswa_nisn_key 
   CONSTRAINT     O   ALTER TABLE ONLY public.siswa
    ADD CONSTRAINT siswa_nisn_key UNIQUE (nisn);
 >   ALTER TABLE ONLY public.siswa DROP CONSTRAINT siswa_nisn_key;
       public            postgres    false    218         �           2606    41842    siswa siswa_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.siswa
    ADD CONSTRAINT siswa_pkey PRIMARY KEY (id_siswa);
 :   ALTER TABLE ONLY public.siswa DROP CONSTRAINT siswa_pkey;
       public            postgres    false    218         �           1259    42341    fki_fk_adminguru    INDEX     E   CREATE INDEX fki_fk_adminguru ON public.guru USING btree (id_admin);
 $   DROP INDEX public.fki_fk_adminguru;
       public            postgres    false    220         �           2606    42342    guru fk_adminguru    FK CONSTRAINT     w   ALTER TABLE ONLY public.guru
    ADD CONSTRAINT fk_adminguru FOREIGN KEY (id_admin) REFERENCES public.admin(id_admin);
 ;   ALTER TABLE ONLY public.guru DROP CONSTRAINT fk_adminguru;
       public          postgres    false    216    4738    220         �           2606    42347    siswa fk_adminsiswa    FK CONSTRAINT     y   ALTER TABLE ONLY public.siswa
    ADD CONSTRAINT fk_adminsiswa FOREIGN KEY (id_admin) REFERENCES public.admin(id_admin);
 =   ALTER TABLE ONLY public.siswa DROP CONSTRAINT fk_adminsiswa;
       public          postgres    false    216    4738    218         �           2606    41911    guru fk_alamatguru    FK CONSTRAINT     {   ALTER TABLE ONLY public.guru
    ADD CONSTRAINT fk_alamatguru FOREIGN KEY (id_alamat) REFERENCES public.alamat(id_alamat);
 <   ALTER TABLE ONLY public.guru DROP CONSTRAINT fk_alamatguru;
       public          postgres    false    228    220    4753         �           2606    41921    siswa fk_alamatsiswa    FK CONSTRAINT     }   ALTER TABLE ONLY public.siswa
    ADD CONSTRAINT fk_alamatsiswa FOREIGN KEY (id_alamat) REFERENCES public.alamat(id_alamat);
 >   ALTER TABLE ONLY public.siswa DROP CONSTRAINT fk_alamatsiswa;
       public          postgres    false    4753    218    228         �           2606    41931    jadwal_pelajaran fk_jadwalguru    FK CONSTRAINT     �   ALTER TABLE ONLY public.jadwal_pelajaran
    ADD CONSTRAINT fk_jadwalguru FOREIGN KEY (id_guru) REFERENCES public.guru(id_guru);
 H   ALTER TABLE ONLY public.jadwal_pelajaran DROP CONSTRAINT fk_jadwalguru;
       public          postgres    false    4745    222    220         �           2606    41941    jadwal_pelajaran fk_jadwalkelas    FK CONSTRAINT     �   ALTER TABLE ONLY public.jadwal_pelajaran
    ADD CONSTRAINT fk_jadwalkelas FOREIGN KEY (id_kelas) REFERENCES public.kelas(id_kelas);
 I   ALTER TABLE ONLY public.jadwal_pelajaran DROP CONSTRAINT fk_jadwalkelas;
       public          postgres    false    222    4749    224         �           2606    42361 #   jadwal_pelajaran fk_jadwalpelajaran    FK CONSTRAINT     �   ALTER TABLE ONLY public.jadwal_pelajaran
    ADD CONSTRAINT fk_jadwalpelajaran FOREIGN KEY (id_pelajaran) REFERENCES public.mata_pelajaran(id_pelajaran);
 M   ALTER TABLE ONLY public.jadwal_pelajaran DROP CONSTRAINT fk_jadwalpelajaran;
       public          postgres    false    232    4761    222         �           2606    41926    siswa fk_kelassiswa    FK CONSTRAINT     y   ALTER TABLE ONLY public.siswa
    ADD CONSTRAINT fk_kelassiswa FOREIGN KEY (id_kelas) REFERENCES public.kelas(id_kelas);
 =   ALTER TABLE ONLY public.siswa DROP CONSTRAINT fk_kelassiswa;
       public          postgres    false    218    224    4749         �           2606    41946    nilai_siswa fk_nilaiguru    FK CONSTRAINT     {   ALTER TABLE ONLY public.nilai_siswa
    ADD CONSTRAINT fk_nilaiguru FOREIGN KEY (id_guru) REFERENCES public.guru(id_guru);
 B   ALTER TABLE ONLY public.nilai_siswa DROP CONSTRAINT fk_nilaiguru;
       public          postgres    false    226    4745    220         �           2606    42380    nilai_siswa fk_nilaijenis    FK CONSTRAINT     �   ALTER TABLE ONLY public.nilai_siswa
    ADD CONSTRAINT fk_nilaijenis FOREIGN KEY (id_tugas) REFERENCES public.jenis_tugas(id_tugas);
 C   ALTER TABLE ONLY public.nilai_siswa DROP CONSTRAINT fk_nilaijenis;
       public          postgres    false    226    230    4757         �           2606    41951    nilai_siswa fk_nilaisiswa    FK CONSTRAINT        ALTER TABLE ONLY public.nilai_siswa
    ADD CONSTRAINT fk_nilaisiswa FOREIGN KEY (id_siswa) REFERENCES public.siswa(id_siswa);
 C   ALTER TABLE ONLY public.nilai_siswa DROP CONSTRAINT fk_nilaisiswa;
       public          postgres    false    218    226    4742         �           2606    42366    guru fk_pelajaranguru    FK CONSTRAINT     �   ALTER TABLE ONLY public.guru
    ADD CONSTRAINT fk_pelajaranguru FOREIGN KEY (id_pelajaran) REFERENCES public.mata_pelajaran(id_pelajaran);
 ?   ALTER TABLE ONLY public.guru DROP CONSTRAINT fk_pelajaranguru;
       public          postgres    false    220    232    4761                                                                                                                                                                     4918.dat                                                                                            0000600 0004000 0002000 00000000143 14621577323 0014267 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Satrio	Satrio423	33444
2	Sutisono	Sutisono44	Sutis99990
3	Hendro Waseso	Hendro55	Waseso0090
\.


                                                                                                                                                                                                                                                                                                                                                                                                                             4930.dat                                                                                            0000600 0004000 0002000 00000000505 14621577323 0014263 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Jawa Timur	Jember	Sumbersari	Jalan Kalimantan 1	No 32
2	Jawa Tengah	Magelang	Borobudur	Jalan Halim 3	No 35
3	Jawa Barat	Bandung	Gejawan	Jalan Pengasaan 3	\N
4	Jawa Timur	Lumajang	Sumberjambe	Jalan Sumatra 1	No 33
5	Jawa Timur	Lumajang	Kaliwates	Jalan Hamdan 7	No 26
6	Jawa Timur	Lumajang	Gejuwan	Jalan Pengasaan 10	\N
\.


                                                                                                                                                                                           4922.dat                                                                                            0000600 0004000 0002000 00000000254 14621577323 0014265 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Sutarjo	08968593299	L	1	1	1	t	\N	1990081720200410
2	Sri Dwi	08909509000	P	2	2	1	t	\N	1978061620200511
3	Bram Prasetyo	081384883838	L	2	3	1	f	Pesiun	1989051020104410
\.


                                                                                                                                                                                                                                                                                                                                                    4924.dat                                                                                            0000600 0004000 0002000 00000000145 14621577323 0014266 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Senin	08:00:00	09:40:00	1	1	1
2	Selesa	10:00:00	11:40:00	2	2	2
3	Rabu	07:00:00	08:40:00	3	2	3
\.


                                                                                                                                                                                                                                                                                                                                                                                                                           4932.dat                                                                                            0000600 0004000 0002000 00000000037 14621577323 0014265 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Tugas 1
2	Tugas 2
3	UTS
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 4926.dat                                                                                            0000600 0004000 0002000 00000000054 14621577323 0014267 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	XMIPA
2	X MIPA1
3	XI IPS2
4	XII IPS1
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    4934.dat                                                                                            0000600 0004000 0002000 00000000060 14621577323 0014263 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	KD1	Matematika	1
2	KD2	IPS	1
3	KD3	PKN	2
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                4928.dat                                                                                            0000600 0004000 0002000 00000000046 14621577323 0014272 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	94	1	1	1
2	85	2	1	2
3	94	3	2	1
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          4920.dat                                                                                            0000600 0004000 0002000 00000000363 14621577323 0014264 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	0046164275	Satria Perdana	08967893939	2024	2008-10-21	Lumajang	L	4	1	1	t	\N
2	0046909020	Widi Andarawati	08967098776	2023	2007-05-25	Lumajang	P	5	2	1	t	\N
3	0046986777	Pratama Agung	081358987656	2021	2006-11-10	Lumajang	L	6	3	1	f	Lulus
\.


                                                                                                                                                                                                                                                                             restore.sql                                                                                         0000600 0004000 0002000 00000047312 14621577323 0015405 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

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

DROP DATABASE "SMAN3";
--
-- Name: SMAN3; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "SMAN3" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';


ALTER DATABASE "SMAN3" OWNER TO postgres;

\connect "SMAN3"

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: admin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admin (
    id_admin integer NOT NULL,
    nama_admin character varying(100) NOT NULL,
    username character varying(50) NOT NULL,
    password character varying(50) NOT NULL
);


ALTER TABLE public.admin OWNER TO postgres;

--
-- Name: admin_id_admin_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.admin_id_admin_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.admin_id_admin_seq OWNER TO postgres;

--
-- Name: admin_id_admin_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.admin_id_admin_seq OWNED BY public.admin.id_admin;


--
-- Name: alamat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alamat (
    id_alamat integer NOT NULL,
    provinsi character varying(30) NOT NULL,
    kabupatenkota character varying(30) NOT NULL,
    kecamatan character varying(30) NOT NULL,
    jalan character varying(60) NOT NULL,
    detail character varying(60)
);


ALTER TABLE public.alamat OWNER TO postgres;

--
-- Name: alamat_id_alamat_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.alamat_id_alamat_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.alamat_id_alamat_seq OWNER TO postgres;

--
-- Name: alamat_id_alamat_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.alamat_id_alamat_seq OWNED BY public.alamat.id_alamat;


--
-- Name: guru; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.guru (
    id_guru integer NOT NULL,
    nama_guru character varying(100) NOT NULL,
    no_telp character varying(13) NOT NULL,
    jenis_kelamin character varying(15) NOT NULL,
    id_pelajaran integer,
    id_alamat integer,
    id_admin integer,
    status boolean,
    deskripsi text,
    nip character varying(18) NOT NULL
);


ALTER TABLE public.guru OWNER TO postgres;

--
-- Name: guru_id_guru_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.guru_id_guru_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.guru_id_guru_seq OWNER TO postgres;

--
-- Name: guru_id_guru_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.guru_id_guru_seq OWNED BY public.guru.id_guru;


--
-- Name: jadwal_pelajaran; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jadwal_pelajaran (
    id_jadwal integer NOT NULL,
    hari character varying(50) NOT NULL,
    awal_pelajaran time without time zone NOT NULL,
    akhir_pelajaran time without time zone NOT NULL,
    id_guru integer,
    id_pelajaran integer,
    id_kelas integer
);


ALTER TABLE public.jadwal_pelajaran OWNER TO postgres;

--
-- Name: jadwal_pelajaran_id_jadwal_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jadwal_pelajaran_id_jadwal_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.jadwal_pelajaran_id_jadwal_seq OWNER TO postgres;

--
-- Name: jadwal_pelajaran_id_jadwal_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jadwal_pelajaran_id_jadwal_seq OWNED BY public.jadwal_pelajaran.id_jadwal;


--
-- Name: jenis_tugas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jenis_tugas (
    id_tugas integer NOT NULL,
    jenis_tugas character varying(60) NOT NULL
);


ALTER TABLE public.jenis_tugas OWNER TO postgres;

--
-- Name: jenis_tugas_id_tugas_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jenis_tugas_id_tugas_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.jenis_tugas_id_tugas_seq OWNER TO postgres;

--
-- Name: jenis_tugas_id_tugas_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jenis_tugas_id_tugas_seq OWNED BY public.jenis_tugas.id_tugas;


--
-- Name: kelas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kelas (
    id_kelas integer NOT NULL,
    kelas character varying(30) NOT NULL
);


ALTER TABLE public.kelas OWNER TO postgres;

--
-- Name: kelas_id_kelas_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.kelas_id_kelas_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.kelas_id_kelas_seq OWNER TO postgres;

--
-- Name: kelas_id_kelas_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.kelas_id_kelas_seq OWNED BY public.kelas.id_kelas;


--
-- Name: mata_pelajaran; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mata_pelajaran (
    id_pelajaran integer NOT NULL,
    kode_pelajaran character varying(5) NOT NULL,
    nama_pelajaran character varying(50) NOT NULL,
    semester integer NOT NULL
);


ALTER TABLE public.mata_pelajaran OWNER TO postgres;

--
-- Name: mata_pelajaran_id_pelajaran_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mata_pelajaran_id_pelajaran_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.mata_pelajaran_id_pelajaran_seq OWNER TO postgres;

--
-- Name: mata_pelajaran_id_pelajaran_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mata_pelajaran_id_pelajaran_seq OWNED BY public.mata_pelajaran.id_pelajaran;


--
-- Name: nilai_siswa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.nilai_siswa (
    id_nilai_siswa integer NOT NULL,
    nilai_tugas integer NOT NULL,
    id_guru integer,
    id_siswa integer,
    id_tugas integer
);


ALTER TABLE public.nilai_siswa OWNER TO postgres;

--
-- Name: nilai_siswa_id_nilai_siswa_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.nilai_siswa_id_nilai_siswa_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.nilai_siswa_id_nilai_siswa_seq OWNER TO postgres;

--
-- Name: nilai_siswa_id_nilai_siswa_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.nilai_siswa_id_nilai_siswa_seq OWNED BY public.nilai_siswa.id_nilai_siswa;


--
-- Name: siswa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.siswa (
    id_siswa integer NOT NULL,
    nisn character varying(10) NOT NULL,
    nama_siswa character varying(100) NOT NULL,
    no_telp character varying(13) NOT NULL,
    tahun_angkatan integer NOT NULL,
    tgl_lahir date NOT NULL,
    tempat_lahir character varying(50) NOT NULL,
    jenis_kelamin character varying(15) NOT NULL,
    id_alamat integer,
    id_kelas integer,
    id_admin integer,
    status boolean NOT NULL,
    deskripsi text
);


ALTER TABLE public.siswa OWNER TO postgres;

--
-- Name: siswa_id_siswa_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.siswa_id_siswa_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.siswa_id_siswa_seq OWNER TO postgres;

--
-- Name: siswa_id_siswa_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.siswa_id_siswa_seq OWNED BY public.siswa.id_siswa;


--
-- Name: admin id_admin; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin ALTER COLUMN id_admin SET DEFAULT nextval('public.admin_id_admin_seq'::regclass);


--
-- Name: alamat id_alamat; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alamat ALTER COLUMN id_alamat SET DEFAULT nextval('public.alamat_id_alamat_seq'::regclass);


--
-- Name: guru id_guru; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.guru ALTER COLUMN id_guru SET DEFAULT nextval('public.guru_id_guru_seq'::regclass);


--
-- Name: jadwal_pelajaran id_jadwal; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal_pelajaran ALTER COLUMN id_jadwal SET DEFAULT nextval('public.jadwal_pelajaran_id_jadwal_seq'::regclass);


--
-- Name: jenis_tugas id_tugas; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jenis_tugas ALTER COLUMN id_tugas SET DEFAULT nextval('public.jenis_tugas_id_tugas_seq'::regclass);


--
-- Name: kelas id_kelas; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kelas ALTER COLUMN id_kelas SET DEFAULT nextval('public.kelas_id_kelas_seq'::regclass);


--
-- Name: mata_pelajaran id_pelajaran; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mata_pelajaran ALTER COLUMN id_pelajaran SET DEFAULT nextval('public.mata_pelajaran_id_pelajaran_seq'::regclass);


--
-- Name: nilai_siswa id_nilai_siswa; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nilai_siswa ALTER COLUMN id_nilai_siswa SET DEFAULT nextval('public.nilai_siswa_id_nilai_siswa_seq'::regclass);


--
-- Name: siswa id_siswa; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.siswa ALTER COLUMN id_siswa SET DEFAULT nextval('public.siswa_id_siswa_seq'::regclass);


--
-- Data for Name: admin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.admin (id_admin, nama_admin, username, password) FROM stdin;
\.
COPY public.admin (id_admin, nama_admin, username, password) FROM '$$PATH$$/4918.dat';

--
-- Data for Name: alamat; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alamat (id_alamat, provinsi, kabupatenkota, kecamatan, jalan, detail) FROM stdin;
\.
COPY public.alamat (id_alamat, provinsi, kabupatenkota, kecamatan, jalan, detail) FROM '$$PATH$$/4930.dat';

--
-- Data for Name: guru; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.guru (id_guru, nama_guru, no_telp, jenis_kelamin, id_pelajaran, id_alamat, id_admin, status, deskripsi, nip) FROM stdin;
\.
COPY public.guru (id_guru, nama_guru, no_telp, jenis_kelamin, id_pelajaran, id_alamat, id_admin, status, deskripsi, nip) FROM '$$PATH$$/4922.dat';

--
-- Data for Name: jadwal_pelajaran; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jadwal_pelajaran (id_jadwal, hari, awal_pelajaran, akhir_pelajaran, id_guru, id_pelajaran, id_kelas) FROM stdin;
\.
COPY public.jadwal_pelajaran (id_jadwal, hari, awal_pelajaran, akhir_pelajaran, id_guru, id_pelajaran, id_kelas) FROM '$$PATH$$/4924.dat';

--
-- Data for Name: jenis_tugas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jenis_tugas (id_tugas, jenis_tugas) FROM stdin;
\.
COPY public.jenis_tugas (id_tugas, jenis_tugas) FROM '$$PATH$$/4932.dat';

--
-- Data for Name: kelas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kelas (id_kelas, kelas) FROM stdin;
\.
COPY public.kelas (id_kelas, kelas) FROM '$$PATH$$/4926.dat';

--
-- Data for Name: mata_pelajaran; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mata_pelajaran (id_pelajaran, kode_pelajaran, nama_pelajaran, semester) FROM stdin;
\.
COPY public.mata_pelajaran (id_pelajaran, kode_pelajaran, nama_pelajaran, semester) FROM '$$PATH$$/4934.dat';

--
-- Data for Name: nilai_siswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.nilai_siswa (id_nilai_siswa, nilai_tugas, id_guru, id_siswa, id_tugas) FROM stdin;
\.
COPY public.nilai_siswa (id_nilai_siswa, nilai_tugas, id_guru, id_siswa, id_tugas) FROM '$$PATH$$/4928.dat';

--
-- Data for Name: siswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.siswa (id_siswa, nisn, nama_siswa, no_telp, tahun_angkatan, tgl_lahir, tempat_lahir, jenis_kelamin, id_alamat, id_kelas, id_admin, status, deskripsi) FROM stdin;
\.
COPY public.siswa (id_siswa, nisn, nama_siswa, no_telp, tahun_angkatan, tgl_lahir, tempat_lahir, jenis_kelamin, id_alamat, id_kelas, id_admin, status, deskripsi) FROM '$$PATH$$/4920.dat';

--
-- Name: admin_id_admin_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.admin_id_admin_seq', 3, true);


--
-- Name: alamat_id_alamat_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.alamat_id_alamat_seq', 6, true);


--
-- Name: guru_id_guru_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.guru_id_guru_seq', 3, true);


--
-- Name: jadwal_pelajaran_id_jadwal_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jadwal_pelajaran_id_jadwal_seq', 3, true);


--
-- Name: jenis_tugas_id_tugas_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jenis_tugas_id_tugas_seq', 3, true);


--
-- Name: kelas_id_kelas_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.kelas_id_kelas_seq', 4, true);


--
-- Name: mata_pelajaran_id_pelajaran_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mata_pelajaran_id_pelajaran_seq', 3, true);


--
-- Name: nilai_siswa_id_nilai_siswa_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.nilai_siswa_id_nilai_siswa_seq', 3, true);


--
-- Name: siswa_id_siswa_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.siswa_id_siswa_seq', 3, true);


--
-- Name: admin admin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (id_admin);


--
-- Name: alamat alamat_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alamat
    ADD CONSTRAINT alamat_pkey PRIMARY KEY (id_alamat);


--
-- Name: guru guru_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.guru
    ADD CONSTRAINT guru_pkey PRIMARY KEY (id_guru);


--
-- Name: jadwal_pelajaran jadwal_pelajaran_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal_pelajaran
    ADD CONSTRAINT jadwal_pelajaran_pkey PRIMARY KEY (id_jadwal);


--
-- Name: jenis_tugas jenis_tugas_jenis_tugas_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jenis_tugas
    ADD CONSTRAINT jenis_tugas_jenis_tugas_key UNIQUE (jenis_tugas);


--
-- Name: jenis_tugas jenis_tugas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jenis_tugas
    ADD CONSTRAINT jenis_tugas_pkey PRIMARY KEY (id_tugas);


--
-- Name: kelas kelas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kelas
    ADD CONSTRAINT kelas_pkey PRIMARY KEY (id_kelas);


--
-- Name: mata_pelajaran mata_pelajaran_kode_pelajaran_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mata_pelajaran
    ADD CONSTRAINT mata_pelajaran_kode_pelajaran_key UNIQUE (kode_pelajaran);


--
-- Name: mata_pelajaran mata_pelajaran_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mata_pelajaran
    ADD CONSTRAINT mata_pelajaran_pkey PRIMARY KEY (id_pelajaran);


--
-- Name: nilai_siswa nilai_siswa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nilai_siswa
    ADD CONSTRAINT nilai_siswa_pkey PRIMARY KEY (id_nilai_siswa);


--
-- Name: siswa siswa_nisn_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.siswa
    ADD CONSTRAINT siswa_nisn_key UNIQUE (nisn);


--
-- Name: siswa siswa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.siswa
    ADD CONSTRAINT siswa_pkey PRIMARY KEY (id_siswa);


--
-- Name: fki_fk_adminguru; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_fk_adminguru ON public.guru USING btree (id_admin);


--
-- Name: guru fk_adminguru; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.guru
    ADD CONSTRAINT fk_adminguru FOREIGN KEY (id_admin) REFERENCES public.admin(id_admin);


--
-- Name: siswa fk_adminsiswa; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.siswa
    ADD CONSTRAINT fk_adminsiswa FOREIGN KEY (id_admin) REFERENCES public.admin(id_admin);


--
-- Name: guru fk_alamatguru; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.guru
    ADD CONSTRAINT fk_alamatguru FOREIGN KEY (id_alamat) REFERENCES public.alamat(id_alamat);


--
-- Name: siswa fk_alamatsiswa; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.siswa
    ADD CONSTRAINT fk_alamatsiswa FOREIGN KEY (id_alamat) REFERENCES public.alamat(id_alamat);


--
-- Name: jadwal_pelajaran fk_jadwalguru; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal_pelajaran
    ADD CONSTRAINT fk_jadwalguru FOREIGN KEY (id_guru) REFERENCES public.guru(id_guru);


--
-- Name: jadwal_pelajaran fk_jadwalkelas; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal_pelajaran
    ADD CONSTRAINT fk_jadwalkelas FOREIGN KEY (id_kelas) REFERENCES public.kelas(id_kelas);


--
-- Name: jadwal_pelajaran fk_jadwalpelajaran; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal_pelajaran
    ADD CONSTRAINT fk_jadwalpelajaran FOREIGN KEY (id_pelajaran) REFERENCES public.mata_pelajaran(id_pelajaran);


--
-- Name: siswa fk_kelassiswa; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.siswa
    ADD CONSTRAINT fk_kelassiswa FOREIGN KEY (id_kelas) REFERENCES public.kelas(id_kelas);


--
-- Name: nilai_siswa fk_nilaiguru; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nilai_siswa
    ADD CONSTRAINT fk_nilaiguru FOREIGN KEY (id_guru) REFERENCES public.guru(id_guru);


--
-- Name: nilai_siswa fk_nilaijenis; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nilai_siswa
    ADD CONSTRAINT fk_nilaijenis FOREIGN KEY (id_tugas) REFERENCES public.jenis_tugas(id_tugas);


--
-- Name: nilai_siswa fk_nilaisiswa; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nilai_siswa
    ADD CONSTRAINT fk_nilaisiswa FOREIGN KEY (id_siswa) REFERENCES public.siswa(id_siswa);


--
-- Name: guru fk_pelajaranguru; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.guru
    ADD CONSTRAINT fk_pelajaranguru FOREIGN KEY (id_pelajaran) REFERENCES public.mata_pelajaran(id_pelajaran);


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      