#(set-default-paper-size "a4")

\paper {
  two-sided = ##f
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  %binding-offset = 0.25\in
}

\header{
  title = "Merely Friends"
  subtitle = "accompanyin piano"
  composer = "Show Lo"
  arranger = "Drillbits"
}


melody = \relative c' {
r1
r1
r2. e4 \key a \major
cis'8 cis16 cis~cis8 cis8 cis8 d16 cis~cis8 b8
b cis16 cis~cis8 cis8 cis8 d16 cis~cis8 b8
}
 
text = \lyricmode {
}

upper = \relative c' {
  \time 4/4
\key c \major
\tempo 4 = 80
a''16 a, e' a a16 a, e' a g g, d' g g g, d' g
f f, c' f f f, c' f e8 e, b' e 
<gis' gis'>1
\key a \major
cis,,,8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
}

lower = \relative c {
  \clef bass
r1
r1
r1 \key a \major
a'2 e2
fis cis
d e
a
}


violin = \relative c{
}

\score {
  <<
    \new Voice = "mel" { \melody}
    \new Lyrics = "firstVerse" \lyricsto mel \text
    \new PianoStaff \with { instrumentName = #"Piano" } <<
      \new Staff = "upper" \upper
      \new Staff = "lower" \lower
    >>
  >>  
  \layout { }
  \midi { }
 }

