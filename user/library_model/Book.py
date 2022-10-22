class Book:
    def __init__(self, inf: tuple):
        self.book_id = inf[0]
        self.book_name = inf[1]
        self.book_writer = inf[2]
        self.book_introduction = inf[3]
        self.book_hot = inf[4]
        self.book_path = inf[5]

    def check(self) -> str:
        s = ''
        # if len(self.cno) > 4 or not self.cno.isalnum():
        #     s += '课程号长度不符或其中有除了字母和数字以外的字符\n'
        # if not self.ccredit.isnumeric():
        #     s += '学分中只能是数字'
        return s

    @staticmethod
    def get_model():
        return '(' + 'book_id' + ',' + 'book_name' + ',' \
               + 'book_writer' + ',' + 'book_introduction' + ',' \
               + 'book_hot' + "," + 'book_path' + ')'

    @staticmethod
    def get_att():
        return 'book_id', 'book_name', 'book_writer', 'book_introduction', 'book_hot', 'book_path'
