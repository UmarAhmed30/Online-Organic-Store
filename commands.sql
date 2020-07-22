create database onlineorganicstore;

\c onlineorganicstore

/*Farmer Table*/

create table farmer (
    farmer_id numeric(4) not NULL,
    name varchar(30) not NULL,
    age numeric(2) not NULL,
    gender varchar(1),
    contact numeric(10) not NULL,
    email_id varchar(50) unique not NULL,
    experience numeric(2) not NULL,
    land_area numeric(10,3) not NULL,
    door_no numeric(4) not NULL,
    street varchar(50) not NULL,
    locality varchar(30) not NULL,
    city varchar(30) not NULL,
    pincode numeric(6) not NULL,
    primary key(farmer_id)
);

/*farmer_id Generation*/

CREATE SEQUENCE farmer_seq START WITH 1000;

CREATE OR REPLACE TRIGGER farmer_tri 
BEFORE INSERT ON farmer
FOR EACH ROW

BEGIN
  SELECT farmer_seq.NEXTVAL
  INTO   :new.farmer_id
  FROM   dual;
END;
/

/*Buyer Table*/

create table buyer (
    buyer_id numeric(4) not NULL,
    name varchar(30) not NULL,
    age numeric(2) not NULL,
    gender varchar(1),
    contact numeric(10) not NULL,
    email_id varchar(50) unique not NULL,
    door_no numeric(4) not NULL,
    street varchar(50) not NULL,
    locality varchar(30) not NULL,
    city varchar(30) not NULL,
    pincode numeric(6) not NULL,
    primary key(buyer_id)
);

/*buyer_id Generation*/

CREATE SEQUENCE buyer_seq START WITH 3000;

CREATE OR REPLACE TRIGGER buyer_tri 
BEFORE INSERT ON buyer
FOR EACH ROW

BEGIN
  SELECT buyer_seq.NEXTVAL
  INTO   :new.buyer_id
  FROM   dual;
END;
/

/*Product Table*/

create table product (
    product_id numeric(4) not NULL,
    name varchar(30) not NULL,
    type varchar(20), 
    price numeric(5,2) not NULL,
    primary key(product_id,name)
);

/* product_id Generation */

CREATE SEQUENCE product_seq START WITH 2000;

CREATE OR REPLACE TRIGGER product_tri 
BEFORE INSERT ON product
FOR EACH ROW

BEGIN
  SELECT product_seq.NEXTVAL
  INTO   :new.product_id
  FROM   dual;
END;
/

/*Stock Table*/

create table stock (
    stock_id numeric(4) not NULL,
    capacity numeric(10,3) not NULL,
    door_no numeric(4) not NULL,
    street varchar(50) not NULL,
    locality varchar(30) not NULL,
    city varchar(30) not NULL,
    pincode numeric(6) not NULL,
    primary key(stock_id)
);

alter table stock add farmer_id numeric(4) not NULL;
alter table stock add constraint farmer_id1 foreign key (farmer_id) references farmer(farmer_id);

/*stock_id Generation*/

CREATE SEQUENCE stock_seq START WITH 4000;

CREATE OR REPLACE TRIGGER stock_tri 
BEFORE INSERT ON stock
FOR EACH ROW

BEGIN
  SELECT stock_seq.NEXTVAL
  INTO   :new.stock_id
  FROM   dual;
END;
/

/*holds Table*/

create table holds (
    stock_id numeric(4) not NULL,
    product_id numeric(4) not NULL,
    name varchar(30) not NULL,
    available_quantity numeric(6,3),
    primary key(stock_id,product_id,name),
    foreign key(stock_id) references stock(stock_id),
    foreign key(product_id,name) references product(product_id,name)
);

/*assign Table*/

create table assign (
    buyer_id NUMERIC(4) not NULL,
    cart_id NUMERIC(4) not NULL,
    PRIMARY key(buyer_id,cart_id),
    FOREIGN key (buyer_id) references buyer(buyer_id)
);

/* Cart Table */

create table cart (
    cart_id numeric(4) not NULL,
    buyer_id NUMERIC(4) not NULL,
    product_id NUMERIC(4) not NULL,
    name varchar(30) NOT NULL,
    stock_id NUMERIC(4) not NULL,
    quantity NUMERIC(4,2) not NULL,
    price numeric(8,2),
    primary key(cart_id,buyer_id,product_id,name,stock_id),
    foreign key(stock_id,product_id,name) references holds(stock_id,product_id,name),
    FOREIGN key(buyer_id,cart_id) REFERENCES assign(buyer_id,cart_id)
);

