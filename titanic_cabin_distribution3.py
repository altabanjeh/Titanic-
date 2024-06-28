import matplotlib.pyplot as plt

# Define the positions of different classes on different decks
decks = {
    'Boat Deck': {},
    'A Deck (Promenade Deck)': {
        'First Class Lounges': (1, 1),
        'First Class Suites': (2, 1),
        'First Class Promenades': (3, 1)
    },
    'B Deck (Bridge Deck)': {
        'First Class cabins': (1, 2),
        'First Class Suites': (2, 2),
        'Verandah Café, Palm Court': (3, 2)
    },
    'C Deck (Shelter Deck)': {
        'First Class cabins': (1, 3),
        'First Class cabins': (2, 3),
        'Second Class cabins': (3, 3)
    },
    'D Deck (Saloon Deck)': {
        'First Class cabins': (1, 4),
        'First Class Dining Saloon': (2, 4),
        'Second Class Dining Saloon': (3, 4)
    },
    'E Deck (Upper Deck)': {
        'First Class cabins': (1, 5),
        'First & Second Class cabins': (2, 5),
        'Second & Third Class cabins': (3, 5)
    },
    'F Deck (Middle Deck)': {
        'Third Class cabins': (1, 6),
        'First Class cabins, Pool, Baths': (2, 6),
        'Second & Third Class cabins': (3, 6)
    },
    'G Deck (Lower Deck)': {
        'Third Class cabins': (1, 7),
        'Crew quarters, Third Class cabins': (2, 7),
        'Third Class cabins': (3, 7)
    },
    'Orlop Deck': {
        'Cargo holds, Third Class berths': (1, 8),
        'Cargo holds, mail room': (2, 8),
        'Cargo holds': (3, 8)
    },
    'Poop Deck': {
        'Third Class open deck': (2, 9)
    }
}

fig, ax = plt.subplots(figsize=(10, 15))

# Loop through each deck and plot the sections
for deck, sections in decks.items():
    for section, position in sections.items():
        ax.text(position[0], position[1], section, ha='center', va='center',
                bbox=dict(facecolor='white', alpha=0.5, boxstyle='round,pad=1'))

# Set the labels and limits
ax.set_yticks(range(1, 11))
ax.set_yticklabels(decks.keys())
ax.set_xticks(range(1, 4))
ax.set_xticklabels(['Forward', 'Midships', 'Aft'])
ax.set_xlim(0.5, 3.5)
ax.set_ylim(0.5, 10.5)

# Add grid lines
ax.grid(True)

# Add title
plt.title('Titanic Cabin Distribution')

# Show plot
plt.show()
