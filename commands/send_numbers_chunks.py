import re


class SendNumbersByChunks:
    def __init__(self, path_to_numbers):
        self.path_to_numbers = path_to_numbers
        with open(self.path_to_numbers, 'r') as file:
            self.text_numbers = [line.strip() for line in file.readlines()]
        self.text_numbers = self.clear_numbers()
        self.numbers_chunks = self.make_chunks()

    def make_chunks(self, n=3):
        chunks = []
        for i in range(0, len(self.text_numbers), n):
            chunks.append(self.text_numbers[i:i + n])
        return chunks

    def clear_numbers(self):
        clear_numbers_list = []
        for line in self.text_numbers:
            line = re.sub(r"(\s|-|_|\(|\)|\t|\n)", "", line)
            if not re.match(r"\+7\d{6,12}", line) and not re.match("\+375\d{5,12}", line):
                print(f"{line} not match +7ххххххххххх or +375ххххххххх")
            else:
                clear_numbers_list.append(line)
                print(f"{line} added.")
        return clear_numbers_list
