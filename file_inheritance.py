class File:
    def __init__(self, path: str):
        self.path = path
        self.contents = ""

    def add_content(self, content: str):
        self.contents += content

    @property
    def size(self):
        sizes = (len(c) for c in self.contents)
        return sum(sizes)

    @property
    def info(self):
        return f"{self.path} [size={self.size}B]"


class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple[float], duration: int):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

    @property
    def info(self):
        return f"{self.path} [codec={self.codec}, geoloc={self.geoloc}, duration={self.duration}s]"


class VideoFile(MediaFile):
    def __init__(
        self,
        path: str,
        codec: str,
        geoloc: tuple[float],
        duration: int,
        dimensions: tuple[int],
    ):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    @property
    def info(self):
        base_info = super().info
        return f"{base_info}\nDimensions: {self.dimensions}"
