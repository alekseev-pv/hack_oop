class InventoryError(Exception):
    pass


class InventoryOverflowError(InventoryError):
    pass


class DropThingError(Exception):
    pass
