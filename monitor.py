class monitor:
    _resolucao_maxima_horizontal:int = 1024
    _resolucao_maxima_vertical:int = 1280
    _resolucao_horizontal_atual:int = 1024
    _resolucao_vertical_atual:int = 1280
    _volume:int = 10 # que pode receber de 0 a 100
    _ligado:bool = False

    def __init__(self):
        pass
    
    def aumentaVolume(self):
        #  possibilita aumentar o volume em incrementos de 5
        self._volume = 100 if (self._volume + 5 > 100 and self._ligado) else self._volume + 5
    
    def diminuiVolume(self):
        # possibilita aumentar o volume em incrementos de 5
        self._volume = 0 if (self._volume - 5 < 0 and self._ligado) else self._volume - 5
    
    def liga(self):
        # liga o monitor
        self._ligado =  True
    def desliga(self):
        # desliga o monitor
        self._ligado =  False
    def alteraResolucao(self, horizontal: int, vertical: int):
        # muda a resolução atual, não pode ser superior à resolução máxima horizontal ou vertical
        self._resolucao_horizontal_atual = self._resolucao_maxima_horizontal if horizontal > self._resolucao_maxima_horizontal and self._ligado else horizontal
        self._resolucao_vertical_atual = self._resolucao_maxima_vertical if vertical > self._resolucao_maxima_vertical and self._ligado else vertical

if __name__ == "__main__":
    n = monitor()
    n.liga()
    n.aumentaVolume()