USE COMP3278_G12;

INSERT INTO  Customer (customer_id,lastname,firstname,gender,birthday,email,phone,certification_type,id_number,password) VALUES
 ('001','Ma','Jack','male','2020-11-01','@gmail.com','12345678','student card','0000011111','iamjack'),
 ('002','Richeal','Rose','female','2020-11-17','@gmail.com','12345678','student card','1111100000','iamjacks'),
 ('003','Yan','Zipeng','male','2000-10-17','@gmail.com','12345678','student card','0000011111','password1'),
 ('004','Zhu','Jiarui','female','2020-11-01','@gmail.com','12345678','student card','0000011111','password2'),
 ('005','Huang','Haoyu','male','2020-11-01','@gmail.com','12345678','student card','0000011111','password3'),
 ('006','Ye','Mao','male','2020-11-01','@gmail.com','12345678','student card','0000011111','password4'),
 ('007','Bai','Qingyu','female','2020-11-01','@gmail.com','12345678','student card','0000011111','password5');

 INSERT INTO Account (account_id, customer_id, create_time, currency_type) VALUES
 ('001','001','1900-10-10','Pound'),
 ('002','001','1910-10-10','Pound'),
 ('003','002','1910-10-10','Pound'),
 ('004','002','1911-10-10','Pound'),
 ('005','002','1912-10-10','HKD'),
 ('006','004','2000-10-10','HKD'),
 ('007','005','2000-10-10','HKD'),
 ('008','006','2000-10-10','HKD'),
 ('009','007','2000-10-10','HKD'),
 ('010','001','1915-10-10','Pound'),
 ('011','002','1920-11-11','Pound'),
 ('012','004','2002-03-10','HKD'),
 ('013','005','2005-10-01','US Dollar'),
 ('014','005','2005-10-01','Yuan'),
 ('015','005','2007-11-11','US Dollar'),
 ('016','002','2021-11-16','US Dollar');

 INSERT INTO Investment_account (account_id, customer_id, currency_type, create_time, total_value) VALUES
 ('002','001','Pound','1910-10-10',1082000),
 ('003','002','Pound','1910-10-10',702000),
 ('008','006','HKD','2000-10-10',7567000),
 ('016','002','US Dollar','2021-11-16',670000);

 INSERT INTO Saving_account (account_id, customer_id, currency_type, create_time, balance) VALUES
 ('001','001','Pound','1900-10-10',4608100),
 ('004','002','Pound','1911-10-10',2313640),
 ('005','002','HKD','2010-10-10', 1318912),
 ('006','004','HKD','2000-10-10',3154792),
 ('007','005','HKD','2000-10-10',9199135),
 ('009','007','HKD','2000-10-10',75939),
 ('013','005','US Dollar','2005-10-01',8408561),
 ('014','005','Yuan','2005-10-01',1103622);

 INSERT INTO Credit_account (account_id, customer_id, currency_type, create_time, total_debt) VALUES
 ('010','001','Pound','1915-10-10',78988),
 ('011','002','Pound','1920-11-11',127781),
 ('012','004','HKD','2001-03-10',157803),
 ('015','005','US Dollar','2007-11-11',806900);

