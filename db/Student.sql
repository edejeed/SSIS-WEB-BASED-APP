-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: student_data
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `colleges`
--

DROP TABLE IF EXISTS `colleges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colleges` (
  `collegeid` int NOT NULL AUTO_INCREMENT,
  `college_code` varchar(45) NOT NULL,
  `college` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`collegeid`,`college_code`),
  UNIQUE KEY `college_code_UNIQUE` (`college_code`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colleges`
--

LOCK TABLES `colleges` WRITE;
/*!40000 ALTER TABLE `colleges` DISABLE KEYS */;
INSERT INTO `colleges` VALUES (4,'COET','College of Engineering and Technology'),(6,'CCS','College of Computer Science'),(9,'CASS','College of Art and Social Sciences'),(12,'CON','College of Nursing'),(13,'CED','College of Education'),(14,'CBAA','College of Business Administration and Accountancy ');
/*!40000 ALTER TABLE `colleges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `courseid` int NOT NULL AUTO_INCREMENT,
  `course_code` varchar(45) NOT NULL,
  `course` varchar(100) DEFAULT NULL,
  `college` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`courseid`,`course_code`),
  UNIQUE KEY `course_code_UNIQUE` (`course_code`),
  KEY `college_idx` (`college`),
  CONSTRAINT `college` FOREIGN KEY (`college`) REFERENCES `colleges` (`college_code`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (8,'BS CS','BS in Computer Science','CCS'),(9,'BS CA','BS in Computer Application','CCS'),(10,'BS IT','BS in Information Technology','CCS'),(11,'BS ECE',' BS Electronics and Communications Engineering','COET'),(12,'BS EE','BS Electrical Engineering','COET'),(13,'BS CE','BS Computer Engineering','COET'),(14,'BS MEE','BS Mechanical Engineering','COET'),(18,'BS N','BS in Nursing','CON');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `studid` int NOT NULL AUTO_INCREMENT,
  `id` varchar(255) NOT NULL,
  `Firstname` varchar(45) DEFAULT NULL,
  `Lastname` varchar(45) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `Level` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`studid`,`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `course` (`Course`),
  CONSTRAINT `Course` FOREIGN KEY (`Course`) REFERENCES `courses` (`course_code`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (16,'2018-0001','Richelle Grace','Romero','BS N','4','F'),(17,'2018-0002','Edejed','Paculba','BS CS','3','M'),(18,'2018-0003','Antonette','Sabayle','BS IT','4','F'),(25,'2018-0004','Jennie ','Kim','BS N','3','F'),(26,'2018-0005','Hershey','Paculba','BS EE','3','F'),(27,'2018-0006','Eden Rose','Risma','BS CS','3','F'),(28,'2018-0007','Lisa','Manoban','BS ECE','3','F'),(29,'2018-0008','Jisoo','Kim','BS ECE','2','F'),(33,'2018-0009','Rose','Park','BS IT','3','F'),(34,'2018-0010','Keet','Lanojan','BS ECE','4','F'),(37,'2018-0011','Sunoo','Kim','BS CA','3','M');
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

-- Dump completed on 2021-11-19 18:57:21
