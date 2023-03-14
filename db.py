import sqlite3


class MyDB:
    def __init__(self, Database_name) :

        self.check_connection = False
        try:
            self.mydb = sqlite3.connect(Database_name)
            self.cursor = self.mydb.cursor()
            # print("Connected to database")
            self.check_connection = True
        except Exception as e:
            print("Database connection Error: ", e)
            self.check_connection = False

    # create Setting Table if not exist
    def create_table(self):
        if self.check_connection:
            try:
                self.mydb.execute("CREATE TABLE Setting (Name TEXT UNIQUE, Value TEXT)")
                self.mydb.commit()
                print("Table created")
                return True
            except Exception as e:
                print("Create table Error: ", e)
                return False
        else:
            raise Exception("Database connection Error")


    # insert data to Setting Table
    def insert_setting(self, name, value):
        if self.check_connection:
            try:
                self.mydb.execute("INSERT INTO Setting (Name, Value) VALUES (?, ?)", (name, value))
                self.mydb.commit()
                print("Data inserted")
                return True
            except Exception as e:
                print("Insert data Error: ", e)
                return False
        else:
            raise Exception("Database connection Error")

    # get setting value when name is given
    def get_setting(self, name):
        if self.check_connection:
            try:
                db_response = self.mydb.execute("SELECT Value FROM Setting WHERE Name = ?", (name,))
                value = db_response.fetchone()
                # print("Data fetched")
                return value[0]
            except Exception as e:
                print("Get data Error: ", e)
                return None
        else:
            raise Exception("Database connection Error")

    # update setting value when name is given
    def update_setting(self, name, value):
        if self.check_connection:
            try:
                self.mydb.execute("UPDATE Setting SET Value = ? WHERE Name = ?", (value, name))
                self.mydb.commit()
                # print("Data updated")
                return True
            except Exception as e:
                print("Update data Error: ", e)
                return False
        else:
            raise Exception("Database connection Error")


    # delete setting value when name is given
    def delete_setting(self, name):
        if self.check_connection:
            try:
                self.mydb.execute("DELETE FROM Setting WHERE Name = ?", (name,))
                self.mydb.commit()
                # print("Data deleted")
                return True
            except Exception as e:
                print("Delete data Error: ", e)
                return False
        else:
            raise Exception("Database connection Error: {}")

    # close database connection
    def close_connection(self):
        if self.check_connection:
            try:
                self.mydb.close()
                # print("Database connection closed")
                return True
            except Exception as e:
                print("Close connection Error: ", e)
                return False
        else:
            raise Exception("Database Not Connected")

if __name__ == "__main__":
    mydb = MyDB("settings.db")
    # mydb.update_setting("selectedLead", "3")
    mydb.insert_setting("bp", "bloodPressure1")
    mydb.insert_setting("medication", "medication1")
    mydb.insert_setting("date", "date1")
    mydb.insert_setting("name", "name1")
    mydb.insert_setting("pid", "pid1")
    mydb.insert_setting("age", "age1")
    mydb.insert_setting("gender", "gender1")
    print("Record inserted")
    print("Done")
    pass

'''
471149
471149
471149
471149
471149

'''