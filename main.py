"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance: toast landing butter-side down.

Candidates considered (3, genuinely different):
  A. Shower curtain with tiny suction-cup hands that pins itself to the
     bathroom wall, so it stops hugging your legs mid-shower.
  B. Toaster that fires each slice out on a tiny parachute, so it drifts
     down butter-side up instead of landing face-down on the floor.
     -- CHOSEN: the laugh is the invention itself (a parachute for
     toast), the fix is silly yet weirdly plausible (a parachute stops
     the flip), and butter-side-down is a universal tiny annoyance.
     Concrete embodied scene: toast floating down onto the kitchen floor.
  C. TV remote with little legs that climbs back onto the coffee table
     whenever it slips down the side of the sofa.

v1: "A toaster that fires each slice out on a tiny parachute, so your
toast drifts down butter-side up instead of landing face-down on the
kitchen floor."
v2 (genuine second-round revision): "fires" -> "fires every slice",
"drifts" -> "floats", "landing face-down" -> "face-planting" --
tighter verbs, the punch lands on the last two words.
"""

import os

ENTRY = (
    "A toaster that fires every slice out on a tiny parachute, so your "
    "toast floats down butter-side up instead of face-planting on the "
    "kitchen floor."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
