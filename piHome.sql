/* 
* @Author: harmoN
* @Date:   2015-04-02 02:41:43
* @Last Modified by:   harmoN
* @Last Modified time: 2015-04-02 02:52:51
*/

CREATE DATABASE `piHome` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

CREATE TABLE `sensors` (
  `id` int(5) NOT NULL,
  `hostname` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `desc` varchar(80) COLLATE utf8_bin DEFAULT NULL,
  `ip_addr` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE `temps` (
  `id` int(20) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `temp` float DEFAULT NULL,
  `sensor_id` int(5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_idx` (`sensor_id`),
  CONSTRAINT `id` FOREIGN KEY (`sensor_id`) REFERENCES `sensors` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;