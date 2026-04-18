---
title: "The SEG-Y seismic data format"
author: "Matt Hall"
date: "2026-04-18"
---
# The SEG-Y seismic data format

SEG‑Y (with a hyphen, as in the standard documentation), also known as SEGY and SEG Y, pronounced “segg why,” is a seismic data file format. The name stands for the Society of Exploration Geophysicists’ “Y” format. The format was intended for data exchange — and was related to the defunct SEG‑X (“exchange”) format — but it has become the de facto standard for processed reflection seismic records. Other standards, such as SEG‑D for field records and SEG‑P for positional data, deal with other data types.

## Background

SEG‑Y means seismic data. For many of us, it’s the only type of seismic file we have much to do with — we might handle others, but for the most part they are closed, proprietary formats that “just work” in the application they belong to (Landmark’s brick files, say, or OpendTect’s CBVS files). Processors care about other kinds of data — the SEG has defined formats for field data (SEG‑D) and positional data (SEG‑P), for example. But SEG‑Y is the seismic file for everyone. Kind of.

> The first rule of the SEG‑Y format is that no‑one follows the SEG‑Y format.

The open SEG‑Y “standard” (those air quotes are an important feature of the standard 😄) was defined by SEG in 1975. The first revision, Rev 1, was published in 2002. The second revision, Rev 2, was announced by the SEG Technical Standards Committee at the SEG Annual Meeting in 2013 and (at that time) was expected to see adoption in 2014.

## Revision 0

