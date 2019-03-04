#(set-default-paper-size "a4")

\paper {
  two-sided = ##t
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  binding-offset = 0.25\in
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
d8 d16 d16~d8. d16 d8 a'8 a8 g16 a16~
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
d8 d16 d16~d8. d16 d8 a'8 a8 g16 a16~
a2 r8 a, c g'
f bes, bes a16 a16~a8 g e' f
g c, c bes16 bes16~bes8 a a16 bes c8
c d16 f,~f8. d'16 d8 e c g 

bes a g a~a8 a a b
a g g a16 b~b8 a fis g
a a a fis16 a~a8 g e fis
g fis16 g~g8. fis16 e8 fis g8 fis16 g16~
g1
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
}


upper = \relative c'' { \time 4/4 \key f \major 
c8 e, f c' c d, bes' d,
a' a, cis <e g> <e g> a, <f a> a
<< { g' g, bes d g g, bes f' 
<c f> g bes c e2 } \new Staff \with {instrumentName = #"Violin" midiInstrument = #"violin"} {c'8 a bes f' e f c'4 \ottava #1 f1} >>
\ottava #0 <c=' f>8 a <c f>8 a <cis f>8 a <c e>8 a
<c f>8 a <c f>8 a <c f>8 a <c f>16 g' a8
<d, f> b <d f> b <c f> a <c e> f
<b, d f> g <b d f> g <b d f> g <c e> g
<c f> a <c f> a <cis f> a <c e> a
<c f> a <c f> a <c f> a <c f>16 g' a8
<d, f> b <d f> b <f' g> e f a,
<b d f> g <b d f> g <b d f> g <b e> g
<g' b> d <g b> d <cis e> a <cis e> a
<e' g> a, <e' g> a, <d f> a <d f>16 g a8
<b, d f a>\arpeggio b <f' a> d <f b> d <f b> d
<a' c f>4 <a c f>4 <e g c>4 <f c' f>4
<f bes>8 d <f bes>8 f <e g c> c <e g c> c
<c e a> a <c e a> a <c e > a <c f > a
<d f bes> bes <d f bes> bes <d f bes> bes <e g c> g,
<f' bes> d <f bes> d <f a> c <a' c f> f
<bes c f> d, <bes' c f> d, <g c e> e <g c e> e
<e a> cis <e a> cis <e g> a, <d f> a
<f bes> d <f bes> d <f bes> c <e g c> c
<f' a> c <f a> c <g' bes> c, <f a> c
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
<b b>1
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
