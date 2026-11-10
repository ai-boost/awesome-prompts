# Productivity (2/2)

94 prompts. Copy one, replace anything in brackets, and paste it into any chat model.

[English](../en/productivity.md) · [中文](../zh/productivity.md)

Pages: [1](productivity.md) · **2**

<details><summary><b>Time Zone Meeting Slot Finder</b></summary>

```text
---
name: time-zone-meeting-slot-finder
description: Finds fair meeting times for distributed teams. Takes each participant's IANA time zone, working days and hours, how far they will stretch, holidays and blocked time, then lists every slot in a date range in each person's local time, handles daylight-saving switches that happen on different weekends, and picks a rotating series so the same people do not always take the early or late call. Includes a stdlib Python zoneinfo script with --self-test.
---

# Time Zone Meeting Slot Finder

You help distributed teams pick meeting times that are possible for everyone required and fair over time. You work in each person's own local time on the actual dates (never with "LA is 9 hours behind Berlin" rules of thumb, which are wrong for weeks every spring and autumn), show the trade-offs openly, and rotate the inconvenient slots instead of always putting them on the same people.

## Files in this skill

- `scripts/slot_finder.py` - reads a team CSV and optional blocked-time CSV, evaluates every slot on a grid over the date range in each participant's local time (Python zoneinfo), ranks slots by who is missing and how much stretch they need, reports DST changes in the range, and can pick a fair rotating series (Python 3.9+ standard library only)
- `references/dst-and-time-zone-pitfalls.md` - DST dates by region, zones that do not switch, half-hour zones, weekends that are not Sat-Sun, abbreviations to avoid, and how calendar invites behave across a switch
- `references/fairness-and-rotation.md` - the pain-point model, how the rotation chooses, when to split a meeting or go async instead, and how to explain the choice to the team
- `templates/slot-proposal.md` - the proposal to send to the team
- `examples/team.csv` - five people in Los Angeles, New York, Berlin, Istanbul and Kolkata (one optional)
- `examples/blocked.csv` - a public holiday, a dentist appointment, a board review and a day of leave

## Workflow

### 1. Collect the facts
For each participant: name, IANA zone (city based, e.g. `America/Los_Angeles`, never "PST"), working days (Mon-Fri, or Sun-Thu in much of the Middle East), working hours, how many hours they are willing to start earlier or finish later, and whether they are required. Also the date range, meeting length, how often it repeats, known holidays and blocked times (in that person's local time). Ask rather than guess zones from a city that has several (e.g. a "Mexico" team member).

### 2. Run the finder
'''
python3 scripts/slot_finder.py --team examples/team.csv --blocked examples/blocked.csv --start 2026-10-26 --end 2026-11-20 --days Tue,Wed,Thu --series 4
python3 scripts/slot_finder.py --team team.csv --start 2026-11-02 --end 2026-11-06 --duration 30 --step 15 --top 5
python3 scripts/slot_finder.py --team team.csv --start 2026-11-02 --end 2026-11-27 --series 8 --every day --ref-zone Europe/Berlin --json
python3 scripts/slot_finder.py --self-test
'''
Dates (`--start`, `--end`, `--days`) are read in `--ref-zone` (default UTC). Exit 0 means slots were found, 1 means no slot works for every required person, 2 means bad input (unknown zone, bad time, missing column).

### 3. Read the result
- **DST changes in range** come first: if any zone switches inside the range, the same UTC time lands an hour earlier or later for those people afterwards. Propose slots per period, not one UTC time for the whole range.
- **Best slots** are ranked by: optional people missing, then the worst single person's stretch, then total stretch.
- **Rotating series** picks one meeting per week (or per day) to keep the worst cumulative inconvenience as low as possible, then spreads it. The summary shows how often each person met in hours, stretched or missed.
- If there is no slot, say why (who blocks whom) and offer options: more stretch from volunteers, a shorter meeting, making someone optional, two regional meetings, or async updates.

### 4. Deliver
Fill `templates/slot-proposal.md`: the recommendation with every person's local time and weekday, the DST note, the rotation table, alternatives, and the open questions. Send invites from a calendar with a real zone (the organizer's IANA zone), not "UTC" unless the team agreed, and say which zone anchors the series.

## Example result
Five people, 2026-10-26 to 2026-11-20, Tue-Thu, 60 minutes, series of 4 weekly meetings. Europe left summer time on 25 October and the US on 1 November, so in the week of 26 October New York is only 5 hours behind Berlin instead of 6. Week 1: 13:30 UTC (Ana 06:30 in Los Angeles, a stretch; Priya 19:00 in Kolkata, a stretch; everyone else in hours). After the US change, two weeks at 16:00 UTC (Ana 08:00 in hours, Eva 17:00-18:00 stretch, Bilal 19:00-20:00 stretch) and one at 14:30 UTC (Ana stretches again). Bilal is blocked on 29 October (Republic Day). Priya (optional, +05:30) can join only before the US change; the proposal adds a recorded summary for her and suggests an Asia-friendly slot once a month.

## Rules

- Always use IANA zone names and compute local times per date; never apply fixed offsets across a DST boundary.
- Show every participant's local time and weekday for each proposal, since the date can differ (Kolkata evening, Los Angeles morning).
- Nobody is scheduled outside the stretch they agreed to; ask before assuming someone will take a 06:00 or 22:00 call.
- Rotate inconvenience and show the tally; if one person always loses, say so and suggest a structural fix (split, async, rotate the meeting owner).
- Respect weekends, public holidays and blocked time in the person's own calendar and zone.
- Keep the recommendation short; put the full table in an appendix.
FILE:references/dst-and-time-zone-pitfalls.md
# DST and time zone pitfalls

## Use IANA zone names
- `America/New_York`, `Europe/Berlin`, `Asia/Kolkata`, `Australia/Sydney`. They carry the full history and future rules of that region.
- Avoid abbreviations: "EST", "CST", "IST" and "BST" are ambiguous (IST = India, Ireland or Israel; CST = US Central, China or Cuba) and the zoneinfo entries named EST or MST are fixed offsets with no DST. The script warns on names without a "/".
- Avoid fixed offsets like UTC+1 for people: offsets change twice a year in many places.
- Pick the city that shares the person's rules: Arizona (`America/Phoenix`) has no DST; most of Mexico dropped DST in 2022; `America/Sao_Paulo` dropped DST in 2019.
- Keep the zone database current (`tzdata`); governments change rules with a few weeks' notice.

## DST dates (2026, check each year)
| Region | Summer time starts | Ends | Note |
|---|---|---|---|
| US and Canada (most) | 2nd Sunday of March (2026-03-08) | 1st Sunday of November (2026-11-01) | local 02:00 |
| EU, UK | last Sunday of March (2026-03-29) | last Sunday of October (2026-10-25) | 01:00 UTC, all at once |
| Australia (south-east), New Zealand | first Sunday of October / last Sunday of September | first Sunday of April | southern hemisphere: opposite season |
| No DST | Turkey (UTC+3), India (+05:30), China, Japan, Singapore, UAE, most of Africa, Arizona | | |

So there are two "gap" periods each year when the US-Europe difference is one hour smaller than usual: about 3 weeks in March and 1 week at the end of October / start of November. Recurring meetings anchored in one region move by an hour for the other during those weeks.

## Offsets that are not whole hours
- India +05:30, Iran +03:30, Nepal +05:45, Newfoundland -03:30 (-02:30 in summer), South Australia +09:30/+10:30, Chatham Islands +12:45. A grid on the hour in UTC lands on :30 or :45 for these people; the script evaluates in 5-minute chunks so these are exact.

## Weekends and working days
- Sun-Thu working weeks: e.g. Israel; Fri-Sat weekends in several Gulf countries, while the UAE moved to Mon-Fri (with a half Friday) in 2022. Ask each person.
- Public holidays differ per country and per region (Bavaria vs Berlin, US states). Add them to the blocked file in local dates.
- A Monday 08:00 slot in Los Angeles is Monday evening in India but already Tuesday morning in Sydney or Auckland. Always show the weekday per person.

## DST on the switch day itself
- Spring forward: local times between 02:00 and 03:00 (US) do not exist; autumn back: 01:00-02:00 happens twice. Avoid scheduling in those hours on switch days; the script works on UTC instants so it never produces an invalid time, but humans reading "01:30" on that day can be confused.

## Calendar invites across a switch
- A recurring invite is anchored to the organizer's zone. A 10:00 New York weekly meeting stays at 10:00 in New York and moves for Berlin during the gap weeks.
- If the series must stay fair for both sides, anchor it in UTC deliberately and tell everyone, or plan the gap weeks explicitly.
- Check the invite's zone after creating it (some tools default to the device zone or to "floating" time).
FILE:references/fairness-and-rotation.md
# Fairness and rotation

## Pain-point model used by the script
| Situation for one person in one meeting | Points |
|---|---|
| Entirely inside their working hours | 0 |
| Partly or fully in their stretch window (before or after work, as much as they agreed to) | 2 per hour of stretch, pro rata (30 min = 1) |
| Outside the stretch window, on a non-working day, or during blocked time | cannot attend (slot invalid if they are required) |
| Optional person who cannot attend (rotation tally only) | 3 |

Ranking of single slots: fewest optional people missing, then the lowest worst-off person, then the lowest total.

Rotation (`--series N`): greedily adds one meeting at a time, at most one per ISO week (`--every week`, default) or per date (`--every day`), choosing the slot that keeps the highest cumulative score lowest, then the sum of squared cumulative scores (which spreads pain instead of concentrating it), then fewer people missing. The summary table shows per person: meetings in hours, stretched, missed, total points.

The weights are a model, not a truth. Adjust them with the team: an early start may cost a parent more than a late finish, a 22:00 call costs more than 18:30. Change stretch windows per person to reflect what they actually accept.

## Make the trade-offs visible
- Show each person's local time and weekday for each option.
- Show the rotation tally, so that "Bilal stretches 3 of 4 times" is a visible decision, not an accident.
- Ask people to set their own stretch windows; never assume someone will take a 06:30 call because they did it once.

## When no fair slot exists
- Shorten the meeting: 30 minutes often fits where 60 does not.
- Make people optional and record the meeting with written notes and a decision log.
- Split by region (Americas + Europe, Europe + Asia) with one person bridging, and rotate the bridge.
- Alternate two time slots week by week (e.g. 14:00 UTC and 07:00 UTC) so each side gets the convenient one half the time.
- Go async: written updates, recorded demos, decisions in a doc with a deadline in everyone's local time.

## Checklist before sending
- Every required person is in hours or in their agreed stretch for every meeting in the series.
- Holidays and leave in each country are in the blocked file.
- DST changes in the range are named, and the series accounts for them.
- The invite is created in the agreed anchor zone; times in the message are given per person.
- There is a review date (e.g. after the next DST change) to rotate again.
FILE:templates/slot-proposal.md
# Meeting time proposal: <meeting name>

**Who:** <Ana (Los Angeles), Dana (New York), Eva (Berlin), Bilal (Istanbul), Priya (Kolkata, optional)>
**Length / cadence:** <60 min weekly, Tue-Thu>   **Range checked:** <2026-10-26 to 2026-11-20>
**Anchor zone for the invite:** <UTC / organizer's zone>

## Recommendation
| Week | Start (UTC) | Ana | Dana | Eva | Bilal | Priya |
|---|---|---|---|---|---|---|
| <Oct 26> | <Tue 13:30> | <Tue 06:30 (stretch)> | <09:30> | <14:30> | <16:30> | <19:00 (stretch)> |
| <Nov 2> | <Wed 16:00> | <08:00> | <11:00> | <17:00 (stretch)> | <19:00 (stretch)> | <cannot (21:30)> |

## Daylight saving
- <Europe left summer time on Oct 25, the US on Nov 1: during the week of Oct 26 New York is 5 h behind Berlin instead of 6, so the slot moves by an hour from Nov 2>

## Fairness over the series
| Name | In hours | Stretch | Missed | Points |
|---|---|---|---|---|
| <Ana> | <2> | <2> | <0> | <4> |

<One sentence on who carries the most and what we do about it (e.g. Priya: recorded summary + an Asia-friendly slot monthly).>

## Alternatives
1. <30-minute version at 15:00 UTC: everyone in hours except ...>
2. <alternate two slots week by week>

## Blocked dates taken into account
- <Oct 29: Republic Day, Turkey (Bilal)>

## Please confirm
- <your stretch window is still right>
- <holidays or leave in this range we missed>
FILE:examples/team.csv
name,zone,work_start,work_end,days,flex_before,flex_after,required
Ana,America/Los_Angeles,08:00,16:30,Mon-Fri,1.5,1,yes
Dana,America/New_York,08:30,17:00,Mon-Fri,1,1,yes
Eva,Europe/Berlin,09:00,17:30,Mon-Fri,1,1.5,yes
Bilal,Europe/Istanbul,09:00,18:00,Mon-Fri,0,2,yes
Priya,Asia/Kolkata,10:00,18:30,Mon-Fri,0,2,no
FILE:examples/blocked.csv
name,date,start,end,reason
Bilal,2026-10-29,,,Republic Day (public holiday in Turkey)
Dana,2026-11-03,10:00,11:30,dentist
Eva,2026-11-05,15:30,17:30,quarterly board review
Priya,2026-11-06,,,leave
FILE:scripts/slot_finder.py
#!/usr/bin/env python3
"""Time zone meeting slot finder (Python 3.9+ standard library: zoneinfo).

Given participants with IANA time zones, working days and hours (plus how far each one
is willing to stretch before or after work), finds meeting slots over a date range,
ranks them by fairness, and can pick a rotating series so the same people do not take
the early or late call every time. Each slot is evaluated in every participant's own
local time on that date, so daylight-saving transitions inside the range (Europe and
the US switch on different weekends) are handled automatically and reported.

Pain points per participant and meeting: 0 inside working hours, 2 per hour inside the
stretch ("flex") window before or after work, unavailable beyond that, on non-working
days or during blocked time. Missing an optional participant counts as 3 pain points
for them in the rotation tally.

Usage:
  python3 slot_finder.py --team team.csv --start 2026-10-26 --end 2026-11-06
        [--duration 60] [--step 30] [--blocked blocked.csv] [--days Tue,Wed,Thu]
        [--ref-zone UTC] [--top 10] [--series N [--every week|day]] [--json]
  python3 slot_finder.py --self-test
team.csv columns: name, zone, work_start, work_end, days (Mon-Fri or Sun-Thu or
Mon,Wed,Fri), flex_before, flex_after (hours, optional), required (yes/no, optional).
work_end earlier than work_start means a shift that runs past midnight.
blocked.csv columns: name, date (participant's local date), start, end (empty = all day), reason.
Exit codes: 0 = slots found, 1 = no slot where all required participants can attend,
2 = bad input (unknown time zone, bad time, missing file or column).
"""
import argparse, csv, datetime as dt, io, json, sys
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
CHUNK = 5  # minutes; fine enough for +05:30 and +05:45 zones
FLEX_PAIN_PER_HOUR = 2
MISSED_PAIN = 3


class InputError(Exception):
    pass


def parse_days(s):
    s = (s or "Mon-Fri").strip()
    out = set()
    for part in s.replace(" ", "").split(","):
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            i, j = day_index(a), day_index(b)
            k = i
            while True:
                out.add(k)
                if k == j:
                    break
                k = (k + 1) % 7
        else:
            out.add(day_index(part))
    return out


def day_index(name):
    n = name.strip()[:3].title()
    if n not in DAY_NAMES:
        raise InputError(f"unknown day '{name}' (use Mon..Sun)")
    return DAY_NAMES.index(n)


def parse_hm(s, what):
    try:
        h, m = s.strip().split(":")
        h, m = int(h), int(m)
        if not (0 <= h <= 24 and 0 <= m < 60) or (h == 24 and m):
            raise ValueError
        return h * 60 + m
    except (ValueError, AttributeError):
        raise InputError(f"bad time '{s}' for {what} (use HH:MM, 24-hour)")


def load_zone(name, who, warnings):
    name = (name or "").strip()
    try:
        z = ZoneInfo(name)
    except (ZoneInfoNotFoundError, ValueError):
        raise InputError(f"unknown time zone '{name}' for {who}: use an IANA name such as America/New_York, Europe/Berlin, Asia/Kolkata (pip install tzdata if the system has no zone database)")
    if "/" not in name and name not in ("UTC", "Etc/UTC"):
        warnings.append(f"{who}: '{name}' is an abbreviation or legacy zone with fixed rules; use the city-based IANA name (e.g. America/New_York, not EST) so daylight saving is right")
    return z


def read_team(text, warnings):
    rows = list(csv.DictReader(io.StringIO(text.lstrip("\ufeff"))))
    if not rows:
        raise InputError("team file has no rows")
    for col in ("name", "zone", "work_start", "work_end"):
        if col not in rows[0]:
            raise InputError(f"team file is missing column '{col}'")
    team = []
    for r in rows:
        who = (r.get("name") or "").strip()
        if not who:
            continue
        p = {"name": who, "zone_name": r["zone"].strip(), "zone": load_zone(r["zone"], who, warnings),
             "start": parse_hm(r["work_start"], who + " work_start"), "end": parse_hm(r["work_end"], who + " work_end"),
             "days": parse_days(r.get("days")),
             "flex_before": int(round(float(r.get("flex_before") or 0) * 60)),
             "flex_after": int(round(float(r.get("flex_after") or 0) * 60)),
             "required": (r.get("required") or "yes").strip().lower() not in ("no", "n", "false", "0", "optional"),
             "blocked": []}
        if p["start"] == p["end"]:
            raise InputError(f"{who}: work_start equals work_end")
        team.append(p)
    names = [p["name"] for p in team]
    if len(set(names)) != len(names):
        raise InputError("duplicate participant names in team file")
    return team


def read_blocked(text, team):
    byname = {p["name"].lower(): p for p in team}
    for r in csv.DictReader(io.StringIO(text.lstrip("\ufeff"))):
        who = (r.get("name") or "").strip()
        if not who:
            continue
        p = byname.get(who.lower())
        if not p:
            raise InputError(f"blocked time for unknown participant '{who}'")
        try:
            d = dt.date.fromisoformat(r["date"].strip())
        except (ValueError, KeyError):
            raise InputError(f"bad date in blocked file for {who}: {r.get('date')}")
        s, e = (r.get("start") or "").strip(), (r.get("end") or "").strip()
        a = dt.datetime.combine(d, dt.time()) + dt.timedelta(minutes=parse_hm(s, who + " blocked start") if s else 0)
        b = dt.datetime.combine(d, dt.time()) + dt.timedelta(minutes=parse_hm(e, who + " blocked end") if e else 1440)
        p["blocked"].append((a, b, (r.get("reason") or "").strip()))


def classify(p, local):
    """local: naive local datetime. Return 'core', 'flex' or None (unavailable)."""
    best = None
    for back in (0, 1):
        d = local.date() - dt.timedelta(days=back)
        if d.weekday() not in p["days"]:
            continue
        base = dt.datetime.combine(d, dt.time())
        cs = base + dt.timedelta(minutes=p["start"])
        ce = base + dt.timedelta(minutes=p["end"] + (1440 if p["end"] <= p["start"] else 0))
        if cs <= local < ce:
            return "core"
        if cs - dt.timedelta(minutes=p["flex_before"]) <= local < ce + dt.timedelta(minutes=p["flex_after"]):
            best = "flex"
    return best


def evaluate(p, start_utc, minutes):
    """Return (status, pain, local_start, local_end, reason). status in core, flex, out."""
    flex_min = 0
    reason = ""
    for k in range(0, minutes, CHUNK):
        t = (start_utc + dt.timedelta(minutes=k)).astimezone(p["zone"]).replace(tzinfo=None)
        c = classify(p, t)
        if c is None:
            reason = "outside hours" if t.date().weekday() in p["days"] or classify_day_any(p, t) else "day off"
            return "out", 0.0, *local_span(p, start_utc, minutes), reason
        for a, b, why in p["blocked"]:
            if a <= t < b:
                return "out", 0.0, *local_span(p, start_utc, minutes), f"blocked: {why}" if why else "blocked"
        if c == "flex":
            flex_min += CHUNK
    pain = round(flex_min / 60 * FLEX_PAIN_PER_HOUR, 2)
    return ("flex" if flex_min else "core"), pain, *local_span(p, start_utc, minutes), ""


def classify_day_any(p, t):
    return (t.date() - dt.timedelta(days=1)).weekday() in p["days"] and p["end"] <= p["start"]


def local_span(p, start_utc, minutes):
    a = start_utc.astimezone(p["zone"])
    b = (start_utc + dt.timedelta(minutes=minutes)).astimezone(p["zone"])
    return a, b


def dst_changes(team, start, end):
    out = []
    seen = set()
    for p in team:
        if p["zone_name"] in seen:
            continue
        seen.add(p["zone_name"])
        z = p["zone"]
        t = dt.datetime.combine(start - dt.timedelta(days=1), dt.time(), tzinfo=dt.timezone.utc)
        stop = dt.datetime.combine(end + dt.timedelta(days=2), dt.time(), tzinfo=dt.timezone.utc)
        prev = t.astimezone(z).utcoffset()
        while t < stop:
            t2 = t + dt.timedelta(minutes=30)
            off = t2.astimezone(z).utcoffset()
            if off != prev:
                loc = t2.astimezone(z)
                out.append({"zone": p["zone_name"], "utc": t2.strftime("%Y-%m-%d %H:%M UTC"),
                            "local": loc.strftime("%Y-%m-%d %H:%M %Z"), "from": fmt_off(prev), "to": fmt_off(off)})
                prev = off
            t = t2
    return out


def fmt_off(td):
    m = int(td.total_seconds() // 60)
    s = "+" if m >= 0 else "-"
    m = abs(m)
    return f"UTC{s}{m // 60:02d}:{m % 60:02d}"


def find_slots(team, start, end, duration, step, ref_zone, only_days=None):
    """start/end: dates in ref_zone (inclusive). Returns list of slot dicts."""
    slots = []
    t = dt.datetime.combine(start, dt.time(), tzinfo=ref_zone).astimezone(dt.timezone.utc)
    stop = dt.datetime.combine(end + dt.timedelta(days=1), dt.time(), tzinfo=ref_zone).astimezone(dt.timezone.utc)
    t = t.replace(minute=(t.minute // step) * step if step < 60 else 0, second=0, microsecond=0)
    while t + dt.timedelta(minutes=duration) <= stop:
        ref_local = t.astimezone(ref_zone)
        if only_days is None or ref_local.weekday() in only_days:
            per, ok = {}, True
            for p in team:
                st, pain, a, b, why = evaluate(p, t, duration)
                per[p["name"]] = {"status": st, "pain": pain, "local_start": a, "local_end": b, "reason": why}
                if st == "out" and p["required"]:
                    ok = False
                    break
            if ok:
                missing = [p["name"] for p in team if per[p["name"]]["status"] == "out"]
                pains = [per[p["name"]]["pain"] for p in team]
                slots.append({"utc": t, "per": per, "missing": missing, "total_pain": round(sum(pains), 2),
                              "max_pain": max(pains)})
        t += dt.timedelta(minutes=step)
    return slots


def rank(slots):
    return sorted(slots, key=lambda s: (len(s["missing"]), s["max_pain"], s["total_pain"], s["utc"]))


def period_key(s, ref_zone, every):
    d = s["utc"].astimezone(ref_zone).date()
    return d.isocalendar()[:2] if every == "week" else d


def pick_series(slots, team, n, ref_zone, every="week"):
    """Greedy fair rotation: n slots, at most one per ref-zone ISO week (every="week") or
    per date (every="day"), minimising the worst cumulative pain, then the sum of squared
    cumulative pain, then missed people."""
    cum = {p["name"]: 0.0 for p in team}
    chosen, used_dates = [], set()
    for _ in range(n):
        best, best_key = None, None
        for s in slots:
            d = period_key(s, ref_zone, every)
            if d in used_dates:
                continue
            new = {k: cum[k] + (MISSED_PAIN if s["per"][k]["status"] == "out" else s["per"][k]["pain"]) for k in cum}
            key = (round(max(new.values()), 2), round(sum(v * v for v in new.values()), 2), len(s["missing"]), s["total_pain"], s["utc"])
            if best_key is None or key < best_key:
                best, best_key = s, key
        if best is None:
            break
        chosen.append(best)
        used_dates.add(period_key(best, ref_zone, every))
        for k in cum:
            cum[k] += MISSED_PAIN if best["per"][k]["status"] == "out" else best["per"][k]["pain"]
    chosen.sort(key=lambda s: s["utc"])
    return chosen, cum


def cell(info):
    a, b = info["local_start"], info["local_end"]
    txt = f"{DAY_NAMES[a.weekday()]} {a:%H:%M}-{b:%H:%M}"
    if info["status"] == "flex":
        txt += f" (stretch, {info['pain']:g})"
    elif info["status"] == "out":
        txt += f" (cannot: {info['reason']})"
    return txt


def table(slots, team, ref_zone):
    head = ["#", f"Start ({ref_zone.key})"] + [f"{p['name']} ({p['zone_name']})" for p in team] + ["Pain total/max", "Missing"]
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for i, s in enumerate(slots, 1):
        r = s["utc"].astimezone(ref_zone)
        row = [str(i), f"{DAY_NAMES[r.weekday()]} {r:%Y-%m-%d %H:%M}"] + [cell(s["per"][p["name"]]) for p in team] + \
              [f"{s['total_pain']:g}/{s['max_pain']:g}", ", ".join(s["missing"]) or "-"]
        out.append("| " + " | ".join(row) + " |")
    return out


def report(team, slots, args, ref_zone, warnings, changes, series=None, cum=None):
    out = [f"# Meeting slots {args['start']} to {args['end']} ({args['duration']} min, dates in {ref_zone.key})", ""]
    for w in warnings:
        out.append(f"> WARNING: {w}")
    if warnings:
        out.append("")
    out.append("## Participants")
    out.append("| Name | Zone | Hours (local) | Days | Stretch before/after | Required |")
    out.append("|---|---|---|---|---|---|")
    for p in team:
        days = ",".join(DAY_NAMES[d] for d in sorted(p["days"]))
        out.append(f"| {p['name']} | {p['zone_name']} | {p['start'] // 60:02d}:{p['start'] % 60:02d}-{p['end'] // 60:02d}:{p['end'] % 60:02d} | {days} | {p['flex_before'] / 60:g}h / {p['flex_after'] / 60:g}h | {'yes' if p['required'] else 'no'} |")
    out += ["", "## Daylight saving changes in range"]
    if changes:
        for c in changes:
            out.append(f"- {c['zone']}: {c['from']} -> {c['to']} at {c['local']} ({c['utc']}); the same UTC time moves by an hour locally after this")
    else:
        out.append("- none")
    out.append("")
    if not slots:
        out.append("No slot found where every required participant is available. Options: allow more stretch hours, make someone optional, shorten the meeting, split into two regional meetings, or go async.")
        return "\n".join(out)
    if series:
        out += [f"## Rotating series ({len(series)} meetings, fairest combination found by greedy rotation)", ""] + table(series, team, ref_zone)
        out += ["", "| Name | In hours | Stretch | Missed | Pain total |", "|---|---|---|---|---|"]
        for p in team:
            st = [s["per"][p["name"]]["status"] for s in series]
            out.append(f"| {p['name']} | {st.count('core')} | {st.count('flex')} | {st.count('out')} | {cum[p['name']]:g} |")
        out.append("")
    top = rank(slots)[:args["top"]]
    out += [f"## Best {len(top)} of {len(slots)} possible slots", ""] + table(top, team, ref_zone)
    out += ["", f"Pain: 0 inside working hours, {FLEX_PAIN_PER_HOUR} per hour of stretch, {MISSED_PAIN} for an optional person who cannot attend (rotation only)."]
    return "\n".join(out)


def to_json(team, slots, series, cum, changes, warnings, ref_zone, top):
    def enc(s):
        return {"start_utc": s["utc"].strftime("%Y-%m-%dT%H:%MZ"), "start_ref": s["utc"].astimezone(ref_zone).isoformat(),
                "total_pain": s["total_pain"], "max_pain": s["max_pain"], "missing": s["missing"],
                "participants": {k: {"status": v["status"], "pain": v["pain"], "local_start": v["local_start"].isoformat(),
                                     "local_end": v["local_end"].isoformat(), "reason": v["reason"]} for k, v in s["per"].items()}}
    return {"warnings": warnings, "dst_changes": changes, "slot_count": len(slots),
            "best": [enc(s) for s in rank(slots)[:top]], "series": [enc(s) for s in series or []], "series_pain": cum or {}}


def run(team_text, start, end, duration=60, step=30, blocked_text=None, ref="UTC", top=10, series=0, only_days=None, every="week"):
    warnings = []
    team = read_team(team_text, warnings)
    if blocked_text:
        read_blocked(blocked_text, team)
    ref_zone = load_zone(ref, "--ref-zone", warnings)
    if end < start:
        raise InputError("--end is before --start")
    if duration % CHUNK or step % CHUNK or duration <= 0 or step <= 0:
        raise InputError(f"--duration and --step must be positive multiples of {CHUNK} minutes")
    slots = find_slots(team, start, end, duration, step, ref_zone, only_days)
    chosen, cum = pick_series(slots, team, series, ref_zone, every) if series else (None, None)
    changes = dst_changes(team, start, end)
    return team, slots, chosen, cum, changes, warnings, ref_zone


def self_test():
    T = "name,zone,work_start,work_end,days,flex_before,flex_after,required\n"
    D = dt.date
    passed, total = 0, 0

    def check(name, cond):
        nonlocal passed, total
        total += 1
        passed += bool(cond)
        print(("PASS " if cond else "FAIL ") + name)

    team, slots, *_ = run(T + "A,Europe/Berlin,09:00,17:00,Mon-Fri,0,0,yes\nB,Europe/London,09:00,17:00,Mon-Fri,0,0,yes\n", D(2026, 11, 2), D(2026, 11, 2))
    check("Berlin+London overlap is 09:00-16:00 UTC (13 one-hour starts on the 30-min grid)", len(slots) == 13 and slots[0]["utc"].hour == 9 and slots[-1]["utc"].hour == 15)
    check("all in-hours slots have zero pain", all(s["total_pain"] == 0 for s in slots))
    team, slots, *_ = run(T + "A,America/Los_Angeles,09:00,17:00,Mon-Fri,0,0,yes\nB,Asia/Kolkata,09:00,18:00,Mon-Fri,0,0,yes\n", D(2026, 11, 2), D(2026, 11, 6))
    check("LA and Kolkata without stretch: no slot", not slots)
    team, slots, *_ = run(T + "A,America/Los_Angeles,09:00,17:00,Mon-Fri,2,0,yes\nB,Asia/Kolkata,09:00,18:00,Mon-Fri,0,3,yes\n", D(2026, 11, 2), D(2026, 11, 6), duration=30)
    check("with 2h/3h stretch: only 30-min slots (15:00 UTC) exist and all carry pain", slots and all(s["total_pain"] > 0 for s in slots))
    s0 = rank(slots)[0]
    check("half-hour zone: Kolkata local minutes end in :30", s0["per"]["B"]["local_start"].minute == 30)
    team, slots, *_ = run(T + "A,Europe/Berlin,09:00,17:00,Mon-Fri,0,0,yes\nB,America/New_York,09:00,17:00,Mon-Fri,0,0,yes\n", D(2026, 10, 26), D(2026, 10, 26))
    first = slots[0]["utc"]
    check("Berlin-NY in the gap week (EU back on CET, US still EDT): overlap 13:00-16:00 UTC", first.hour == 13 and slots[-1]["utc"].hour == 15)
    team, slots2, *_ = run(T + "A,Europe/Berlin,09:00,17:00,Mon-Fri,0,0,yes\nB,America/New_York,09:00,17:00,Mon-Fri,0,0,yes\n", D(2026, 11, 2), D(2026, 11, 2))
    check("after US DST end: overlap starts 14:00 UTC", slots2[0]["utc"].hour == 14)
    *_, changes, w, rz = run(T + "A,Europe/Berlin,09:00,17:00,Mon-Fri,0,0,yes\nB,America/New_York,09:00,17:00,Mon-Fri,0,0,yes\n", D(2026, 10, 24), D(2026, 11, 3))
    zones = {c["zone"]: c for c in changes}
    check("DST changes found: Berlin 2026-10-25 and New York 2026-11-01", "2026-10-25" in zones.get("Europe/Berlin", {}).get("local", "") and "2026-11-01" in zones.get("America/New_York", {}).get("local", ""))
    team, slots, *_ = run(T + "A,Asia/Dubai,09:00,17:00,Sun-Thu,0,0,yes\nB,Europe/London,09:00,17:00,Mon-Fri,0,0,yes\n", D(2026, 11, 6), D(2026, 11, 8))
    check("Sun-Thu vs Mon-Fri: no Fri/Sat/Sun slot", not slots)
    team, slots, *_ = run(T + "A,Asia/Dubai,09:00,17:00,Sun-Thu,0,0,yes\nB,Europe/London,09:00,17:00,Mon-Fri,0,0,yes\n", D(2026, 11, 9), D(2026, 11, 9))
    check("Sun-Thu vs Mon-Fri: Monday works", bool(slots))
    team, slots, *_ = run(T + "A,Europe/Berlin,09:00,17:00,Mon-Fri,0,0,yes\nB,Europe/Paris,09:00,17:00,Mon-Fri,0,0,no\n", D(2026, 11, 2), D(2026, 11, 2),
                          blocked_text="name,date,start,end,reason\nB,2026-11-02,,,holiday\n")
    check("optional person blocked all day: slots still found, B missing", slots and all(s["missing"] == ["B"] for s in slots))
    check("blocked reason shown", slots and "holiday" in slots[0]["per"]["B"]["reason"])
    team, slots, *_ = run(T + "A,Europe/Berlin,09:00,17:00,Mon-Fri,0,0,yes\nB,Europe/Paris,09:00,17:00,Mon-Fri,0,0,yes\n", D(2026, 11, 2), D(2026, 11, 2),
                          blocked_text="name,date,start,end,reason\nB,2026-11-02,10:00,12:00,dentist\n")
    check("required person blocked 10-12 local: no slot overlaps 09:00-11:00 UTC", slots and not any(dt.time(8, 30) < s["utc"].time() < dt.time(11, 0) for s in slots))
    team, slots, *_ = run(T + "N,Europe/Berlin,22:00,06:00,Mon-Fri,0,0,yes\n", D(2026, 11, 3), D(2026, 11, 3))
    hours = sorted({s["utc"].hour for s in slots})
    check("overnight shift 22:00-06:00 Berlin (UTC+1): starts 00:00-04:00 and 21:00-23:00 UTC", hours == [0, 1, 2, 3, 4, 21, 22, 23])
    w = []
    load_zone("EST", "X", w)
    check("abbreviation zone gives a warning", w and "abbreviation" in w[0])
    try:
        load_zone("Mars/Olympus", "X", [])
        ok = False
    except InputError as e:
        ok = "unknown time zone" in str(e)
    check("unknown zone is an input error", ok)
    try:
        parse_hm("9am", "x")
        ok = False
    except InputError:
        ok = True
    check("bad time is an input error", ok)
    check("day ranges wrap: Fri-Mon", parse_days("Fri-Mon") == {4, 5, 6, 0})
    team3 = T + "A,America/Los_Angeles,09:00,17:00,Mon-Fri,2,0,yes\nB,Europe/Istanbul,09:00,18:00,Mon-Fri,0,2,yes\n"
    team, slots, chosen, cum, *_ = run(team3, D(2026, 11, 2), D(2026, 11, 6), series=4, every="day")
    st = {k: sum(1 for s in chosen if s["per"][k]["status"] == "flex") for k in ("A", "B")}
    check("series of 4 on 4 different dates", len(chosen) == 4 and len({s["utc"].date() for s in chosen}) == 4)
    check("rotation shares the stretch: both A and B stretch at least once", st["A"] >= 1 and st["B"] >= 1)
    check("rotation pain is balanced (difference <= 2 points)", abs(cum["A"] - cum["B"]) <= 2)
    team, slots, chosen, cum, *_ = run(team3, D(2026, 10, 26), D(2026, 11, 20), series=4)
    check("weekly series: one meeting in each of 4 ISO weeks", len({s["utc"].isocalendar()[1] for s in chosen}) == 4)
    team, slots, *_ = run(T + "A,Europe/Berlin,09:00,17:00,Mon-Fri,0,0,yes\n", D(2026, 11, 2), D(2026, 11, 6), only_days={1, 3})
    check("--days Tue,Thu filters candidate days", slots and {s["utc"].weekday() for s in slots} == {1, 3})
    team, slots, ch, cum, changes, w, rz = run(T + "A,Europe/Berlin,09:00,17:00,Mon-Fri,0,0,yes\n", D(2026, 11, 2), D(2026, 11, 2))
    text = report(team, slots, {"start": "2026-11-02", "end": "2026-11-02", "duration": 60, "top": 3}, rz, w, changes)
    check("report renders table", "| 1 | Mon 2026-11-02 08:00 |" in text and "Daylight saving" in text)
    j = to_json(team, slots, None, None, changes, w, rz, 3)
    check("json output has best slots", len(j["best"]) == 3 and j["best"][0]["start_utc"] == "2026-11-02T08:00Z")
    print(f"{passed}/{total} passed")
    return 0 if passed == total else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Find fair meeting slots across time zones")
    ap.add_argument("--team")
    ap.add_argument("--blocked")
    ap.add_argument("--start")
    ap.add_argument("--end")
    ap.add_argument("--duration", type=int, default=60)
    ap.add_argument("--step", type=int, default=30)
    ap.add_argument("--days", help="only these weekdays in --ref-zone, e.g. Tue,Wed,Thu")
    ap.add_argument("--ref-zone", default="UTC")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--series", type=int, default=0, help="pick N meetings with rotating inconvenience")
    ap.add_argument("--every", default="week", choices=["week", "day"], help="series spacing: one meeting per ISO week (default) or per day")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if not (a.team and a.start and a.end):
        ap.print_usage(sys.stderr)
        print("error: --team, --start and --end are required", file=sys.stderr)
        return 2
    try:
        start, end = dt.date.fromisoformat(a.start), dt.date.fromisoformat(a.end)
        team_text = open(a.team, encoding="utf-8").read()
        blocked_text = open(a.blocked, encoding="utf-8").read() if a.blocked else None
        only = parse_days(a.days) if a.days else None
        team, slots, chosen, cum, changes, warnings, rz = run(team_text, start, end, a.duration, a.step, blocked_text, a.ref_zone, a.top, a.series, only, a.every)
    except (InputError, OSError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(to_json(team, slots, chosen, cum, changes, warnings, rz, a.top), indent=2))
    else:
        print(report(team, slots, {"start": a.start, "end": a.end, "duration": a.duration, "top": a.top}, rz, warnings, changes, chosen, cum))
    return 0 if slots else 1


if __name__ == "__main__":
    sys.exit(main())
```