/*cart_id Generation*/

CREATE SEQUENCE cart_seq START WITH 7012;

CREATE OR REPLACE TRIGGER cart_tri 
BEFORE INSERT ON assign
FOR EACH ROW

BEGIN
  SELECT cart_seq.NEXTVAL
  INTO   :new.cart_id
  FROM   dual;
END;
/

/*Payment Table*/

create table payment (
    payment_id numeric(4) not NULL,
    buyer_id NUMERIC(4) not NULL,
    cart_id NUMERIC(4) not NULL,
    total_amount numeric(10,2) not NULL, 
    p_mode varchar(25),
    payment_date date,
    primary key(payment_id),
    FOREIGN key (buyer_id,cart_id) REFERENCES assign(buyer_id,cart_id)
);

/*payment_id Generation*/

CREATE SEQUENCE payment_seq START WITH 5000;

CREATE OR REPLACE TRIGGER payment_tri 
BEFORE INSERT ON payment
FOR EACH ROW

BEGIN
  SELECT payment_seq.NEXTVAL
  INTO   :new.payment_id
  FROM   dual;
END;
/

/*sells Table*/

create table sells (
    farmer_id numeric(4) not NULL,
    product_id numeric(4) not NULL,
    name varchar(30) not NULL,
    primary key(farmer_id,product_id),
    foreign key(farmer_id) references farmer(farmer_id),
    foreign key(product_id,name) references product(product_id,name)
);

/*Data*/

insert into farmer values (&farmer_id,'&name',&age,'&gender',&contact,'&email_id',&experience,&land_area,&door_no,'&street','&locality','&city',&pincode);

insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('Siva Kumar',48,'M',7898990099,'siva147@gmail.com',13,200,36,'Sivan Street','Sankaran Kovil','Tirunelveli',627756);
insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('Arun Raj',56,'M',7898990789,'arun156@gmail.com',18,30.5,19,'Sugam Street','Aruvapakkam','Villupuram',604102);
insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('Sathish',53,'M',7890990789,'sat196@gmail.com',21,80,65,'Vinayagar Street','Alagapuram','Salem',636004);
insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('Vineeth',38,'M',7230990789,'vinee190@gmail.com',12,65,194,'2nd Street','Sivanthipuram','Tirunelveli',627756);
insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('Abdul Hameem',38,'M',7450990789,'abdul@gmail.com',8,110,43,'Kumaran Street','Tambaram','Chennai',600045);
insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('Jayanthi',49,'F',7450900789,'jaya198@gmail.com',22,95,11,'Kambar Street','Srirangam','Trichy',620005);
insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('John',63,'M',7450980078,'john292@gmail.com',33,155,212,'Thiruvalluvar Street','Sevilimedu','Kanchipuram',631502);
insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('Vijaya Krishnan',56,'F',7450981078,'vijaya342@gmail.com',21,45,12,'4th Street','Sankaran Kovil','Tirunelveli',627756);
insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('Muthusamy',44,'M',9850981078,'muthu1@gmail.com',7,30,90,'Raghavan Street','Tambaram','Chennai',600045);
insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('Raghavi',36,'F',8450981078,'raghavi8@gmail.com',7,76,7,'Murugan Street','Sattur','Virudhunagar',626203);
insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values ('Kannan',36,'M',6450981078,'kannan@gmail.com',7,76,7,'Murugan Street','Sattur','Virudhunagar',626203);


insert into product (name,type,price) values ('Tomato','Vegetable',12);
insert into product (name,type,price) values ('Apple','Fruit',160);
insert into product (name,type,price) values ('Milk','Dairy',50);
insert into product (name,type,price) values ('Capsicum','Vegetable',20);
insert into product (name,type,price) values ('Onion','Vegetable',45);
insert into product (name,type,price) values ('Green Chilli','Vegetable',50);
insert into product (name,type,price) values ('Pineapple','Fruit',70);
insert into product (name,type,price) values ('Orange','Fruit',50);
insert into product (name,type,price) values ('Curd','Dairy',44.50);
insert into product (name,type,price) values ('Carrot','Vegetable',40);
insert into product (name,type,price) values ('Beetroot','Vegetable',40);
insert into product (name,type,price) values ('Brinjal','Vegetable',40);
insert into product (name,type,price) values ('Peas','Vegetable',80);
insert into product (name,type,price) values ('Watermelon','Fruit',15);
insert into product (name,type,price) values ('Banana','Fruit',50);


