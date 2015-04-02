/* 
* @Author: harmoN
* @Date:   2015-04-02 02:41:43
* @Last Modified by:   harmoN
* @Last Modified time: 2015-04-02 02:41:51
*/

CREATE DATABASE `piHome` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

CREATE TABLE `sensors` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `desc` varchar(80) COLLATE utf8_bin DEFAULT NULL,
  `ip_addr` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE `temps` (
  `id` int(15) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime DEFAULT NULL,
  `temp` float DEFAULT NULL,
  `sensor_id` int(5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_idx` (`sensor_id`),
  CONSTRAINT `id` FOREIGN KEY (`sensor_id`) REFERENCES `sensors` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;