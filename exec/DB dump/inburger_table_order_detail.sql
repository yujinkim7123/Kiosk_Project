-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: inburger
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `table_order_detail`
--

DROP TABLE IF EXISTS `table_order_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_order_detail` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `menu_count` int NOT NULL,
  `is_set` bit(1) DEFAULT NULL,
  `each_menu_price` int NOT NULL,
  `menu_id` bigint DEFAULT NULL,
  `order_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKg4ay1l5b1tg40yo5c37jl657x` (`menu_id`),
  KEY `FK9kcb20et7bde43cekjlogutiv` (`order_id`),
  CONSTRAINT `FK9kcb20et7bde43cekjlogutiv` FOREIGN KEY (`order_id`) REFERENCES `table_order` (`id`),
  CONSTRAINT `FKg4ay1l5b1tg40yo5c37jl657x` FOREIGN KEY (`menu_id`) REFERENCES `table_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_order_detail`
--

LOCK TABLES `table_order_detail` WRITE;
/*!40000 ALTER TABLE `table_order_detail` DISABLE KEYS */;
INSERT INTO `table_order_detail` VALUES (1,1,_binary '\0',3000,15,1),(2,1,_binary '\0',6000,31,1),(3,1,_binary '',9000,28,2),(4,1,_binary '',8500,27,3),(5,1,_binary '',9000,23,4),(6,1,_binary '\0',3000,15,5),(7,1,_binary '\0',6000,31,5),(8,1,_binary '\0',3000,15,6),(9,1,_binary '\0',6000,31,6);
/*!40000 ALTER TABLE `table_order_detail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-17 11:12:33
