# cual-id changelog

## Version 0.9.0 (changes since 0.9.0 release go here)

### Features
* Added the ability to add a previously existing list of IDs to the create command  
* Changed the format of ID creation to (cual-id, UUID) instead of (UUID, cual-id) to make the --existing -ids function work with cual-ids. Changed label.py and fix.py to reflect these changes

### Bugs
* Bug fix: There was a small bug in the previous version that would occasionally cause issues when installing with conda