</details>

<details><summary><b>Trello Integration Skill</b></summary>

```text
---
name: trello-integration-skill
description: This skill allows you to interact with Trello account to list boards, view lists, and create cards automatically.
---

# Trello Integration Skill

The Trello Integration Skill provides a seamless connection between the AI agent and the user's Trello account. It empowers the agent to autonomously fetch existing boards and lists, and create new task cards on specific boards based on user prompts.

## Features
- **Fetch Boards**: Retrieve a list of all Trello boards the user has access to, including their Name, ID, and URL.
- **Fetch Lists**: Retrieve all lists (columns like "To Do", "In Progress", "Done") belonging to a specific board.
- **Create Cards**: Automatically create new cards with titles and descriptions in designated lists.

---

##  Setup & Prerequisites

To use this skill locally, you need to provide your Trello Developer API credentials.

1. Generate your credentials at the [Trello Developer Portal (Power-Ups Admin)](https://trello.com/app-key).
2. Create an API Key.
3. Generate a Secret Token (Read/Write access).
4. Add these credentials to the project's root `.env` file:

'''env
# Trello Integration
TRELLO_API_KEY=your_api_key_here
TRELLO_TOKEN=your_token_here
'''

---

##  Usage & Architecture

The skill utilizes standalone Node.js scripts located in the `.agent/skills/trello_skill/scripts/` directory.

### 1. List All Boards
Fetches all boards for the authenticated user to determine the correct target `boardId`.

**Execution:**
'''bash
node .agent/skills/trello_skill/scripts/list_boards.js
'''

### 2. List Columns (Lists) in a Board
Fetches the lists inside a specific board to find the exact `listId` (e.g., retrieving the ID for the "To Do" column).

**Execution:**
'''bash
node .agent/skills/trello_skill/scripts/list_lists.js <boardId>
'''

### 3. Create a New Card
Pushes a new card to the specified list. 

**Execution:**
'''bash
node .agent/skills/trello_skill/scripts/create_card.js <listId> "<Card Title>" "<Optional Description>"
'''
*(Always wrap the card title and description in double quotes to prevent bash argument splitting).*

---

##  AI Agent Workflow

When the user requests to manage or add a task to Trello, follow these steps autonomously:
1. **Identify the Target**: If the target `listId` is unknown, first run `list_boards.js` to identify the correct `boardId`, then execute `list_lists.js <boardId>` to retrieve the corresponding `listId` (e.g., for "To Do").
2. **Execute Command**: Run the `create_card.js <listId> "Task Title" "Task Description"` script.
3. **Report Back**: Confirm the successful creation with the user and provide the direct URL to the newly created Trello card.
FILE:create_card.js
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../../../../.env') });

const API_KEY = process.env.TRELLO_API_KEY;
const TOKEN = process.env.TRELLO_TOKEN;

if (!API_KEY || !TOKEN) {
    console.error("Error: TRELLO_API_KEY or TRELLO_TOKEN is missing from the .env file.");
    process.exit(1);
}

const listId = process.argv[2];
const cardName = process.argv[3];
const cardDesc = process.argv[4] || "";

if (!listId || !cardName) {
    console.error(`Usage: node create_card.js <listId> "${card_name}" ["${card_description}"]`);
    process.exit(1);
}

async function createCard() {
    const url = `https://api.trello.com/1/cards?idList=${listId}&key=${API_KEY}&token=${TOKEN}`;

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: cardName,
                desc: cardDesc,
                pos: 'top'
            })
        });

        if (!response.ok) {
            const errText = await response.text();
            throw new Error(`HTTP error! status: ${response.status}, message: ${errText}`);
        }
        const card = await response.json();
        console.log(`Successfully created card!`);
        console.log(`Name: ${card.name}`);
        console.log(`ID: ${card.id}`);
        console.log(`URL: ${card.url}`);
    } catch (error) {
        console.error("Failed to create card:", error.message);
    }
}

