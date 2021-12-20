-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Дек 19 2021 г., 19:33
-- Версия сервера: 10.3.22-MariaDB
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `users`
--

-- --------------------------------------------------------

--
-- Структура таблицы `person`
--

CREATE TABLE `person` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `surname` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `person`
--

INSERT INTO `person` (`id`, `name`, `surname`) VALUES
(1, 'Ellynn', 'Grimmett'),
(2, 'Kate', 'Bumfrey'),
(3, 'Virge', 'Krollmann'),
(4, 'Kai', 'Chesswas'),
(5, 'Herminia', 'Girodias'),
(6, 'Liuka', 'Honniebal'),
(7, 'Norbert', 'Hemmingway'),
(8, 'Leese', 'Leathes'),
(9, 'Lorilee', 'Mattiato'),
(10, 'Andie', 'Sibun'),
(11, 'Annemarie', 'Swainston'),
(12, 'Jamie', 'Felgate'),
(13, 'Chester', 'Avey'),
(14, 'Casandra', 'Gonzalvo'),
(15, 'Thaddus', 'Dundridge'),
(16, 'Louis', 'Ketton'),
(17, 'Tabbi', 'Plews'),
(18, 'Grenville', 'Bletsor'),
(19, 'Sancho', 'Treat'),
(20, 'Betteann', 'Crecy'),
(21, 'Myron', 'Thominga'),
(22, 'Lorne', 'Meugens'),
(23, 'Heloise', 'Eborall'),
(24, 'Lannie', 'Reeders'),
(25, 'Barbara', 'Spatarul'),
(26, 'Raviv', 'Jedrzejczyk'),
(27, 'Brita', 'Bonnier'),
(28, 'Darbee', 'Maudlin'),
(29, 'Brenda', 'Sanpher'),
(30, 'Deeann', 'Rosewall'),
(31, 'Quintina', 'Bearblock'),
(32, 'Bobinette', 'Earney'),
(33, 'Lindie', 'Dossit'),
(34, 'Gennifer', 'Dorn'),
(35, 'Bibi', 'Lines'),
(36, 'Emili', 'Petroff'),
(37, 'Kingsley', 'Dyball'),
(38, 'Rheba', 'Tilio'),
(39, 'Frayda', 'Pentony'),
(40, 'Sheelah', 'Railton'),
(41, 'Maurita', 'Celier'),
(42, 'Chelsea', 'Paoletti'),
(43, 'Johnath', 'Farnell'),
(44, 'Misti', 'Truin'),
(45, 'Town', 'Le Barr'),
(46, 'Tab', 'Elcum'),
(47, 'Nissy', 'Coleman'),
(48, 'Lusa', 'Dosdell'),
(49, 'Etty', 'Ollington'),
(50, 'Brigg', 'Mapes');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `person`
--
ALTER TABLE `person`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
