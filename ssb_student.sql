-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: ssb
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `번호` int NOT NULL,
  `ID` varchar(45) DEFAULT NULL,
  `비밀번호` varchar(45) DEFAULT NULL,
  `이름` varchar(45) DEFAULT NULL,
  `구분` varchar(45) DEFAULT '학생',
  `클래스` varchar(45) DEFAULT '데이터 기반 AI SW개발자 양성',
  `훈련회차` varchar(45) DEFAULT '2회차',
  `훈련기관` varchar(45) DEFAULT '대한상공회의소 광주인력개발원',
  `기관위치` varchar(45) DEFAULT '광주 광산구',
  `전화번호` varchar(45) DEFAULT '062-940-3520',
  `훈련기간` varchar(45) DEFAULT '2022.10.25 - 2023.05.24',
  `훈련유형` varchar(45) DEFAULT '통합심사과정훈련',
  `금일훈련` varchar(45) DEFAULT NULL,
  `입실` varchar(45) DEFAULT NULL,
  `복귀` varchar(45) DEFAULT NULL,
  `외출` varchar(45) DEFAULT NULL,
  `퇴실` varchar(45) DEFAULT NULL,
  `출석횟수` int DEFAULT '46',
  `지각횟수` int DEFAULT '0',
  `조퇴횟수` int DEFAULT '0',
  `외출횟수` int DEFAULT '0',
  `결석` int DEFAULT '0',
  `출석일수` int DEFAULT '46',
  `최대출석일수` int DEFAULT '140',
  `과정진행` int DEFAULT '46',
  `총과정진행` int DEFAULT '140',
  PRIMARY KEY (`번호`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'1234','12','강민영','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(2,'yj','1','고연재','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(3,'12','1234','김기태','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(4,'km','1','김명은','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(5,NULL,NULL,'김성일','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(6,'ys','1','김연수','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(7,NULL,NULL,'노도현','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(8,NULL,NULL,'박규환','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(9,'11','12','박성빈','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(10,'s','1','박시형','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(11,'o','1','박의용','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(12,NULL,NULL,'오송화','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(13,NULL,NULL,'이범규','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(14,NULL,NULL,'이보라','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(15,NULL,NULL,'이소윤','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(16,NULL,NULL,'이여름','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(17,NULL,NULL,'이지혜','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(18,NULL,NULL,'이현도','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(19,NULL,NULL,'임성경','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(20,NULL,NULL,'임영효','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(21,NULL,NULL,'임홍선','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(22,NULL,NULL,'장은희','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(23,NULL,NULL,'정연우','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(24,NULL,NULL,'정철우','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(25,NULL,NULL,'주민석','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(26,'j','1','최지혁','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(27,NULL,NULL,'류가미','학생','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(100,'sb','1','이상복','교수','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(101,'hg','1','류홍걸','교수','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140),(102,NULL,NULL,'조동현','교수','데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,NULL,NULL,NULL,NULL,46,0,0,0,0,46,140,46,140);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-13 23:52:43
