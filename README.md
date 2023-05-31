# PaSSAGE-for-EMGlue

A version of PaSSAGE that works with [EM-Glue](https://github.com/liogiu2/EM-Glue) platform. 
# New release is about to come out. This page is under manteinance.
![work in progress](https://icambrogiolorenzetti.edu.it/wp-content/uploads/sites/91/Work-in-progress-1024x603-1.png?x67262)

## Table of Compatibility
### Initialization - additional_data field
| Key           | Format              | Additional information    |
|---------------|---------------------|---------------------------|
| "encounters"  | list of dictionary  | Each dictionary has 4 keys "name", "description", "metadata", "preconditions" <p> "name": string, indicates the name of the encounter. The EM will send this name to have an encounter executed. <p>"description": string, description of the encounter that the author defined.<p>"metadata": dictionary, with key "target-model" containing a list of the features that the author has defined as target for the encounter <p>"preconditions": string, a list of preconditions using PDDL   |

### Normal Communication - EM -> ENV
| Message accepted | Format              | Additional information    |
|------------------|---------------------|---------------------------|
| PDDL actions     | string              | Message containing the PDDL action to be executed |

### Normal Communication - ENV -> EM
| Key                   | Format              | Additional information                                    |
|-----------------------|---------------------|-----------------------------------------------------------|
| "new"                 | string              | New relation added to the world state                     |
| "changed_value"       | string              | Relation changed value in the world state                 |
| "update_player_model" | string              | An update to the player model happened in the environment. <p> The string contains five values formatted as: <p> "('value_1', 'value_2', 'value_3', 'value_4', 'value_5')"|