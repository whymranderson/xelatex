#(set-default-paper-size "a4")

\paper {
  two-sided = ##f
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  %binding-offset = 0.25\in
}

\header{
  title = "End of World"
  subtitle = "accompanyin piano"
  composer = "Jay Chou"
  arranger = "Drillbits"
}


melody = \relative c' {
\key g \major
r1
r1
r1
r2. r8 d
\repeat volta 2 {b'4. b8 c b a g
a4 a16~g b4 r8 a b
c2 c8 b a g
g4 a8 a8~a4 b8 c
d4. d8 d c b a16~g }
\alternative {{a8 b c b~ b4 a8 b16 d16~
c2 c8 b g g16~e 
g8~a~g~a~ a4. d,8} 
{a'8 b c16 a b8~ b4 a8 b
c8 b g g16 e g8 a b g~
g4~g4 g8 a8 b c8~}}
c2. b8 c8
d4 c8 b b4 b8 a 
g a b fis' d2
e4 d8 c d4 c8 b
c b g b a2
g4 a8 b fis'4 g8 fis
e8~d~b g~ g2
r4 c8 c b g b a~
a2. b8 c8
d4 c8 b b4 b8 a
g8 a b fis' d2
e4 d8 c d4 c8 b
c8 b g b a2
g4 a8 b fis'4 g8 fis
e8~d~b g~g2
r4 c8 c b c b d~
d2 b8 g e g~
g1
r1
r1
r2. r8 d8
b'4. b8 c b a g
a4 a16~g b4 r8 a b
c2 c8 b g g16~e16
g4 a8 a8~a4 b8 c
d4. d8 d c b a16~g
a8 b c16 a16 b8~ b4 a8 b
c8 b g g16 e g8 a b g~
g4~g4 g8 a8 b c8~
c2. b8 c8
d4 c8 b b4 b8 a 
g a b fis' d2
e4 d8 c d4 c8 b
c b16 a8. g16 b8.~a4.
g4 a8 b fis'4 g8 fis
e8~d~b g~ g2
r4 c8 c b g b a~
a2. b16 c b c
d4 c8 b b4 b8 a
g8 a b fis' d2
e4 d8 c d4 c8 b
c8 c16 b'~b8 c16 b8~a8.~a4
g,4 a8 b fis'4 g8 fis
e8~d~b g~g2
r4 c8 c b c b d~
d8~e16~g16~g4 b,8 g e g~
g1
}
 
