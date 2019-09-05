#(set-default-paper-size "a4")

\paper {
  two-sided = ##f
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  %binding-offset = 0.25\in
}

\header{
  title = "Black Joker"
  subtitle = "accompanyin piano"
  composer = "Jay Chou"
  arranger = "Drillbits"
}


melody = \relative c'' {\tempo 4 = 72 \key bes \major
r1
r1
r1
r1
d4 d8. d16 ees8 d c bes
d4 d8. d16 ees8 d c bes16 a16~
a8 bes4~bes16 bes16 f'8 ees d c16~bes~
d4. c16 c16~c2
d4 d8. d16 ees8 d c bes
d4 d8. d16 ees8 d c bes16 a16~
a8 bes4~bes16 bes16 f'8 ees d c16~bes
d4. c8 c8~c8 d8 ees8
f4 f8. f,16 f8 f'8 ees d
c4 c8 bes8 c bes c d
ees4 ees8. g,16 g8 ees' d c16~bes16
bes8 bes bes16 c16~c8 a16~g~f8 r16 d'8 ees16 
f4 f8. f,16 f8 f' ees d
c4 c8 bes c bes c d
ees4 ees8. g,16 g8 ees'8 d ees 
f4 f16 g16~g8 g16~f16~f8 r4
\key cis \major eis,8. eis'16~eis4~eis8 cisis dis eis
eis4. dis8 fis2
gis,8. fis'16~ fis4~fis8 dis eis fis
fis4. eis8 eis2
cis8. gis'16~gis4~gis8 eis fis gis
gis4. fis8 fis4. eis8
eis4 dis gis4. eis16 eis~
eis16~dis~dis4.~dis16~eis4..
eis,8. eis'16~eis4~eis8 cisis dis eis
eis4. dis8 fis2
gis,8. fis'16~ fis4~fis8 dis eis fis
fis4.. eis16 eis8~dis16~cis~ais~gis~dis'~cis
cis8.  cis'16~cis4~cis8 ais bis cis
bis4.  cis16 bis~bis8~ais16~gis16~gis8 eis8
eis8. dis16~dis8 ais8 fis'8. eis16~eis8 dis8
cis1 
\key bes \major r1
r1
r1
r1
r1
r1
r1
r1
f4 f8. f,16 f8 f' ees d
c4 c8 bes c bes c d
ees4 ees8. g,16 g8 ees' d c16 bes~
bes16 g'8 f16 d16 c bes d8 c16 a f~f d'8 ees16
g16~f16~d~c~d~ees~g~f~f4. bes,8
c4 c8 bes c bes c d
f16~ees~c~bes~c~d~f~ees~ ees4. f16 f16~
f8 f16 f~f bes8 c16~c16 d4..
\key cis \major eis,,8. eis'16~eis4~eis8 cisis dis eis
eis4. dis8 fis2
gis,8. fis'16~ fis4~fis8 dis eis fis
fis4. eis8 eis2
cis8. gis'16~gis4~gis8 eis fis gis
gis4. ais8 fis4. eis8
eis4 dis fis4. eis16 eis16~ 
\grace {eis8} dis4..~cis16~eis4~ais4
eis,8. eis'16~eis4~eis8 cisis dis eis
eis4. dis8 fis2
gis,8. fis'16~ fis4~fis8 ais8. gis8 fis16
fis4.. eis16 eis8~dis16~cis~ais~gis~dis'~cis
cis8.  cis'16~cis4~cis8 ais bis cis
bis4.  cis16 bis~bis8~ais16~gis16~gis8 eis8
eis8. dis16~dis8 ais8 fis'8. eis16~eis8 dis8
cis2~ cis16 eis16~dis~gis,~dis'~cis8~ais16
cis8. gis'16~gis4~gis8 eis8 fis8 gis8
cis,4. dis16 eis16~eis4~eis16 gis,16 cis dis
eis4. dis16 eis fis8. eis8. dis8\fermata
cis1~
cis \bar "|."
}
 
text = \lyricmode {
難 過 是 因 為 悶 了 很 久
是 因 為 想 了 太 多 
是 心 理 起 了 作 用
你 說 是 哭 笑 常 陪 著 你
在 一 起 有 點 勉 強

}

