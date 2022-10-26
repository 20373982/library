class Manager:
    def __init__(self, inf: tuple):
        self.manager_id = inf[0]
        self.manager_name = inf[1]
        self.manager_pwd = inf[2]
        self.manager_phone = inf[3]

    def check(self) -> str:
        s = ''
        # if len(self.cno) > 4 or not self.cno.isalnum():
        #     s += '课程号长度不符或其中有除了字母和数字以外的字符\n'
        # if not self.ccredit.isnumeric():
        #     s += '学分中只能是数字'
        return s

    @staticmethod
    def get_model():
        return '(' + 'manager_id' + ',' + 'manager_name' + ',' \
               + 'manager_pwd' + ',' + 'manager_phone' + ')'

    @staticmethod
    def get_att():
        return 'manager_id', 'manager_name', 'manager_pwd', 'manager_phone'
