#(set-default-paper-size "a4")

\paper {
  two-sided = ##t
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  binding-offset = 0.25\in
}

\header{
  title = "Oak"
  subtitle = "accompanyin"
  composer = "Jay"
  arranger = "Drillbits"
}


melody = \relative c'' {
\key c \major
r1 r r r r
r8 c8 c c c g c d
d  d  d8 e16 d16( d8) g,4.
r8 c8 c  c c d e f
f4. e8 e4. e8
d8 c16 c16 (c2) r8 e8
d c d e16 d16 (d8) c4.
c8 a16 c16 (c8) a16 c16 (c8) a16 c16 (c8) d8
d2. r4

r8 c8 c c c g c d
d  d  d8 e16 d16( d8) g,4.
r8 c8 c  c c d e f
f4 (f16) e16 d8 e4. e8
d8 c16 c16 (c2) r8 e8
d c d e16 d16 (d8) c4.
c8 a16 c16 (c8) a16 c16 (c8) a16 c16 (c8) a'8
g2. r4


}

text = \lyricmode {

}

upper = \relative c'' {
  \time 4/4
\key c \major
r2 c'8 e,16 b'16 (b16) c8. b8 d,16 g16 (g4)
\acciaccatura g8
a8 c,16 g'16 (g16) f8. <c f>8 g16 e'16 (e8) d,16 e
c8 d16 e16( e16) c'8. b8 c c b16 c16 (c1)
r2

<g c d g>4 <g d' g>4 <g d' g>4 <g d' g>4
<g d'> <g d'> <g d'> <g d'> 
<c f> <c f> <c f> <c f> 
<g c f> <g c f> <g c> <g c> 
<f c'> <f c'> <f c'> <f c'> 
<e c'> <e c'> <c a' c>8 e8 <a c e>4
<a, c d f>1
<g' c d>4 <g c d>4 <g b> r

<g c d g>4 <g d' g>4 <g d' g>4 <g d' g>4
<g d'> <g d'> <g d'> <g d'> 
<c f> <c f> <c f> <c f> 
<g c f> <g c f> <g c> <g c> 
<f c'> <f c'> <c' f > <f, c'> 
<e c'> <e c'> <c a' c>8 e8 <a c e>4
<c, g'>4 r8 <c g'>8 (<c g'>2)
<g' c d>4 <g c d>4 <g b> <g b d>4

}

lower = \relative c {
  \clef bass
\key c \major
r2 a8 e'8 c'4 e,8 g d'4
f,,8 c'8 g'4 c,8 g' <g b d> g
a,4 c' <e, g>2
<f a>8 c8 g'16 a c8 <d, g a c>2
<g b>2

c1
b1
a1
g2 c4 <e, d'>4
<c f a>4 c' c <c, f a>4
<e g b>2 <a, b'>
<d, d'>1
<g d'>4 (<g d'>8) g'8 <g, d'>4 r

c,4 e'' g, c,
b, b'' g d8 e8
a,1
<g g'>2 c'8 g <e d'>4
<c f a>4 c'8 g c4 <c, f a>4
<e g b>2 <a, a'>
<f d' f>4 r8 <f d' f>8 <f d' f>2 
<g d'>4 (<g d'>8) g'8 <g, d'>4 <g d'>4
}

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

