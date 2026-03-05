from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Card:
    name: str
    team: str
    parallel: str = "Base"
    serial_number: Optional[str] = None
    case_hit: bool = False
    rookie: bool = False

    
    def __str__(self):
        serial = f" {self.serial_number}" if self.serial_number else ""

        result = f"{self.name} | {self.team} | {self.parallel}{serial}"

        if self.case_hit:
            result += " | CASE HIT"

        if self.rookie:
            result += " | RC"

        return result

@dataclass
class Pack:
    name: str
    capacity: int
    cards: list[Card] = field(default_factory=list)

    def add_card(self, card: Card) -> None:
        if len(self.cards) >= self.capacity:
            raise ValueError(f"Pack '{self.name} is full (Capcity = {self.capacity}).")
        self.cards.append(card)
    def is_full(self) -> bool:
        return len(self.cards) >= self.capacity
    
    def empty(self):
        self.cards.clear()

    def __str__(self):
        header = f"{self.name}:"

        if not self.cards:
            return header + "\n  [Pack is Empty]"

        cards_in_pack = "\n".join(f"    {card}" for card in self.cards)
        return f"{header}\n{cards_in_pack}"

@dataclass
class Box:
    name: str
    capacity: int
    packs: list[Pack] = field(default_factory=list)

    def add_pack(self, pack: Pack) -> None:
        if len(self.packs) >= self.capacity:
            raise ValueError(f"Box '{self.name} is full (Capcity = {self.capacity}).")
        self.packs.append(pack)

    def is_full(self) -> bool:
        return len(self.packs) >= self.capacity
    
    def empty(self):
        self.packs.clear()

    def __str__(self):
        header = f"{self.name}:"

        if not self.packs:
            return header + "\n  [Box is Empty]"

        packs_in_box = "\n".join("\n".join("    " + 
                        line for line in str(pack).splitlines())
                        for pack in self.packs)
        
        return f"{header}\n{packs_in_box}"


if __name__ == "__main__":
    card1 = Card("Mike Trout", "Angels", rookie=True)
    card2 = Card("Elly De La Cruz", "Reds", parallel="Blue", serial_number="/150", rookie=True)
    card3 = Card("Ken Griffey Jr.", "Mariners", parallel="Downtown", case_hit=True)

    print(card1)
    print(card2)
    print(card3)

    pack = Pack("Test Pack", 3)

    pack.add_card(Card("Mike Trout", "Angels"))
    pack.add_card(Card("Elly De La Cruz", "Reds", parallel="Orange Refractor", serial_number="/400", rookie=True))

    print(f"\n{pack}")

    box = Box("Test box", 2)

    box.add_pack(pack)

    print(f"\n{box}")