The original SEG‑Y data exchange format was introduced in 1975. See “Report on recommended standards for digital tape formats” (Barry, Cavers, and Kneale, 1975) — [SEG‑Y Rev 0 PDF (archived)](https://web.archive.org/web/20211017060649/http://seg.org/Portals/0/SEG/News%20and%20Resources/Technical%20Standards/seg_y_rev0.pdf).

## Revision 1

New high‑density media and the widespread adoption of 3D seismic data necessitated an update to the format. Rev 1 was adopted in 2002 and introduced the following improvements over the original specification ([SEG‑Y Rev 1 PDF (archived)](https://web.archive.org/web/20211017060649/http://www.seg.org/documents/10161/77915/seg_y_rev1.pdf)):

- Files may be written to any medium that is resolvable to a stream of variable‑length records.
- Data word formats now include 4‑byte IEEE float and 1‑byte integer words.
- A small number of additional fields in the 400‑byte binary file header and the 240‑byte trace header were defined.
- Some other fields in those headers were clarified.
- An extended text file header, consisting of additional 3200‑byte blocks, was introduced.
- The data in the extended header uses a stanza layout; standard stanzas were defined.
- Trace identification was expanded.
- Engineering conversions were introduced.
- The text file header can be ASCII encoded, not only EBCDIC.

See a schematic of the byte stream structure: [SEG‑Y file byte stream structure (archived)](https://web.archive.org/web/20211017060649/https://subsurfwiki.org/wiki/File:SEGY_file_byte_stream_structure.svg).

Selected Rev 1 trace header fields (start byte, length, description, note):

- 1, 4 bytes: Trace sequence number within line — strongly recommended
- 9, 4 bytes: Original field record number — strongly recommended
- 13, 4 bytes: Trace number in original field record — strongly recommended
- 29, 2 bytes: Trace identification code — strongly recommended
- 115, 2 bytes: Samples in trace — strongly recommended
- 117, 2 bytes: Sample interval (ms) — strongly recommended
- 181, 4 bytes: X coordinate of ensemble position of this trace — recommended
- 185, 4 bytes: Y coordinate of ensemble position of this trace — recommended
- 189, 4 bytes: 3D inline number — recommended for 3D
- 193, 4 bytes: 3D crossline number (often equals ensemble number in bytes 21–24) — recommended for 3D
- 197, 4 bytes: Shotpoint number (probably 2D only) — recommended for 2D

More details: [Full SEG‑Y header table (archived)](https://web.archive.org/web/20211017060649/https://subsurfwiki.org/wiki/SEG-Y/Full_header_table).

## Revision 2

Rev 2 was approved in March 2017 ([SEG‑Y Rev 2 specification PDF (archived)](https://web.archive.org/web/20211017060649/https://seg.org/Portals/0/SEG/News%20and%20Resources/Technical%20Standards/seg_y_rev2_0-mar2017.pdf)). Byte stream schematic: [SEG‑Y Rev 2 stream diagram (archived)](https://web.archive.org/web/20211017060649/https://subsurfwiki.org/wiki/File:SEGY_rev_2_stream.png).

Key features:

- Allow up to 65,535 additional 240‑byte trace headers; bytes 233–240 reserved for trace header name.
- Stanzas can appear after the trace data in a “data trailer.”
- Support up to 2^32 − 1 samples per trace (nearly 4.3 billion).
- Support up to 2^64 − 1 traces per line or ensemble (about 1.8 × 10^19).
- Permit arbitrarily large and small sample intervals.
- Support 3‑byte and IEEE 8‑byte (64‑bit) sample formats.
- Support little‑endian and pairwise byte swapping.
- Support microsecond date and time stamps.
- Provide additional precision in coordinates, depths, elevations.
- Synchronize coordinate reference system specification with SEG‑D Rev 3.
- Include depth, velocity, EM, gravity, and rotational sensor data.
- Backward compatible with Rev 1, as long as undefined fields were filled with binary zeros.

Here are three blog posts I wrote about Rev 2:

- [What is SEG-Y?](https://agilescientific.com/blog/2014/3/26/what-is-seg-y.html)
- [More precise SEG-Y?](https://agilescientific.com/blog/2017/3/29/more-precise-segy)
- [SEG-Y Rev 2 again: little endian is legal!](https://agilescientific.com/blog/2017/3/31/little-endian-is-legal)

## SEG‑Y file handling libraries

Most proprietary seismic interpretation software can read SEG‑Y data. The only open‑source interpretation application noted here is [OpendTect (archived)](https://web.archive.org/web/20211017060649/https://subsurfwiki.org/wiki/OpendTect).

Python libraries for reading SEG‑Y files include:

- [segyio (archived)](https://web.archive.org/web/20211017060649/https://github.com/equinor/segyio) — by Jørgen Kvalsvik and others at Equinor
- [SegPY (archived)](https://web.archive.org/web/20211017060649/https://github.com/sixty-north/segpy) — by Rob Smallshire and others
- [ObsPy (archived)](https://web.archive.org/web/20211017060649/http://github.com/obspy/obspy/wiki) — by Moritz Beyreuther and others

If you just want SEG‑Y data in another format (e.g., an image), a utility like [segy2ascii (archived)](https://web.archive.org/web/20211017060649/http://pubs.usgs.gov/of/2005/1311/) can work well.

See also: [List of seismic software libraries (archived)](https://web.archive.org/web/20211017060649/https://subsurfwiki.org/wiki/List_of_seismic_software_libraries).

## See also

- SEG‑D for field data
- SEG‑P for positional information
- SEG‑2, another format (often seen with GPR data)

## References

1) Barry, K.; Cavers, D.; Kneale, C. (1975). Report on recommended standards for digital tape formats. Geophysics 40(2), 344–352. [SEG‑Y Rev 0 PDF (archived)](https://web.archive.org/web/20211017060649/http://seg.org/Portals/0/SEG/News%20and%20Resources/Technical%20Standards/seg_y_rev0.pdf)

2) SEG Technical Standards Committee (2002). SEG‑Y Rev 1 specification. [SEG‑Y Rev 1 PDF (archived)](https://web.archive.org/web/20211017060649/http://www.seg.org/documents/10161/77915/seg_y_rev1.pdf)

3) Assertion by “Matt” (2013‑01‑03, UTC) regarding recommended fields.

4) SEG Technical Standards Committee (2017). SEG‑Y Rev 2.0 specification (approved March 2017). [SEG‑Y Rev 2 PDF (archived)](https://web.archive.org/web/20211017060649/https://seg.org/Portals/0/SEG/News%20and%20Resources/Technical%20Standards/seg_y_rev2_0-mar2017.pdf)

## External links

- [SEG‑Y — Wikipedia](https://en.wikipedia.org/wiki/SEG-Y)
- [SEG Technical Standards](https://library.seg.org/seg-technical-standards)