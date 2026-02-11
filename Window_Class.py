from tkinter.tix import TEXT
from PySide6.QtWidgets import *
from ui_window import Ui_MainWindow
import os
import sqlite3
def get_db_path():
    db_path = os.path.join(
        os.getenv("LOCALAPPDATA"),
        "LibraryManagement",
        "library.db"
    )
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return db_path
class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Library Management System")

        self.widget.setHidden(True)

        #Moving to different pages
        self.dashboard_btn_1.clicked.connect(self.show_dashboard_page)
        self.dashboard_btn_2.clicked.connect(self.show_dashboard_page)
        self.books_btn_1.clicked.connect(self.show_books_page)
        self.books_btn_2.clicked.connect(self.show_books_page)
        self.returned_btn_1.clicked.connect(self.show_returned_page)
        self.returned_btn_2.clicked.connect(self.show_returned_page)
        self.borrowed_btn_1.clicked.connect(self.show_borrowed_page)
        self.borrowed_btn_2.clicked.connect(self.show_borrowed_page)
        self.fines_btn_1.clicked.connect(self.show_fines_page)
        self.fines_btn_2.clicked.connect(self.show_fines_page)
        self.transaction_btn_1.clicked.connect(self.show_transaction_page)
        self.transaction_btn_2.clicked.connect(self.show_transaction_page)

        #Books page
        self.add_book_btn.clicked.connect(self.add_book)
        self.View_books_btn.clicked.connect(self.view_books)
        self.remove_book_btn.clicked.connect(self.remove_book)
        self.books_table_search.textChanged.connect(self.search_books)

        #Returned page
        self.add_record_btn.clicked.connect(self.add_record)
        self.view_returns_btn.clicked.connect(self.view_records)
        self.remove_record_btn.clicked.connect(self.remove_record)
        self.return_table_search.textChanged.connect(self.search_records)

        #Borrowed Page
        self.add_borrow_record_btn.clicked.connect(self.add_borrow_record)
        self.view_borrows_btn.clicked.connect(self.view_borrowed_records)
        self.remove_borrow_record_btn.clicked.connect(self.remove_borrowed_record)
        self.borrow_table_search.textChanged.connect(self.search_borrowed_records)

        #Fines Page
        self.add_fine_btn.clicked.connect(self.add_fine)
        self.add_fines_btn.clicked.connect(self.view_fines)
        self.remove_fine_btn.clicked.connect(self.remove_fine)
        self.borrow_line_17.textChanged.connect(self.search_fines)

        #Transaction Page
        self.add_transaction_btn.clicked.connect(self.add_transaction)
        self.view_transaction_btn.clicked.connect(self.view_transactions)
        self.remove_transaction_btn.clicked.connect(self.remove_transaction)
        self.transaction_table_search.textChanged.connect(self.search_transactions)

        #Dashboard Page
        self.show_books_btn.clicked.connect(self.show_books)
        self.how_returned_btn.clicked.connect(self.show_returned)
        self.show_borrowed_btn.clicked.connect(self.show_borrowed)
        self.show_fines_btn.clicked.connect(self.show_fines)
        self.show_transaction_btn.clicked.connect(self.show_transaction)

    def show_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(2)
    def show_books_page(self):
        self.stackedWidget.setCurrentIndex(3)
    def show_returned_page(self):
        self.stackedWidget.setCurrentIndex(4)
    def show_borrowed_page(self):
        self.stackedWidget.setCurrentIndex(5)
    def show_fines_page(self):
        self.stackedWidget.setCurrentIndex(0)
    def show_transaction_page(self):
        self.stackedWidget.setCurrentIndex(1)
    def create_connection(self):
        self.connection=sqlite3.connect(get_db_path())
        return self.connection
    def add_book(self):
        self.crsr=self.create_connection().cursor()
        self.crsr.execute("""CREATE TABLE IF NOT EXISTS books (
                Book_Name TEXT,
                Book_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Book_Type TEXT,
                Author TEXT,
                Publisher TEXT,
                Copies INTEGER,
                Price INTEGER,
                Date TEXT,
                Time TEXT,
                Remarks TEXT)""")
        self.add_new_book=[self.books_line_1.text(),
                        self.books_line_2.text(),
                       self.books_line_3.text(),
                       self.books_line_4.text(),
                       self.books_line_5.text(),
                       self.books_line_6.text(),
                       self.books_line_7.text(),
                       self.books_line_8.text(),
                       self.books_line_9.text(),
                       self.books_line_10.text()]
        self.crsr.execute("INSERT INTO books VALUES (?,?,?,?,?,?,?,?,?,?)",self.add_new_book)
        self.books_line_1.clear()
        self.books_line_2.clear()
        self.books_line_3.clear()
        self.books_line_4.clear()
        self.books_line_5.clear()
        self.books_line_6.clear()
        self.books_line_7.clear()
        self.books_line_8.clear()
        self.books_line_9.clear()
        self.books_line_10.clear()
        self.connection.commit()
        self.connection.close()
    def view_books(self):
        self.crsr=self.create_connection().cursor()
        book_sqlquery="SELECT COUNT(*) FROM books"
        books_sqlquery="SELECT * FROM books"
        self.crsr.execute(book_sqlquery)
        result=self.crsr.fetchone()
        self.books_table.setRowCount(result[0])
        self.books_table.setColumnCount(10)
        self.books_table.setHorizontalHeaderLabels(["Book_Name","Book_ID","Book_Type","Author","Publisher","Copies","Price","Date","Time","Remarks"])
        #using loop to display all data in the table
        table_row=0
        for i in self.crsr.execute(books_sqlquery):
            self.books_table.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.books_table.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.books_table.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.books_table.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.books_table.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.books_table.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.books_table.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            self.books_table.setItem(table_row,7,QTableWidgetItem(str(i[7])))
            self.books_table.setItem(table_row,8,QTableWidgetItem(str(i[8])))
            self.books_table.setItem(table_row,9,QTableWidgetItem(str(i[9])))
            table_row += 1
        self.connection.commit()
        self.connection.close()
    def remove_book(self):
        self.crsr=self.create_connection().cursor()
        current_row=self.books_table.currentRow()
        book_id=str(self.books_table.item(current_row,1).text())
        if current_row<0:
            warning=QMessageBox.warning(self,'Warning','Please select a record to remove')
        else:
            question=QMessageBox.question(self,'Conformation','Are you sure you want to delete this record?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if question==QMessageBox.StandardButton.Yes:
                sqlquery="DELETE FROM books WHERE Book_ID=?"
                self.crsr.execute(sqlquery,(book_id,))
        self.connection.commit()
        self.connection.close()
    def search_books(self):
        search_Id=self.books_table_search.text().strip()
        for row in range(self.books_table.rowCount()):
            item=self.books_table.item(row,1)
            if item and item.text() == search_Id:
                self.books_table.selectRow(row)
                self.books_table.scrollToItem(item)
                return
    def add_record(self):
        self.crsr=self.create_connection().cursor()
        self.crsr.execute("""CREATE TABLE IF NOT EXISTS returned(
                Return_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Book_Name TEXT,
                Book_Type TEXT,
                Student_Name TEXT,
                Student_ID TEXT,
                Book_ID INTEGER,
                Received_By TEXT,
                Borrow_Date TEXT,
                Return_Date TEXT,
                Remarks TEXT)""")
        self.add_new_record=[
                       self.return_line_1.text(),
                       self.return_line_2.text(),
                       self.return_line_3.text(),
                       self.return_line_4.text(),
                       self.return_line_5.text(),
                       self.return_line_6.text(),
                       self.return_line_7.text(),
                       self.return_line_8.text(),
                       self.return_line_9.text(),
                       self.return_line_10.text()]
        self.crsr.execute("INSERT INTO returned VALUES (?,?,?,?,?,?,?,?,?,?)",self.add_new_record)
        self.return_line_1.clear()
        self.return_line_2.clear()
        self.return_line_3.clear()
        self.return_line_4.clear()
        self.return_line_5.clear()
        self.return_line_6.clear()
        self.return_line_7.clear()
        self.return_line_8.clear()
        self.return_line_9.clear()
        self.return_line_10.clear()
        self.connection.commit()
        self.connection.close()
    def view_records(self):
        self.crsr=self.create_connection().cursor()
        record_sqlquery="SELECT COUNT(*) FROM returned"
        records_sqlquery="SELECT * FROM returned"
        self.crsr.execute(record_sqlquery)
        result=self.crsr.fetchone()
        self.return_books_table.setRowCount(result[0])
        self.return_books_table.setColumnCount(10)
        self.return_books_table.setHorizontalHeaderLabels(["Return_ID","Book_Name","Book_Type","Student_Name","Student_ID","Book_ID","Received_By","Borrow_Date","Return_Date","Remarks"])
        #using loop to display all data in the table
        table_row=0
        for i in self.crsr.execute(records_sqlquery):
            self.return_books_table.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.return_books_table.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.return_books_table.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.return_books_table.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.return_books_table.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.return_books_table.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.return_books_table.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            self.return_books_table.setItem(table_row,7,QTableWidgetItem(str(i[7])))
            self.return_books_table.setItem(table_row,8,QTableWidgetItem(str(i[8])))
            self.return_books_table.setItem(table_row,9,QTableWidgetItem(str(i[9])))
            table_row += 1
        self.connection.commit()
        self.connection.close()
    def remove_record(self):
        self.crsr=self.create_connection().cursor()
        current_row=self.return_books_table.currentRow()
        return_id=str(self.return_books_table.item(current_row,0).text())
        if current_row<0:
            warning=QMessageBox.warning(self,'Warning','Please select a record to remove')
        else:
            question=QMessageBox.question(self,'Conformation','Are you sure you want to delete this record?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if question==QMessageBox.StandardButton.Yes:
                sqlquery="DELETE FROM returned WHERE Return_ID=?"
                self.crsr.execute(sqlquery,(return_id,))
        self.connection.commit()
        self.connection.close()
    def search_records(self):
        search_Id=self.return_table_search.text().strip()
        for row in range(self.return_books_table.rowCount()):
            item=self.return_books_table.item(row,0)
            if item and item.text() == search_Id:
                self.return_books_table.selectRow(row)
                self.return_books_table.scrollToItem(item)
                return
    def add_borrow_record(self):
        self.crsr=self.create_connection().cursor()
        self.crsr.execute("""CREATE TABLE IF NOT EXISTS borrowed(
                Borrow_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Student_Name TEXT,
                Student_ID TEXT,
                Book_Name TEXT,
                Remarks TEXT,
                Borrow_Date TEXT,
                Return_Date TEXT,
                Book_Type TEXT,
                Book_ID INTEGER)""")
        self.add_new_borrow_record=[
                       self.borrow_line_1.text(),
                       self.borrow_line_2.text(),
                       self.borrow_line_3.text(),
                       self.borrow_line_4.text(),
                       self.borrow_line_5.text(),
                       self.borrow_line_6.text(),
                       self.borrow_line_7.text(),
                       self.borrow_line_8.text(),
                       self.borrow_line_9.text()]
        self.crsr.execute("INSERT INTO borrowed VALUES (?,?,?,?,?,?,?,?,?)",self.add_new_borrow_record)
        self.borrow_line_1.clear()
        self.borrow_line_2.clear()
        self.borrow_line_3.clear()
        self.borrow_line_4.clear()
        self.borrow_line_5.clear()
        self.borrow_line_6.clear()
        self.borrow_line_7.clear()
        self.borrow_line_8.clear()
        self.borrow_line_9.clear()
        self.connection.commit()
        self.connection.close()
    def view_borrowed_records(self):
        self.crsr=self.create_connection().cursor()
        borrow_sqlquery="SELECT COUNT(*) FROM borrowed"
        borrows_sqlquery="SELECT * FROM borrowed"
        self.crsr.execute(borrow_sqlquery)
        result=self.crsr.fetchone()
        self.borrow_books_table.setRowCount(result[0])
        self.borrow_books_table.setColumnCount(9)
        self.borrow_books_table.setHorizontalHeaderLabels(["Borrow_ID","Student_Name","Student_ID","Book_Name","Remarks","Borrow_Date","Return_Date","Book_Type","Book_ID"])
        #using loop to display all data in the table
        table_row=0
        for i in self.crsr.execute(borrows_sqlquery):
            self.borrow_books_table.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.borrow_books_table.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.borrow_books_table.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.borrow_books_table.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.borrow_books_table.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.borrow_books_table.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.borrow_books_table.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            self.borrow_books_table.setItem(table_row,7,QTableWidgetItem(str(i[7])))
            self.borrow_books_table.setItem(table_row,8,QTableWidgetItem(str(i[8])))
            table_row += 1
        self.connection.commit()
        self.connection.close()
    def remove_borrowed_record(self):
        self.crsr=self.create_connection().cursor()
        current_row=self.borrow_books_table.currentRow()
        borrow_id=str(self.borrow_books_table.item(current_row,0).text())
        if current_row<0:
            warning=QMessageBox.warning(self,'Warning','Please select a record to remove')
        else:
            question=QMessageBox.question(self,'Conformation','Are you sure you want to delete this record?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if question==QMessageBox.StandardButton.Yes:
                sqlquery="DELETE FROM borrowed WHERE Borrow_ID=?"
                self.crsr.execute(sqlquery,(borrow_id,))
        self.connection.commit()
        self.connection.close()
    def search_borrowed_records(self):
        search_Id=self.borrow_table_search.text().strip()
        for row in range(self.borrow_books_table.rowCount()):
            item=self.borrow_books_table.item(row,0)
            if item and item.text() == search_Id:
                self.borrow_books_table.selectRow(row)
                self.borrow_books_table.scrollToItem(item)
                return
    def add_fine(self):
        self.crsr=self.create_connection().cursor()
        self.crsr.execute("""CREATE TABLE IF NOT EXISTS fines(
                Fine_No INTEGER PRIMARY KEY AUTOINCREMENT,
                Student_ID TEXT,
                Student_Name TEXT,
                Borrowed_Book TEXT,
                Book_ID INTEGER,
                Amount INTEGER,
                Status TEXT,
                Reason TEXT,
                Remarks TEXT)""")
        self.add_new_fine=[
                       self.fine_line_1.text(),
                       self.fine_line_2.text(),
                       self.fine_line_3.text(),
                       self.fine_line_4.text(),
                       self.fine_line_5.text(),
                       self.fine_line_6.text(),
                       self.fine_line_7.currentText(),
                       self.fine_line_8.currentText(),
                       self.fine_line_9.text()]
        self.crsr.execute("INSERT INTO fines VALUES (?,?,?,?,?,?,?,?,?)",self.add_new_fine)
        self.fine_line_1.clear()
        self.fine_line_2.clear()
        self.fine_line_3.clear()
        self.fine_line_4.clear()
        self.fine_line_5.clear()
        self.fine_line_6.clear()
        self.fine_line_9.clear()
        self.connection.commit()
        self.connection.close()
    def view_fines(self):
        self.crsr=self.create_connection().cursor()
        fine_sqlquery="SELECT COUNT(*) FROM fines"  
        fines_sqlquery="SELECT * FROM fines"
        self.crsr.execute(fine_sqlquery)
        result=self.crsr.fetchone()
        self.borrow_books_table_2.setRowCount(result[0])
        self.borrow_books_table_2.setColumnCount(9)
        self.borrow_books_table_2.setHorizontalHeaderLabels(["Fine_No","Student_ID","Student_Name","Borrowed_Book","Book_ID","Amount","Status","Reason","Remarks"])
        #using loop to display all data in the table
        table_row=0
        for i in self.crsr.execute(fines_sqlquery):
            self.borrow_books_table_2.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.borrow_books_table_2.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.borrow_books_table_2.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.borrow_books_table_2.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.borrow_books_table_2.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.borrow_books_table_2.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.borrow_books_table_2.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            self.borrow_books_table_2.setItem(table_row,7,QTableWidgetItem(str(i[7])))
            self.borrow_books_table_2.setItem(table_row,8,QTableWidgetItem(str(i[8])))
            table_row += 1
        self.connection.commit()
        self.connection.close()
    def remove_fine(self):
        self.crsr=self.create_connection().cursor()
        current_row=self.borrow_books_table_2.currentRow()
        fine_no=str(self.borrow_books_table_2.item(current_row,0).text())
        if current_row<0:
            warning=QMessageBox.warning(self,'Warning','Please select a record to remove')
        else:
            question=QMessageBox.question(self,'Conformation','Are you sure you want to delete this record?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if question==QMessageBox.StandardButton.Yes:
                sqlquery="DELETE FROM fines WHERE Fine_No=?"
                self.crsr.execute(sqlquery,(fine_no,))
        self.connection.commit()
        self.connection.close()
    def search_fines(self):
        search_Id=self.borrow_line_17.text().strip()
        for row in range(self.borrow_books_table_2.rowCount()):
            item=self.borrow_books_table_2.item(row,0)
            if item and item.text() == search_Id:
                self.borrow_books_table_2.selectRow(row)
                self.borrow_books_table_2.scrollToItem(item)
                return
    def add_transaction(self):
        self.crsr=self.create_connection().cursor()
        self.crsr.execute("""CREATE TABLE IF NOT EXISTS transactions(
                Transaction_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                From_Account TEXT,
                To_Account TEXT,
                Amount INTEGER,
                Transaction_For TEXT)""")
        self.add_new_transaction=[
                       self.transaction_line_1.text(),
                       self.transaction_line_2.text(),
                       self.transaction_line_3.text(),
                       self.lineEdit_2.text(),
                       self.transaction_line_5.currentText()]
        self.crsr.execute("INSERT INTO transactions VALUES (?,?,?,?,?)",self.add_new_transaction)
        self.transaction_line_1.clear()
        self.transaction_line_2.clear()
        self.transaction_line_3.clear()
        self.lineEdit_2.clear()
        self.connection.commit()
        self.connection.close()
    def view_transactions(self):
        self.crsr=self.create_connection().cursor()
        transaction_sqlquery="SELECT COUNT(*) FROM transactions"  
        transactions_sqlquery="SELECT * FROM transactions"
        self.crsr.execute(transaction_sqlquery)
        result=self.crsr.fetchone()
        self.transaction_table.setRowCount(result[0])
        self.transaction_table.setColumnCount(5)
        self.transaction_table.setHorizontalHeaderLabels(["Transaction_ID","From_Account","To_Account","Amount","Transaction_For"])
        #using loop to display all data in the table
        table_row=0
        for i in self.crsr.execute(transactions_sqlquery):
            self.transaction_table.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.transaction_table.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.transaction_table.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.transaction_table.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.transaction_table.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            table_row += 1
        self.connection.commit()
        self.connection.close()
    def remove_transaction(self):
        self.crsr=self.create_connection().cursor()
        current_row=self.transaction_table.currentRow()
        transaction_id=str(self.transaction_table.item(current_row,0).text())
        if current_row<0:
            warning=QMessageBox.warning(self,'Warning','Please select a record to remove')
        else:
            question=QMessageBox.question(self,'Conformation','Are you sure you want to delete this record?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if question==QMessageBox.StandardButton.Yes:
                sqlquery="DELETE FROM transactions WHERE Transaction_ID=?"
                self.crsr.execute(sqlquery,(transaction_id,))
        self.connection.commit()
        self.connection.close()
    def search_transactions(self):
        search_Id=self.transaction_table_search.text().strip()
        for row in range(self.transaction_table.rowCount()):
            item=self.transaction_table.item(row,0)
            if item and item.text() == search_Id:
                self.transaction_table.selectRow(row)
                self.transaction_table.scrollToItem(item)
                return
    def show_books(self):
        self.crsr=self.create_connection().cursor()
        book_sqlquery="SELECT COUNT(*) FROM books"
        books_sqlquery="SELECT * FROM books"
        self.crsr.execute(book_sqlquery)
        result=self.crsr.fetchone()
        self.dashboard_table.setRowCount(result[0])
        self.dashboard_table.setColumnCount(10)
        self.dashboard_table.setHorizontalHeaderLabels(["Book_Name","Book_ID","Book_Type","Author","Publisher","Copies","Price","Date","Time","Remarks"])
        #using loop to display all data in the table
        table_row=0
        for i in self.crsr.execute(books_sqlquery):
            self.dashboard_table.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.dashboard_table.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.dashboard_table.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.dashboard_table.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.dashboard_table.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.dashboard_table.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.dashboard_table.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            self.dashboard_table.setItem(table_row,7,QTableWidgetItem(str(i[7])))
            self.dashboard_table.setItem(table_row,8,QTableWidgetItem(str(i[8])))
            self.dashboard_table.setItem(table_row,9,QTableWidgetItem(str(i[9])))
            table_row += 1
        self.connection.commit()
        self.connection.close()
    def show_returned(self):
        self.crsr=self.create_connection().cursor()
        record_sqlquery="SELECT COUNT(*) FROM returned"
        records_sqlquery="SELECT * FROM returned"
        self.crsr.execute(record_sqlquery)
        result=self.crsr.fetchone()
        self.dashboard_table.setRowCount(result[0])
        self.dashboard_table.setColumnCount(10)
        self.dashboard_table.setHorizontalHeaderLabels(["Return_ID","Book_Name","Book_Type","Student_Name","Student_ID","Book_ID","Received_By","Borrow_Date","Return_Date","Remarks"])
        #using loop to display all data in the table
        table_row=0
        for i in self.crsr.execute(records_sqlquery):
            self.dashboard_table.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.dashboard_table.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.dashboard_table.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.dashboard_table.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.dashboard_table.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.dashboard_table.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.dashboard_table.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            self.dashboard_table.setItem(table_row,7,QTableWidgetItem(str(i[7])))
            self.dashboard_table.setItem(table_row,8,QTableWidgetItem(str(i[8])))
            self.dashboard_table.setItem(table_row,9,QTableWidgetItem(str(i[9])))
            table_row += 1
        self.connection.commit()
        self.connection.close()
    def show_borrowed(self):    
        self.crsr=self.create_connection().cursor()
        borrow_sqlquery="SELECT COUNT(*) FROM borrowed"
        borrows_sqlquery="SELECT * FROM borrowed"
        self.crsr.execute(borrow_sqlquery)
        result=self.crsr.fetchone()
        self.dashboard_table.setRowCount(result[0])
        self.dashboard_table.setColumnCount(9)
        self.dashboard_table.setHorizontalHeaderLabels(["Borrow_ID","Student_Name","Student_ID","Book_Name","Remarks","Borrow_Date","Return_Date","Book_Type","Book_ID"])
        #using loop to display all data in the table
        table_row=0
        for i in self.crsr.execute(borrows_sqlquery):
            self.dashboard_table.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.dashboard_table.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.dashboard_table.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.dashboard_table.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.dashboard_table.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.dashboard_table.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.dashboard_table.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            self.dashboard_table.setItem(table_row,7,QTableWidgetItem(str(i[7])))
            self.dashboard_table.setItem(table_row,8,QTableWidgetItem(str(i[8])))
            table_row += 1
        self.connection.commit()
        self.connection.close()
    def show_fines(self):
        self.crsr=self.create_connection().cursor()
        fine_sqlquery="SELECT COUNT(*) FROM fines"  
        fines_sqlquery="SELECT * FROM fines"
        self.crsr.execute(fine_sqlquery)
        result=self.crsr.fetchone()
        self.dashboard_table.setRowCount(result[0])
        self.dashboard_table.setColumnCount(9)  
        self.dashboard_table.setHorizontalHeaderLabels(["Fine_No","Student_ID","Student_Name","Borrowed_Book","Book_ID","Amount","Status","Reason","Remarks"])
        #using loop to display all data in the table
        table_row=0
        for i in self.crsr.execute(fines_sqlquery):
            self.dashboard_table.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.dashboard_table.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.dashboard_table.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.dashboard_table.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.dashboard_table.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.dashboard_table.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.dashboard_table.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            self.dashboard_table.setItem(table_row,7,QTableWidgetItem(str(i[7])))
            self.dashboard_table.setItem(table_row,8,QTableWidgetItem(str(i[8])))
            table_row += 1
        self.connection.commit()
        self.connection.close()
    def show_transaction(self):
        self.crsr=self.create_connection().cursor()
        transaction_sqlquery="SELECT COUNT(*) FROM transactions"  
        transactions_sqlquery="SELECT * FROM transactions"
        self.crsr.execute(transaction_sqlquery)
        result=self.crsr.fetchone()
        self.dashboard_table.setRowCount(result[0])
        self.dashboard_table.setColumnCount(5)
        self.dashboard_table.setHorizontalHeaderLabels(["Transaction_ID","From_Account","To_Account","Amount","Transaction_For"])
        #using loop to display all data in the table
        table_row=0
        for i in self.crsr.execute(transactions_sqlquery):
            self.dashboard_table.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.dashboard_table.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.dashboard_table.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.dashboard_table.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.dashboard_table.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            table_row += 1
        self.connection.commit()
        self.connection.close()