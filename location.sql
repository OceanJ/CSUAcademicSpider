-- phpMyAdmin SQL Dump
-- version 4.4.13.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2016-01-11 03:02:32
-- 服务器版本： 5.6.25-0ubuntu0.15.04.1
-- PHP Version: 5.6.11-1ubuntu3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `csuspider`
--

-- --------------------------------------------------------

--
-- 表的结构 `location`
--

CREATE TABLE IF NOT EXISTS `location` (
  `location_id` int(10) unsigned NOT NULL,
  `title` varchar(100) NOT NULL,
  `longitude` double NOT NULL,
  `latitude` double NOT NULL,
  `match_string` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `location`
--

INSERT INTO `location` (`location_id`, `title`, `longitude`, `latitude`, `match_string`) VALUES
(1, '本部民主楼', 112.936979, 28.176791, '民主楼-民主楼小礼堂-民主'),
(2, '本部计算机楼', 112.937651, 28.177171, '计算机楼-计算机'),
(3, '铁道世纪楼', 112.997042, 28.145763, '世纪楼-国际报告厅-铁道校区世纪楼C座'),
(4, '本部科教楼', 112.934933, 28.176685, '科教楼-科北-科南'),
(5, '新校中南讲堂', 112.950506, 28.155421, '中南讲堂'),
(6, '本部立言厅', 112.935158, 28.179631, '立言厅-立言'),
(7, '本部升华楼', 112.935851, 28.176783, '升华楼-升华北-升华后楼-升华'),
(8, '本部物理楼', 112.936878, 28.173613, '物理楼'),
(9, '南校区双超所', 112.944061, 28.168653, '超微超快所-双超所'),
(10, '新校区物电院', 112.952204, 28.153048, '物理与电子学院-物电院'),
(11, '新校区机电楼', 112.947146, 28.153535, '机电楼'),
(12, '中铝科技大楼', 112.947218, 28.153037, '中铝科技大楼-中铝'),
(13, '新校数理楼', 112.952368, 28.15265, '数学楼-数理楼-数学与统计学院-数统院'),
(14, '铁道土木风洞实验室', 112.997444, 28.141701, '风洞'),
(15, '铁道建工楼', 113.000162, 28.147618, '建工楼-建工'),
(16, '本部冶金馆', 112.936116, 28.175324, '冶金馆'),
(17, '湘雅公共卫生学院', 112.991397, 28.221955, '公共卫生学院-公卫院'),
(18, '湘雅新校区图书馆', 112.94771, 28.22684, '湘雅新校区图书馆-湘雅医学院新校区图书馆-湘雅图书馆'),
(19, '湘雅流行病与卫生统计学系', 0, 0, '流行病与卫生统计学系-卫生统计学');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`location_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `location`
--
ALTER TABLE `location`
  MODIFY `location_id` int(10) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=20;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
