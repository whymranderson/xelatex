#(set-default-paper-size "a4")

\paper {
  two-sided = ##f
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  %binding-offset = 0.25\in
}

\header{
  title = "Stranded"
  subtitle = "accompanyin piano"
  composer = "Jay"
  arranger = "GS Simulation"
}


melody = \relative c'' {\tempo 4 = 70 \key f \major 
r1
r1
r1
r1
r8 a bes a g a16 bes16~bes16 a8.
r8 a bes a g a16 a16~a16 e8.
f4 d' c4. f,8
bes a bes c16 a~a8 g4.
r8 a bes a g a16 bes16~bes16 a8.
r8 a bes a g a16 a16~a16 c8.
f,4 d' c8 g'16 f16~f8. g16 
a8 a a f16 f16~f16 g16~g4 f16 e16
d8 d d e16 d~d16 cis16~cis4~cis16 a16
e'8 e f g16 g16~g16 f16~f8 f16 f~f e
d8 d16 d16~d8. d16 d8 g8 g8 f16 g16~
a2 r8 a, c g'
f bes, bes a16 a16~a8 g e' f
g c, c bes16 bes16~bes8 a a16 bes c8
c d16 f,~f8. d'16 d8 e c g 
bes a g a~a8 a c g'
f bes, bes a16 a~a8 g e' f
g g g e16 g~g8 f d e
f e16 f~f8. e16 d8 e f8 e16 f16~
f1
r1
r1
r1
r1
r1
r8 a, bes a g a16 bes16~bes16 a8.
r8 a bes a g a16 a16~a16 e8.
f4 d' c4. f,8
bes a bes c16 a~a8 g4.
r8 a bes a g a16 bes16~bes16 a8.
r8 a bes a g a16 a16~a16 c8.
f,4 d' c8 g'16 f16~f8. g16 
a8 a a f16 f16~f16 g16~g4 f16 e16
d8 d d e16 d~d16 cis16~cis4~cis16 a16
e'8 e f g16 g16~g16 f16~f8 f16 f~f e
d8 d16 d16~d8. d16 d8 g8 g8 f16 g16~
g2 r8 a, c g'
f bes, bes a16 a16~a8 g e' f
g c, c bes16 bes16~bes8 a a16 bes c8
c d16 f,~f8. d'16 d8 e c g 
bes a g a~a8 a c g'
f bes, bes a16 a16~a8 g e' f
g g g e16 g16~g8 f d e
f e16 f16~f8 e d e f4
\key fis \major \transpose f fis { \relative c' { r4 c'' a g
f8 bes, bes a16 a16~a8 g8 e' f
g c, c bes16 bes16~bes8 a8 a16 bes16 c8
c8 d16 f,16~f8. d'16 d8 e c g'
bes a g a~a8 g g a
g f f8 g16 a16~a8 g8 e f
g g g a16 g16~g8 f8 d e
f e16 f16~f8. e16 d8 e f e16 f16~
f1 } }
r1
r1
r1 \bar "|."
}

text = \lyricmode {
久 未 放 晴 的 天 空   依 舊 留 著 妳 的 笑 容
哭 過   卻 無 法 掩 埋 歉 疚
風 箏 在 陰 天 擱 淺   想 念 還 在 等 待 救 援
我 拉 著 線   復 習 妳 給 的 溫 柔
曝 曬 在 一 旁 的 寂 寞   笑 我 給 不 起 承 諾
怎 麼 會 怎 麼 會   妳 竟 原 諒 了 我

我 只 能 永 遠 讀 著 對 白   讀 著 我 給 妳 的 傷 害
我 原 諒 不 了 我   就 請 妳 當 作 我 已 不 在
我 睜 開 雙 眼   看 著 空 白   忘 記 妳 對 我 的 期 待
讀 完 了 依 賴   我 很 快 就 離 開

久 未 放 晴 的 天 空   依 舊 留 著 妳 的 笑 容
哭 過   卻 無 法 掩 埋 歉 疚
風 箏 在 陰 天 擱 淺   想 念 還 在 等 待 救 援
我 拉 著 線   復 習 妳 給 的 溫 柔
曝 曬 在 一 旁 的 寂 寞   笑 我 給 不 起 承 諾
怎 麼 會 怎 麼 會   妳 竟 原 諒 了 我

我 只 能 永 遠 讀 著 對 白   讀 著 我 給 妳 的 傷 害
我 原 諒 不 了 我   就 請 妳 當 作 我 已 不 在
我 睜 開 雙 眼   看 著 空 白   忘 記 妳 對 我 的 期 待
讀 完 了 依 賴   我 很 快 就
我 只 能 永 遠 讀 著 對 白   讀 著 我 給 妳 的 傷 害
我 原 諒 不 了 我   就 請 妳 當 作 我 已 不 在
我 睜 開 雙 眼   看 著 空 白   忘 記 妳 對 我 的 期 待
讀 完 了 依 賴   我 很 快 就 離 開
}


