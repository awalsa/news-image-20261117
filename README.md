# The World in One Image — Tuesday, 17 November 2026

Entry for make.fun bounty **news-image-20261117**: sum up 17 November 2026's
world news in one image.

## What it does

`main.py` copies the baked-in image `entry.png` to `/output/entry.png`.
The image is a newspaper-style infographic (1024×1024, rendered with PIL by
`build_image.py`) with the day's six biggest stories, an "also" strip and a
sources line. No network is needed at run time.

## The stories (all from 17 November 2026)

1. **War in the Gulf** — U.S.–Iran war escalates in the Strait of Hormuz:
   a fourth tanker is hit by a mine in 24 hours; U.S. forces strike an IRGC
   launch site on Qeshm Island; Iranian drones target the U.S. base in Bahrain.
2. **Ukraine** — a Kyiv strike closes the Crimean Bridge; Russia answers by
   hitting bridges in Kyiv; a strike on Zaporizhzhia kills 40 people.
3. **Gaza** — Britain, Australia, Canada and Italy urge Israel to open aid
   crossings; 1.7 million people remain displaced as winter closes in.
4. **France** — Gérard Depardieu pleads guilty to sexual assault and drops
   his appeal in a Paris court.
5. **Japan** — Tokyo scrambles fighter jets as Russian aircraft breach its
   airspace.
6. **Climate** — COP31 draft deal in Antalya: faster fossil-fuel phase-out
   and $120bn a year in climate finance for developing nations by 2035.

Also: the U.S. loses measles-elimination status after ~30 years; Xi, Trump
and Putin are set to meet Thursday in Shenzhen; Mongolia's president resigns.

Sources: Reuters, Al Jazeera, AFP, BBC — 17 November 2026.

## Run it

```sh
python3 main.py        # writes /output/entry.png
python3 build_image.py # re-renders entry.png from the headlines
```

## License

MIT — see LICENSE.
