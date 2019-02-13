#(set-default-paper-size "a4")

\paper {
  two-sided = ##t
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  binding-offset = 0.25\in
}

\header{
  title = "excuse"
  subtitle = "accompanyin"
  composer = "Jay"
  arranger = "GS Simulation"
}


melody = \relative c'' { \tempo 4 = 80 \key d \major
r1 r r r
r8 a a fis g fis16 g~ g a8.
fis8 a d cis16 b~ b a8.~a4
b4 d cis8 d16 d~ d4 
fis8 d16 d~ d8 a16 a~ a16 e'8.~ e4
r8 a=' a fis g fis16 g~ g a8.
fis8 a d cis16 b~ b a8.~ a4
b4 d cis8 d16 d~ d4 
fis8 d16 d~ d8 e16 fis~ fis16 e16~ e4.
cis=''8 cis16 cis16~ cis8 b16 bes16~ bes8 b16 cis16~ cis16 e8.
\transpose c'' d'' { \relative c'' {
c=''8 c16 c16~ c8 b16 a16~ a8 b16 c16~ c16 e8.
e=''8 d16 d16~ d8 c16 c16~ c8 a16 d16~ d16 c8.
}}
b='8 cis16 d8 d16~ d8 d8 cis16 d16~ d8 e8.
fis=''4 fis8 e16 fis16 e8.~ e8.~fis16
\transpose c'' d'' { \relative c'' { \repeat volta 2 { r8 g=' e g d'8. f16~f8 e8
r8 g=' e g d'8. f16~ f8 e8
r8 g=' e g d'8. f16~ f8 e8
d8 c d e16 d16~ d16 c8.~ c4
r8 a8 a f e' d16 e16~ e16 d8.
r8 g='8 g e d' c16 b16~ b16 c8.}
\alternative {{c8 d16 e16~ e16 c8. c8 d16 e16~ e16 c8 d16
e4 e8 d16 e16~ e8 d4 ~ e8}
{c8 d16 e16~e16 c8. g8 e' d8. c16~
c8 c8~c2.}}
r1
r1
r1
c8 d16 e16~e16 c8. g8 e' d8. c16~
c8 c8~c2.
r1
c8 d16 e16~e16 c8. g8 e' d8. c16~
c8 c8~c2.
r1 \bar "|."
}}}

text = \lyricmode {
翻 著 我 們 的 照 片 想 念 若 隱 若 現 去 年 的 冬 天 我 們 笑 得 很 甜 
看 著 妳 哭 泣 的 臉 對 著 我 說 再 見 來 不 及 聽 見 妳 已 走 得 很 遠 

也 許 妳 已 經 放 棄 我 也 許 已 經 很 難 回 頭 
我 知 道 是 自 己 錯 過 請 再 給 我 一 個 理 由 說 妳 不 愛 我 
<<
{就 算 是 我 不 懂 能 不 能 原 諒 我 請 不 要 把 分 手 當 作 妳 的 請 求  
我 知 道 堅 持 要 走 是 妳 受 傷 的 藉 口 請 妳 回 頭 我 會 陪 妳 一 直 走 到 最 後} 
\new Lyrics \with { alignBelowContext = #"firstVerse" } { \set associatedVoice = "Voice"
就 算 沒 有 結 果 我 也 能 夠 承 受 我 知 道 妳 的 痛 是 我 給 的 承 諾 
妳 說 給 過 我 縱 容 沉 默 是 因 為 包 容 
{\skip 1}
}
>>
如 果 要 走 請 妳 記 得 我  
如 果 要 走 請 妳 記 得 我  
如 果 難 過 請 妳 忘 了 我 
}

upper = \relative c'' { \time 4/4 \key d \major
\transpose c'' d'' { \relative c'' { c8 bes aes4 g8  c d e 
f e d4 c2
c2 r2
c2 r2 }}
<d=' fis>8 a <d fis> a <d fis> a <d fis> a
<d fis> a <d fis> a <cis fis> a <d fis> a
<d fis> b <d fis> b <e a> <cis a'> <d a'> fis
<g d g,>4 <g d>8 g, <d' g>4 <e g>
<d=' fis>8 a <d fis> a <d fis> a <d fis> a
<d fis> a <d fis> a <cis fis> a <d fis> a
<d fis> b <d fis> b <e a> <cis a'> <d a'> fis
<g d g,>4 <g d>8 g, <d' g>4 <cis g'>
<cis=' e g>4 <e g>8 cis <fes bes> e <fes cis> e
<fis b>8 d <fis b>8 d <fis b>8 d <fis a> d
<b=' d>8 g <b=' d> g <a e'> cis <b d> fis
<e=' g>8 d <e g> d <e g b> d <g b d> e
<e=' g d'>4 <e g d'> <e g cis> <e g cis>
<d=' fis>8 a <d fis> a <d g> a <d fis> a
<d fis> a <d fis> a <d g> a <d fis> a
<d fis> a <d fis> a <d g> a <d fis> a
<d fis> a <d fis> a <d g> a <d fis> a
<b d fis>8 b d b <cis e> e a e
<cis a> a cis a <cis e> d cis d
<b g> b d b <b g> b d b
<a cis> b d b <a cis> e' a e
\transpose c'' d'' { \relative c' {
<c f>8 a <c f>8 a <a c d g>4 <b d>4
<< { \voiceOne 
e8 c e c f e c d
e  c e c f e f e
e8 c e c f e c d
e8 c e c <c f>2
}
\new Voice { \voiceTwo 
g8 e g e g e g e
aes f aes f aes f aes f
g8 e g e g e g e
aes f aes f aes f aes f
}
>> \oneVoice
<c' f a>8\arpeggio c <f a> c <a c f g>4\arpeggio <g b d g>4\arpeggio
c'8 c, f c' b, d' f e 
<e, g c e>\arpeggio g d' b <c, e d'>\arpeggio \acciaccatura {c'16 d} c8 b c
<c, f c'>8 c f c' <c, f c'>2\arpeggio
<< { <c e>8 g <c e>8 g <c d f>8 aes <c d f>8 aes 
<g c d e>1 } \new Staff {\key c \major e'8 g e g f g aes bes c1 } >>
}}
}

lower = \relative c { \clef bass \key d \major
\transpose c'' d'' { \relative c { aes8 f' c' f, g, e' c' e,
f, c' aes' c, e, c' g' c,
d, c' f aes c f4.
g,,=,8 d' c'4
<b g d>2\arpeggio }}
d2 cis 
b  fis
g fis4 b
e,2 a
d=2 cis 
b  fis
g fis4 b
e,2 a
cis=2 fis,4. bes'8    %e=4. b8 e,4. bes'8
b2 a
g fis4 b4
e,2 e2 
a2 a,2
d=8 a' d a e' a, d a
cis=8 a' d a e' a, cis d
b, a' d a e' a, d a
a, a' d a e' a, cis d
g,,1
fis2 b
e,1
a
\transpose c'' d'' { \relative c {d,4 d g g, 
c2 c2
c2 c2
c2 c2
c2 c2
d8 a' d d, g4 g
a8 f' a f aes, f' aes f
g, e' c' e, a, e' c' e,
<d, d'> a' f'4 g,2
c,8 g' c g c, f c'4
c,1
}}
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

