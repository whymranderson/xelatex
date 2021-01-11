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
b cis16 cis~cis8 cis8 cis8 d16 cis~cis8 b16 a~
a2 cis8 cis cis d
cis2. r8 e,
cis'8 cis16 cis~cis8 cis8 cis8 d16 cis~cis8 b8
b cis16 cis~cis8 cis8 cis8 d16 cis~cis8 b8
a4.~a16 fis16 cis'8 cis cis fis,~
fis a8~a2 b8 cis
d16 cis d cis d8 cis16 d~d16 cis16 d8~d8 cis16 d
e4 cis8 d16 cis~cis2 
d16 cis d cis d8 cis16 d~d16 cis16 d8~d8 d8
a'4 f e d
cis16 d e4 cis16 d e4 cis8 e
\acciaccatura e8 fis4. gis8 e16~d~cis4.
r4 e8 cis g'8. fis8. cis8 e4. fis8 d4. a8
e' d4 a8 e' d4 d8 
d cis cis e d4 cis8. cis16
cis8. b16 b8 a16 b16~b4. fis8
cis'8. b16 cis8 d16 e~e2
b8 cis16 cis~cis8 cis8 cis8 d16 cis~cis8 b8
b8 cis16 cis~cis8 cis8 cis8 d16 cis~cis8 b8
b16 a16 a4 fis8 cis'4 a4 
fis8 a cis d cis4 b4 
b8 cis16 cis16~cis8 cis cis8 d16 cis~cis8 b8 
b8 cis16 cis16~cis8 cis8 cis d16 cis~cis8 b8
b16 a16 a4. cis8 cis cis fis,8~
fis8 a4.~a2
cis16 d e4 cis16 d e4 cis8 e
fis4. gis8 e16~d~cis4.
r4 e8 cis g'8. fis8. cis8 e4. fis8 d4. a8
e' d4 a8 e' d4 d8 
d cis cis e d4 cis8. cis16
cis8. b16 b8 a16 b16~b4. fis8
cis'8. b16 cis8 d16 e~e2
r1
r1
r1
r1
}
 
text = \lyricmode {
像 兩 首 節 拍 不 同 的 歌   卻 又 同 時 被 愛 情 合 奏   旋 律 勉 強 著 
愉 快 不 能 夠 假 裝 快 樂   你 心 中 有 寬 闊 的 天 空   但 空 氣 好 稀 薄 
曾 經 以 為 等 待 會 改 變 什 麼   你 總 會 屬 於 我 
但 是 最 後 時 間 證 明 了   你 只 喜 歡 我 
你 說 我 比 較 像 你 的 好 朋 友   只 是 不 小 心 擁 抱 著 
你 道 歉   你 難 過   於 是 我 給 你 笑 容 
誰 在 乎 我 的 心   還 會 不 會 寂 寞 
如 果 愛 情 是 五 線 譜   我 曾 希 望 用 全 音 符 
吟 唱 出   愛 上 你   那 完 整 的 幸 福 
但 你 的 心 沒 有 耳 朵   即 使 我 為 你 唱 著 歌 
你 也 只   看 見 我 哭 了 
你 說 過   我 是 你 最 好 的 朋 友   卻 不 應 該 再 擁 抱 著 
你 退 縮   你 冷 漠   於 是 我 放 開 雙 手 
不 在 乎 我 的 心   會 永 遠 的 寂 寞 
}

upper = \relative c' {
  \time 4/4
\key c \major
\tempo 4 = 80
a''16 a, e' a a16 a, e' a g g, d' g g g, d' g
f f, c' f f f, c' f e8 e, b' e 
<gis' gis'>1 \key a \major
cis,,,8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
<b, d fis>4 <b d fis>4 <b d fis>4 <b d fis>
<cis e gis>4 <cis e gis>4 <cis e gis>4 <cis e gis>
<d fis a>4 <d fis a>4 <d fis a>4 <d fis a>
<d f a>4 <d f a>4 <d f a>4 <d f a>4 
<a cis e>4 <a cis e>4 <a cis e>4 <a cis e>4 
<cis e gis>4 <cis e gis>4 <cis e gis>4 <cis e gis>4 %\chordmode { c1
<bes cis e>4 <bes cis e>4 <bes cis e>4 <bes cis e>4 %fis4 fis4 fis4 fis4
<b d fis>4 <b d fis>4 <b d fis>4 <b d fis>4 %b,1:m
<d fis a>4 <d fis a>4 <d fis a>4 <d fis a>4 %d:m
<a cis e>4 <a cis e>4 <fis a cis>4 <fis a cis>4 %a,
<fis b d>4 <fis b d>4 <fis b d>4 <fis b d>4 %b,:m/fis
<b e gis>4 <b e gis>4 <b e gis>4 <b e gis>4 %e }
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
cis8 e fis4 cis8 e fis4
<a cis e>4 <a cis e>4 <a cis e>4 <a cis e>4 
<cis e gis>4 <cis e gis>4 <cis e gis>4 <cis e gis>4 %\chordmode { c1
<bes cis e>4 <bes cis e>4 <bes cis e>4 <bes cis e>4 %fis4 fis4 fis4 fis4
<b d fis>4 <b d fis>4 <b d fis>4 <b d fis>4 %b,1:m
<d fis a>4 <d fis a>4 <d fis a>4 <d fis a>4 %d:m
<a cis e>4 <a cis e>4 <fis a cis>4 <fis a cis>4 %a,
<fis b d>4 <fis b d>4 <fis b d>4 <fis b d>4 %b,:m/fis
<b e gis>4 <b e gis>4 <b e gis>4 <b e gis>4 %e }

<< { \voiceOne 
cis'4. b16 a b2
a4. gis16 fis gis2
fis2 gis
a1
}
\new Voice { \voiceTwo 
r8 e fis4 r8 e fis4
r8 e fis4 r8 e fis4
r8 e fis4 r8 e fis4
r8 e fis4~fis2 
}
>> \oneVoice
}

lower = \relative c {
  \clef bass
r1
r1
r1 \key a \major
a'2 e2
fis cis
d e
a fis4 e4
a2 e2
fis cis
d e
a fis4 e4
b1
cis1
d1
d1
a8 a8~a8 a4 a8 e a
cis cis~cis cis cis e gis cis,
bes bes~bes bes~bes bes fis bes
b b~b b b cis d fis
d d~d d d d~d d
a a a e fis fis~fis fis
b b~b b~b b fis b 
e4 b e,2
a'2 e2
fis cis
d e
a fis4 e4
a2 e2
fis cis
d e
a fis4 e4
a,8 a8~a8 a4 a8 e a
cis cis~cis cis cis e gis cis,
bes bes~bes bes~bes bes fis bes
b b~b b b cis d fis
d d~d d d d~d d
a a a e fis fis~fis fis
b b~b b~b b fis b 
e4 b e,2
a2 e
fis cis
d e
a1
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

