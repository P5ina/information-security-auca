# Lab 8: Vim Editor — Command Reference

## Modes
| Mode | How to enter | Purpose |
|------|-------------|---------|
| Normal | `ESC` | Navigation and commands (default) |
| Insert | `i` / `a` / `o` | Typing text |
| Visual | `v` / `V` / `Ctrl+v` | Selecting text |
| Command | `:` | Executing commands |

## Navigation (Normal mode)
| Command | Action |
|---------|--------|
| `h j k l` | Left / Down / Up / Right |
| `w` / `b` | Next / previous word |
| `0` / `$` | Start / end of line |
| `gg` / `G` | Start / end of file |
| `Ctrl+f` / `Ctrl+b` | Page down / up |
| `:N` | Jump to line N |

## Editing (Normal mode)
| Command | Action |
|---------|--------|
| `i` | Insert before cursor |
| `a` | Insert after cursor |
| `o` / `O` | New line below / above |
| `x` | Delete character |
| `dd` | Delete line |
| `yy` | Copy (yank) line |
| `p` / `P` | Paste below / above |
| `u` | Undo |
| `Ctrl+r` | Redo |
| `r<char>` | Replace single character |
| `cw` | Change word |
| `.` | Repeat last command |

## Search & Replace
| Command | Action |
|---------|--------|
| `/pattern` | Search forward |
| `?pattern` | Search backward |
| `n` / `N` | Next / previous match |
| `:%s/old/new/g` | Replace all in file |
| `:%s/old/new/gc` | Replace all with confirmation |

## File Commands (Command mode)
| Command | Action |
|---------|--------|
| `:w` | Save |
| `:q` | Quit |
| `:wq` / `ZZ` | Save and quit |
| `:q!` | Quit without saving |
| `:e filename` | Open file |
| `:split` / `:vsplit` | Split window horizontally / vertically |

## Visual Mode
| Command | Action |
|---------|--------|
| `v` | Character selection |
| `V` | Line selection |
| `Ctrl+v` | Block selection |
| `y` | Copy selection |
| `d` | Delete selection |
| `>` / `<` | Indent / unindent |

## Useful Extras
| Command | Action |
|---------|--------|
| `:%d` | Delete all content |
| `gg=G` | Auto-indent entire file |
| `:set number` | Show line numbers |
| `:syntax on` | Enable syntax highlighting |
| `Ctrl+z` | Suspend vim (resume with `fg`) |
