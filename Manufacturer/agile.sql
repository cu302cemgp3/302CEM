-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2019 年 04 月 05 日 06:49
-- 伺服器版本: 10.1.34-MariaDB
-- PHP 版本： 7.2.8

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
-- 資料表結構 `delivery`
--

CREATE TABLE `delivery` (
  `delivery_id` int(11) NOT NULL,
  `item_id` varchar(11) NOT NULL,
  `retailer_id` varchar(11) NOT NULL,
  `order_id` varchar(11) NOT NULL,
  `timeslot` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `delivery`
--

INSERT INTO `delivery` (`delivery_id`, `item_id`, `retailer_id`, `order_id`, `timeslot`) VALUES
(1, 'I001', 'R001', '1', '2019-04-03 09:00:00');

-- --------------------------------------------------------

--
-- 資料表結構 `inv`
--

CREATE TABLE `inv` (
  `product_id` varchar(11) NOT NULL,
  `product_description` text NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `inv`
--

INSERT INTO `inv` (`product_id`, `product_description`, `amount`) VALUES
('I001', 'Juice', 98600),
('I002', 'Cable G48', 99550),
('I003', 'Charger M320', 23469),
('I004', 'Pen', 42200),
('I005', 'Mouse', 50000);

-- --------------------------------------------------------

--
-- 資料表結構 `man`
--

CREATE TABLE `man` (
  `exp_key` varchar(11) NOT NULL,
  `item_no` varchar(11) DEFAULT NULL,
  `expected_shipment_date` text,
  `qty` int(11) DEFAULT NULL,
  `price_per_item` int(11) DEFAULT NULL,
  `manufacturer_id` text,
  `retailer_id` varchar(11) DEFAULT NULL,
  `handle` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `man`
--

INSERT INTO `man` (`exp_key`, `item_no`, `expected_shipment_date`, `qty`, `price_per_item`, `manufacturer_id`, `retailer_id`, `handle`) VALUES
('1', 'I001', '2019-02-20 12:30:00', 100, 20, 'M001', 'R001', 1),
('2', 'I002', '2019-02-20 16:25:00', 50, 61, 'M001', 'R001', 0),
('3', 'I003', '2019-04-03 15:10:00', 10, 40, 'M001', 'R001', 0),
('8', 'I003', '2019-04-03 08:00:00', 10, 1, 'M001', 'R001', 0);

-- --------------------------------------------------------

--
-- 資料表結構 `retailer`
--

CREATE TABLE `retailer` (
  `retailer_id` varchar(11) NOT NULL,
  `location` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `retailer`
--

INSERT INTO `retailer` (`retailer_id`, `location`) VALUES
('R001', 'Hong Kong Island'),
('R003', 'Tsuen Wan');

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
(2, '2019-04-03 09:00:00', 0),
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
-- 資料表索引 `delivery`
--
ALTER TABLE `delivery`
  ADD PRIMARY KEY (`delivery_id`),
  ADD KEY `item_id` (`item_id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `retailer_id` (`retailer_id`);

--
-- 資料表索引 `inv`
--
ALTER TABLE `inv`
  ADD PRIMARY KEY (`product_id`);

--
-- 資料表索引 `man`
--
ALTER TABLE `man`
  ADD PRIMARY KEY (`exp_key`),
  ADD KEY `item_no` (`item_no`),
  ADD KEY `retailer_id` (`retailer_id`);

--
-- 資料表索引 `retailer`
--
ALTER TABLE `retailer`
  ADD PRIMARY KEY (`retailer_id`);

--
-- 資料表索引 `time`
--
ALTER TABLE `time`
  ADD PRIMARY KEY (`time_id`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `delivery`
--
ALTER TABLE `delivery`
  MODIFY `delivery_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用資料表 AUTO_INCREMENT `time`
--
ALTER TABLE `time`
  MODIFY `time_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- 已匯出資料表的限制(Constraint)
--

--
-- 資料表的 Constraints `delivery`
--
ALTER TABLE `delivery`
  ADD CONSTRAINT `delivery_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `inv` (`product_id`),
  ADD CONSTRAINT `delivery_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `man` (`exp_key`),
  ADD CONSTRAINT `delivery_ibfk_3` FOREIGN KEY (`retailer_id`) REFERENCES `retailer` (`retailer_id`);

--
-- 資料表的 Constraints `man`
--
ALTER TABLE `man`
  ADD CONSTRAINT `man_ibfk_1` FOREIGN KEY (`item_no`) REFERENCES `inv` (`product_id`),
  ADD CONSTRAINT `man_ibfk_2` FOREIGN KEY (`retailer_id`) REFERENCES `retailer` (`retailer_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
