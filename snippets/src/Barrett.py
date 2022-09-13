class Barrett:
    def mul(self, a, b):
        assert 0 <= a < self._m
        assert 0 <= b < self._m
        z = a * b
        v = z - ((z * self.im)>>64) * self._m
        if v < 0: v += self._m
        return v