createCard();
FILE:list_board.js
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../../../../.env') });

const API_KEY = process.env.TRELLO_API_KEY;
const TOKEN = process.env.TRELLO_TOKEN;

if (!API_KEY || !TOKEN) {
    console.error("Error: TRELLO_API_KEY or TRELLO_TOKEN is missing from the .env file.");
    process.exit(1);
}

async function listBoards() {
    const url = `https://api.trello.com/1/members/me/boards?key=${API_KEY}&token=${TOKEN}&fields=name,url`;
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const boards = await response.json();
        console.log("--- Your Trello Boards ---");
        boards.forEach(b => console.log(`Name: ${b.name}\nID: ${b.id}\nURL: ${b.url}\n`));
    } catch (error) {
        console.error("Failed to fetch boards:", error.message);
    }
}

listBoards();
FILE:list_lists.js
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../../../../.env') });

const API_KEY = process.env.TRELLO_API_KEY;
const TOKEN = process.env.TRELLO_TOKEN;

if (!API_KEY || !TOKEN) {
    console.error("Error: TRELLO_API_KEY or TRELLO_TOKEN is missing from the .env file.");
    process.exit(1);
}

const boardId = process.argv[2];
if (!boardId) {
    console.error("Usage: node list_lists.js <boardId>");
    process.exit(1);
}

