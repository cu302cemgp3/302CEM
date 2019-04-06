-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2019 年 04 月 06 日 04:32
-- 伺服器版本: 10.1.28-MariaDB
-- PHP 版本： 7.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `agile`
--

-- --------------------------------------------------------

--
-- 資料表結構 `time`
--

CREATE TABLE `time` (
  `time_id` int(11) NOT NULL,
  `timeslot` datetime NOT NULL,
  `available` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `time`
--

INSERT INTO `time` (`time_id`, `timeslot`, `available`) VALUES
(2, '2019-04-03 09:00:00', 1),
(3, '2019-04-03 10:00:00', 1),
(4, '2019-04-03 14:00:00', 1),
(5, '2019-04-03 16:00:00', 1),
(6, '2019-04-04 09:00:00', 1),
(7, '2019-04-04 14:00:00', 1),
(8, '2019-04-04 16:00:00', 1),
(9, '2019-04-05 09:00:00', 1),
(10, '2019-04-05 11:00:00', 1),
(11, '2019-04-05 14:00:00', 1),
(12, '2019-04-05 16:00:00', 1),
(13, '2019-04-06 09:00:00', 1),
(14, '2019-04-06 11:00:00', 1),
(15, '2019-04-06 14:00:00', 1),
(16, '2019-04-06 16:00:00', 1),
(17, '2019-04-07 09:00:00', 1),
(18, '2019-04-07 11:00:00', 1),
(19, '2019-04-08 09:00:00', 1),
(20, '2019-04-08 11:00:00', 1),
(21, '2019-04-08 14:00:00', 1),
(22, '2019-04-08 16:00:00', 1);

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `time`
--
ALTER TABLE `time`
  ADD PRIMARY KEY (`time_id`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `time`
--
ALTER TABLE `time`
  MODIFY `time_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
