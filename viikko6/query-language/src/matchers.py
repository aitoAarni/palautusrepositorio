class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class Or:
    def __init__(self, matchers) -> None:
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        return False


class PlaysIn:
    def __init__(self, previous_matcher, team):
        self.previous_matcher = previous_matcher
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, previous_matcher, value, attr):
        self.previous_matcher = previous_matcher
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, previous_matcher, value, attr) -> None:
        self.previous_matcher = previous_matcher
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
    def __init__(self, previous_matcher=None) -> None:
        self.previous_matcher = previous_matcher

    def matches(self, player):
        previous_matcher = self.previous_matcher
        while True:
            if previous_matcher is None:
                return True
            if not previous_matcher.matches(player):
                return False
            previous_matcher = previous_matcher.previous_matcher

class OneOff:
    def __init__(self, pre) -> None:
        pass
        


class QueryBuilder:
    def __init__(self, matcher=None) -> None:
        self._matcher_object = matcher

    def build(self):
        return All(self._matcher_object)

    def hasAtLeast(self, value, attribute):
        return QueryBuilder(HasAtLeast(self._matcher_object, value, attribute))

    def hasFewerThan(self, value, attribute):
        return QueryBuilder(HasFewerThan(self._matcher_object, value, attribute))
    
    def playsIn(self, team):
        return QueryBuilder(PlaysIn(self._matcher_object, team))
    
    def negative(self, matcher):
        return QueryBuilder(Not(self._matcher_object, matcher))

    def oneOf(self, *matchers):
        return QueryBuilder(Or((matchers)))