upper = \relative c { \time 4/4 \key bes \major
<f bes d>4 <f bes d>4 <a f'>16 bes g bes~bes f8.
<g d>4 <g d>4 <ees f bes>2
\grace {f16 bes c} f4 <bes, f'>4 <a f'>16 bes g <bes f'>~bes16 f8.
<ees bes' d>4 <ees g c> <g bes>2
<f bes d>4 <f bes d>4 <a f'>16 bes g bes~bes f8.
<f bes d>4 <f bes d>4 <a f'>16 bes g bes~bes f8.
<f bes d>4 <f bes d>4 <bes d>16 c a <bes d>~bes f8.
<bes c>4 <bes c>4 <a c f>4 <a c f>4
\grace {f16 bes c d} f4 <f, bes d>4 <a f'>16 bes g bes~bes f8.
<f bes d f>4 <f bes d>4 <a f'>16 bes g bes~bes f8.
<f bes d>4 <f bes d>4 <bes d>16 c a <bes d>~bes f8.
<bes c f>4 <bes f'>16 c bes f <a c f>4 <a c f c'>16 a' f c
<f, a c f>4 <f a c>4 <f a c f>4 <f a c f>4
<f a bes d>4 <f a bes d>4 <f a bes d>4 <f a bes d>4
<g bes ees>4 <g bes ees>4 <g bes ees>4 <g bes ees>16 bes g8
<f bes c>4 <f bes c>4 <f a c f>4 \acciaccatura c'16 c'8 a
<a, c f>4 <a c f>4 <a c f>4 <a c f>4
<g bes d f>4 <g bes d f>4 <g bes d f>4 <g bes d f>4
<g bes ees>4 <g bes ees>4 <g bes ees>4 <g bes ees>16 bes g8
<g bes ees>4 <g bes ees>16 bes g8 <g bes c f>2
\key cis \major <eis ais cisis>4 <eis ais cisis>4 <eis ais cisis>4 <eis ais cisis>16 ais eis8
<fis bis>4 <fis cis'> <fis ais dis> <fis ais cis eis>8 fis8
<fis ais cis>4 <fis cis'> <gis bis dis gis>4 <gis bis dis gis>4
<gis cis fis>4 <gis cis fis>4 <gis cis eis>4 <gis bis dis>4
<eis gis cisis>4 <eis gis cisis>4 <eis gis cisis>4 <eis gis cisis>16 gis eis8
<ais cis gis'>4 <ais cis gis'>4 <ais cis fis>4 <ais cis fis>16 eis'16 dis8
<fis, b cis fis>4 <fis b cis fis>4 <fis b cis fis>4 <fis b cis fis>16 cis' b fis
<gis cis dis gis>4 <gis cis dis gis>4 <eis ais bis eis>4 <eis ais dis>4
<eis ais cisis>4 <eis ais cisis>4 <eis ais cisis>4 <eis ais cisis>16 dis' eis8
<fis, ais bis>8. fis16 <fis cis'>4 <fis ais dis> <fis ais cis eis>4
<fis ais cis fis>4 <fis ais cis fis> <gis bis dis gis>4 <gis bis dis gis>4
<gis cis fis>4 <gis cis fis>4 <gis cis eis>4 <gis bis dis>4
<eis gis cis>4 <eis gis cis>8 bis'16 cis gis'8 bis,16 cis bis'16 gis eis cis
<bis dis>4 <bis dis gis>4 <gis bis>4 <gis bis dis>16 bis gis8
<fis bis cis>4 <eis' fis cis'>4 <fis, ais cis fis>2
\grace {gis16 cis dis} gis1
\key bes \major bes,8 d f d a d f d
g, bes f' d aes c aes' ees
g, bes g' ees g, bes g' ees 
a, c a' f g, <ees' g> a, <f' a>
bes,8 d f d a d f d
g, bes f' d aes c aes' aes,
g bes g' ees g, bes g' g,
f bes f' bes, c bes <a c> ees'
<a, c f>8 c f c a a' f a,
g4 d'8 bes g g' d bes
g bes ees bes g g' ees g,
f bes f' bes, f' c <a f'> c
a c f c a a' f f,16 fis16
g8 bes d bes d g d bes
bes d ees bes g' bes, ees bes
<f bes ees> bes <f bes ees> bes <f a c f>2
\key cis \major <eis ais eis'>4 <eis ais eis'>4 <eis ais eis'>4 <eis ais cisis>16 dis' eis8
<fis, bis>4 <fis ais cis> <fis ais dis> <fis ais cis fis>
<fis ais cis> <fis ais cis> <gis bis dis> <gis bis dis gis>
<gis cis fis> <gis cis fis> <gis cis eis> <gis bis dis>
<eis gis cis> <eis gis cis> <eis gis cis> <eis gis cis>
<ais cis gis'> <ais cis gis'> <ais cis fis> <ais cis fis>16 eis' dis8
<fis, b cis fis>4 <fis b cis fis>4 <fis b cis fis>4 <fis b cis fis>4
<gis cis dis gis> <gis cis dis gis> <eis ais bis eis> <eis ais>
<eis ais eis'> <eis ais eis'> <eis ais eis'> <eis ais cisis>16 dis' eis8
<fis, bis>4 <fis ais cis> <fis ais dis> <fis ais cis fis>
<fis ais cis> <fis ais cis> <gis bis dis> <gis bis dis gis>
<gis cis fis> <gis cis fis> <gis cis eis> <gis bis dis>
<eis gis cis> <eis gis cis> <eis gis cis> <eis gis cis>
<gis bis dis> <gis bis dis> <gis bis dis> <gis bis dis>
<fis ais cis> <fis ais cis fis> <fis gis ais cis>2
<gis cis eis gis>4 <gis cis eis> <gis cis eis> <gis b eis>
<gis cis dis gis>4\arpeggio <gis cis fis> <gis cis eis> dis'16 cis gis8
<gis cis dis gis>4\arpeggio <gis cis fis> <gis cis eis>8.\arpeggio gis16 dis' cis gis8
<fis ais cis>4 <fis ais cis> <fis ais cis fis>2\arpeggio\fermata
<gisis cis gisis'>4 <fisis b fisis'> <e gisis bis e> <e gis b e>
<gis cis eis gis>1\arpeggio
}


