Create Table Instruments(
    InstrumentID int NOT NULL AUTO_INCREMENT,
    InstrumentName varchar(255) NOT NULL,
    Category varchar(255) NOT NULL,
    InstrumentQuantity int NOT NULL,
    InstrumentDescription varchar(255) NOT NULL,
    Institute varchar(255) NOT NULL,
    PRIMARY KEY (InstrumentID),
    FOREIGN KEY (Category) REFERENCES Categories(Category),
    FOREIGN KEY (Institute) REFERENCES Institute(Institute)
    
);



Create Table Institute(
    Institute varchar(255) NOT NULL,
    InstituteLocation varchar(255) NOT NULL,
    InstituteContact varchar(255) NOT NULL,
    InstituteEmail varchar(255) NOT NULL,
    Pincode int(11) ,
    PRIMARY KEY (Institute)
);

Create Table Categories(
    Category varchar(255) NOT NULL,
    CategoryDescription varchar(255) NOT NULL,
    PRIMARY KEY (Category)
);

-- Category	Description
-- Basic	abAHSBJSB
-- Spectroscopy	CDJBJ
-- Centrifuge	abAHSBJSB
-- Cell Culture	CDJBJ
-- Electrophoresis	abAHSBJSB
-- Chromatography	CDJBJ
-- Xray	CDJBJ

insert into Categories(Category, CategoryDescription) values('Basic', 'abAHSBJSB');
insert into Categories(Category, CategoryDescription) values('Spectroscopy', 'CDJBJ');
insert into Categories(Category, CategoryDescription) values('Centrifuge', 'abAHSBJSB');
insert into Categories(Category, CategoryDescription) values('Cell Culture', 'CDJBJ');
insert into Categories(Category, CategoryDescription) values('Electrophoresis', 'abAHSBJSB');
insert into Categories(Category, CategoryDescription) values('Chromatography', 'CDJBJ');
insert into Categories(Category, CategoryDescription) values('Xray', 'CDJBJ');


-- Institute	institutelocation	instituteContact	instituteemail	Pincode
-- IITJ	Jodh	2111	ejejn	123456
-- MBMJ	Jodh	22111	dwdw	23456
-- AIMSS-J	Jodh	21111		11111
-- AIMSS-D	delhi	221212	dw2d	77777

insert into Institute values('IITJ', 'Jodh', '2111', 'ejejn', '123456');
insert into Institute values('MBMJ', 'Jodh', '22111', 'dwdw', '23456');
insert into Institute values('AIMSS-J', 'Jodh', '21111', '', '11111');
insert into Institute values('AIMSS-D', 'delhi', '221212', 'dw2d', '77777');



-- IID	instrumentname	category	instrumentquantity	instrumentdescription	institute
-- 1	Microscope	Basic	4	aaaaa	IITJ
-- 2	Microscope	Bioimaging	4	bbbb	MBMJ
-- 3	Microwave	Centrifuge	5	ccccc	AIMSS-J
-- 4	Microscope	Cell Culture	2	aaaaa	AIMSS-D
-- 5	machine1	Electrophoresis	5	bbbb	IITJ
-- 6	machine2	Chromatography	3	ccccc	MBMJ
-- 7	machine3	Spectroscopy	7	aaaaa	AIMSS-J
-- 8	machine4	Xray	1	bbbb	AIMSS-D
-- 9	machine5	Basic	9	ccccc	IITJ
-- 10	machine6	Bioimaging	3	aaaaa	MBMJ
-- 11	machine7	Centrifuge	5	bbbb	AIMSS-J
-- 12	machine8	Cell Culture	0	ccccc	AIMSS-D
-- 13	machine9	Electrophoresis	9	aaaaa	IITJ
-- 14	machine10	Chromatography	2	bbbb	MBMJ
-- 15	machine11	Spectroscopy	11	aaaaa	AIMSS-J

insert into Instruments values(1, 'Microscope', 'Basic', 4, 'aaaaa', 'IITJ');
insert into Instruments values(2, 'Microscope', 'Bioimaging', 4, 'bbbb', 'MBMJ');
insert into Instruments values(3, 'Microwave', 'Centrifuge', 5, 'ccccc', 'AIMSS-J');
insert into Instruments values(4, 'Microscope', 'Cell Culture', 2, 'aaaaa', 'AIMSS-D');
insert into Instruments values(5, 'machine1', 'Electrophoresis', 5, 'bbbb', 'IITJ');
insert into Instruments values(6, 'machine2', 'Chromatography', 3, 'ccccc', 'MBMJ');
insert into Instruments values(7, 'machine3', 'Spectroscopy', 7, 'aaaaa', 'AIMSS-J');
insert into Instruments values(8, 'machine4', 'Xray', 1, 'bbbb', 'AIMSS-D');
insert into Instruments values(9, 'machine5', 'Basic', 9, 'ccccc', 'IITJ');
insert into Instruments values(10, 'machine6', 'Bioimaging', 3, 'aaaaa', 'MBMJ');
insert into Instruments values(11, 'machine7', 'Centrifuge', 5, 'bbbb', 'AIMSS-J');
insert into Instruments values(12, 'machine8', 'Cell Culture', 0, 'ccccc', 'AIMSS-D');
insert into Instruments values(13, 'machine9', 'Electrophoresis', 9, 'aaaaa', 'IITJ');
insert into Instruments values(14, 'machine10', 'Chromatography', 2, 'bbbb', 'MBMJ');
insert into Instruments values(15, 'machine11', 'Spectroscopy', 11, 'aaaaa', 'AIMSS-J');
