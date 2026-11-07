# V03 verification report: energy and protein balance (Henry and Godden 1995), independent rebuild (Opus checker, blind), 2026-11-07

**Reproduction of the authors' figures.** From their Tables 2 to 4 the checker gets 108.9 (109) and 95.66 (96) million, their 618.8 scaled energy exactly, and their percentage rows. Holds.

**Current data, against the project's test (`henry_godden.py`).** Checker / project, million people, energy and protein: no scale-up 140.1 and 132.9 / 138 and 134; 45.7 Mha land base 214.6 and 203.5 / 211 and 205; 59.95 Mha base 163.6 and 155.2 / 161 and 156. Totals: energy 796 against 782 x 10^15 J (1.8%); protein 651 against 656 x 10^10 g (0.8%); cereals 63.8% against 65% of energy. **Holds within 2% on every figure**, with the differences in the item list (the checker includes alcoholic beverages and cottonseed, and clamps negative items at zero; each choice moves totals 1% to 3%).

**Both implementations flag the same weakness.** FAO's world food densities for canola and cottonseed rest on tiny direct food use (0.5 Mt and 6 kt), so canola is valued at about half a raw seed's energy and cottonseed implausibly high; a raw-seed basis would add about 60 x 10^15 J. The consumption factors inferred from Gifford imply 3,720 kcal and 134 g of protein a day, above today's Australian supply (3,525 kcal, 121 g), so the people figures are conservative; and Gifford's Table 4 output embeds his yield assumptions as well as diet (466 is not 214 x 70/40.5 = 370).

**A wording slip in the brief.** The brief said "divided by their consumption factors"; the factors are people per unit of output and are multiplied (equivalently, divided by per-person consumption). The project script multiplies; no change needed.

**Status.** The Henry and Godden claims (fidelity check; the 134 to 211 million range; totals and cereal share) are independently verified.
