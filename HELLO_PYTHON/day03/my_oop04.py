class LeeJY:
    def __init__(self):
        self.cnt_company = 20
    
    def seat(self):
        self.cnt_company += 1

class Bin:
    def __init__(self):
        self.amount_oil = 10000
    
    def dig(self):
        self.amount_oil *= 2
    
class KimJeungUn:
    def __init__(self):
        self.cnt_nuclear = 30
    
    def aoji(self):
        self.cnt_nuclear += 2
    
class KimJiWan(LeeJY, Bin, KimJeungUn):
    def __init__(self):
        super().__init__()
        LeeJY.__init__(self)
        Bin.__init__(self)
        KimJeungUn.__init__(self)
        
kjw = KimJiWan()
print(kjw.cnt_company)
print(kjw.amount_oil)
print(kjw.cnt_nuclear)

kjw.seat()
kjw.dig()
kjw.aoji()
print(kjw.cnt_company)
print(kjw.amount_oil)
print(kjw.cnt_nuclear)