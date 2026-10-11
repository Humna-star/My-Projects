class Pakistan():
    def capital(self):
        print("Isalamabad is the capital of Pakistan")

    def language(self):
        print("Urdu is the national language of Pakistan")

    def type(self):
        print("Pakistan is a developing country")

class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the national language of India")

    def type(self):
        print("India is a developing country")

class China():
    def capital(self):
        print("Beijing is the capital of China")

    def language(self):
        print("Mandarin is the national language of China")

    def type(self):
        print("China is a developing country")

class USA():
    def capital(self):
        print("Washington D.C. is the capital of USA")

    def language(self):
        print("English is the national language of USA")

    def type(self):
        print("USA is a developed country")

class UK():
    def capital(self):
        print("London is the capital of UK")

    def language(self):
        print("English is the national language of UK")

    def type(self):
        print("UK is a developed country")

class Germany():
    def capital(self):
        print("Berlin is the capital of Germany")

    def language(self):
        print("German is the national language of Germany")

    def type(self):
        print("Germany is a developed country")

class France():
    def capital(self):
        print("Paris is the capital of France")

    def language(self):
        print("French is the national language of France")

    def type(self):
        print("France is a developed country")

class Japan():
    def capital(self):
        print("Tokyo is the capital of Japan")

    def language(self):
        print("Japanese is the national language of Japan")

    def type(self):
        print("Japan is a developed country")

class Australia():
    def capital(self):
        print("Canberra is the capital of Australia")

    def language(self):
        print("English is the national language of Australia")

    def type(self):
        print("Australia is a developed country")

class Canada():
    def capital(self):
        print("Ottawa is the capital of Canada")

    def language(self):
        print("English and French are the national languages of Canada")

    def type(self):
        print("Canada is a developed country")

obj_pak = Pakistan()
obj_ind = India()
obj_chi = China()
obj_usa = USA()
obj_uk = UK()
obj_ger = Germany()
obj_fra = France()
obj_jap = Japan()
obj_aus = Australia()
obj_can = Canada()

for country in (obj_pak, obj_ind, obj_chi, obj_usa, obj_uk, obj_ger, obj_fra, obj_jap, obj_aus, obj_can):
    country.capital()
    country.language()
    country.type()