class Topic:
    def __init__(self, inf: tuple):
        self.topic_id = inf[0]
        self.topic_title = inf[1]
        self.topic_intro = inf[2]

    def check(self) -> str:
        s = ''
        # if len(self.cno) > 4 or not self.cno.isalnum():
        #     s += '课程号长度不符或其中有除了字母和数字以外的字符\n'
        # if not self.ccredit.isnumeric():
        #     s += '学分中只能是数字'
        return s

    @staticmethod
    def get_model():
        return '(' + 'topic_id' + ',' + 'topic_title' + ',' + 'topic_intro' + ')'

    @staticmethod
    def get_att():
        return 'topic_id', 'topic_title', 'topic_intro'