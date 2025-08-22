
class Simulator:
    def __init__(self, order_book):
        self.book = order_book

    def market_buy(self, size):
        return self._walk_levels(size, side='sell')

    def market_sell(self, size):
        return self._walk_levels(size, side='buy')

    def _walk_levels(self, target_size, side):
        if target_size <= 0:
            raise ValueError("target_size must be positive")
        levels = self.book.levels(side)
        filled = 0.0
        total_value = 0.0
        level_index = 0
        leftover_from_level = 0.0

        while filled < target_size and level_index < len(levels):
            level = levels[level_index]
            take = level.amount
            if filled + take > target_size:
                leftover_from_level = filled + take - target_size
                take = target_size - filled

            total_value += level.price * take
            filled += take
            level_index += 1

        if filled < target_size:
            return {
                'filled': filled,
                'avg_price': None,
                'last_price': None,
                'total_value': None,
                'levels_used': level_index,
                'note': 'Insufficient depth to fully fill the order.'
            }

        avg_price = total_value / target_size
        last_price = levels[level_index - 1].price if level_index > 0 else None

        first_price = levels[0].price if levels else None
        price_move = None
        if first_price is not None and last_price is not None:
            price_move = last_price - first_price

        return {
            'filled': round(target_size, 8),
            'avg_price': round(avg_price, 8),
            'last_price': round(last_price, 8) if last_price is not None else None,
            'total_value': round(total_value, 2),
            'levels_used': level_index,
            'leftover_from_last_level': round(leftover_from_level, 8),
            'price_move': round(price_move, 8) if price_move is not None else None
        }
