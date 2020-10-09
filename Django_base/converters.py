class MobilePhoneConverter:
    regex = '1[3-9]\d{9}'
    def to_python(self, value):
        return int(value)
    def to_url(self, value):
        return str(value)

class EmailConverter:
    regex='[0-9a-zA-Z_]{3,19}@(qq|163|126)\.com'
    def to_python(self,value):
        return value

    def to_url(self, value):
        return str(value)