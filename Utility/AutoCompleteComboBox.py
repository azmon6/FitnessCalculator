from tkinter import ttk

class AutocompleteCombobox(ttk.Combobox):
    def set_completion_list(self, completion_list):
        self._hits = completion_list
        self._hits_lower = [x.lower() for x in completion_list]
        self['values'] = self._hits
        self.bind('<KeyRelease>', self.handle_keyrelease)

    def handle_keyrelease(self, event):
        # Filter the list based on the user input
        typed = self.get().lower()
        if typed == '':
            hits = self._hits
        else:
            hits = [item for item in self._hits if typed in item.lower()]
        
        # Update the Combobox dropdown list
        self['values'] = hits