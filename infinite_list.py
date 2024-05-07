class InfiniteList:
    def __init__(self, *args, fill_value=None):
        self.args = list(args)
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        if isinstance(index, int):
            if index >= len(self.args):
                return self.fill_value
            else:
                return self.args[index]
        return self.args

    def __len__(self):
        return len(self.args)

    def __setitem__(self, index: int, item) -> None:
        if isinstance(index, int):
            if index >= len(self.args):
                self.args += [self.fill_value] * (index - len(self.args) + 1)
            self.args[index] = item

    def __str__(self):
        return f"{self.args}"
