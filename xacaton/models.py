class Cars:
    objects = []
    def __init__(self, marka, model, year, engine_volume, color, cusov, probeg, price):
        self.marka = marka
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        self.cusov = cusov 
        self.probeg = probeg
        self.price = price
        Cars.objects.append(self)
    def __str__(self):
        return self

    