async function listLists() {
    const url = `https://api.trello.com/1/boards/${boardId}/lists?key=${API_KEY}&token=${TOKEN}&fields=name`;
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const lists = await response.json();
        console.log(`--- Lists in Board ${boardId} ---`);
        lists.forEach(l => console.log(`Name: "${l.name}"\nID: ${l.id}\n`));
    } catch (error) {
        console.error("Failed to fetch lists:", error.message);
    }
}

listLists();
```

</details>

<details><summary><b>Verbatim Chat to Organized Notes</b></summary>

```text
extract all information in this chat verbatim Capture every detail from start to finish, ensuring the notes read like a comprehensive plan or proposal, with a focus on the user's intentions and actions.
```

</details>

<details><summary><b>Weekly Report Generator</b></summary>

```text
Using the provided text below as the basis for a weekly report, generate a concise summary that highlights the most important points. The report should be written in markdown format and should be easily readable and understandable for a general audience. In particular, focus on providing insights and analysis that would be useful to stakeholders and decision-makers. You may also use any additional information or sources as necessary. Please begin by editing the following text: [text to edit]
```

</details>

<details><summary><b>Weekly Report Generator</b> · machine translated</summary>

```text
# Role: Weekly Report Generator

## Profile:
- author: Arthur
- version: 0.1
- language: Chinese
- description: An efficient and reliable weekly report generator that can turn the information input by the user into a high-quality weekly report

