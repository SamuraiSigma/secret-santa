"""Contains the Matchmaker class."""

import random


class Matchmaker:
    """Randomly chooses secret santas for participating people.

    The class guarantees that a person won't get themselves as their
    secret santa.
    """

    @staticmethod
    def match(people):
        """Choose and set a secret santa for each given person.

        Arg:
            people: List of Person objects that will each receive a secret
                    santa.

        Raises:
            ValueError: If length of people is < 2.
        """
        if len(people) < 2:
            raise ValueError('At least 2 people are required for a '
                             'secret santa!')

        is_derangement = False

        while not is_derangement:
            is_derangement = True
            santas = list(people)
            random.shuffle(santas)

            # Check if a person got themselves as their secret santa
            for i in range(len(people)):
                if people[i] == santas[i]:
                    is_derangement = False
                    break
                people[i].santa = santas[i]
