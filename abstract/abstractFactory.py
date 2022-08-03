from abc import ABC, abstractmethod

class Sword(ABC):
    @abstractmethod
    def item_info(self):
        pass

class WoodSword(Sword):
    def item_info(self):
        return (5, 60, "Melee weapon that is mainly used to damage entities and for cutting cobwebs or bamboo.", "Wood")

class StoneSword(Sword):
    def item_info(self):
        return (6, 132, "Melee weapon that is mainly used to damage entities and for cutting cobwebs or bamboo.", "Stone")

class DiamondSword(Sword):
    def item_info(self):
        return (8, 1562, "Melee weapon that is mainly used to damage entities and for cutting cobwebs or bamboo.", "Diamond")

class Axe(ABC):
    @abstractmethod
    def item_info(slef):
        pass

class WoodAxe(Axe):
    def item_info(self):
        return (7, 60, "Tool mainly used to hasten the breaking of wood-based blocks, remove the surface layer of certain blocks, and as a melee weapon.", "Wood")

class StoneAxe(Axe):
    def item_info(self):
        return (9, 132, "Tool mainly used to hasten the breaking of wood-based blocks, remove the surface layer of certain blocks, and as a melee weapon.", "Stone")

class DiamondAxe(Axe):
    def item_info(self):
        return (9, 1562, "Tool mainly used to hasten the breaking of wood-based blocks, remove the surface layer of certain blocks, and as a melee weapon.", "Diamond")

class ItemFactory(ABC):
    @abstractmethod
    def create_sword(self):
        pass
    def create_axe(self):
        pass

class WoodFactory(ItemFactory):
    def create_sword(self):
        return WoodSword()
    def create_axe(self):
        return WoodAxe()

class StoneFactory(ItemFactory):
    def create_sword(self):
        return StoneSword()
    def create_axe(self):
        return StoneAxe()

class DiamondFactory(ItemFactory):
    def create_sword(self):
        return DiamondSword()
    def create_axe(self):
        return DiamondAxe()

if __name__ == "__main__":
    #para este ejercicio no se realizara el metodo exacto para elegir un item, en caso de modificar cambiar los elementos de abajo a su respectivo item
    factory = DiamondFactory()
    item = factory.create_axe()
    info = item.item_info()

    print( "Damage:", info[0] )
    print( "Durability:", info[1] )
    print( "Description:", info[2] )
    print( "Material:", info[3] )


