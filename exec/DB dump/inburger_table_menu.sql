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
-- Table structure for table `table_menu`
--

DROP TABLE IF EXISTS `table_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_menu` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `menu_name` varchar(255) NOT NULL,
  `menu_price` int NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK5at7tklj6kxp23abts9s8icrf` (`category_id`),
  CONSTRAINT `FK5at7tklj6kxp23abts9s8icrf` FOREIGN KEY (`category_id`) REFERENCES `table_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_menu`
--

LOCK TABLES `table_menu` WRITE;
/*!40000 ALTER TABLE `table_menu` DISABLE KEYS */;
INSERT INTO `table_menu` VALUES (1,'초코 쉐이크',2300,2),(2,'우유',1000,2),(3,'오렌지 주스',1200,2),(4,'스프라이트',1000,2),(5,'환타',1000,2),(6,'딸기쉐이크',2500,2),(7,'코카콜라',900,2),(8,'해쉬브라운',2000,3),(9,'프렌치 프라이',1500,3),(10,'바닐라 선데이 아이스크림',1000,3),(11,'상하이치킨스낵랩',2500,3),(12,'초코 선데이 아이스크림',1500,3),(13,'빅맥',5000,1),(14,'치즈버거',3000,1),(15,'불고기버거',3000,1),(16,'더블치즈',4000,1),(17,'쿼터파운더 치즈',6500,1),(18,'베이컨 토마토 디럭스',7000,1),(19,'에그 불고기버거',5000,1),(20,'불고기버거 세트',5000,1),(21,'치즈버거 세트',5000,1),(22,'더블치즈버거 세트',6500,1),(23,'쿼터파운더 치즈버거 세트',9000,1),(24,'베이컨 토마토 디럭스 세트',8500,1),(25,'에크 불고기버거 세트',7500,1),(26,'빅맥 세트',7000,1),(27,'1955 버거 세트',8500,1),(28,'맥크리스피디럭스버거세트',9000,1),(29,'맥너겟',3000,3),(30,'더블 불고기 버거',5000,1),(31,'1955 버거',6000,1);
/*!40000 ALTER TABLE `table_menu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-17 11:12:41
