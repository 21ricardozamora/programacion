class InfiniteList:
    def __init__(self, *args, fill_value=None):
        self.args = list(args)
        self.items = args
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        return self.items[index]

    def __len__(self):
        return len(self.args)

    def __setitem__(self, index: int, items) -> None:
        self.item = items
        if isinstance(index, int):
            if index >= len(self.args):
                self.args += [self.fill_value] * (index - len(self.args) + 1)
                self.items[index] = self.args    
    def __str__(self):

        return f"{self.args}"
