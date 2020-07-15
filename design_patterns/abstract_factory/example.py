import enum
from abc import ABC, abstractmethod
from typing import List


class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


class Guitar(Instrument):
    def play(self):
        print("Strum strings")


class Saxophone(Instrument):
    def play(self):
        print("Blow into mouthpiece")


class InstrumentFactory(ABC):
    @abstractmethod
    def build(self, amount: int) -> Instrument:
        pass


class GuitarFactory(InstrumentFactory):
    def build(self, amount: int) -> Guitar:
        print(
            "Put body and neck together, "
            f"put some strings on it, do it {amount} time(s)."
        )
        return Guitar()


class SaxophoneFactory(InstrumentFactory):
    def build(self, amount: int) -> Saxophone:
        print(
            "Smash metal and make if look like saxophone, "
            f"do it {amount} time(s)."
        )
        return Saxophone()


class InstrumentBuilder:
    class AvailableInstrument(enum.Enum):
        SAXOPHONE = enum.auto()
        GUITAR = enum.auto()

    factories: List[InstrumentFactory] = []
    initialized: bool = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True

            for instrument in self.AvailableInstrument:
                name = instrument.name.title()
                factory_name = f"{name}Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_instrument(self) -> Instrument:
        print("Available instruments: ")
        for i, f in enumerate(self.factories):
            print(f"{i}. {f[0]}")

        s = input(f"Please pick instrument (0-{len(self.factories) - 1}): ")
        idx = int(s)
        s = input(f"Specify amount: ")
        amount = int(s)
        return self.factories[idx][1].build(amount)


if __name__ == "__main__":
    instrument_builder = InstrumentBuilder()
    instrument = instrument_builder.make_instrument()
    instrument.play()