INSERT INTO Transaction (transaction_id, in_account_id, out_account_id, in_customer_id, out_customer_id, amount, currency_type, timepoint_date, timepoint_time) VALUES
('001','007','014','005','005',63034,'Yuan','2018-01-05','01:15:34'),
('002','011','006','002','004',136352,'HKD','2018-01-07','07:42:36'),
('003','015','006','005','004',154729,'HKD','2018-01-11','10:54:57'),
('004','013','014','005','005',74637,'Yuan','2018-01-18','09:43:17'),
('005','010','013','001','005',18240,'US Dollar','2018-01-22','18:02:21'),
('006','013','012','005','004',33899,'HKD','2018-01-26','14:11:19'),
('007','009','004','007','002',958,'Pound','2018-01-28','05:56:43'),
('008','012','009','004','007',100347,'HKD','2018-02-09','06:54:03'),
('009','005','007','002','005',48625,'HKD','2018-02-15','03:17:15'),
('010','007','010','005','001',11584,'Pound','2018-02-20','00:09:25'),
('011','014','013','005','005',11017,'US Dollar','2018-02-27','19:37:23'),
('012','005','014','002','005',108026,'Yuan','2018-03-07','11:12:33'),
('013','014','005','005','002',58196,'HKD','2018-03-07','14:13:07'),
('014','010','006','001','004',137233,'HKD','2018-03-14','19:21:37'),
('015','014','004','005','002',11919,'Pound','2018-03-20','00:42:31'),
('016','004','006','002','004',99575,'HKD','2018-03-23','10:23:06'),
('017','006','013','004','005',15735,'US Dollar','2018-03-26','01:35:03'),
('018','007','012','005','004',58157,'HKD','2018-04-15','16:57:27'),
('019','006','007','004','005',66011,'HKD','2018-05-10','05:41:24'),
('020','015','010','005','001',9562,'Pound','2018-05-15','16:46:12'),
('021','001','007','001','005',139589,'HKD','2018-05-30','04:53:55'),
('022','005','013','002','005',14385,'US Dollar','2018-06-01','11:20:32'),
('023','010','015','001','005',8457,'US Dollar','2018-06-06','12:50:51'),
('024','011','005','002','002',121134,'HKD','2018-06-15','03:13:18'),
('025','006','007','004','005',2301,'HKD','2018-06-17','22:51:44'),
('026','014','005','005','002',113350,'HKD','2018-06-24','04:37:28'),
('027','014','006','005','004',152061,'HKD','2018-07-02','03:29:34'),
('028','007','009','005','007',48454,'HKD','2018-07-03','20:57:23'),
('029','007','001','005','001',4498,'Pound','2018-07-07','16:09:43'),
('030','005','013','002','005',1658,'US Dollar','2018-07-10','23:36:22'),
('031','009','007','007','005',128848,'HKD','2018-07-12','02:18:12'),
('032','004','009','002','007',140119,'HKD','2018-07-17','06:22:54'),
('033','012','015','004','005',19249,'US Dollar','2018-07-22','07:59:53'),
('034','001','006','001','004',60778,'HKD','2018-07-26','01:36:10'),
('035','004','014','002','005',73242,'Yuan','2018-07-26','10:03:02'),
('036','010','013','001','005',9379,'US Dollar','2018-07-27','11:38:39'),
('037','010','011','001','002',974,'Pound','2018-07-31','11:08:05'),
('038','009','014','007','005',108723,'Yuan','2018-08-01','16:30:24'),
('039','010','005','001','002',107484,'HKD','2018-08-02','18:49:48'),
('040','004','010','002','001',2708,'Pound','2018-08-05','18:06:28'),
('041','007','014','005','005',31066,'Yuan','2018-08-08','21:14:14'),
('042','014','005','005','002',99255,'HKD','2018-08-26','18:55:18'),
('043','009','013','007','005',6605,'US Dollar','2018-09-02','17:35:25'),
('044','010','015','001','005',9790,'US Dollar','2018-09-13','17:29:03'),
('045','015','009','005','007',41613,'HKD','2018-09-17','20:35:02'),
('046','006','009','004','007',127390,'HKD','2018-09-19','11:34:30'),
('047','011','010','002','001',2602,'Pound','2018-09-22','08:01:01'),
('048','014','010','005','001',13270,'Pound','2018-10-07','00:11:16'),
('049','004','006','002','004',13712,'HKD','2018-10-14','21:28:13'),
('050','007','004','005','002',13252,'Pound','2018-10-17','21:11:07'),
('051','013','009','005','007',10280,'HKD','2018-10-18','14:08:12'),
('052','004','013','002','005',12303,'US Dollar','2018-10-20','03:55:57'),
('053','001','013','001','005',11770,'US Dollar','2018-10-24','10:56:32'),
('054','011','014','002','005',32256,'Yuan','2018-10-26','08:20:28'),
('055','011','001','002','001',3592,'Pound','2018-10-31','22:34:31'),
('056','005','004','002','002',9889,'Pound','2018-11-06','15:44:30'),
('057','012','001','004','001',8684,'Pound','2018-11-17','15:25:32'),
('058','001','014','001','005',3386,'Yuan','2018-11-21','14:58:53'),
('059','009','005','007','002',105386,'HKD','2018-11-25','05:52:11'),
('060','015','007','005','005',37791,'HKD','2018-11-26','00:07:54'),
('061','011','014','002','005',100954,'Yuan','2018-11-30','14:17:10'),
('062','010','001','001','001',13519,'Pound','2018-12-04','11:51:16'),
('063','004','011','002','002',13799,'Pound','2018-12-04','21:32:25'),
('064','013','006','005','004',110830,'HKD','2018-12-12','22:43:42'),
('065','009','001','007','001',13697,'Pound','2018-12-15','00:58:37'),
('066','012','001','004','001',4100,'Pound','2018-12-23','10:21:36'),
('067','001','004','001','002',1918,'Pound','2018-12-28','04:37:28'),
('068','015','012','005','004',99473,'HKD','2019-01-13','23:44:29'),
('069','012','005','004','002',27066,'HKD','2019-01-15','13:09:23'),
('070','004','015','002','005',15724,'US Dollar','2019-01-16','18:31:20'),
('071','004','012','002','004',112055,'HKD','2019-01-17','16:50:57'),
('072','009','013','007','005',2477,'US Dollar','2019-01-21','06:13:07'),
('073','005','011','002','002',4739,'Pound','2019-01-24','21:14:32'),
('074','009','013','007','005',999,'US Dollar','2019-01-24','22:30:37'),
('075','015','012','005','004',93662,'HKD','2019-01-29','23:50:36'),
('076','012','015','004','005',15678,'US Dollar','2019-02-01','00:07:07'),
('077','005','015','002','005',10259,'US Dollar','2019-02-03','14:56:42'),
('078','015','006','005','004',152482,'HKD','2019-02-15','05:36:57'),
('079','009','012','007','004',27253,'HKD','2019-02-19','00:04:44'),
('080','011','014','002','005',115539,'Yuan','2019-02-19','20:25:35'),
('081','013','012','005','004',38501,'HKD','2019-02-21','16:26:14'),
('082','013','012','005','004',35997,'HKD','2019-03-11','05:01:15'),
('083','015','001','005','001',8832,'Pound','2019-03-12','00:24:13'),
('084','001','011','001','002',12449,'Pound','2019-03-22','18:22:07'),
('085','005','010','002','001',11355,'Pound','2019-03-28','16:57:45'),
('086','001','013','001','005',1311,'US Dollar','2019-03-28','22:46:42'),
('087','006','011','004','002',9826,'Pound','2019-03-30','07:32:43'),
('088','012','010','004','001',6152,'Pound','2019-04-01','07:39:47'),
('089','001','014','001','005',81978,'Yuan','2019-04-11','20:25:34'),
('090','011','006','002','004',6521,'HKD','2019-04-12','00:34:50'),
('091','013','010','005','001',4241,'Pound','2019-04-25','04:39:02'),
('092','004','015','002','005',2748,'US Dollar','2019-04-27','13:45:11'),
('093','014','013','005','005',18122,'US Dollar','2019-05-03','15:20:40'),
('094','010','009','001','007',112772,'HKD','2019-05-04','17:36:35'),
('095','001','006','001','004',141609,'HKD','2019-05-12','14:41:18'),
('096','009','010','007','001',1579,'Pound','2019-05-15','12:55:29'),
('097','011','009','002','007',144378,'HKD','2019-05-29','16:42:11'),
('098','005','006','002','004',65372,'HKD','2019-06-11','13:42:21'),
('099','005','004','002','002',8266,'Pound','2019-06-19','15:01:39'),
('100','009','010','007','001',14141,'Pound','2019-06-23','18:37:48'),
('101','005','012','002','004',8455,'HKD','2019-06-24','11:20:16'),
('102','006','004','004','002',5902,'Pound','2019-06-26','07:51:58'),
('103','014','005','005','002',140509,'HKD','2019-06-27','00:31:41'),
('104','006','011','004','002',5675,'Pound','2019-06-29','02:56:24'),
('105','012','010','004','001',12979,'Pound','2019-07-01','14:44:43'),
('106','011','015','002','005',3756,'US Dollar','2019-07-02','21:41:02'),
('107','015','010','005','001',10467,'Pound','2019-07-10','02:10:06'),
('108','015','010','005','001',7580,'Pound','2019-07-11','23:28:56'),
('109','001','012','001','004',64498,'HKD','2019-07-22','05:53:36'),
('110','006','004','004','002',5464,'Pound','2019-07-28','07:40:38'),
('111','007','006','005','004',132444,'HKD','2019-07-31','08:42:45'),
('112','004','005','002','002',56425,'HKD','2019-08-05','14:19:27'),
('113','007','005','005','002',136555,'HKD','2019-08-11','02:01:54'),
('114','007','013','005','005',15331,'US Dollar','2019-08-20','12:18:31'),
('115','005','001','002','001',262,'Pound','2019-08-21','13:29:47'),
('116','009','010','007','001',9228,'Pound','2019-08-22','20:30:21'),
('117','010','013','001','005',7367,'US Dollar','2019-09-02','20:39:14'),
('118','014','006','005','004',43009,'HKD','2019-09-05','16:56:12'),
('119','001','009','001','007',84427,'HKD','2019-09-06','21:51:50'),
('120','009','015','007','005',4862,'US Dollar','2019-09-15','21:34:42'),
('121','014','012','005','004',63866,'HKD','2019-09-19','01:47:39'),
('122','015','005','005','002',151211,'HKD','2019-09-26','08:52:30'),
('123','009','013','007','005',1313,'US Dollar','2019-10-04','13:10:37'),
('124','010','001','001','001',5568,'Pound','2019-10-10','09:42:53'),
('125','009','013','007','005',19518,'US Dollar','2019-10-14','18:01:40'),
('126','012','011','004','002',14189,'Pound','2019-10-23','17:56:28'),
('127','009','015','007','005',3390,'US Dollar','2019-10-26','07:14:54'),
('128','010','014','001','005',45523,'Yuan','2019-10-30','13:17:49'),
('129','006','015','004','005',19792,'US Dollar','2019-10-31','01:30:46'),
('130','012','011','004','002',979,'Pound','2019-11-04','01:34:18'),
('131','007','009','005','007',51082,'HKD','2019-11-07','12:03:31'),
('132','014','009','005','007',45677,'HKD','2019-11-14','18:00:28'),
('133','006','014','004','005',28390,'Yuan','2019-11-22','08:04:14'),
('134','012','001','004','001',1284,'Pound','2019-11-29','01:28:46'),
('135','005','004','002','002',4655,'Pound','2019-11-29','17:13:58'),
('136','014','001','005','001',12935,'Pound','2019-12-01','17:37:08'),
('137','005','012','002','004',93475,'HKD','2019-12-01','23:01:03'),
('138','014','012','005','004',12613,'HKD','2019-12-02','01:31:29'),
('139','001','004','001','002',14382,'Pound','2019-12-07','14:01:54'),
('140','010','007','001','005',19781,'HKD','2019-12-16','14:18:37'),
('141','004','013','002','005',9805,'US Dollar','2019-12-18','09:25:14'),
('142','013','015','005','005',8076,'US Dollar','2019-12-20','14:45:44'),
('143','014','012','005','004',116602,'HKD','2019-12-22','02:40:21'),
('144','009','006','007','004',45653,'HKD','2019-12-22','15:15:49'),
('145','012','007','004','005',65598,'HKD','2019-12-29','15:54:51'),
('146','014','001','005','001',10451,'Pound','2020-01-04','07:03:32'),
('147','012','014','004','005',99213,'Yuan','2020-01-06','07:04:07'),
('148','015','011','005','002',8621,'Pound','2020-01-06','11:10:28'),
('149','012','011','004','002',4281,'Pound','2020-01-08','01:39:57'),
('150','006','011','004','002',10171,'Pound','2020-01-15','08:17:03'),
('151','010','007','001','005',127585,'HKD','2020-02-04','00:00:19'),
('152','011','014','002','005',70323,'Yuan','2020-02-09','12:08:01'),
('153','004','015','002','005',15629,'US Dollar','2020-02-11','02:20:14'),
('154','010','012','001','004',125954,'HKD','2020-02-21','09:35:49'),
('155','006','005','004','002',86783,'HKD','2020-02-25','06:17:51'),
('156','015','006','005','004',43766,'HKD','2020-02-26','14:07:26'),
('157','015','012','005','004',137171,'HKD','2020-03-09','16:20:34'),
('158','011','015','002','005',9203,'US Dollar','2020-03-12','20:20:18'),
('159','006','005','004','002',21668,'HKD','2020-03-17','21:56:41'),
('160','011','012','002','004',45256,'HKD','2020-03-24','03:23:17'),
('161','011','006','002','004',128482,'HKD','2020-03-30','19:05:57'),
('162','010','012','001','004',21286,'HKD','2020-04-08','13:21:24'),
('163','006','007','004','005',26434,'HKD','2020-04-10','19:34:39'),
('164','009','007','007','005',10881,'HKD','2020-04-13','02:06:13'),
('165','006','011','004','002',10378,'Pound','2020-04-16','09:17:45'),
('166','014','009','005','007',136789,'HKD','2020-04-23','04:18:31'),
('167','013','014','005','005',31514,'Yuan','2020-04-27','01:08:57'),
('168','005','010','002','001',10036,'Pound','2020-04-28','02:21:45'),
('169','015','001','005','001',2478,'Pound','2020-05-17','03:55:08'),
('170','010','005','001','002',86861,'HKD','2020-05-20','07:53:32'),
('171','013','010','005','001',4459,'Pound','2020-05-22','01:22:29'),
('172','007','015','005','005',5777,'US Dollar','2020-05-23','22:46:51'),
('173','013','015','005','005',9486,'US Dollar','2020-05-26','19:06:18'),
('174','010','012','001','004',150329,'HKD','2020-05-31','07:28:09'),
('175','001','014','001','005',65229,'Yuan','2020-05-31','12:27:43'),
('176','006','010','004','001',14415,'Pound','2020-06-13','16:15:04'),
('177','012','004','004','002',2246,'Pound','2020-06-18','11:14:09'),
('178','015','006','005','004',23275,'HKD','2020-06-21','17:18:31'),
('179','006','014','004','005',55437,'Yuan','2020-07-03','10:11:22'),
('180','009','015','007','005',4258,'US Dollar','2020-07-21','18:03:14'),
('181','009','005','007','002',32776,'HKD','2020-07-26','08:52:44'),
('182','009','014','007','005',40128,'Yuan','2020-07-27','06:14:50'),
('183','010','007','001','005',95410,'HKD','2020-07-30','23:33:50'),
('184','014','005','005','002',88561,'HKD','2020-08-08','16:58:19'),
('185','006','013','004','005',13773,'US Dollar','2020-08-16','10:54:11'),
('186','007','012','005','004',32487,'HKD','2020-08-31','08:39:02'),
('187','004','011','002','002',9858,'Pound','2020-09-04','06:35:29'),
('188','011','013','002','005',19024,'US Dollar','2020-09-12','08:24:29'),
('189','004','006','002','004',6162,'HKD','2020-09-17','00:58:01'),
('190','009','001','007','001',7840,'Pound','2020-09-19','12:12:36'),
('191','004','013','002','005',12450,'US Dollar','2020-09-25','14:42:29'),
('192','004','007','002','005',122842,'HKD','2020-10-09','03:47:27'),
('193','012','005','004','002',71877,'HKD','2020-10-25','05:01:19'),
('194','004','007','002','005',10468,'HKD','2020-10-27','13:04:37'),
('195','007','015','005','005',2850,'US Dollar','2020-10-31','06:03:59'),
('196','007','010','005','001',11582,'Pound','2020-11-03','02:36:10'),
('197','001','004','001','002',172,'Pound','2020-11-03','11:36:14'),
('198','006','012','004','004',102617,'HKD','2020-11-12','06:27:57'),
('199','005','014','002','005',12755,'Yuan','2020-11-14','01:46:55'),
('200','005','007','002','005',69623,'HKD','2020-11-18','11:33:38'),
('201','010','015','001','005',10552,'US Dollar','2020-11-22','11:45:47'),
('202','013','011','005','002',7298,'Pound','2020-11-27','20:57:38'),
('203','005','015','002','005',17006,'US Dollar','2020-11-28','11:18:37'),
('204','014','010','005','001',1675,'Pound','2020-12-04','19:27:54'),
('205','001','009','001','007',23548,'HKD','2020-12-07','02:15:38'),
('206','010','014','001','005',24826,'Yuan','2020-12-08','14:07:00'),
('207','012','005','004','002',124839,'HKD','2020-12-16','20:56:39'),
('208','014','015','005','005',7722,'US Dollar','2020-12-17','05:54:30'),
('209','013','015','005','005',13606,'US Dollar','2020-12-21','19:41:22'),
('210','006','015','004','005',9732,'US Dollar','2020-12-24','13:58:15'),
('211','009','004','007','002',704,'Pound','2020-12-24','15:38:02'),
('212','001','009','001','007',63515,'HKD','2020-12-25','16:14:06'),
('213','013','006','005','004',92804,'HKD','2021-01-01','16:46:38'),
('214','006','015','004','005',2260,'US Dollar','2021-01-08','04:51:51'),
('215','004','015','002','005',352,'US Dollar','2021-01-14','11:39:22'),
('216','005','015','002','005',3094,'US Dollar','2021-01-16','04:19:40'),
('217','007','004','005','002',559,'Pound','2021-01-22','07:17:58'),
('218','001','015','001','005',12129,'US Dollar','2021-01-22','17:21:00'),
('219','012','001','004','001',13934,'Pound','2021-01-23','23:12:52'),
('220','005','001','002','001',10520,'Pound','2021-02-03','15:07:54'),
('221','006','004','004','002',13462,'Pound','2021-02-12','09:11:04'),
('222','012','005','004','002',30342,'HKD','2021-02-14','14:31:33'),
('223','012','006','004','004',55450,'HKD','2021-02-16','04:08:05'),
('224','005','012','002','004',47104,'HKD','2021-02-22','07:37:28'),
('225','007','006','005','004',43898,'HKD','2021-02-25','14:21:26'),
('226','006','014','004','005',49427,'Yuan','2021-02-26','15:16:32'),
('227','013','011','005','002',5818,'Pound','2021-03-12','19:59:22'),
('228','006','007','004','005',102859,'HKD','2021-03-13','08:37:10'),
('229','006','001','004','001',1796,'Pound','2021-03-19','15:08:51'),
('230','010','015','001','005',18988,'US Dollar','2021-03-22','20:27:58'),
('231','011','009','002','007',147069,'HKD','2021-03-24','13:47:51'),
('232','014','011','005','002',13499,'Pound','2021-03-25','23:03:45'),
('233','004','013','002','005',1415,'US Dollar','2021-04-06','13:49:53'),
('234','012','013','004','005',18146,'US Dollar','2021-04-26','21:41:33'),
('235','005','012','002','004',113810,'HKD','2021-05-04','07:38:16'),
('236','014','010','005','001',6134,'Pound','2021-05-10','06:59:46'),
('237','014','005','005','002',53563,'HKD','2021-05-19','06:17:42'),
('238','004','011','002','002',2102,'Pound','2021-05-26','00:27:34'),
('239','001','006','001','004',80083,'HKD','2021-05-28','06:21:03'),
('240','011','001','002','001',13985,'Pound','2021-05-29','00:54:21'),
('241','006','011','004','002',14684,'Pound','2021-05-30','07:05:11'),
('242','005','011','002','002',973,'Pound','2021-06-03','09:53:11'),
('243','013','012','005','004',43914,'HKD','2021-06-11','20:36:31'),
('244','007','015','005','005',3630,'US Dollar','2021-06-21','22:52:45'),
('245','012','010','004','001',10809,'Pound','2021-07-06','03:52:28'),
('246','010','011','001','002',10745,'Pound','2021-07-08','17:26:09'),
('247','013','015','005','005',4257,'US Dollar','2021-07-11','17:08:13'),
('248','010','011','001','002',14063,'Pound','2021-07-15','04:08:49'),
('249','015','004','005','002',8132,'Pound','2021-07-21','16:48:32'),
('250','007','004','005','002',12307,'Pound','2021-07-24','20:24:23'),
('251','015','007','005','005',59717,'HKD','2021-07-29','01:00:11'),
('252','011','001','002','001',5667,'Pound','2021-08-02','00:34:20'),
('253','007','006','005','004',115580,'HKD','2021-08-06','07:10:37'),
('254','015','009','005','007',64709,'HKD','2021-08-09','22:01:49'),
('255','005','014','002','005',18707,'Yuan','2021-08-12','06:52:34'),
('256','013','015','005','005',4399,'US Dollar','2021-08-20','14:18:01'),
('257','015','006','005','004',26021,'HKD','2021-08-24','11:44:21'),
('258','015','014','005','005',85613,'Yuan','2021-09-03','11:25:23'),
('259','010','007','001','005',5054,'HKD','2021-09-11','11:28:29'),
('260','014','010','005','001',3380,'Pound','2021-09-13','23:27:00'),
('261','007','010','005','001',12410,'Pound','2021-09-14','12:10:01'),
('262','006','015','004','005',10014,'US Dollar','2021-09-23','07:08:49'),
('263','013','015','005','005',1964,'US Dollar','2021-09-23','16:26:31'),
('264','004','009','002','007',128521,'HKD','2021-09-24','15:25:46'),
('265','014','013','005','005',3069,'US Dollar','2021-09-30','03:48:08'),
('266','005','006','002','004',128567,'HKD','2021-10-11','18:34:29'),
('267','014','005','005','002',55442,'HKD','2021-10-17','13:29:40'),
('268','006','014','004','005',4224,'Yuan','2021-10-18','08:32:53'),
('269','014','007','005','005',92375,'HKD','2021-11-01','05:15:08'),
('270','004','013','002','005',6163,'US Dollar','2021-11-03','21:52:43'),
('271','014','013','005','005',16478,'US Dollar','2021-11-05','03:47:59');

