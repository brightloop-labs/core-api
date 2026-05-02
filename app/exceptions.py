class CoreApiError(Exception):
    """Base class for application-specific errors."""


class OrderNotFoundError(CoreApiError):
    def __init__(self, order_id: int):
        self.order_id = order_id
        super().__init__(f"Order {order_id} not found")


class InvalidOrderStateError(CoreApiError):
    pass