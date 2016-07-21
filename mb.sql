-- phpMyAdmin SQL Dump
-- version 4.6.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2016-07-22 00:31:27
-- 服务器版本： 5.6.27-2
-- PHP Version: 5.6.17-1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mb`
--

-- --------------------------------------------------------

--
-- 表的结构 `polls_result`
--

CREATE TABLE `polls_result` (
  `id` int(11) NOT NULL,
  `taskid` int(11) NOT NULL,
  `port` int(11) NOT NULL,
  `port_detail` varchar(255) NOT NULL,
  `bad_port` tinyint(1) NOT NULL,
  `scan_time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `polls_task`
--

CREATE TABLE `polls_task` (
  `id` int(11) NOT NULL,
  `ipdir` varchar(32) NOT NULL,
  `state` tinyint(1) NOT NULL,
  `white_port` longtext NOT NULL,
  `create_time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `polls_result`
--
ALTER TABLE `polls_result`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `polls_task`
--
ALTER TABLE `polls_task`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `polls_result`
--
ALTER TABLE `polls_result`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `polls_task`
--
ALTER TABLE `polls_task`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
