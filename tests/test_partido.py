import pytest
import sys
sys.path.append('src')
sys.path.append('../src')

from partido import Partido
from partidoJSON import PartidoJSON
from partido import EstadoPartido


def test_partido_no_comenzado():
    partido1 = Partido("Madrid", "Barcelona", "Liga", "2019")

    assert partido1.estado == EstadoPartido.NO_COMENZADO


def test_partido_en_juego():
    partido1 = Partido("Madrid", "Barcelona", "Liga", "2019")
    partido1.comenzar_partido()

    assert partido1.estado == EstadoPartido.EN_JUEGO


def test_partido_finalizado():
    partido1 = Partido("Madrid", "Barcelona", "Liga", "2019")
    partido1.comenzar_partido()
    partido1.finalizar_partido()

    assert partido1.estado == EstadoPartido.FINALIZADO

def test_partido_json():
    partido1 = Partido("Madrid", "Barcelona", "Liga", "2019")
    partido2 = PartidoJSON('./data/partido1.json')

    assert partido1.nombre == partido2.nombre
