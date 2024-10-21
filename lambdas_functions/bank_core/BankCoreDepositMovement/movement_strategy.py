class MovementStrategy:
    def add_movement(self, movements, movement_id_, concept, amount, date):
        raise NotImplementedError
    
    # this example to Fernanda


class ChargeMovementStrategy(MovementStrategy):
    def add_movement(self, movements, movement_id, concept, amount, date):
        movements['movements'].append({
            'id': movement_id,
            'type': 'charge',
            'concept': concept,
            'amount': -amount,
            'date': date
        })


class DepositMovementStrategy(MovementStrategy):
    def add_movement(self, movements, movement_id, concept, amount, date):
        movements['movements'].append({
            'id': movement_id,
            'type': 'deposit',
            'concept': concept,
            'amount': amount,
            'date': date
        })
