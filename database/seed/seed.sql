-- Шаблон тестового наполнения базы данных.
-- Артефакт: ART-007 (модель данных) · Источник: ЛР №4.
-- Заполните тестовыми данными после создания схемы в database/migrations/.

-- Тестовые пользователи
INSERT INTO [user] ([id], [vk_id], [display_name]) VALUES
    ([...], [...], [...]);

-- Тестовые автоматы
INSERT INTO [machine] ([id], [location], [status]) VALUES
    ([...], [...], [...]);

-- Тестовые заказы
INSERT INTO [order] ([id], [user_id], [machine_id], [status], [total_amount]) VALUES
    ([...], [...], [...], [...], [...]);

-- Тестовые оплаты
INSERT INTO [payment] ([id], [order_id], [amount], [status]) VALUES
    ([...], [...], [...], [...]);

-- Тестовые задания печати
INSERT INTO [print_task] ([id], [order_id], [status]) VALUES
    ([...], [...], [...]);