lower = \relative c { \clef bass \key bes \major
<bes, bes'>4.. f'16 bes,4 bes'8 bes16 bes,16
<ees, ees'>4.. bes'16 ees,2
<bes' bes'>8. bes'16~ bes8. bes16 bes,4 bes'8 bes16 bes,16
<ees, ees'>4.. bes'16 ees,2
<bes' bes'>4.. f'16   bes,4 bes'8 bes16 bes,16
<g 	g'>4.. d'16   g,4     g'8 g16   bes,16
<ees, ees'>4.. bes'16 ees,4 ees'8 ees16 ees,16
f'2 f,2
<bes bes'>4.. f'16   <bes, bes'>4 bes'8 bes16 bes,16
<g     g'>4.. d'16   <g, g'>4       g'8 g16     g,16
<ees     ees'>4.. bes''16 <ees, ees'>4 ees'8 ees16 ees,16
<f, f'>8. f'16~f8. f16 <f, f'>8. f'16 ees4
d4.. a'16 d,8. a'16 d,8. f32 fis32
g4.. d16  g,8.  d'16 g,8. bes32 b32
c4.. c'16 c,8.   c'16 c,4
<f f'>4. f'8 <f, f'>4 <ees ees'>4
<d d'>4..  d'16 d,8. d'16 d,8. f32 fis32
<g, g'>4.. g'16 g,8. g'16 g,8. bes32 b32
<c c'>2~ <c c'>8. c'16~ c8. f,16
<f, f'>8. f'16~ f8. f,16~f4 f16 g16 a8
\key cis \major <ais ais'>4.. ais'16 ais,8. ais'16 ais,8. ais'16
<dis,, dis'>4. dis'16 ais <dis, dis'>8. dis'16 dis,4
<gis gis'>8. gis'16~gis8 gis16 ais bis4.. <bis, bis'>16
<cis cis'>4.. <cis cis'>16 <cis cis'>4 bis'4
<ais, ais'>4.. ais'16 ais,8. ais'16 ais,4
<dis dis'>8. dis'16 dis,8. dis'16 dis,8. dis'16 dis,4
<b b'>4.. b'16 b,8. b'16 b,8. ais'16
<gis, gis'>8. gis'16 gis8. gis32 ais32 <bis, bis'>8. bis'16 <eis, eis'>4
<ais, ais'>4.. ais'16 ais,8. ais'16 ais,4
<dis, dis'>4.. dis'16 dis,8. dis'16 dis,4
<gis gis'>8. gis16~gis8 gis'16 ais bis8. bis,16~bis8 bis'8
<cis, cis'>8. cis'16 gis cis gis cis, <cis cis'>8. cis'16 <bis, bis'>4
<ais ais'>8. ais'16~ais4 ais16 eis'8.~eis4
<eis,, eis'>2. eis'4
<dis, dis'>2 <gis gis'>2 
cis,1
\key bes \major <bes' bes'>4. <bes bes'>8 <a a'>4. <a a'>8
<g g'>4. <g g'>8 <f f'>8. f'16 <d bes'> c' d8
<ees,, ees'>4. <ees ees'>8~<ees ees'>16 bes''8 a16 f bes, a g
<f f'>8 <f f'>8 <f f'>8 <f f'>8 <g g'>8. g'16 a8 a8
<bes, bes'>4.  <bes bes'>8 <a a'>4.  <a a'>8 
<g g'>4.. <g g'>16 <f f'>8. f'16 <d bes'>16 c' d8
<ees,, ees'>4.  <ees ees'>8~ <ees ees'>16 bes''8 a16 f bes, a g
<f f'>8 <f f'>8 <f f'>8 <f f'>8~<f f'>8 <f f'>8 <f f'>8 <f f'>8 
\ottava #-1 <d d'>4. c8 c4. ees16 eis
\ottava #0 <g g'>4. g8 g8. bes'16~bes d, bes g
\ottava #-1 c4. c8 c4 g16 c g eis
\ottava #0 ees8. c'16 f16 c f f~f8. c16 f,4
d'4. d8 d4~d16 d f fis
g,4. g8 g8. \grace {a'8} bes16~bes f d g,
\ottava #-1 c4. c8 c4 c8 ees16 e
f,8. c'16 f, c' f f, <f f'>2
\key cis \major <ais ais'>4. ais8~ais4 ais'8 eis16 cisis
<dis, dis'>4. dis'8~dis4 fis16 dis eis fis
gis,4. gis16 ais bis4~ bis16 gis bis gis
<cis, cis'>8. gis'16~gis cis dis eis~eis dis cis bis~bis8 gis
<ais ais'>4. ais8~ais ais8. fis16 eis e
<dis dis'>4. <dis dis'>8~<dis dis'>4~dis'16 dis cis' bis
\ottava #0 <b, b'>8. b'16 cis8. dis16~dis16 fis8 eis16~eis dis cis b
gis8. gis16~gis8 gis <bis, bis'>4 <dis, dis'>4
<ais' ais'>4. ais'8~ais4~ais16 eis bis ais
<dis, dis'>4. dis'8~dis4~dis16 ais fis dis
<gis gis'>4.  gis'16 ais <bis, bis'>4. bis'16 gis
cis,4. cis8 cis8. gis'16 <bis, bis'>4
<ais ais'>4. ais'8~ ais16 ais bis cis dis4
eis,4 eis'8 eis, eis4 ~eis16 bis'16 dis eis,
dis4. eis16 fis <gis, gis'>2
cis'4.. cis16 <cis, cis'>8. cis'16 <eis,, eis'>4
fis'4.. fis16 fis8. fis'16~fis4
eis,2 ais4 ais
<dis,, dis'>2 <gis gis'>2
<gis gis'>4 <fis fis'> <eis eis'> <e e'>
cis'8 gis' dis' eis fisis2
}

showLastLength = R1*35

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

