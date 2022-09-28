from ev_pddl.world_state import WorldState
import debugpy

class Encounter:

    def __init__(self, initialization_text, worldstate : WorldState):
        self.name = initialization_text['name']
        self.description = initialization_text['description']
        self.metadata = initialization_text['metadata']
        self.preconditions_text = initialization_text['preconditions']
        self.preconditions = worldstate.create_action_proposition_from_PDDL(self.preconditions_text)