insert into buyer values (&buyer_id,'&name',&age,'&gender',&contact,'&email_id',&door_no,'&street','&locality','&city',&pincode);

insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Sudarshan',43,'M',9298989321,'sudarshan7@gmail.com',1003,'2nd Street','Ashok Nagar','Chennai',600083);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Naren',48,'M',9298198921,'naren27@gmail.com',6,'Velan Street','T Nagar','Chennai',600017);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Shweta',57,'F',9298589321,'shwetha223@gmail.com',103,'9th Cross','Peelamedu','Coimbatore',641004);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Shankar Kumar',56,'M',7298398931,'shankar20@gmail.com',1090,'Jayaram Street','Anna Nagar','Madurai',625020);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Paargav',48,'M',9393989321,'paarshan3@gmail.com',23,'Murugan Street','Woraiyur','Trichy',620020);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Sivakarthikeyan',41,'M',7983989321,'siva700@gmail.com',68,'6th Street','KK Nagar','Chennai',600026);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Shruthi',29,'F',9298396321,'shruthi88@gmail.com',65,'7th Sector','Perundurai','Erode',638052);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Sneha',35,'F',9298398933,'sneha200@gmail.com',1002,'Vishnu Street','West Mambalam','Chennai',600033);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Abhishek Kumar',54,'M',6783989321,'abikumar60@gmail.com',903,'3rd Cross','Guindy','Chennai',600015);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Aparna',47,'F',9298398930,'aparna13@gmail.com',164,'United Cross Street','Singanallur','Coimbatore',641005);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Aarti',37,'F',9879008930,'aarti@gmail.com',165,'United Cross Street','Singanallur','Tirunelveli',641089);
insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values ('Subha',38,'F',6879008930,'subha12@gmail.com',162,'United Cross Street','Guindy','Chennai',600020);


insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (9000,345,'Sivan Street','Sankaran Kovil','Tirunelveli',627756,1000);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (500,3055,'Sugam Street','Aruvapakkam','Villupuram',604102,1001);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (2000,145,'Vinayagar Street','Alagapuram','Salem',636004,1002);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (1500,125,'2nd Street','Sivanthipuram','Tirunelveli',627756,1003);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (5500.400,3,'Kumaran Street','Tambaram','Chennai',600045,1004);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (4000.250,18,'Kambar Street','Srirangam','Trichy',620005,1005);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (900,390,'Thiruvalluvar Street','Sevilimedu','Kanchipuram',631502,1006);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (800,305,'4th Street','Sankaran Kovil','Tirunelveli',627756,1007);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (400,10,'Raghavan Street','Tambaram','Chennai',600045,1008);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (1500,45,'Murugan Street','Sattur','Virudhunagar',626203,1009);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (200,46,'Murugan Street','Sattur','Virudhunagar',626203,1009);
insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (250,45,'Murugan Street','Sattur','Virudhunagar',626203,1009);



insert into sells values (&farmer_id,&product_id,'&name');

insert into sells(farmer_id,product_id,name) values (1000,2000,'Tomato');
insert into sells(farmer_id,product_id,name) values (1000,2001,'Apple');
insert into sells(farmer_id,product_id,name) values (1000,2002,'Milk');
insert into sells(farmer_id,product_id,name) values (1000,2003,'Capsicum');
insert into sells(farmer_id,product_id,name) values (1000,2004,'Onion');
insert into sells(farmer_id,product_id,name) values (1000,2005,'Green Chilli');
insert into sells(farmer_id,product_id,name) values (1000,2006,'Pineapple');
insert into sells(farmer_id,product_id,name) values (1000,2007,'Orange');
insert into sells(farmer_id,product_id,name) values (1000,2008,'Curd');
insert into sells(farmer_id,product_id,name) values (1000,2009,'Carrot');
insert into sells(farmer_id,product_id,name) values (1001,2002,'Milk');
insert into sells(farmer_id,product_id,name) values (1002,2005,'Green Chilli');
insert into sells(farmer_id,product_id,name) values (1003,2001,'Apple');
insert into sells(farmer_id,product_id,name) values (1004,2007,'Orange');
insert into sells(farmer_id,product_id,name) values (1005,2009,'Carrot');
insert into sells(farmer_id,product_id,name) values (1006,2008,'Curd');
insert into sells(farmer_id,product_id,name) values (1007,2009,'Carrot');
insert into sells(farmer_id,product_id,name) values (1008,2008,'Curd');
insert into sells(farmer_id,product_id,name) values (1009,2003,'Capsicum');

