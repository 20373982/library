class Message:
    def __init__(self, inf: tuple):
        self.message_id = inf[0]
        self.message_writer = inf[1]
        self.message_content = inf[2]
        self.message_topic = inf[3]
        self.message_reply = inf[4]

    def check(self) -> str:
        s = ''
        # if len(self.cno) > 4 or not self.cno.isalnum():
        #     s += '课程号长度不符或其中有除了字母和数字以外的字符\n'
        # if not self.ccredit.isnumeric():
        #     s += '学分中只能是数字'
        return s

    @staticmethod
    def get_model():
        return '(' + 'message_id' + ',' + 'message_writer' + ',' \
               + 'message_content' + ',' + 'message_topic' + ',' + 'message_reply' + ')'

    @staticmethod
    def get_att():
        return 'message_id', 'message_writer', 'message_content', 'message_topic', 'message_reply'
