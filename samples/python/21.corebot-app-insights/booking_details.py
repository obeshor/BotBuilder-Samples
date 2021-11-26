# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


class BookingDetails:
    def __init__(
        self,
        destination: str = None,
        origin: str = None,
        start: str = None,
        end: str = None,
        budget: str = None,
        unsupported_airports=None,
        user_input = None,
        luis_intent = None,
        luis_entities = None,
        final_entities = None
    ):
        if unsupported_airports is None:
            unsupported_airports = []
        self.destination = destination
        self.origin = origin
        self.start = start
        self.end = end
        self.budget = budget
        self.unsupported_airports = unsupported_airports
        self.user_input = user_input
        self.luis_intent = luis_intent
        self.luis_entities = luis_entities
        self.final_entities = final_entities
