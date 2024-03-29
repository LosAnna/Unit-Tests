#### Задание 1. Представьте, что вы работаете над разработкой простого приложения для записной книжки, которое позволяет пользователям добавлять, редактировать и удалять контакты. Ваша задача - придумать как можно больше различных тестов (юнит-тесты, интеграционные тесты, сквозные тесты) для этого приложения. Напишите название каждого теста, его тип и краткое описание того, что этот тест проверяет.

1. Юнит-тесты:
- Добавление контакта. Создаем новые контакт, добавляем его в записную книжку и проверяем, что контакт успешно добавлен и содержит все необходимые и корректные данные.
- Редактирование контакта. Создаем новый контакт и сохраняем его в записной книжке, изменяем некоторые данные контакта и проверяем корректность проведенных изменений.
- Удаление контакта. Создаем новый контакт, затем удаляем его и проверяем, что контакт успешно удален из записной книжки.
- Валидация данных. Проверяем корректность валидации данных контакта перед их добавлением в записную книгу.
- Сохранение контакта. Проверяем обработку ошибок при сохранении в записную книгу, например, отсутствие доступа к базе данных.
- Дублирование контактов. Проверяем, что один и тот же контакт не может быть записан два и более раз.
- Поиск контакта по имени (фамилии и другим данным). Добавляем несколько контактов, делаем поиск по имени (фамилии и тп), проверяем корректность поиска.
- Выдача всех контактов из записной книжки. Проверяем, что кол-во контактов в записной книге совпадает с длиной списка поиска всех контактов.

2. Интеграционные тесты:
- Сохранение данных при выходе из приложения. Проверяем, что при закрытии/открытии приложения все данные добавленного контакта сохраняются корректно.
- Сортировка контактов. Проверяем корректность сортировка контактов по различным свойствам таблицы контактов.
- Системный календарь. Проверяем сохранение и отображение дат рождения контактов в системном календаре.
- Системное время. Проверяем создание и отображение событий/напоминаний в соответствии с системным временем.

3. Сквозные тесты:
- Навигация по приложению. Проверяем навигацию пользователя по всем разделам приложения. Открываем меню, переключаемся между вкладками, проверяем корректность отображения информации в приложении.
- Ввод данных через пользовательский интерфейс. Вводим различную текстовую информацию в проверяемые поля, проверяем работу опций, корректность отображения и обработки/сохранения введенных данных.