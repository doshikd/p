-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: 127.127.126.50    Database: shoe_store
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address` (
  `index` int NOT NULL,
  `city` varchar(45) NOT NULL,
  `street` varchar(45) NOT NULL,
  `house` varchar(5) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (420151,'Лесной','Вишневая','32',1),(125061,'Лесной','Подгорная','8',2),(630370,'Лесной','Шоссейная','24',3),(400562,'Лесной','Зеленая','32',4),(614510,'Лесной','Маяковского','47',5),(410542,'Лесной','Светлая','46',6),(620839,'Лесной','Цветочная','8',7),(443890,'Лесной','Коммунистическая','1',8),(603379,'Лесной','Спортивная','46',9),(603721,'Лесной','Гоголя','41',10),(410172,'Лесной','Северная','13',11),(614611,'Лесной','Молодежная','50',12),(454311,'Лесной','Новая','19',13),(660007,'Лесной','Октябрьская','19',14),(603036,'Лесной','Садовая','4',15),(394060,'Лесной','Фрунзе','43',16),(410661,'Лесной','Школьная','50',17),(625590,'Лесной','Коммунистическая','20',18),(450983,'Лесной','Комсомольская','26',19),(394782,'Лесной','Чехова','3',20),(603002,'Лесной','Дзержинского','28',21),(450558,'Лесной','Набережная','30',22),(344288,'Лесной','Чехова','1',23),(614164,'Лесной','Степная','30',24),(394242,'Лесной','Коммунистическая','43',25),(660540,'Лесной','Солнечная','25',26),(125837,'Лесной','Шоссейная','40',27),(125703,'Лесной','Партизанская','49',28),(625283,'Лесной','Победы','46',29),(614753,'Лесной','Полевая','35',30),(426030,'Лесной','Маяковского','44',31),(450375,'Лесной','Клубная','44',32),(625560,'Лесной','Некрасова','12',33),(630201,'Лесной','Комсомольская','17',34),(190949,'Лесной','Мичурина','26',35);
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturer`
--

DROP TABLE IF EXISTS `manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturer`
--

