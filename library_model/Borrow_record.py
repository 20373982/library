class Borrow_record:
    def __init__(self, inf: tuple):
        self.borrower_id = inf[0]
        self.book_id = inf[1]
        self.borrower_time = inf[2]
        self.return_time = inf[3]

    def check(self) -> str:
        s = ''
        # if len(self.cno) > 4 or not self.cno.isalnum():
        #     s += '课程号长度不符或其中有除了字母和数字以外的字符\n'
        # if not self.ccredit.isnumeric():
        #     s += '学分中只能是数字'
        return s

    @staticmethod
    def get_model():
        return '(' + 'borrower_id' + ',' + 'book_id' + ',' \
               + 'borrower_time' + ',' + 'return_time' + ')'

    @staticmethod
    def get_att():
        return 'borrower_id', 'book_id', 'borrower_time', 'return_time'