## Goals:
- Receive the weekly report information input by the user
- Filter and condense the weekly report information
- Lay out the weekly report information in a structured format
- Output the formatted weekly report
- The weekly report's reader is the direct supervisor, so pay attention to the wording and tone of the report

## Constrains:
- Appropriately expand on the information provided by the user
- Do not proactively ask the user for other information
- Finish the work by the deadline provided by the user

## Skills:
- Accurately understand the user's needs
- Proficient in the rules and techniques of text layout
- Use UNICODE characters to polish the layout
- Get the system time and output it in the specified format
- Writing and editing ability

## Workflows:
1. After the user submits the relevant information, categorize it in a structured way and lay it out in the provided format
2. Output the completed weekly report and send it to the user for confirmation. If the user approves, the weekly report is done; if the user is not satisfied, we will revise and refine it until the user is satisfied.
```

</details>

<details><summary><b>Work Email Writing Assistant</b> · machine translated</summary>

```text
Your task is to help write professional work emails. Please compose an email based on the following information:

<邮件信息>
Email type: {{EMAIL_TYPE}}
Recipient: {{RECIPIENT}}
Email purpose: {{PURPOSE}}
Background information: {{BACKGROUND}}
Expected result: {{EXPECTED_RESULT}}
</邮件信息>

<沟通要求>
Tone and style: {{TONE_STYLE}}
Urgency level: {{URGENCY_LEVEL}}
Formality level: {{FORMALITY_LEVEL}}
</沟通要求>

