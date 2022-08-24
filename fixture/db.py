import pymysql.cursors

from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(
            host=host, 
            database=name, 
            user=user, 
            password=password, 
            autocommit=True,
            )

    def get_group_list(self):
        result = []
        with self.connection.cursor() as cursor:
            sql = "SELECT group_id, group_name, group_header, group_footer FROM group_list"
            cursor.execute(sql)
            for row in cursor:
                result.append(
                    Group(
                        id=str(row[0]) or None, 
                        name=row[1] or None, 
                        header=row[2] or None, 
                        footer=row[3] or None
                    )
                )
        return result

    def get_contact_list(self):
        result= []
        with self.connection.cursor() as cursor:
            sql = "SELECT id, firstname, middlename, lastname,  address, home, mobile, work, phone2, email, email2, email3 FROM addressbook WHERE deprecated='0000-00-00 00:00:00'"
            cursor.execute(sql)
            for row in cursor:
                result.append(
                    Contact(
                        id=str(row[0]) or None, 
                        first_name=row[1] or None, 
                        middle_name=row[2] or None, 
                        last_name=row[3] or None,
                        address=row[4] or None, 
                        home=row[5] or None,
                        mobile=row[6] or None, 
                        work=row[7] or None,
                        phone2=row[8] or None,
                        email=row[9] or None,
                        email2=row[10] or None, 
                        email3=row[11] or None,
                    )
                )
        return result

    def destroy(self):
        self.connection.close()