-- phpMyAdmin SQL Dump
-- version 4.4.13.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2016-01-11 03:58:43
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
-- 表的结构 `academic`
--

CREATE TABLE IF NOT EXISTS `academic` (
  `html_content` mediumtext CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `time` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `aca_id` int(10) unsigned NOT NULL,
  `location` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `location_id` int(10) unsigned NOT NULL,
  `title` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `url` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `academy` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `date_sort` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `academic`
--
ALTER TABLE `academic`
  ADD PRIMARY KEY (`aca_id`),
  ADD UNIQUE KEY `url` (`url`),
  ADD KEY `academy` (`academy`),
  ADD KEY `type` (`type`),
  ADD KEY `location` (`location`),
  ADD KEY `location_id` (`location_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `academic`
--
ALTER TABLE `academic`
  MODIFY `aca_id` int(10) unsigned NOT NULL AUTO_INCREMENT;
--
-- 限制导出的表
--

--
-- 限制表 `academic`
--
ALTER TABLE `academic`
  ADD CONSTRAINT `academic_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
