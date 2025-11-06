print("Welcome to SMIT TechFest!")
print("Organized by Jacob Catayoc of APPDAET BTCS0")
# --- Registration Setup ---
try:
    num_participants = int(input("How many participants will register? "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()
if num_participants <= 0:
    print("Invalid number of participants.")
    exit()
# --- Collect Participant Information ---
participants = []
for i in range(num_participants):
    print(f"\nParticipant {i + 1}:")
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")
    participant = {"name": name, "track": track}
    participants.append(participant)
# --- Display Registered Participants ---
print("\nRegistered Participants:")
for i, p in enumerate(participants, start=1):
    print(f"{i}. {p['name']} - {p['track']}")
# --- Track Diversity Report ---
tracks = {p['track'] for p in participants}
print("\nTracks offered in this event:")
print(", ".join(tracks))
if len(tracks) < 2:
    print("Not enough variety in tracks.")
# --- Duplicate Name Detection ---
names_seen = set()
duplicates = set()
for p in participants:
    if p["name"] in names_seen:
        duplicates.add(p["name"])
    else:
        names_seen.add(p["name"])
if duplicates:
    for name in duplicates:
        print(f"\nDuplicate name found: {name}")
else:
    print("\nNo duplicate names.")
# --- Track Summary Report ---
summary = {}
for p in participants:
    track = p["track"]
    summary[track] = summary.get(track, 0) + 1
print("\nParticipants per track:")
for track, count in summary.items():
    print(f"{track}: {count}")