LOCK TABLES `manufacturer` WRITE;
/*!40000 ALTER TABLE `manufacturer` DISABLE KEYS */;
INSERT INTO `manufacturer` VALUES (1,'Kari'),(2,'Marco Tozzi'),(3,'Рос'),(4,'Rieker'),(5,'Alessio Nesca'),(6,'CROSBY');
/*!40000 ALTER TABLE `manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_date` date NOT NULL,
  `delivery_date` date DEFAULT NULL,
  `address_id` int NOT NULL,
  `user_id` int DEFAULT NULL,
  `receipt_code` varchar(6) NOT NULL,
  `status_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `address_id_idx` (`address_id`),
  KEY `user_id_idx` (`user_id`),
  KEY `status_id_idx` (`status_id`),
  CONSTRAINT `address_id` FOREIGN KEY (`address_id`) REFERENCES `address` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `status_id` FOREIGN KEY (`status_id`) REFERENCES `status` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,'2025-02-27','2025-04-20',1,4,'901',1),(2,'2022-09-28','2025-04-21',11,1,'902',1),(3,'2025-03-21','2025-04-22',2,2,'903',1),(4,'2025-02-20','2025-04-23',11,3,'904',1),(5,'2025-03-17','2025-04-24',2,4,'905',1),(6,'2025-03-01','2025-04-25',15,1,'906',1),(7,'2025-03-30','2025-04-26',3,2,'907',1),(8,'2025-03-31','2025-04-27',19,3,'908',2),(9,'2025-04-02','2025-04-28',5,4,'909',2),(10,'2025-04-03','2025-04-29',19,4,'910',2);
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_position`
--

DROP TABLE IF EXISTS `order_position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_position` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id_idx` (`order_id`),
  KEY `product_id_idx` (`product_id`),
  CONSTRAINT `order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_position`
--

LOCK TABLES `order_position` WRITE;
/*!40000 ALTER TABLE `order_position` DISABLE KEYS */;
INSERT INTO `order_position` VALUES (1,1,1,5),(2,2,2,3),(3,3,3,4);
/*!40000 ALTER TABLE `order_position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `article` varchar(45) DEFAULT NULL,
  `name` varchar(45) NOT NULL,
  `unit` varchar(5) NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `provider_id` int NOT NULL,
  `manufacturer_id` int NOT NULL,
  `category_id` int NOT NULL,
  `discount` int NOT NULL,
  `quantity_stock` int NOT NULL,
  `description` text,
  `image_path` varchar(300) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `provider_id_idx` (`provider_id`),
  KEY `manufacturer_id_idx` (`manufacturer_id`),
  KEY `category_id_idx` (`category_id`),
  CONSTRAINT `category_id` FOREIGN KEY (`category_id`) REFERENCES `product_category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `manufacturer_id` FOREIGN KEY (`manufacturer_id`) REFERENCES `manufacturer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `provider_id` FOREIGN KEY (`provider_id`) REFERENCES `provider` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('А112Т4','Ботинки','шт.',4990,1,1,1,3,6,'Женские Ботинки демисезонные kari','1.jpg',1),('F635R4','Ботинки','шт.',3244,2,2,1,2,13,'Ботинки Marco Tozzi женские демисезонные, размер 39, цвет бежевый','2.jpg',2),('H782T5','Туфли','шт.',4499,1,1,2,4,5,'Туфли kari мужские классика MYZ21AW-450A, размер 43, цвет: черный','3.jpg',3),('G783F5','Ботинки','шт.',5900,1,3,2,2,8,'Мужские ботинки Рос-Обувь кожаные с натуральным мехом','4.jpg',4),('J384T6','Ботинки','шт.',3800,2,4,2,2,16,'B3430/14 Полуботинки мужские Rieker','5.jpg',5),('D572U8','Кроссовки','шт.',4100,2,3,2,3,6,'129615-4 Кроссовки мужские','6.jpg',6),('F572H7','Туфли','шт.',2700,1,2,1,2,14,'Туфли Marco Tozzi женские летние, размер 39, цвет черный','7.jpg',7),('D329H3','Полуботинки','шт.',1890,2,5,1,4,4,'Полуботинки Alessio Nesca женские 3-30797-47, размер 37, цвет: бордовый','8.jpg',8),('B320R5','Туфли','шт.',4300,1,4,1,2,6,'Туфли Rieker женские демисезонные, размер 41, цвет коричневый','9.jpg',9),('G432E4','Туфли','шт.',2800,1,1,1,3,15,'Туфли kari женские TR-YR-413017, размер 37, цвет: черный','10.jpg',10),('S213E3','Полуботинки','шт.',2156,2,6,2,3,6,'407700/01-01 Полуботинки мужские CROSBY','',11),('E482R4','Полуботинки','шт.',1800,1,1,1,2,14,'Полуботинки kari женские MYZ20S-149, размер 41, цвет: черный','',12),('S634B5','Кеды','шт.',5500,2,6,2,3,0,'Кеды Caprice мужские демисезонные, размер 42, цвет черный','',13),('K345R4','Полуботинки','шт.',2100,2,6,2,2,3,'407700/01-02 Полуботинки мужские CROSBY','',14),('O754F4','Туфли','шт.',5400,2,4,1,4,18,'Туфли женские демисезонные Rieker артикул 55073-68/37','',15),('G531F4','Ботинки','шт.',6600,1,1,1,12,9,'Ботинки женские зимние ROMER арт. 893167-01 Черный','',16),('J542F5','Тапочки','шт.',500,1,1,2,13,0,'Тапочки мужские Арт.70701-55-67син р.41','',17),('B431R5','Ботинки','шт.',2700,2,4,2,2,5,'Мужские кожаные ботинки/мужские ботинки','',18),('P764G4','Туфли','шт.',6800,1,6,1,15,15,'Туфли женские, ARGO, размер 38','',19),('C436G5','Ботинки','шт.',10200,1,5,1,15,9,'Ботинки женские, ARGO, размер 40','',20),('F427R5','Ботинки','шт.',11800,2,4,1,15,11,'Ботинки на молнии с декоративной пряжкой FRAU','',21),('N457T5','Полуботинки','шт.',4600,1,6,1,3,13,'Полуботинки Ботинки черные зимние, мех','',22),('D364R4','Туфли','шт.',12400,1,1,1,16,5,'Туфли Luiza Belly женские Kate-lazo черные из натуральной замши','',23),('S326R5','Тапочки','шт.',9900,2,6,2,17,15,'Мужские кожаные тапочки \"Профиль С.Дали\"\" \"','',24),('L754R4','Полуботинки','шт.',1700,1,1,1,2,7,'Полуботинки kari женские WB2020SS-26, размер 38, цвет: черный','',25),('M542T5','Кроссовки','шт.',2800,2,4,2,18,3,'Кроссовки мужские TOFA','',26),('D268G5','Туфли','шт.',4399,2,4,1,3,12,'Туфли Rieker женские демисезонные, размер 36, цвет коричневый','',27),('T324F5','Сапоги','шт.',4699,1,6,1,2,5,'Сапоги замша Цвет: синий','',28),('K358H6','Тапочки','шт.',599,1,4,2,20,2,'Тапочки мужские син р.41','',29),('H535R5','Ботинки','шт.',2300,2,4,1,2,7,'Женские Ботинки демисезонные','',30);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_category`
--

DROP TABLE IF EXISTS `product_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_category`
--

LOCK TABLES `product_category` WRITE;
/*!40000 ALTER TABLE `product_category` DISABLE KEYS */;
INSERT INTO `product_category` VALUES (1,'Женская обувь'),(2,'Мужская обувь');
/*!40000 ALTER TABLE `product_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provider`
--

DROP TABLE IF EXISTS `provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provider` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider`
--

LOCK TABLES `provider` WRITE;
/*!40000 ALTER TABLE `provider` DISABLE KEYS */;
INSERT INTO `provider` VALUES (1,'Kari'),(2,'Обувь для вас');
/*!40000 ALTER TABLE `provider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Администратор'),(2,'Менеджер'),(3,'Авторизированный клиент');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
INSERT INTO `status` VALUES (1,'Завершен'),(2,'Новый');
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `role_id` int NOT NULL,
  `surname` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `patronymic` varchar(45) DEFAULT NULL,
  `login` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `role_id_idx` (`role_id`),
  CONSTRAINT `role_id` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Никифорова','Весения','Николаевна','94d5ous@gmail.com','uzWC67',1),(1,'Сазонов','Руслан','Германович','uth4iz@mail.com','2L6KZG',2),(1,'Одинцов','Серафим','Артёмович','yzls62@outlook.com','JlFRCZ',3),(2,'Степанов','Михаил','Артёмович','1diph5e@tutanota.com','8ntwUp',4),(2,'Ворсин','Петр','Евгеньевич','tjde7c@yahoo.com','YOyhfR',5),(2,'Старикова','Елена','Павловна','wpmrc3do@tutanota.com','RSbvHv',6),(3,'Михайлюк','Анна','Вячеславовна','5d4zbu@tutanota.com','rwVDh9',7),(3,'Ситдикова','Елена','Анатольевна','ptec8ym@yahoo.com','LdNyos',8),(3,'Ворсин','Петр','Евгеньевич','1qz4kw@mail.com','gynQMT',9),(3,'Старикова','Елена','Павловна','4np6se@mail.com','AtnDjr',10);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-25 13:14:14
