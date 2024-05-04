##########################################
# CONTEXT

# Helps trace errors back to their origin
class Context:
    def __init__(self, display_name, parent=None, parent_entry_position=None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_position = parent_entry_position