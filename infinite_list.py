class InfiniteList:
    def __init__(self, *args, fill_value=None):
        self.items = list(args)
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __setitem__(self, index: int, items) -> None:
        if isinstance(index, int):
            if index > len(self.items):
                self.items += [self.fill_value] * abs(index - len(self.items) + 1)
            self.items[index] = items
        print(self.args)

    def __str__(self):

        return ",".join(str(_) for _ in self.items)