insert into holds(stock_id,product_id,name,available_quantity) values (4000,2000,'Tomato',90);
insert into holds(stock_id,product_id,name,available_quantity) values (4000,2001,'Apple',120.500);
insert into holds(stock_id,product_id,name,available_quantity) values (4000,2002,'Milk',70);
insert into holds(stock_id,product_id,name,available_quantity) values (4000,2003,'Capsicum',500.200);
insert into holds(stock_id,product_id,name,available_quantity) values (4000,2004,'Onion',600);
insert into holds(stock_id,product_id,name,available_quantity) values (4000,2005,'Green Chilli',300);
insert into holds(stock_id,product_id,name,available_quantity) values (4000,2006,'Pineapple',460);
insert into holds(stock_id,product_id,name,available_quantity) values (4000,2007,'Orange',450.600);
insert into holds(stock_id,product_id,name,available_quantity) values (4000,2008,'Curd',30);
insert into holds(stock_id,product_id,name,available_quantity) values (4000,2009,'Carrot',90);
insert into holds(stock_id,product_id,name,available_quantity) values (4001,2002,'Milk',0);
insert into holds(stock_id,product_id,name,available_quantity) values (4000,2020,'Beetroot',20);



insert into assign values (&buyer_id,&cart_id);
3000    7000
3001    7001
3002    7002
3003    7003
3004    7004
3005    7005
3006    7006
3007    7007
3008    7008
3009    7009
3024    7010
3025    7011

insert into cart values (&cart_id,&buyer_id,&product_id,'&name',&stock_id,&quantity,&price);
insert into cart(cart_id,buyer_id,product_id,name,stock_id,quantity,price) values (7010,3024,2009,'Carrot',4000,10,400);

7000    3000    2008    Curd        4000    3   133.50
7000    3000    2004    Onion       4000    2   90
7000    3000    2000    Tomato      4000    4   48
7001    3001    2000    Tomato      4000    10  120
7001    3001    2004    Onion       4000    2   90
7001    3001    2009    Carrot      4000    3   120
7001    3001    2007    Orange      4000    1   50
7002    3002    2006    Pineapple   4000    2   140
7002    3002    2003    Capsicum    4000    3   60
7003    3003    2002    Milk        4000    12  600
7004    3004    2000    Tomato      4000    3   36
7005    3005    2002    Milk        4000    2   100
7006    3006    2007    Orange      4000    4   200
7007    3007    2009    Carrot      4000    5   200
7008    3008    2003    Capsicum    4000    6   120
7009    3009    2004    Onion       4000    4   180
7010    3024    2009    Carrot      4000    10  400
7011    3025    2009    Carrot      4000    5   200



insert into payment(buyer_id,cart_id,total_amount,p_mode,payment_date) values (3000,7000,323.50,'Net Banking','02-FEB-20');
insert into payment(buyer_id,cart_id,total_amount,p_mode,payment_date) values (3001,7001,308,'PayTm','03-FEB-20');
insert into payment(buyer_id,cart_id,total_amount,p_mode,payment_date) values (3002,7002,200,'GPay','04-FEB-20');
insert into payment(buyer_id,cart_id,total_amount,p_mode,payment_date) values (3003,7003,600,'Net Banking','05-FEB-20');
insert into payment(buyer_id,cart_id,total_amount,p_mode,payment_date) values (3004,7004,36,'Cash on Delivery','06-FEB-20');
insert into payment(buyer_id,cart_id,total_amount,p_mode,payment_date) values (3005,7005,100,'Net Banking','07-FEB-20');
insert into payment(buyer_id,cart_id,total_amount,p_mode,payment_date) values (3006,7006,200,'GPay','08-FEB-20');
insert into payment(buyer_id,cart_id,total_amount,p_mode,payment_date) values (3007,7007,200,'PayTm','09-FEB-20');
insert into payment(buyer_id,cart_id,total_amount,p_mode,payment_date) values (3008,7008,120,'Net Banking','10-FEB-20');
insert into payment(buyer_id,cart_id,total_amount,p_mode,payment_date) values (3024,7010,400,'Net Banking','29-MAR-20');    