class Borrower:
    def __init__(self, inf: tuple):
        self.borrower_id = inf[0]
        self.borrower_name = inf[1]
        self.borrower_pwd = inf[2]
        self.borrower_phone = inf[3]
        self.borrower_credit = inf[4]

    def check(self) -> str:
        s = ''
        # if len(self.cno) > 4 or not self.cno.isalnum():
        #     s += '课程号长度不符或其中有除了字母和数字以外的字符\n'
        # if not self.ccredit.isnumeric():
        #     s += '学分中只能是数字'
        return s

    @staticmethod
    def get_model():
        return '(' + 'borrower_id' + ',' + 'borrower_name' + ',' \
               + 'borrower_pwd' + ',' + 'borrower_phone' + ',' \
               + 'borrower_credit' + ')'

    @staticmethod
    def get_att():
        return 'borrower_id', 'borrower_name', 'borrower_pwd', 'borrower_phone', 'borrower_credit'
