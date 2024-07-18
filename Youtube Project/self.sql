-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 29, 2023 at 02:59 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `self`
--

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

CREATE TABLE `images` (
  `id` int(30) NOT NULL,
  `images` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `images`
--

INSERT INTO `images` (`id`, `images`) VALUES
(7, 'data/frame255.jpg,data/frame255.jpg,data/frame255.jpg'),
(9, 'data/frame255.jpg,data/frame255.jpg,data/frame255.jpg,data/frame255.jpg,data/frame255.jpg,data/frame255.jpg,data/frame525.jpg,data/frame525.jpg,data/frame525.jpg,data/frame525.jpg,data/frame795.jpg,data/frame795.jpg,data/frame795.jpg,data/frame795.jpg,dat'),
(10, 'data/frame255.jpg,data/frame255.jpg,data/frame255.jpg,data/frame525.jpg,data/frame525.jpg,data/frame525.jpg,data/frame795.jpg,data/frame795.jpg,data/frame795.jpg,data/frame1065.jpg,data/frame1065.jpg,data/frame1065.jpg,data/frame1335.jpg,data/frame1335.jp'),
(11, ''),
(12, 'data/frame255.jpg,data/frame255.jpg'),
(13, 'data/frame0.jpg,data/frame15.jpg'),
(14, 'data/frame120.jpg,data/frame105.jpg,data/frame45.jpg,data/frame30.jpg,data/frame570.jpg,data/frame585.jpg'),
(15, 'data/frame120.jpg,data/frame105.jpg,data/frame540.jpg,data/frame555.jpg'),
(16, 'data/frame120.jpg,data/frame105.jpg,data/frame540.jpg,data/frame555.jpg'),
(17, 'data/frame720.jpg,data/frame735.jpg'),
(18, ''),
(19, 'data/frame0.jpg,data/frame15.jpg,data/frame540.jpg,data/frame525.jpg'),
(20, 'data/frame540.jpg,data/frame525.jpg'),
(21, 'data/frame540.jpg,data/frame525.jpg'),
(22, 'data/frame0.jpg,data/frame1.jpg,data/frame35.jpg,data/frame36.jpg'),
(23, 'data/frame15.jpg,data/frame16.jpg'),
(24, 'data/frame5.jpg,data/frame6.jpg'),
(25, 'data/frame20.jpg,data/frame21.jpg'),
(26, 'data/frame1.jpg,data/frame0.jpg,data/frame23.jpg,data/frame24.jpg,data/frame17.jpg,data/frame18.jpg,data/frame26.jpg,data/frame27.jpg,data/frame28.jpg,data/frame29.jpg,data/frame23.jpg,data/frame24.jpg,data/frame21.jpg,data/frame20.jpg'),
(27, 'data/frame30.jpg,data/frame38.jpg,data/frame43.jpg,data/frame44.jpg'),
(28, 'data/frame34.jpg,data/frame33.jpg'),
(29, 'data/frame30.jpg,data/frame31.jpg,data/frame32.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `images`
--
ALTER TABLE `images`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
