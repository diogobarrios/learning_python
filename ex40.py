# Exercise 40 Modules, Classes and Objects

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there\n"])


bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells\n"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Another way around


class MySong(object):

    def __init__(self):
        self.happy_birthday = (["Happy birthday to you",
                                "I don't want to get sued",
                                "So I'll stop right there"])

    def bulls_song(self):
        print(["They rally around tha family",
               "With pockets full of shells"])


listen = MySong()
listen.bulls_song()
print(listen.happy_birthday)
