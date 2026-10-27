"""The group-trend rule for crops the ABS does not report (SCOPE.md B10).

A crop with no usable figure in a window keeps its own 2006-2010 regional pattern and its national level moves by the factor of its group:
the median, over the crops of that group that the window does report, of (national yield in the window / national yield in 2006-2010).
A group needs at least MIN_CROPS reported crops for its own factor (a median of one or two crops is one crop's luck). Below that, which includes a window
that reports none (vegetables after 2020-21: the ABS publishes no area), the latest earlier factor of the group is carried forward and recorded as carried;
with no earlier factor the group does not change (1.0).

  factors(ratios, groups, earlier) -> {group: {"factor", "crops", "carried"}}
     ratios   {crop: new/old national yield} for the crops the window reports
     groups   {crop: group}
     earlier  {group: factor} from the previous window, or None
  absent_yield(old, factor) -> the old regional yields (g/m2 or t/ha, None where there is none) times the factor
"""
import statistics

GROUPS = ('field crops', 'vegetables', 'fruit', 'nuts')
MIN_CROPS = 3


def factors(ratios, groups, earlier=None):
    out = {}
    for g in GROUPS:
        r = [v for c, v in ratios.items() if groups.get(c) == g and v and v > 0]
        if len(r) >= MIN_CROPS: out[g] = {'factor': statistics.median(r), 'crops': len(r), 'carried': False}
        elif earlier and g in earlier: out[g] = {'factor': earlier[g], 'crops': len(r), 'carried': True}
        else: out[g] = {'factor': 1.0, 'crops': len(r), 'carried': True}
    return out


def absent_yield(old, factor):
    return [None if v is None else v * factor for v in old]
