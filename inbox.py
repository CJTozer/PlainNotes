# -*- coding: utf-8 -*-

import sublime, sublime_plugin

class InboxItemToNoteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        pos = view.sel()[0].a + 1 # Start of new note counts as in the note
        section_starts = view.find_all('^# ')

        this_note_start = 0
        this_note_end = view.size()
        for r in reversed(section_starts):
            if r.a < pos:
                this_note_start = r.a
                break
            this_note_end = r.a

        r = sublime.Region(this_note_start, this_note_end)
        new_note_text = view.substr(r)

        view.window().run_command('notes_new', {'text': new_note_text})
        view.erase(edit, r)