INSERT INTO Product (product_id, type, price, holdings, issuer) VALUES
('001','A1',100,'NULL','NULL'),
('002','B2',200,'NULL','NULL'),
('003','C3',10,'NULL','NULL'),
('004','D4',10,'NULL','NULL');

INSERT INTO Loan (loan_id, interest_rate) VALUES
('001',5000),
('002',4955);

INSERT INTO Product_contain (product_id, account_id, holdings, product_values) VALUES
('001','002','NULL',100000),
('002','002','NULL',100000),
('004','002','NULL',100000),
('003','003','NULL',100000);

INSERT INTO Loan_contain (loan_id, account_id, borrow_time, next_due_time, unpaid_amount) VALUES
('001','010','2020-09-01','2022-09-01',1000000),
('002','011','2020-09-01','2022-09-01',1000000);

INSERT INTO Login_history(timepoint, customer_id) VALUES
('1952-05-20 00:00:00','002'),
('1952-05-20 00:20:00','001'),
('1952-05-20 00:30:00','001'),
('1960-05-20 00:10:00','002'),
('1960-05-20 00:30:00','001'),
('1970-05-20 01:00:00','001'),
('1970-05-20 10:00:00','002'),
('2019-01-02 12:42:24','004'),
('2019-01-02 21:54:38','006'),
('2019-01-05 23:50:37','005'),
('2019-01-09 05:16:46','002'),
('2019-01-13 23:01:48','007'),
('2019-01-14 03:51:09','003'),
('2019-01-16 15:31:00','004'),
('2019-01-19 15:18:59','001'),
('2019-01-23 17:26:00','001'),
('2019-02-03 20:32:26','005'),
('2019-02-05 10:50:13','001'),
('2019-02-08 08:47:09','005'),
('2019-02-09 02:30:42','006'),
('2019-02-15 00:39:10','002'),
('2019-02-15 14:25:09','004'),
('2019-02-17 18:24:19','004'),
('2019-02-18 20:16:59','002'),
('2019-02-26 07:25:56','002'),
('2019-03-05 12:55:14','007'),
('2019-03-11 13:24:50','006'),
('2019-03-13 23:05:34','005'),
('2019-03-19 00:52:58','002'),
('2019-03-19 06:31:12','004'),
('2019-03-20 07:41:03','002'),
('2019-03-26 16:47:39','004'),
('2019-03-29 16:51:13','004'),
('2019-03-29 19:16:19','004'),
('2019-03-31 22:44:44','004'),
('2019-04-04 09:19:28','005'),
('2019-04-11 03:05:57','003'),
('2019-04-15 08:34:12','001'),
('2019-04-21 22:57:35','004'),
('2019-04-23 21:54:31','003'),
('2019-04-24 12:27:51','001'),
('2019-04-25 01:56:32','004'),
('2019-04-25 12:33:36','005'),
('2019-04-26 14:20:37','006'),
('2019-05-20 23:48:43','006'),
('2019-05-23 12:25:22','006'),
('2019-05-29 23:27:48','002'),
('2019-06-05 21:40:32','002'),
('2019-06-12 18:12:05','007'),
('2019-06-13 05:22:34','003'),
('2019-06-14 10:40:28','005'),
('2019-06-21 22:16:34','006'),
('2019-06-23 21:36:43','005'),
('2019-06-25 17:39:51','005'),
('2019-06-25 23:04:07','003'),
('2019-06-25 23:48:35','007'),
('2019-06-26 17:38:02','003'),
('2019-06-28 11:40:15','001'),
('2019-07-01 13:58:25','003'),
('2019-07-02 03:38:33','001'),
('2019-07-06 15:14:12','007'),
('2019-07-08 15:47:07','001'),
('2019-07-12 15:34:47','002'),
('2019-07-14 11:30:58','001'),
('2019-07-15 11:49:57','004'),
('2019-07-17 15:30:13','001'),
('2019-07-19 10:44:43','003'),
('2019-07-19 20:25:50','005'),
('2019-08-02 05:01:04','002'),
('2019-08-03 22:40:38','004'),
('2019-08-11 08:15:44','003'),
('2019-08-15 20:00:14','001'),
('2019-08-26 08:57:56','001'),
('2019-08-27 01:58:02','004'),
('2019-08-31 13:38:06','005'),
('2019-09-08 01:34:07','005'),
('2019-09-10 17:17:38','001'),
('2019-09-12 15:11:48','007'),
('2019-09-18 09:48:38','001'),
('2019-09-27 19:45:00','006'),
('2019-10-01 13:51:51','006'),
('2019-10-07 20:16:13','006'),
('2019-10-08 10:41:17','004'),
('2019-10-11 21:23:14','007'),
('2019-10-12 12:26:47','006'),
('2019-10-13 16:58:22','007'),
('2019-10-17 04:24:25','002'),
('2019-10-18 03:29:01','007'),
('2019-10-18 19:45:17','003'),
('2019-10-27 01:56:57','005'),
('2019-10-27 12:44:01','007'),
('2019-10-30 09:48:21','004'),
('2019-11-07 14:19:53','006'),
('2019-11-10 09:43:08','002'),
('2019-11-12 09:45:43','007'),
('2019-11-19 19:36:48','003'),
('2019-11-21 05:29:18','004'),
('2019-11-22 04:37:57','007'),
('2019-11-24 12:52:19','006'),
('2019-11-24 18:06:21','002'),
('2019-12-03 22:13:26','007'),
('2019-12-09 07:11:53','002'),
('2019-12-12 09:09:58','003'),
('2019-12-13 03:07:29','007'),
('2019-12-13 14:52:26','007'),
('2019-12-20 21:24:06','007'),
('2019-12-30 11:42:15','007'),
('2020-01-01 16:31:13','007'),
('2020-01-05 02:13:56','004'),
('2020-01-09 08:15:55','006'),
('2020-01-10 09:03:51','007'),
('2020-01-15 13:57:59','002'),
('2020-01-23 00:20:43','005'),
('2020-01-23 22:14:44','007'),
('2020-01-24 14:13:39','005'),
('2020-01-25 23:35:59','001'),
('2020-01-27 06:36:37','002'),
('2020-01-28 02:21:05','006'),
('2020-01-29 03:33:59','003'),
('2020-01-31 10:50:36','001'),
('2020-02-07 10:53:16','005'),
('2020-02-09 05:00:33','007'),
('2020-02-13 15:04:01','006'),
('2020-02-15 18:00:28','003'),
('2020-02-16 05:45:37','001'),
('2020-02-17 04:15:53','002'),
('2020-02-18 16:47:46','007'),
('2020-02-21 09:48:41','002'),
('2020-02-26 07:42:30','001'),
('2020-02-29 09:40:49','006'),
('2020-03-06 14:26:08','005'),
('2020-03-07 23:04:16','005'),
('2020-03-15 19:59:45','005'),
('2020-03-23 06:39:54','006'),
('2020-04-02 13:04:20','001'),
('2020-04-02 16:57:34','007'),
('2020-04-05 23:08:17','001'),
('2020-04-12 03:10:34','003'),
('2020-04-27 19:20:51','004'),
('2020-05-01 02:39:45','003'),
('2020-05-10 18:02:49','003'),
('2020-05-11 13:56:00','002'),
('2020-05-11 21:17:57','006'),
('2020-05-12 16:26:35','002'),
('2020-05-18 04:38:38','005'),
('2020-05-22 03:01:55','004'),
('2020-05-24 22:21:23','002'),
('2020-05-30 12:52:11','001'),
('2020-05-30 22:46:14','002'),
('2020-06-15 08:50:00','004'),
('2020-06-16 04:02:12','006'),
('2020-06-20 14:15:50','001'),
('2020-06-23 14:27:40','004'),
('2020-06-25 14:11:14','001'),
('2020-06-25 20:22:16','001'),
('2020-06-26 02:11:17','003'),
('2020-06-26 09:07:31','004'),
('2020-06-26 12:36:29','001'),
('2020-07-02 09:25:58','003'),
('2020-07-06 09:05:13','004'),
('2020-07-22 16:34:39','003'),
('2020-07-25 20:11:25','004'),
('2020-07-27 19:31:03','004'),
('2020-07-28 01:28:34','007'),
('2020-07-30 14:26:15','003'),
('2020-08-03 03:52:01','006'),
('2020-08-08 05:06:43','002'),
('2020-08-09 22:37:13','007'),
('2020-08-10 07:15:45','003'),
('2020-08-12 15:22:55','003'),
('2020-08-15 11:51:18','007'),
('2020-08-16 08:48:07','004'),
('2020-08-19 07:12:15','002'),
('2020-08-21 08:27:55','007'),
('2020-09-03 11:33:50','002'),
('2020-09-05 07:39:47','003'),
('2020-09-11 00:41:01','001'),
('2020-09-16 02:58:25','004'),
('2020-09-17 05:09:39','002'),
('2020-09-18 06:51:49','006'),
('2020-09-19 10:03:08','002'),
('2020-09-25 02:50:49','007'),
('2020-10-04 11:26:24','005'),
('2020-10-04 17:19:52','006'),
('2020-10-09 08:10:47','004'),
('2020-10-14 01:25:49','006'),
('2020-10-15 00:56:47','002'),
('2020-10-15 07:38:10','001'),
('2020-10-16 13:25:55','004'),
('2020-10-21 22:57:54','006'),
('2020-10-27 17:12:25','004'),
('2020-11-01 18:20:43','007'),
('2020-11-04 20:28:24','005'),
('2020-11-07 20:09:16','006'),
('2020-11-08 15:32:54','007'),
('2020-11-13 00:09:56','007'),
('2020-11-14 06:00:31','006'),
('2020-11-16 03:33:24','001'),
('2020-11-26 03:38:06','004'),
('2020-11-26 05:37:20','004'),
('2020-11-29 16:33:36','005'),
('2020-12-02 16:44:22','007'),
('2020-12-07 11:05:28','002'),
('2020-12-07 14:21:54','006'),
('2020-12-13 04:57:11','003'),
('2020-12-15 06:24:28','007'),
('2020-12-17 11:54:52','006'),
('2020-12-24 12:27:01','006'),
('2020-12-25 00:20:46','003'),
('2020-12-27 19:03:04','007'),
('2020-12-31 15:11:39','003'),
('2021-01-01 16:30:15','007'),
('2021-01-09 04:56:17','005'),
('2021-01-11 18:09:50','001'),
('2021-01-13 18:45:52','007'),
('2021-01-15 19:07:05','007'),
('2021-01-15 19:44:47','001'),
('2021-01-21 00:04:17','004'),
('2021-01-22 03:36:11','005'),
('2021-01-22 11:52:50','007'),
('2021-01-23 12:06:09','007'),
('2021-01-30 23:35:49','001'),
('2021-02-04 21:41:35','005'),
('2021-02-05 14:38:31','001'),
('2021-02-06 04:41:47','007'),
('2021-02-21 20:55:01','006'),
('2021-02-22 22:12:45','007'),
('2021-02-23 13:44:27','006'),
('2021-02-24 17:06:28','006'),
('2021-02-27 20:42:48','001'),
('2021-03-04 18:44:18','005'),
('2021-03-10 00:20:30','002'),
('2021-03-21 07:28:56','004'),
('2021-03-24 03:33:56','004'),
('2021-03-25 16:02:20','002'),
('2021-03-31 05:36:03','001'),
('2021-03-31 21:29:19','001'),
('2021-04-02 09:09:49','001'),
('2021-04-07 10:12:22','007'),
('2021-04-13 07:00:00','007'),
('2021-04-15 17:47:02','002'),
('2021-04-27 18:59:16','003'),
('2021-04-30 23:20:28','005'),
('2021-05-02 17:14:04','007'),
('2021-05-07 07:56:40','002'),
('2021-05-10 06:07:10','006'),
('2021-05-14 12:47:24','006'),
('2021-05-18 20:27:28','006'),
('2021-05-28 07:01:06','001'),
('2021-05-30 01:08:31','003'),
('2021-05-30 10:30:37','002'),
('2021-06-08 09:03:11','004'),
('2021-06-12 16:13:49','006'),
('2021-06-17 13:23:38','003'),
('2021-06-22 13:13:00','004'),
('2021-06-24 11:54:37','001'),
('2021-06-28 18:46:38','002'),
('2021-06-29 19:50:49','002'),
('2021-06-30 00:46:15','006'),
('2021-07-01 17:52:32','005'),
('2021-07-06 02:00:45','003'),
('2021-07-06 04:58:37','006'),
('2021-07-06 15:01:55','001'),
('2021-07-07 02:19:58','001'),
('2021-07-08 16:37:25','003'),
('2021-07-09 19:10:52','002'),
('2021-07-13 07:07:09','007'),
('2021-07-16 19:14:15','003'),
('2021-07-22 08:35:03','001'),
('2021-07-29 04:53:50','003'),
('2021-07-29 14:10:38','001'),
('2021-08-03 18:23:57','004'),
('2021-08-06 09:57:31','004'),
('2021-08-06 15:39:39','007'),
('2021-08-10 22:02:47','003'),
('2021-08-11 16:38:03','007'),
('2021-08-12 15:23:16','002'),
('2021-08-17 00:47:43','001'),
('2021-08-17 15:24:28','006'),
('2021-08-19 17:01:08','001'),
('2021-08-25 18:57:59','006'),
('2021-08-28 00:20:43','002'),
('2021-08-29 22:47:43','004'),
('2021-09-05 17:24:24','003'),
('2021-09-07 23:00:58','006'),
('2021-09-09 23:19:39','004'),
('2021-09-11 04:22:09','004'),
('2021-09-16 08:20:44','006'),
('2021-09-18 10:49:05','004'),
('2021-09-19 01:12:44','005'),
('2021-09-19 14:46:23','001'),
('2021-09-20 19:40:07','006'),
('2021-09-25 18:22:41','007'),
('2021-09-26 23:50:43','006'),
('2021-09-29 02:42:55','001'),
('2021-10-03 01:09:51','001'),
('2021-10-03 07:42:54','001'),
('2021-10-04 18:47:56','002'),
('2021-10-05 17:45:16','006'),
('2021-10-09 13:34:17','006'),
('2021-10-10 14:28:42','004'),
('2021-10-11 11:55:05','006'),
('2021-10-12 13:20:08','001'),
('2021-10-29 02:27:48','004'),
('2021-11-12 11:12:38','003'),
('2021-11-12 21:11:23','006'),
('2021-11-14 14:05:49','005');

