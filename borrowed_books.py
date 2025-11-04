class BorrowedBook:
    def __init__(self, ID, MSSV, full_name, name_book, borrow_date, return_date, countdown, status, action):
        self.ID = ID
        self.MSSV = MSSV
        self.full_name = full_name
        self.name_book = name_book
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.countdown = countdown
        self.status = status
        self.action = action