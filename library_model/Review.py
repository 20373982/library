class Review:
    def __init__(self, inf: tuple):
        self.review_id = inf[0]
        self.review_book = inf[1]
        self.review_content = inf[2]
        self.review_mark = inf[3]

    def check(self) -> str:
        s = ''
        # if len(self.cno) > 4 or not self.cno.isalnum():
        #     s += '课程号长度不符或其中有除了字母和数字以外的字符\n'
        # if not self.ccredit.isnumeric():
        #     s += '学分中只能是数字'
        return s

    @staticmethod
    def get_model():
        return '(' + 'review_id' + ',' + 'review_book' + ',' \
               + 'review_content' + ',' + 'review_mark' + ')'

    @staticmethod
    def get_att():
        return 'review_id', 'review_book', 'review_content', 'review_mark'