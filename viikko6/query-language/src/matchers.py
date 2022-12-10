class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class Or:
    def __init__(self, *matchers) -> None:
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        return False


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr) -> None:
        self._value = value
        self._attribute = attr

    def matches(self, player):
        player_value = getattr(player, self._attribute)
        return self._value > player_value

class Not:
    def __init__(self, matcher) -> None:
        self._matcher_object = matcher

    def matches(self, player):
        return not self._matcher_object.matches(player)

class All:
    def matches(self):
        return True