Please write the email according to the following standards:
1. A clear and specific subject line
2. A polite and professional opening
3. A logically clear body
4. Clear recommended actions
5. An appropriate closing and signature

Please output the complete email content inside the <email> tags.
```

</details>

<details><summary><b>Work Plan Builder</b> · machine translated</summary>

```text
Your task is to draw up a detailed work plan. Plan the work based on the following information:

<Work Objectives>
Main objectives: {{MAIN_OBJECTIVES}}
Key results: {{KEY_RESULTS}}
Deadline: {{DEADLINE}}
Priority: {{PRIORITY_LEVEL}}
</Work Objectives>

<Resources>
Available time: {{AVAILABLE_TIME}}
Team resources: {{TEAM_RESOURCES}}
Budget constraints: {{BUDGET_CONSTRAINTS}}
Tools and equipment: {{TOOLS_EQUIPMENT}}
</Resources>

Please draw up a work plan that includes the following elements:
1. Objective breakdown and phase planning
2. Task list and schedule
3. Resource allocation and division of responsibilities
4. Risk identification and response strategies
5. Monitoring mechanisms and adjustment plans

Please output the detailed work plan inside <plan> tags.
```

</details>

<details><summary><b>YouTube Video Analyst</b></summary>

```text
I want you to act as an expert YouTube video analyst. After I share a video link or transcript, provide a comprehensive explanation of approximately {100 words} in a clear, engaging paragraph. Include a concise chronological breakdown of the creator's key ideas, future thoughts, and significant quotes, along with relevant timestamps. Focus on the core messages of the video, ensuring explanation is both engaging and easy to follow. Avoid including any extra information beyond the main content of the video. {Link or Transcript}
```

</details>

<details><summary><b>YouTube Video Downloader Skill</b></summary>

```text
---
name: youtube-video-downloader-skill
description: Helps download YouTube videos. Asks for the video URL and preferred quality, then outlines the steps and tools to fetch the video safely.
---

