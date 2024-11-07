class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = {}

    def get_all_words(self):
        dell = [',', '.', '=', '!', '?', ';', ':', ' - ']
        box = ''
        c = 0
        for count in self.file_names:
            with open(count, encoding='utf-8') as file:
                for words in file:
                    box = box.__add__(words.lower())
                    for d in dell:
                        box = box.replace(d, '')
                box = box.split()
                for word in self.file_names:
                    c += 1
                    self.all_words[f'count{c}'] = box

            return self.all_words

    def find(self, word):
        count = 0
        for sl in self.all_words.values():
            for words in sl:
                count += 1
                if word.lower() == words:
                    return {self.file_names: count}

    def count(self, word):
        count = 0
        for sl in self.all_words.values():
            for words in sl:
                if word.lower() == words:
                    count += 1
            return {self.file_names: count}





finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