upper = \relative c'' { \time 4/4 \key f \major 
c8 e, f c' c d, bes' d,
a' a, cis <e g> <e g> a, <f' a> a,
<< { g' g, bes d g g, bes f' 
<c f> g bes c e2 } \new Staff \with {instrumentName = #"Violin" midiInstrument = #"violin"} {c'8 a bes f' e f c'4 \ottava #1 f1} >>
\ottava #0 <c=' f>8 a <c f>8 a <cis f>8 a <cis e>8 a
<c f>8 a <c f>8 a <c f>8 a <c f>16 g' a8
<d, f> bes <d f> bes <c f> a <c e> f
<bes, d f> g <bes d f> g <bes d f> g <c e> g
<c f> a <c f> a <cis f> a <cis e> a
<c f> a <c f> a <c f> a <c f>16 g' a8
<d, f> bes <d f> bes <f' g> e f a,
<bes d f> g <bes d f> g <bes d f> g <bes e> g
<g' bes> d <g bes> d <cis e> a <cis e> a
<e' g> a, <e' g> a, <d f> a <d f>16 g a8
<b, d f a>\arpeggio b <f' a> d <f bes> d <f bes> d
<a' c f>4 <a c f>4 <e g c>4 <f c' f>4
<f bes>8 d <f bes>8 f <e g c> c <e g c> c
<c e a> a <c e a> a <c e > a <c f > a
<d f bes> bes <d f bes> bes <d f bes> bes <e g c> g,
<f' bes> d <f bes> d <f a> c <a' c f> f
<bes c f> d, <bes' c f> d, <g c e> e <g c e> e
<e a> cis <e a> cis <e g> a, <d f> a
<f bes> d <f bes> d <f bes> c <e g c> c
<f' a> c <f a> c <g' bes> c, <f a> c
\key f \minor <aes' c>8 ees c ees <aes c> ees <g bes> c
<g bes> ees <g bes> ees <f aes> g <e g>16 aes bes8
<f aes>8 c <f aes>8 c <f aes>8 des f16 g aes8
<f aes>8 ees <f aes>8 ees <bes des> ees <bes des> ees
<des f> g, bes c e g, g' g, 
\key f \major f'8 a, c f f g, <cis e> g
f' a, d f f a, f'16 g a8
a bes, d a' g e f c'
c d, bes'16 a g f f f e f e8 g,
<c f>8 a c f <cis f> a <cis e> a
<c f> a <c f> a <c f> a <c f>16 g' a8
<d, f bes> d <d f a> bes <f' g> e16 f~f c' f, c'
<f, bes>8 d <f bes>8 d <bes d f> g <bes e> g
<e' g b>8 b d g <cis, e a> a <cis e> a
<e' g> a, <e' g> a, <d f> a <d f> a
<b d f a> b <f' a> d <f b> d <f b> d
<f a c> c <f a c> c <e g c> c <c f> a
<d f bes> bes <d f bes> bes <e g c> c <e g c> c
<c f a> a <c f a> a <e' g> a, <d f> a
<d f bes> bes <d f bes> bes <bes e f> g <bes e> g
<bes d bes'> <f f'> <bes d bes'> <f f'> <f a c>4 <f' a c>16 e f c'
<f, c'>8 d <f c'>8 f <e g c> c <c e g c> bes'
<e, a> cis <e a> cis <e g> a, <d f> a'
<bes, d f> g <bes d f> g <f' a c> bes, <bes c e>4
\key fis \major r4 <ais ais'>4 <cis cis'> <gis' gis'>
<dis fis ais>8 b <dis fis ais>8 b <gis' cis eis> gis <gis cis eis> gis
<gis cis> eis <gis cis> eis <gis cis> fis eis fis
<fis b> dis <fis b> dis <fis b> dis <eis gis> cis
<dis fis b> dis <dis fis b> cis <cis fis ais> cis <fis ais> gis
<ais b dis fis> fis <ais b dis fis> fis <gis cis eis> cis, <gis' cis eis> gis
<gis b d> eis <gis b d> eis <fis ais dis> fis eis fis
<fis b> dis <fis b> dis <eis gis b> cis <cis eis gis b>4
dis'8 fis, b dis cis fis fis4
b,8 dis, fis b <eis, b'>4 <b gis'>4
<ais fis'>8 cis, fis gis ais fis <dis b'> fis
<cis fis ais>1\arpeggio
}


lower = \relative c { \clef bass \key f \major 
a8 f' c'4 bes,8 f' bes4
a,2 <d, d'>4 <c c'>4
g'8 g'~g2.
c,,1
<f f'>2 <a, a'>4.~a'16 a16
d,2 <c c'>4 <c c'>4
<bes bes'>2 <a a'>2
g'4.~g16 g16 <c, c'>4 <c c'>4
<f f'>4.~f16 f16 <a, a'>4.~a'16 a16
d,4.~d16 d16 <c c'>4 <c c'>4
<bes bes'>4.~b16 b16 a4 d4
<g, g'>4.~g'16 g16 <c, c'>4 <c c'>4
e4.~e16 e16 <a, a'>8 <a a'>4 <a a'>8
<d d'>4.~d16 d16 <d d'>4 <c c'>4
<b b'>1
<c' \parenthesize c'>4 <c \parenthesize c'>4 <c, \parenthesize c'>4 <a' \parenthesize a'>4
<bes bes'>4.~bes16 bes <c c'>4 <c, c'>
<a a'>4.~a16 a <d d'>2
<g, g'>4~g'16 g a bes <c, c'>4 <c c'>4
<f, f'>4.~f'16 c <f, f'>4 <c' c'>4
<bes bes'>4.~bes16 bes <c c'>8 <c c'>4 <bes bes'>8
<a a'>4 <cis cis'>8.  <cis cis'>16 <d d'>4.~d'16 a
g4.~g16 g16 <c, c'>4 <c c'>4
<f f'>4.~f'16 c <f, f'>4 <f f'>4
\key f \minor <aes aes'>4.~aes16 aes16 <aes, aes'>4. <aes aes'>8
<ees' ees'>4.~ees'16 ees16 <ees, ees'>4 <e e'>4
<f f'>4.~f'16 f16 <des, des'>4 <des des'>4
<ees ees'>4.~ees'16 bes16 <ees, ees'>8 <ees ees'>4 <ees ees'>8
<c c'>1
\key f \major f2 <a, a'>4.~a'16 a16
d,2 c4 c4
bes'4.~bes16 bes16 a4 <d a' c>4
g,8 d' bes'4 c,4. c,8
<f f'>4.~f16 f16 <a, a'>4.~a'16 a16
<d, d'>4.~d16 d16 <c c'>8 <c c'>4 <c c'>8
<bes bes'>4.~bes16 bes16 <a a'>4 <d d'>4
<g g'>8 <g g'>4 <g g'>8 <c, c'>4 <c c'>
<e e'>4.~e16 g16 <a a'>4 <a a'>
<d, d'>4. r16 a'16 <d, d'>4 <c c'>
<b b'>2 <a b'>4 <c d'>4
<c' c'>4 <f, f'> <c c'> <a' a'>
<bes, bes'>4.~bes'16 bes16 <bes, c'>4 <bes c'>
<a a'>4.~a'16 a16 <d, d'>4 <d d'>
<g, g' bes>4.~bes'16 bes16 <g, c'>4 <g c'>
<f' f'>4.~f16 f16 <f f'>4 <a f' a>
<bes, bes'>4.~bes16 bes16 <c c'>4 <c c'>
<a a'>4 <cis cis'>2 d'16 a d,8
<g g'>4.~g16 g16 <c, c'>4 <c c'>4
\key fis \major r4 <cis cis'>4 <ais' cis fis> <fis' cis'>
<b,, b'>4.~<b b'>16 <b b'>16 <cis cis'>4 <cis cis'>4
<ais ais'>4.~<ais ais'>16 <ais ais'>16 <dis dis'>4 <dis dis'>
<gis gis'>4.~<gis gis'>16 <gis gis'>16 <cis, cis'>8 <cis cis'> <cis cis'>4
<fis fis'>4.~fis16 cis16 <fis, fis'>4 <ais ais'>
<b b'>4.~<b b'>16 <b b'>16 <cis cis'>4 <cis, cis'>4
<ais' ais'>4 <d d'> <dis dis'> <dis dis'>16 ais' dis,8
<gis, gis'>4.~<gis gis'>16 <b b'>16 <cis cis'>4 <cis cis'>4
b'8 fis' dis'4 ais,8 fis' cis'4
gis,8 dis' gis dis'
<cis, cis'>4 <cis, cis'>4
<fis fis'>2. b,4
<fis fis'>1\arpeggio
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
