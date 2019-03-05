#(set-default-paper-size "a4")

\paper {
  two-sided = ##t
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  binding-offset = 0.25\in
}

\header{
  title = "Rainbow"
  subtitle = "accompanyin piano"
  composer = "Jay"
  arranger = "GS Simulation"
}


melody = \relative c' {\tempo 4 = 80
r1
r1
r1
r1
e4 e8 e e f g g8~
g8 c8~c2 c,8 d
e8 e e e e a b d8~
d c8~c2~c4
a4 a8 a a b c d~
d8 g,8~g2 c8 d
e e e d d c e d~
d2. r8 d,8
e4 e8 e e f g g8~
g8 c8~c2 c8 d
e e e f e d b d~
d8 c8~c2 r8 b8
a4 a8 a a b c d~
d8 g,8~g4. g8 c d
e4 a,8 a a e' f e~
e d2 g,8 f' e 
d c c c b c d e 
g,2 r8 g c b
a g g f e d e f
g2 r8 g fis g
a4. a8 gis a b e,
c'2 r8 c b c
d4. d8 d c e f
d2 r8 g, fis g
e'4. e8 f e d b~
b c2 c8 b c
g'4. g8 f e d e
e2~d8 g, fis g
e'4. e8 f e d b
c d e b' a4. e8
g f e f e4. d8
c1 
r1
r1
r1 \bar "|." 
}

text = \lyricmode {
哪 裡 有 彩 虹 告 訴 我   能 不 能 把 我 的 願 望 還 給 我
為 什 麼 天 這 麼 安 靜   所 有 的 雲 都 跑 到 我 這 裡
有 沒 有 口 罩 一 個 給 我   釋 懷 說 了 太 多 就 成 真 不 了
也 許 時 間 是 一 種 解 藥   也 是 我 現 在 正 服 下 的 毒 藥
看 不 見 妳 的 笑 我 怎 麼 睡 得 著   妳 的 聲 音 這 麼 近 我 卻 抱 不 到
沒 有 地 球   太 陽 還 是 會 繞   沒 有 理 由   我 也 能 自 己 走
妳 要 離 開   我 知 道 很 簡 單   妳 說 依 賴   是 我 們 的 阻 礙
就 算 放 開   但 能 不 能 別 沒 收 我 的 愛   當 作 我 最 後 才 明 白

有 沒 有 口 罩 一 個 給 我   釋 懷 說 了 太 多 就 成 真 不 了
也 許 時 間 是 一 種 解 藥   也 是 我 現 在 正 服 下 的 毒 藥
看 不 見 妳 的 笑 我 怎 麼 睡 得 著   妳 的 聲 音 這 麼 近 我 卻 抱 不 到
沒 有 地 球   太 陽 還 是 會 繞   沒 有 理 由   我 也 能 自 己 走
妳 要 離 開   我 知 道 很 簡 單   妳 說 依 賴   是 我 們 的 阻 礙
就 算 放 開   但 能 不 能 別 沒 收 我 的 愛   當 作 我 最 後 才 明 白

看 不 見 妳 的 笑   要 我 怎 麼 睡 得 著
妳 的 聲 音 這 麼 近 我 卻 抱 不 到
沒 有 地 球 太 陽 還 是 會 繞 會 繞
沒 有 理 由 我 也 能 自 己 走 掉
釋 懷 說 了 太 多 就 成 真 不 了
也 許 時 間 是 一 種 解 藥 解 藥
也 是 我 現 在 正 服 下 的 毒 藥

妳 要 離 開   我 知 道 很 簡 單   妳 說 依 賴   是 我 們 的 阻 礙
就 算 放 開   但 能 不 能 別 沒 收 我 的 愛   當 作 我 最 後 才 明 白
}


upper = \relative c' { \time 4/4
e8 g, c4 f8 a, c4
g'8 g, c4 f8 a, c4
e8 g, c4 f8 a, c4
d8 g, <g c>\staccato <g b>~<g b>2
e'8 g, c4 f8 a, c4
g'8 g, c4 f8 a, c4
e8 g, c4 e8 g, b4
c8 a e' a, c8 a e' a,
c8 a f' a, b g g' g,
b g d' g, c a e' a,
c8 a f' a, c8 a f' a,
c8 a f' g <g, b>2
e'8 g, c4 f8 a, c4
g'8 g, c4 f8 a, c4
e8 g, c4 e8 g, b4
c8 a e' a, c8 a e' a,
c8 a f' a, b g g' g,
b g d' g, c a e' a,
c8 a f' a, c8 a f' a,
<g c g'>8 <g c g'>8 <g c g'>8 <g c g'>8 <g b g'>2
\chordmode { f,4 f,4 g, g,
e,:m e,:m a,:m a,:m
d,:m d,:m g, g,
c, c, c,2 
f,4 f, e, e,
a,:m a,:m c/g c/g 
f, f, fis,:dim fis,:dim
g,} g8 c b2
\chordmode { c4 c e:m/b e:m/b
a,:m a,:m c/g c/g
f, f, g, g,
c c b,2:dim6-^5
c4 c e:m/b e:m/b 
a,:m c/g fis,2:dim }
<a c f>4 <a c f> <g d' g> <g d' g>
<c e g>4 c8 f e2
e8 g, c4 f8 a, c4
g'8 g, c4 f8 a, c4
<c e>1\arpeggio
}

lower = \relative c { \clef bass
c4. c8 d4. d8
e4. e8 d4. d8
c4. c8 d4. d8
g,1
c4. c8 d4. d8
e4. e8 d4. d8
c4. c8 b4. b8
a2 g2
f2 g2
e2 a2
d,2 d2 
g2 g
c4. c8 d4. d8
e4. e8 d4. d8
c4. c8 b4. b8
a2 g2
f2 g2
e2 a2
d,2 d2 
g2 g
f8 c'4 c8 g d'4 d8
e, b'4 b8 a e'4 e8
d, a'4 a8 g d'4 d8
c, g'4 g8~g2 
f8 c'4 c8 e, b'4 b8
a8 e'4 e8 g, e'4 e8
f,8 c'4 c8 fis, c'4 c8
g8 d'~d2.
c8 g'4 g8 b,8 g'4 g8
a,8 e'4 e8 g,8 e'4 e8
f,8 c'4 c8 g8 d'4 d8
c8 g'4 g8 g,2
c8 g'4 g8 b,8 g'4 g8
a,8 e'8 g,8 e'8 fis,2 
d8 a'4 a8 g8 d'4 d8
c8 g'~g2.
c,4. c8 d4. d8
e4. e8 d4. d8
<c g'>1\arpeggio
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
