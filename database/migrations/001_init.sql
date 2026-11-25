-- Шаблон миграции схемы базы данных.
-- Артефакт: ART-007 (модель данных) · Источник: ЛР №4.
-- Заполните по ERD проекта «Автомат печати фото из ВКонтакте».
-- Правило: каждая миграция — отдельный файл вида NNN_<название>.sql.

BEGIN;

-- Таблица: Пользователь
CREATE TABLE [user] (
    [id]            [PRIMARY KEY],          -- первичный ключ
    [vk_id]         [уникальный ID ВКонтакте],
    [display_name]  [имя пользователя],
    [phone]         [телефон],
    [created_at]    [дата регистрации]
);

-- Таблица: Автомат
CREATE TABLE [machine] (
    [id]            [PRIMARY KEY],
    [location]      [адрес размещения],
    [status]        [статус автомата],
    [paper_left]    [остаток бумаги]
);

-- Таблица: Заказ
CREATE TABLE [order] (
    [id]            [PRIMARY KEY],
    [user_id]       [FK -> user.id],
    [machine_id]    [FK -> machine.id],
    [status]        [new / paid / printing / done / cancelled],
    [total_amount]  [сумма заказа],
    [created_at]    [дата создания]
);

-- Таблица: Фото (позиция заказа)
CREATE TABLE [photo] (
    [id]            [PRIMARY KEY],
    [order_id]      [FK -> order.id],
    [source_url]    [ссылка на фото во ВКонтакте],
    [print_format]  [формат печати],
    [copies]        [количество копий]
);

-- Таблица: Оплата
CREATE TABLE [payment] (
    [id]            [PRIMARY KEY],
    [order_id]      [FK -> order.id],
    [amount]        [сумма],
    [method]        [способ оплаты],
    [status]        [pending / confirmed / failed],
    [paid_at]       [дата оплаты]
);

-- Таблица: Задание печати
CREATE TABLE [print_task] (
    [id]            [PRIMARY KEY],
    [order_id]      [FK -> order.id],
    [status]        [queued / printing / printed / failed],
    [queued_at]     [время постановки в очередь],
    [finished_at]   [время выполнения]
);

COMMIT;