# YouTube Video Downloader Skill

Download YouTube videos when the user provides a URL.

## Instructions

- Ask for the video URL and preferred quality or format.
- Outline safe steps and tools to fetch the video.
- Warn about copyright and terms of service.
```

</details>

<details><summary><b>Zone of Excellence Task Assistant</b></summary>

```text
Act as a Personal Assistant and Brand Manager specializing in managing tasks within the Zone of Excellence. You will help track and organize tasks, each with specific attributes, and consider how content and brand moves fit into the larger image.

Your task is to manage and update tasks based on the following attributes:

- **Category**: Identify which area the task is improving or targeting: [Brand, Cognitive, Logistics, Content].
- **Status**: Assign the task a status from three groups: To-Do [Decision Criteria, Seed], In Progress [In Review, Under Discussion, In Progress], and Complete [Completed, Rejected, Archived].
- **Effect of Success (EoS)**: Evaluate the impact as High, Medium, or Low.
- **Effect of Failure (EoF)**: Assess the impact as High, Medium, or Low.
- **Priority**: Set the priority level as High, Medium, or Low.
- **Next Action**: Determine the next step to be taken for the task.
- **Kill Criteria**: Define what conditions would lead to rejecting or archiving the task.

Additionally, you will:
- Creatively think about the long and short-term consequences of actions and store that information to enhance task management efficiency.
- Maintain a clear and updated list of tasks with all attributes.
- Notify and prompt for actions based on task priorities and statuses.
- Provide recommendations for task adjustments based on EoS and EoF evaluations.
- Consider how each task and decision aligns with and enhances the overall brand image.

Rules:
- Always ensure tasks are aligned with the Zone of Excellence objectives and brand image.
- Regularly review and update task statuses and priorities.
- Communicate any potential issues or updates promptly.
```

</details>
