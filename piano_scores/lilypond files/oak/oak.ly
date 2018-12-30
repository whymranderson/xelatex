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
d  d  d8 e16 d16~d8 g,4.
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

r8 g,8 c b c d e c
d g4 g d8 c b
c c c b c d e f
(f) e4. r8 e8 e g
g a4 c,8 (c8) b b a'
a g g f16 f (f16) e8. r8 f16 g
g8 f f e16 e16 (e) d8. r8 d16 e
g8 f16 f16 (f16) e8. e8 d16 d (d) c8. 

r8 g8 c b c d e c
d g4 g d8 c b
c c c b c d e f
(f) e4. r8 e8 e g
g a4 c,8 (c8) b b a'
a g g f16 f (f16) e8. r8 f16 g
g8 f f e16 e16 (e) d8. r8 d16 e
g8 f16 f16 (f16) e8. d8 c d8. c16
(c1) r1 r r

r8 c8 c c c g c d
d  d  d8 e16 d16( d8) g,4.
r8 c8 c  c c d e f
f4 (f16) e16 d8 e4. e8
d8 c16 c16 (c2) r8 e8
d c d e16 d16 (d8) c4.
c8 a16 c16 (c8) a16 c16 (c8) a16 c16 (c8) e8
d1

\key des \major
aes8. des8 des aes des ees
f8. ees8 bes (bes4.) ees8
}

text = \lyricmode {

}

upper = \relative c'' {
  \time 4/4
\key c \major

r2 c'8 e,16 b'16 (b16) c8. 
b8 d,16 g16 (g4) \acciaccatura g8 a8 c,16 g'16 (g16) f8. 
<c f>8 g16 e'16 d,8 d16 e c8 d16 e16( e16) c'8. 
b8 c c b16 c16 (c1)
r2

<g c d g>4 <g c g'>4 <g c g'>4 <g c g'>4
<g d' g> <g d' g> <g d' g> <g d' g> 
<a c f> <a c f> <a c f> <a c f> 
<g c f> <g c f> <g c e> <g c> 
<f c'> <f c'> <f a c> <f a c> 
<e g b> <e b'> <a c>8 e8 <a c e>4
<a, c f>4. <a c f>8 (<a c f>2)
<g' c d>4 <g c d>4 <g b d> r

<g c d g>4 <g c g'>4 <g c g'>4 <g c g'>4
<g d' g> <g d' g> <g d' g> <g d' g> 
<a c f> <a c f> <a c f> <a c f> 
<g c f> <g c f> <g c e> <g c> 
<f c'> <f c'> <f a c> <f a c> 
<e g c> <e g c> <c a' c>8 e8 <a c e>4
<a, c f>4. <a c f>8 (<a c f>2)
<c d g>4 <c d g>4 <b d g> <b d g>4

<c e>8 g <c e>8 g <c e>8 g <c e>8 g
<d' g> g, <d' g> g, <d' g> g, <gis' b>4
<a c>8 e <a c>8 e <a c>8 e <a c>8 e
<g b>8 e <g b>8 e <g b>8 e <g b>8 e 
<a c>8 f <a c>8 f <b d> g <b d> g
<g b>8 e <g b>8 e <a c>8 e <a c>8 e
<a d>8 f <a d>8 f <a d>8 f <a d>8 f
<g b>8 f <g b d>8 f <g b d>8 f <g b d>8 f

<c e>8 g <c e>8 g <c e>8 g <c e>8 g
<d' g> g, <d' g> g, <d' g> g, <gis' b>4
<a c>8 e <a c>8 e <a c>8 e <a c>8 e
<g b>8 e <g b>8 e <g b>8 e <g b>8 e 
<f a> c <f a> c <g' b> d <g b> d   
<e g> b <e g> b <e a> c <e a> c
<f a> d <f a> d <f a> d <f a> d
<g b> d <g b> d <gis b> d <gis b> d


r16 e c' b e, c' b e, c' b e, d' c b e, c'
e, c' b e, c' b e, c' b4 c32 b e, c b e, c b
c''16 e c' b e, c' b e, d' c b c b g d e
c d g8 c16  d g8 (g2)

<c,,, e>8 g <c e>8 g <c e>8 g <c e>8 g
<d' g> g, <d' g> g, <d' g> g, <d' g> g,
<c f> a <c f> a <c f> a <c f> a 
<c g'> g <c g'> g <c e> g <c e> g 
<c f> a <c f> a <c f> a c16 d e g
<e g>8 b <e g>8 b <e a> c <e a> c
<f, c'>4. <f c'>8 (<f c' >2)
<c' d g>2 <b d g>8 <g' c>8 <g d>8 <g e>8

\key des \major
<aes des>8 f <aes des>8 f <aes des>8 f <aes des>8 f
<bes des> ges <bes des> ges <bes des> ges <bes des> ges
<aes c> ges <aes c> ges <aes c> ges <aes c> ges
<ges bes> ees <ges bes> ees <aes c> ees <aes c> ees
<aes des> f <aes des> f <aes des> f <aes des> f
<bes des> ges <bes des> ges <bes des> ges <bes des> ges
<aes c> <f ges> <aes c> ges <aes c> ges <aes c> ges
<ges bes> ees <ges bes> ees <aes c> ees <aes c> ees

<des f> aes <des f> aes <des f> aes <des f> aes
<ees' aes> aes, <ees aes> aes, <ees aes> aes, <a c>4 #fix
}

lower = \relative c {
  \clef bass
\key c \major
r2 a8 e'8 c'4 
e,8 g d'4 f,,8 c'8 g'4 
c,4 <b g'> a r4
<e' g b>2 <f a>8 <c d>8 g'16 a c8 
<g, d' g c>2 <g' b>2

c1
b1
a1
g2. e4
f1
e2 <a c>
<d,, d'>4.  <d d'>8~<d d'>2 
g'2 g2

c,4 e'' g, c,
b, b'' g d8 e8
a,1
<g g'>2 c'8 g <e d'>4
<c f a>4 c'8 g c4 <c, f a>4
<e g b>2 <a, a'>
<f d' f>4 r8 <f d' f>8 <f d' f>2 
<g d'>4 (<g d'>8) g'8 <g, d'>4 <g d'>4

c,2 c2
b   b
a   a
g   g
f   f
e   e
d   d
g   g

c'2 c2
b   b
a   a
g   g
f   f
e   e
d   d
f   gis4 gis

<a e'>1
<f c'>
<a' e'>
<f, c'>

c'1
b1
a1
g2 c4 <e, d'>4
<c f a>4 c' c <c, f a>4
<e g b>2 <a, b'>
<d, d'>1
<g g'>2 <g g'>2 

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

