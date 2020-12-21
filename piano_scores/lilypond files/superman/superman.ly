#(set-default-paper-size "a4")

\paper {
  two-sided = ##f
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  %binding-offset = 0.25\in
}

\header{
  title = "Superman"
  subtitle = "Symphany"
  composer = "Han Zimmers"
  arranger = "GSS"
}


melody = \relative c'' {\tempo 4 = 70 \key d \major 
a4 \tuplet 3/4 { a4 d,4 a'4 } a2
d4 a d,2
}

text = \lyricmode {
}


upper = \relative c'' { \time 4/4 \key f \major 
}


lower = \relative c { \clef bass \key f \major 
}

%showLastLength = R1*7
\score {
  <<
    \new Voice = "mel" { \melody}
    \new Lyrics \lyricsto mel \text
    \new PianoStaff \with { instrumentName = #"Piano" } <<
      \new Staff = "upper" \upper
      \new Staff = "lower" \lower
    >>
  >>
  \layout { }
  \midi { }
}
