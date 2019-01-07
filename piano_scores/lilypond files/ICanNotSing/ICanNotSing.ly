#(set-default-paper-size "a4")

\paper {
  two-sided = ##f
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  %binding-offset = 0.25\in
}

\header{
  title = "I Can't Sing"
  subtitle = "accompanyin piano"
  composer = "Show Lo"
  arranger = "Drillbits"
}


melody = \relative c' {
\key c \major
r1
r1
r1
r1
r1
r1
r1
e4 e e8 d e f
g4 g g8 f g g
a4 a a8 g g a
g8 e4. e2
e4 e e8 d e f
g4 g g8 f g g
a4 a a8 g a16 b8 b16~
b2 r4 a8 b16 c16~
c2 c8 b16 c16~c8 e8
d8 b a g r4 e8 g16 a16~
a4.~a16 g16 f'8 e d c
f e d e r4 c8 b16 c16~
c2 c8 b16 c8. e8
d8 b a' g~ g4. e8
e4 d c8 d4 d8~
d2 r8 g,8 f' f

f e d e4 e,8 e d'
d c b c4 c8 d e
g16 f8. c4 g'16 f8. c8 g8
f' e d e4 e,8 e f'
f e d e4 e8 e c'
c b b a8\fermata r8 c,, d e
g16 f8. c4 g'16 f8. c4
f16 e8. c2 d4
c1
r1
r1
r1


}

text = \lyricmode {

}

upper = \relative c'' {
  \time 4/4
\key c \major
\tempo 4 = 80
r2 r8 g'8 f' f
f e d e r8 e, e d'
d c b c r8 c d e
g16 f8  c16~c4 g16 f8 c16~ c8 g8
a1

<c, e g>4 <c e g>4 <c e g>8 d <c f g> d
<c e g>4 <c e g>4 <c e g>8 d <c f g> d
<c e g>4 <c e g>4 <c e g>8 d <c f g>4
<b e g>4 <b e g>4 <b e g>8 f' <b, f' g>4
<c f a>4 <c f a>4 <c f a>8 e <c f a>8 d
<c e g>4 <c e g>4 <c e g>8 d <b f' g> d
<a c e>4 <a c e>4 <a c e>8 d <a c e>8 f'
<b, e g>4 <b e g>4 <b e g>8 f' <b, e g>4
<c f a>4 <c f a>4 <c f a>8 g' <c, f a>4
<d g b>2 <d gis b>2
<e a c>4 <e a c>4 <e a c>8 b' <e, a c>8 a
<e g b>4 <e g b>4 <e g b>8 a <e g b>8 g
<f a c>4 <f a c>4 <a c f>4 <a c f>4
<g c e>4 <g c e>4 <g c e>4 <b d g>4
<a c e>4 <a c e>4 <a c e>8 d <a c e>8 c
<g b d>4 <g b d>4 <b d g>2
<a c e>4 <a c e>4 <fis a c>4 <fis a c>4
<g b d>8 <f, g d'>8 g'16 d' g c b2
<g, c e>4 <g c e>4 <g c e>4 <g b d>4
<a c e>4 <a c e>4 <a c e>4 <g b d>4
<f a c>4 <f a c>4 <f a d>4 <f a d>4
<g c e>4 <g c e>4 <g c e>4 <g b d>4
<a c e>4 <a c e>4 <a c e>4 <a c e>4
<fis a c>1
<d f a>4 <d f a>4 <e g b>4 <e g b>4
<f a c>4 <f a c>4 <g b d>2

r2 r8 c'8 d e
g16 f8 c8 r16 e,16 f16 g16 f8 c8 r16 e,16 f16 
g16 f8 c8 r16 r8 d,2
<d' g d'>4.  <d g d'>8~  <d g d'>2 

<c e g>4 <c e g>4 <c e g>8 d <c e g>8 f
<b, e g>4 <b e g>4 <b e g>8 f' <b, e g>4
<c f a>4 <c f a>4 <c f a>8 e <c f a>8 d 
<c e g>4 <c e g>4 <c e g>8 d <f g> d 
<c e f>4 <c e> <c e>8 d <c e> f 
<b, e g>4 <b e g> <e g>8 f <e g>4 
<c f a>4 <c f a> <c f a>8 g' <c, f a>16 b'8. 
<d, g b>2 <d gis b>2 
<e a c>4 <e a c>4 <e a c>8 b' <e, a c>8 a
<e g b>4 <e g b>4 <e g b>8 a <e g b>8 g
<f a c>4 <f a c>4 <a c f> <a c f>
<g c e> <g c e> <g c e> <b d g>
<a c e> <a c e> <a c e> <a c e>
<g b d> <g b d> <b d g >2
<a c e>4 <a c e>4 <fis a c>4 <fis a c>4
<g b d>8 c16 b g b c d g8 r4.

<g, c e>4 <g c e>4 <g c e>4 <g b d>4
<a c e>4 <a c e>4 <a c e>4 <g b d>4
<f a c>4 <f a c>4 <f a d>4 <f a d>4
<g c e>4 <g c e>4 <g c e>4 <g b d>4
<a c e>4 <a c e>4 <gis c e>4 <gis c e>4
<g c e>4 <g c e>4 <fis a c>2
<f a d>8 f <a d> f <g b e> g <g b e> g 
<f a c>8 f <f a c>8 f <g b d>2

r8 c' d e g16 f8. c8 e,16 f16
g16 f8. c8 r8 e,16 f16 g f8. c4
r4 e,2 


}

lower = \relative c {
  \clef bass
\key c \major
r1
<c' g'>4 <c  g'>4 <c  g'>4 <b  g'>4
<a e'>4 <a e'>4 <a e'>4 <g e'>4
<f c'>4 <f c'>4 <f c'>4 <f c'>4
<f, c'>1

c'4. g'8~g2
c,4. g'8~g2
c,4. g'8~g2
e4. g8~g2
f4. f8~f4 d4
c4. c8~c4 <b b'>4
a4. a8~a2
e'4. e8~e2
f4. f8~f4 d
g2 gis
a,4. a8~a2
e4. e8~e2
f4. f8 g4. g8
c,2. b'4
a4. a8~a2
e4. e8~e2
fis4. fis8 d4. d8
g,1

c'4. c8~c4 b4
a4. a8~a4 g4
f2 g2
c2 c4 b4
a4. a8~a2
fis1
d'8 f4~f8 e8 g4~g8
f8 a4~a8 g2
r1
<f' c'>2 <f, c'>2
<f, c'>2 g,2
r1

c'4. g'8~g2
e4. g8~g2
f4. f8~f4 d4
c2 c4 <b b'>4
a4. a8~a2
<e e'>4. <e e'>8~<e e'>2
<f f'>4.  <f f'>8~ <f f'>4 <d d'>4
<g g'>2 <gis gis'>2 
<a a'>4.  <a a'>8~<a a'>2
<e e'>4.  <e e'>8~<e e'>2
<f f'>2 <g g'>2
<c, c'>2. <b' b'>4
<a a'>4.  <a a'>8~<a a'>2
<e e'>4.  <e e'>8~<e e'>2
<fis fis'>4.  <fis fis'>8 <d d'>4.  <d d'>8
<g, g'>1


}

violin = \relative c{
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

