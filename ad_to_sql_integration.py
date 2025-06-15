import logging
from datetime import datetime

# Библиотеки для работы с Active Directory
try:
    from pyad import adquery, aduser
except ImportError:
    print("pyad not installed. Install it with 'pip install pyad'.")
    exit()

# Библиотека для работы с SQL Server
import pyodbc

# Настройки подключения к AD
AD_SERVER = "your-ad-server.com"  # Замените на адрес вашего AD сервера
AD_USER = "domain\\admin_user"  # Замените на ваше имя пользователя в домене
AD_PASSWORD = "password"  # Замените на ваш пароль
GROUP_NAME = "Developers"  # Название группы, из которой нужно получить пользователей

# Настройки подключения к SQL Server
SQL_SERVER = "your-sql-server.com"  # Замените на адрес вашего SQL сервера
SQL_DATABASE = "your_database"  # Замените на имя вашей базы данных
SQL_USER = "sql_user"  # Замените на имя пользователя SQL
SQL_PASSWORD = "sql_password"  # Замените на пароль пользователя SQL

# Настройка логирования
logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


def connect_to_ad():
    """
    Подключаемся к Active Directory и получаем список пользователей из группы Developers.
    Возвращаем список пользователей.
    """
    try:
        q = adquery.ADQuery(AD_SERVER, username=AD_USER, password=AD_PASSWORD)
        q.execute_query(
            attributes=["sAMAccountName", "displayName", "mail"],
            where_clause="memberOf = 'CN={0},OU=Groups,DC=your,DC=domain'".format(GROUP_NAME),
            base_dn="DC=your,DC=domain"
        )
        users = []
        for row in q.get_results():
            user_data = {
                "sAMAccountName": row["sAMAccountName"][0],
                "displayName": row["displayName"][0],
                "mail": row["mail"][0]
            }
            users.append(user_data)
        return users
    except Exception as e:
        logger.error(f"Ошибка при подключении к AD: {e}")
        raise


def create_table(cursor):
    """
    Создаем таблицу Users в SQL Server, если она еще не существует.
    """
    query = """
    IF NOT EXISTS (
        SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Users]')
    )
    BEGIN
        CREATE TABLE [dbo].[Users] (
            username VARCHAR(255) PRIMARY KEY,
            full_name VARCHAR(255),
            email VARCHAR(255)
        );
    END
    """
    cursor.execute(query)
    cursor.commit()


def insert_users(users, connection):
    """
    Вставляем данные пользователей в таблицу Users.
    """
    cursor = connection.cursor()
    for user in users:
        try:
            query = f"""
            INSERT INTO [dbo].[Users] (username, full_name, email)
            VALUES ('{user['sAMAccountName']}', '{user['displayName']}', '{user['mail']}');
            """
            cursor.execute(query)
            cursor.commit()
            logger.info(f"Вставка данных пользователя {user['sAMAccountName']} выполнена.")
        except pyodbc.IntegrityError as ie:
            logger.warning(f"Пользователь {user['sAMAccountName']} уже существует в таблице.")
        except Exception as e:
            logger.error(f"Ошибка при вставке данных пользователя {user['sAMAccountName']}: {e}")


def main():
    """Основная функция для выполнения процесса извлечения пользователей из AD и вставки их в SQL."""

    # Подключение к AD и получение списка пользователей
    users = connect_to_ad()

    if len(users) == 0:
        logger.info("Не найдено пользователей в группе Developers.")
        return

    # Подключение к SQL Server
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};' \
               f'SERVER={SQL_SERVER};DATABASE={SQL_DATABASE};UID={SQL_USER};PWD={SQL_PASSWORD}'

    try:
        connection = pyodbc.connect(conn_str)
        logger.info("Успешное подключение к SQL Server.")
    except pyodbc.Error as e:
        logger.error(f"Ошибка при подключении к SQL Server: {e}")
        return

    # Создание таблицы Users, если она не существует
    create_table(connection.cursor())

    # Вставка данных пользователей в таблицу Users
    insert_users(users, connection)

    # Закрытие соединения с SQL Server
    connection.close()
    logger.info("Соединение с SQL Server закрыто.")


if __name__ == "__main__":
    main()  # Запуск основного процесса