text = \lyricmode {
想 <<{
笑 來 偽 裝 掉 下 的 眼 淚 
點 點 頭   承 認 自 己 會 怕 黑 
我 只 求   能 借 一 點 的 時 間 來 陪
你 卻 連 同 情 都 不 給 想 
}
\new Lyrics 
\with { alignBelowContext = #"firstVerse" }
{
\set associatedVoice = "Voice"
哭   來 試 探 自 己 麻 痺了 沒 
全 世 界   好 像 只 有 我 疲 憊 
無 所 謂   反 正 難 過 就  
{\skip 1}
}
>>
敷 衍 走 一 回 但 願
絕 望 和 無 奈 遠 走 高 飛   遠 走 高 飛 

天 灰 灰   會 不 會   讓 我 忘 了 你 是 誰 
夜 越 黑   夢 違 背   難 追 難 回 味 
我 的 世 界 將 被 摧 毀   也 許 事 與 願 違 

累 不 累   睡 不 睡   單 影 無 人 相 依 偎 
夜 越 黑   夢 違 背   有 誰 肯 安 慰 
我 的 世 界 將 被 摧 毀   也 許 頹 廢 也 是 
另 一 種 美 
想 哭   來 試 探 自 己 麻 痺了 沒 
全 世 界   好 像 只 有 我 疲 憊 
無 所 謂   反 正 難 過 就 敷 衍 走 一 回 
但 願 絕 望 和 無 奈 遠 走 高 飛   遠 走 高 飛 

天 灰 灰   會 不 會   讓 我 忘 了 你 是 誰 
夜 越 黑   夢 違 背   難 追 難 回 味 
我 的 世 界 將 被 摧 毀   也 許 事 與 願 違 

累 不 累 不 累   睡 不 睡   單 影 無 人 相 依 偎 
夜 越 黑   夢 違 背   有 誰 肯 安 慰 
我 的 世 界 將 被 摧 毀   也 許 頹 廢 也 是   另 一 種 美 
}

upper = \relative c' {
  \time 4/4
\key g \major
\tempo 4 = 80
<d b'>8 g16 d <d b'>8 g16 d <e c'>4 d'8 <d, b'>8~
<d b'>8 g16 d b'8 g16 d <e c'>2
<d b'>8 g16 d <d b'>8 <e c'>8~ <e c'>8 <g c g'>4 <g d' g>8 
<g d' g>4 <a d fis>2.
<d, g b>4 <d g b>4 <d g b>4 <d fis a>4
<b e g>4 <b e g>4 <b e g>4 <b e g>4
<e a c>4 <e a c>4 <e a c>4 <e g b>4
<d fis a>4 <d fis a>4 <d fis a>4 <c e g>4
<b d fis>4 <fis' b d>4 <fis b d>4 <fis b c>4
<e g b>4 <e g b>4 <d fis a>4 <e gis b>4
<e a c>4 <e a c>4 <e a c>4 <e g b>4 
<c e g>4 <c e g>4 <c fis a>4 <c fis a>4
<e g b>4 <e g b>4 <d fis a>4 <e gis b>4
<e a c>  <e g b>  <g, d' g>  <g d' fis>
<b d g> <b d g> <b d g> <b d g>
<e g c> <e g c> <d fis d'>2
<g b d>4 <g b d>4 <a b dis>4 <a b dis>4
<g b e>4 <g b e>4 <b d fis>4 <b d fis>4
<g c e>4 <g c e>4 <fis b d>4 <fis b d>4
<e a c>4 <e g b>4 <d fis a>4 <dis fis b>4
<e g b>4 <e g b>4 <ees fis a>4 <ees fis a>4
<d g b> <d g b> <b cis e g>2 
<a c e g>1
<c e g>4 <c e g>4 <c e g>4 <c e g>4
<g' b d>4 <g b d>4 <a b dis>4 <a b dis>4
<g b e>4 <g b e>4 <b d fis>4 <b d fis>4
<g c e>4 <g c e>4 <fis b d>4 <fis b d>4
<e a c>4 <e g b>4 <d fis a>4 <dis fis b>4
<e g b>4 <e g b>4 <ees fis a>4 <ees fis a>4
<d g b> <d g b> <b cis e g>2 
<a c e g>1
<c e g>4 <c e g>4 <c e g>4 <c e g>4
<d b'>16 c' c b c b c8 d4 c8 <d, b'>8 
g16 b, b'8 c8 c4 <d, b'>8 g16 d16 b'8 
c4 g'8 g4 fis4 r8
r1
<g, b>8 d <g b> d <g b> d <fis a> d 
<e g>8 b <e g>8 b <e g>8 b <e g>8 b
<a' c>8 e <a c>8 e <a c>8 e <g b>8 e
<fis a>8 d <fis a>8 d <fis a>8 d <e g>8 c
<d fis>8 b  <b' d>8 fis <b d>8 fis <b c>8 fis 
<g b>8 e <g b>8 e <fis a>8 d <gis b>8 e 
<a c>  e <g b> e  <g, d' g>4  <g d' fis>
<b d g> <b d g> <b d g> <b d g>
<e g c> <e g c> <d fis d'>2
<b' d>8 g <b d>8 g <b dis>8 a <b dis>8 a 
<b e>8 g <b e>8 g <d' fis>8 b <d fis>8 b 
<c e>8 g <c e>8 g <b d>8 fis <b d>8 fis 
<a c>8 e <g b>8 e <fis a>8 d <fis b>8 dis 
<g b>8 e <g b>8 e <fis a>8 ees <fis a>8 ees 
<g b> d <g b> d <b cis e g>2 
<a c e g>1
<c e g>4 <c e g>4 <c e g>4 <c e g>4
<g' b d>4 <g b d>4 <a b dis>4 <a b dis>4
<g b e>4 <g b e>4 <b d fis>4 <b d fis>4
<g c e>4 <g c e>4 <fis b d>4 <fis b d>4
<e a c>4 <e g b>4 <d fis a>4 <dis fis b>4
<e g b>4 <e g b>4 <ees fis a>4 <ees fis a>4
<d g b> <d g b> <b cis e g>2 
<a c e g>1
<c e g>4 <c e g>4 <c e g>4 <c e g>4
<d b'>16 c' c b c b c8 d4 c8 <d, b'>8 
g16 b, b'8 c8 c4 <d, b'>8 g16 d16 b'8 
c8 d4 g8 <g,, d' g>
 

}

lower = \relative c {
  \clef bass
\key g \major
g2 g2
g2 g2
g2 g2
d4 d'2.
g,2. fis4
e1
a2. g4
fis2. e4
b2 b'
e,2 d4 e
a2 a4 g
d1
e2 d4 e
a2 d,2
g1
<d d'>2 <d d'>2
g2 fis2
e2 d2
c2 b2
a2 <d, d'>4 <dis dis'>
e'2 ees2
d2 des2
a1
g'2 g2
g2 fis2
e2 d2
c2 b2
a2 <d, d'>4 <dis dis'>
e'2 ees2
d2 des2
a1
d2 d2
<g, g'>1
<g g'>1
<g g'>1
d'4 d'2.
g,2. fis4
e1
a2. g4
fis2. e4
b2 b'
e,2 d4 e
a2 d,2
g1
<d d'>2 <d d'>2
g2 fis2
e2 d2
c2 b2
a2 <d, d'>4 <dis dis'>
e'2 ees2
d2 des2
a1
g'2 g2
g2 fis2
e2 d2
c2 b2
a2 <d, d'>4 <dis dis'>
e'2 ees2
d2 des2
a1
d2 d2
<g, g'>1
<g g'>1
<g g'>1
<g g'>1
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

