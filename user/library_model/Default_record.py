class Default_record:
    def __init__(self, inf: tuple):
        self.borrower_id = inf[0]
        self.book_id = inf[1]
        self.return_time = inf[2]

    def check(self) -> str:
        s = ''
        # if len(self.cno) > 4 or not self.cno.isalnum():
        #     s += '课程号长度不符或其中有除了字母和数字以外的字符\n'
        # if not self.ccredit.isnumeric():
        #     s += '学分中只能是数字'
        return s

    @staticmethod
    def get_model():
        return '(' + 'borrower_id' + ',' + 'book_id' + ',' + 'return_time' + ')'

    @staticmethod
    def get_att():
        return 'borrower_id', 'book_id', 'return_time'
